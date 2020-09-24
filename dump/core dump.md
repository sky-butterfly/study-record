## core dump
- 참고 https://m.blog.naver.com/PostView.nhn?blogId=bumsukoh&logNo=110116491995&proxyReferer=https%3A%2F%2Fwww.google.co.kr%2F

### javacore 파일
- JVM 프로세스에 대한 상세한 정보 제공
- 각 라인 앞에는 Tag 가 붙어있다.
    - 최대 15자리의 문자
    - 첫 번째 숫자는 각 구성요소의 순번
    - 2~3번째 문자는 Section 정보 (JVM subcomponent에 대한 정보임)
        - ```
            - CI : Command-line interpreter
            - CL : Class loader
            - LK : Locking
            - ST : Storage(Memory Management)
            - TI : Title
            - XE : Execution Engine
            - XM : Execution Management
    - 나머지는 출력라인에 대한 정보 문자
    - OSECTION Tag는 모든 Section 의 시작을 의미
    - NULL은 공백 라인에 대한 Tag