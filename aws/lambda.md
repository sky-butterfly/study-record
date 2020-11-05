## AWS Lambda
- 참고 : https://medium.com/harrythegreat/%EB%B9%84%EC%A0%84%EA%B3%B5%EC%9E%90%EB%A5%BC-%EC%9C%84%ED%95%9C-aws-lambda-1%ED%8E%B8-5697cee473eb

### Lambda에 대해
- 흔히 람다함수라고도 부르며 자바에서의 람다함수와는 다른 개념
- 함수가 어떤 인자를 넣으면 출력인자를 내뱉듯이, 람다도 마찬가지
- ex) API Gateway -> restful 요청 -> Lambda -> 데이터베이스 저장 -> Dynamo DB
- 별도의 서버를 구비해두고 동작시켜지 않아도, AWS가 자동으로 함수를 동작시켜 줌
- 간단하게 웹서버 구현이 가능
- 동작시에만 과금
