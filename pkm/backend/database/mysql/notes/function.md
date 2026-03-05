
# 存储函数

存储函数：带返回值的存储过程。参数只允许是in（但不能写显示的写in）。没有out，也没有inout。
语法格式：
```plsql
CREATE FUNCTION 存储函数名称(参数列表) RETURNS 数据类型 [特征]
BEGIN
	--函数体
	RETURN ...;
END;
```

“特征”的可取重要值如下：

- `deterministic`：用该特征标记该函数为确定性函数（什么是确定性函数？每次调用函数时传同一个参数的时候，返回值都是固定的）。这是一种优化策略，这种情况下整个函数体的执行就会省略了，直接返回之前缓存的结果，来提高函数的执行效率。
- `no sql`：用该特征标记该函数执行过程中不会查询数据库，如果确实没有查询语句建议使用。告诉 MySQL 优化器不需要考虑使用查询缓存和优化器缓存来优化这个函数，这样就可以避免不必要的查询消耗产生，从而提高性能。
- `reads sql data`：用该特征标记该函数会进行查询操作，告诉 MySQL 优化器这个函数需要查询数据库的数据，可以使用查询缓存来缓存结果，从而提高查询性能；同时 MySQL 还会针对该函数的查询进行优化器缓存处理。

案例：计算1~n的所有偶数之和
```plsql
-- 删除函数
drop function if exists sum_fun;

-- 创建函数
create function sum_fun(n int)
returns int deterministic 
begin 
	declare result int default 0;
	while n > 0 do 
		if n % 2 = 0 then 
			set result := result + n;
		end if;
		set n := n - 1;
	end while;
	return result;
end;

-- 调用函数
set @result = sum_fun(100);
select @result;
```
