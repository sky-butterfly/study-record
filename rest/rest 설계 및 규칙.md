## Rest 설계 및 규칙
- 참고 : https://devuna.tistory.com/79

### 중요 포인트
- URI 는 정보의 자원을 표현
- 행위는 HTTP Method (GET, POST, PUT, DELETE) 로 표현

### 규칙
- 소문자 사용
- 하이픈 사용 (사용은 최소화)
- 마지막 슬래시는 미포함
- 행위는 미표시 (행위 : Method)
- 파일 확장자 미포함
    - 파일 확장자는 Accept header 를 사용
    - Accept: image/jpg
- 명사 사용. 컨트롤 자원을 의미하는 경우 예외적으로 동사 허용