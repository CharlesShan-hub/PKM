# %i 当日索引。如果同一天内日志文件大小超过限制，产生第二个归档文件时，索引会递增。

logging.logback.rollingpolicy.file-name-pattern=${LOG_FILE}.%d{yyyy-MM-dd}.%i.gz

```

