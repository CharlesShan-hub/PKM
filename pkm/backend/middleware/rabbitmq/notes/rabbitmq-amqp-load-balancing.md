# RabbitMQ AMQP 负载均衡
listen rabbitmq_amqp
    bind *:5670
    mode tcp
    balance roundrobin
    server rabbitmq1 172.16.0.13:5672 check inter 5s rise 2 fall 3
    server rabbitmq2 172.16.0.15:5672 check inter 5s rise 2 fall 3
    server rabbitmq3 172.16.0.16:5672 check inter 5s rise 2 fall 3