## Fegin
- 참고 : https://woowabros.github.io/experience/2019/05/29/feign.html

### Fegin 이란
- 웹 서비스 클라이언트를 보다 쉽게 작성할 수 있음
- interface 작성 후 annotation 선언하면 됨
    - Spring Data JAP 에서 실제 쿼리를 작성하지 않고 Interface 만 지정하여 쿼리 실행 구현체를 자동으로 만들어주는 것과 유사

### 소스 분석
- 필요 라이브러리
    - org.springframework.cloud:spring-cloud-starter-openfeign
- 사용에 필요한 어노테이션
    - @EnableFeignClients
- 인터페이스 작성
    - @FeignClient 으로 선언된 인터페이스 작성
