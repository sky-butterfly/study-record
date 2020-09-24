## 502 Error

- 502 Bad Gateway

- proxy_pass 의 값을 변수로 설정해주었더니 502 에러 발생
- resolver 설정하지 않아 발생한 오류
- /etc/resolv.cof 의 nameserver 를 참고 하여 resolver 설정해야 함

- ex)
```
    location / {
        resolver 127.0.0.11;
        proxy_pass $service_url;
    }
```