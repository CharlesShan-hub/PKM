# DbUtils.java


```java
package com.jkweilai.servlet.util;

import java.sql.*;
import java.util.ResourceBundle;

/**
 * Database utility class for managing JDBC connections and resources.
 * Reads database configuration from jdbc.properties file.
 */
public class DbUtils {

    private static String url;
    private static String user;
    private static String password;

    static {
        // Load JDBC configuration from properties file
        ResourceBundle bundle = ResourceBundle.getBundle("jdbc");
        String driver = bundle.getString("driver");
        url = bundle.getString("url");
        user = bundle.getString("user");
        password = bundle.getString("password");

        // Register JDBC driver
        try {
            Class.forName(driver);
        } catch (ClassNotFoundException e) {
            throw new RuntimeException("Failed to load JDBC driver", e);
        }
    }

    /**
     * Establishes and returns a connection to the database.
     *
     * @return a Connection object
     * @throws SQLException if a database access error occurs
     */
    public static Connection getConnection() throws SQLException {
        return DriverManager.getConnection(url, user, password);
    }

    /**
     * Closes JDBC resources safely.
     * Resources are closed in reverse order of creation:
     * ResultSet -> Statement -> Connection
     *
     * @param conn the Connection to close (may be null)
     * @param stmt the Statement to close (may be null)
     * @param rs   the ResultSet to close (may be null)
     */
    public static void close(Connection conn, Statement stmt, ResultSet rs) {
        // Close ResultSet first
        if (rs != null) {
            try {
                rs.close();
            } catch (SQLException e) {
                // Log or ignore - resource already closed or not available
                e.printStackTrace();
            }
        }

        // Then close Statement
        if (stmt != null) {
            try {
                stmt.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }

        // Finally close Connection
        if (conn != null) {
            try {
                conn.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
    }
}
```
