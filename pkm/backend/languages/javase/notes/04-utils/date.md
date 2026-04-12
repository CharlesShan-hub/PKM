# 日期类

![Date-drawing|1000](../../assets/Date-drawing.md)

---
## Date 

源码 

```java
public class Date  
    implements java.io.Serializable, Cloneable, Comparable<Date> {}
```

构造函数

```java
public Date() {  
    this(System.currentTimeMillis());   // 当前时间
}  
  
public Date(long date) {  
    fastTime = date;   // 输入时间戳
}
```

案例

```java
package ex_commom;  
  
import java.text.ParseException;  
import java.text.SimpleDateFormat;  
import java.util.Date;  
  
public class DateExample {  
    public static void main(String[] args) throws ParseException {  
        Date date1 = new Date();  
        System.out.println(date1);  
        // Sat Mar 22 00:52:23 CST 2025  
  
        Date date2 = new Date(1934567);  
        System.out.println(date2);  
        // Thu Jan 01 08:32:14 CST 1970  
        
        // 获取当前系统时间的前10分钟时间
        Date date3 = new Date(System.currentTimeMillis() - 1000 * 60 * 10); 
        System.out.println(date3);

        // 日期格式化
        SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");  
        System.out.println(sdf.format(date1));  
        // 2025-03-22 00:53:50  
  
        String dateStr = "2025-09-22 00:53:50";  
        Date parsedDate = sdf.parse(dateStr);//要加 throws ParseException   
        
        System.out.println(sdf.format(parsedDate));  
        // 2025-09-22 00:53:50  
    }  
}
```

---
## Calendar 

```java
package ex_commom;  
  
import java.util.Calendar;  
import java.util.TimeZone;  
  
public class CanlendarExample {  
    public static void main(String[] args) {  
        // Calendar 不能 new        
        Calendar calendar = Calendar.getInstance(  
                TimeZone.getTimeZone("Asia/Shanghai")  
        );  
        System.out.println(calendar.get(Calendar.YEAR));  
        // 2025  
        System.out.println(calendar.get(Calendar.MONTH) + 1);//注意，要加一  
        // 3  
        System.out.println(calendar.get(Calendar.DAY_OF_MONTH));  
        // 22  
        System.out.println(calendar.get(Calendar.HOUR_OF_DAY));  
        // 1  
        System.out.println(calendar.get(Calendar.MINUTE));  
        // 20  
        System.out.println(calendar.get(Calendar.SECOND));  
        // 51  
        System.out.println(calendar.get(Calendar.MILLISECOND));  
        // 333  
        System.out.println(calendar.get(Calendar.ZONE_OFFSET));  
        // 28800000  
        System.out.println(calendar.get(Calendar.DST_OFFSET));  
        // 0  
        System.out.println(calendar.get(Calendar.AM_PM));  
        // 0（凌晨一点半学 java）  
    }  
}
```

* 日历的set方法：设置日历
    * calendar.set(Calendar.YEAR, 2023);  
    * calendar.set(2008, Calendar.SEPTEMBER,8);
* 日历的add方法（日历中各个部分的加减）：
    * calendar.add(Calendar.YEAR, 1);
* 日历对象的setTime()让日历关联具体的时间
    * calendar.setTime(new Date());
* 日历对象的getTime()方法获取日历的具体时间：
    * Date time = calendar.getTime();

```java
package com.powernode.javase.datetest;  
  
import java.text.ParseException;  
import java.text.SimpleDateFormat;  
import java.util.Calendar;  
import java.util.Date;  
  
public class CalendarTest02 {  
    public static void main(String[] args) throws ParseException {  
        // 获取系统当前时间的日历  
        Calendar cal = Calendar.getInstance();  
        // 设置该日历的年是2008年  
        cal.set(Calendar.YEAR, 2008);  
        //cal.set(Calendar.MONTH, 10);  
        // 获取日历的年月日信息  
        System.out.println(cal.get(Calendar.YEAR) + "年" + (cal.get(Calendar.MONTH) + 1) + "月" + cal.get(Calendar.DAY_OF_MONTH) + "日");  
        // 设置日历是2008年8月8日 8时8分8秒的日历  
        cal.set(2008, Calendar.AUGUST,8,8,8,8);  
        // 获取日历的年月日信息  
        System.out.println(cal.get(Calendar.YEAR) + "年" + (cal.get(Calendar.MONTH) + 1) + "月" + cal.get(Calendar.DAY_OF_MONTH) + "日");  
  
        // 年加1  
        //cal.add(Calendar.YEAR, 2);        
        cal.add(Calendar.YEAR, -2);  
        // 获取日历的年月日信息  
        System.out.println(cal.get(Calendar.YEAR) + "年" + (cal.get(Calendar.MONTH) + 1) + "月" + cal.get(Calendar.DAY_OF_MONTH) + "日");  
  
        // 获取一个2008年5月12日 15:30:30的Date  
        String strDate = "2008-05-12 15:30:30";  
        SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");  
        Date date = sdf.parse(strDate);  
        cal.setTime(date);  
        // 获取这个日历的小时和分  
        System.out.println(cal.get(Calendar.HOUR_OF_DAY));  
        System.out.println(cal.get(Calendar.MINUTE));  
  
        // 获取日历代表的日期  
        cal.set(Calendar.SECOND, 56); // 修改日历中的秒  
        Date time = cal.getTime();  
        String s = sdf.format(time);  
        System.out.println(s);  
  
    }  
}
```

---
## LocalDate

1. 前两代的缺点
    JDK 1.0 中包含了一个 java.util.Date 类，但是它的大多数方法已经在 JDK 1.1 引入 Calendar 类之后被弃用了。而 Calendar 也存在问题：  
    1）可变性：像日期和时间这样的类应该是不可变的。  
    2）偏移性：Date 中的年份是从 1900 开始的，而月份都从 0 开始。  
    3）格式化：格式化只对 Date 有用，Calendar 则不行。  
    4）此外，它们也不是线程安全的；不能处理闰秒等（每隔 2 天，多出 1s）。

 2. 第三代日期类常见方法：`LocalDate`(日期)、`LocalTime`(时间)、`LocalDateTime`(日期时间) JDK8加入
    - **LocalDate** 只包含日期（年月日），可以获取日期字段
    - **LocalTime** 只包含时间（时分秒），可以获取时间字段
    - **LocalDateTime** 包含日期+时间（年月日+时分秒），可以获取日期和时间字段
    ```java
    LocalDateTime ldt = LocalDateTime.now(); // LocalDate.now() // LocalTime.now()
    System.out.println(ldt);
    ldt.getYear();
    ldt.getMonthValue();
    ldt.getMonth();
    ldt.getDayOfMonth();
    ldt.getHour();
    ldt.getMinute();
    ldt.getSecond();
    ```
    
    ```java
    LocalDate date = LocalDate.now();  
    LocalTime time = LocalTime.now();  
    LocalDateTime dateTime = LocalDateTime.of(date, time);  
    System.out.println(date + " " + time); // 2025-03-22 01:28:41.658802  
    System.out.println(dateTime); // 2025-03-22T01:28:41.658802
    ```

3. 格式调整：`DateTimeFormatter`
    ```java
    LocalDate date = LocalDate.now();  
    LocalTime time = LocalTime.now();  
    LocalDateTime dateTime = LocalDateTime.of(date, time);  
    DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");  
    System.out.println(dateTime.format(formatter)); // 2025-03-22 01:32:56
    ```

4. 时间戳：`Instant`
    ```java
    Instant instant = Instant.now();  
    System.out.println(instant);  
    System.out.println(Instant.ofEpochMilli(instant.toEpochMilli()));  
    System.out.println(Instant.ofEpochSecond(instant.toEpochMilli()));  
    // 2025-03-21T17:37:51.970891Z  
    // 2025-03-21T17:37:51.970Z  
    // +57190-02-13T15:06:10Z
    Date d = Date.from(instant);  
    System.out.println(d);  
    // Sat Mar 22 01:38:47 CST 2025
    ```

5. 计算日期间隔：`Period`

    ```java
    // 计算两个日期间隔
    
    LocalDate now1 = LocalDate.of(2007,7,7);
    LocalDate now2 = LocalDate.of(2008,8,8);
    Period between = Period.between(now1, now2);
    // 相差年数
    System.out.println(between.getYears());
    // 相差月数
    System.out.println(between.getMonths());
    // 相差天数
    System.out.println(between.getDays());
    
    ```

6. 时间矫正器：`TemporalAdjusters`

    ```java
    LocalDateTime now = LocalDateTime.now(); // 获取系统当前时间
    now.with(TemporalAdjusters.firstDayOfMonth()); // 当前月的第一天
    now.with(TemporalAdjusters.firstDayOfNextYear()); // 下一年的第一天
    now.with(TemporalAdjusters.lastDayOfYear()); // 本年最后一天
    now.with(TemporalAdjusters.lastDayOfMonth()); // 本月最后一天
    now.with(TemporalAdjusters.next(DayOfWeek.MONDAY)); // 下周一
    
    ```