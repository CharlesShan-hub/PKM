
- 可以使用这个命令：`show profiles;` 这个命令可以查看在mysql中执行的所有SQL以及命令的耗费时长。
- `show profiles;` 是在mysql5.0.37之后添加的。所以要确保你的mysql版本没问题。
- 如何开启时长统计功能：`set profiling = 1;`
- 查看时长统计功能是否开启：`show variables like '%pro%';`
- 查看每条SQL的耗时：`show profiles;`
- 查看其中某条SQL耗时明细：`show profile for query query_id`
- 查看最新一条SQL的耗时明细：`show profile;`
- 查看cpu，io等信息：`show profile block io, cpu for query query_id;`
