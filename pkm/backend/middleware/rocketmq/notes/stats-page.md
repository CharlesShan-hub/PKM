# 统计信息页面

listen stats
    bind *:8100
    mode http
    stats enable
    stats uri /
    stats refresh 5s
