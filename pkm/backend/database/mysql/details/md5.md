md5函数，可以将给定的字符串经过md5算法进行加密处理，字符串经过加密之后会生成一个固定长度32位的字符串，md5加密之后的密文通常是不能解密的：

```sql
mysql> select md5('Charles');
ERROR 1305 (42000): FUNCTION bjpowernode.md5 does not exist
mysql> SELECT SHA1('Charles');
ERROR 1305 (42000): FUNCTION bjpowernode.SHA1 does not exist

mysql> SELECT SHA2('Charles', 256);
+------------------------------------------------------------------+
| SHA2('Charles', 256)                                             |
+------------------------------------------------------------------+
| c43139196d576427b9073922c4da86ff6d0ecff71d1a2c2ad9116ad2a1e8d50d |
+------------------------------------------------------------------+
1 row in set (0.002 sec)
```