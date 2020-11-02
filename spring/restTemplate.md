## RestTemplate
- 참고 https://sjh836.tistory.com/141

### 개념
- 스프링에서 제공하는 템플릿
- http 통신에서 유용하게 쓰인다
- 기존 방법들
    - URLConnection
        - 응답코드가 4~ 거나 5~ 이면 IOException 발생
        - 타임아웃 설정 할 수 없음
        - 쿠키 제어 불가
    - HttpClient
        - 반복적인 코드가 길다
        - 스트림처리 로직 필요
        - 응답의 컨텐츠타입에 따른 별도 로직 필요

### 동작원리
- RestTemplate 생성하여 URI, HTTP메소드 등의 헤더를 담아 요청
- HttpMessageConverter를 사용하여 requestEntity를 요청메세지로 변환
- RestTemplate 는 CllientHttpReauestFactory로 부터 ClientHttpRequest를 가져와서 요청을 보냄
- ClientHttpRequest는 요청메세지를 만들어 Http 프로토콜을 통해 서버와 통신
- ResponsesErrorHandler로 오류 확인 후 처리로직 태움
- ResponseErrorHandler가 오류가 있다면 ClientHttpResponse에서 응답데이터를 가져와서 처리한다.
- RestTemplate 는 HttpMessageConverter를 이용해서 응답메세지를 java object(Class responseType) 로 변환한다.
- 어플리케이션에 반환된다.

