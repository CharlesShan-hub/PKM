# nginx

---
## 简介

nginx = 「Web服务器」 + 「方向代理服务器」 + 「IMAP/POP3/SMTP代理服务器」

* 官网: https://nginx.org/en/
* 视频（19年尚硅谷）: https://www.bilibili.com/video/BV1zJ411w7SV
* 视频（22年尚硅谷-比较啰嗦）: https://www.bilibili.com/video/BV1yS4y1N76R
* 短视频（反向代理比喻）: https://www.bilibili.com/video/BV16h411L7NK 

---
## 概念



---
403错误大概率因为路径没有权限

```bash
sudo chmod 755 /home/charles
sudo systemctl restart nginx
```

---
反向代理：客户端请求 `example.com/api/user` → 代理到 `http://127.0.0.1:8080/user`

```txt
server {
    listen 80;
    server_name example.com;

    location /api/ {
        # 去掉 `/api/`，将请求代理到后端的 `/`
        proxy_pass http://127.0.0.1:8080/;  # 注意末尾的 `/`
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

