## Redis 명령어
- 참고 : http://redisgate.kr/redis/command/getset.php

- SORT : 정렬 조회
- EXISTS : 해당 키가 있는지 확인
- DEL : 값에 관계없이 키 삭제
- TYPE : 해당 키에 연결된 자료구조가 어떤 형태인지 반환

### String
- incr
    - string으로 저장된 값을 integer으로 변환한 뒤 1 증가시킴. 증가시킨 값을 다시 string으로 저장
- incrby
    - 명령문 : INCRBY key increment(정수)
    - 지정한 정수값 만큼 증가시킨다
- getset
    - 명령문 : GETSET key value
    - 새로운 값을 저장하고 이전 값을 반환
- setnx
    - 명령문 : SETNX key value
    - 동일한 key가 없을 경우에만 저장

### List
- LPUSH
    - 명령문 : LPUSH key value
    - 리스트 왼쪽에 데이터를 저장하며, 리스트에 포함된 값의 개수를 리턴한다.
- RPUSH
    - 명령문 : RPUSHX key value
    - 키가 이미 있을 경우에만 리스트의 오른쪽에 데이터를 저장
- BRPOP
    - 명령문 : BRPOP key timeout
    - 리스트에 데이터가 이미 있을 경우 RPOP과 같은 기능
    - 데이터가 없는 경우 timeout(초)만큼 대기
    - timeout이 0일때, 데이터가 입력될때까지 대기
    - 데이터가 들어오면 pop을 하고 key, data, 시간(초)를 표시 

### Hash
- HMGET
    - 명령문 : HMGET key field1 field2
    - 여러개의 value를 조회
- HINCRBY
    - 명령문 : HINCRBY key field increment
    - value를 increment 만큼 증가 또는 감소
    - 해당 field가 없으면 increment 값을 set
- SADD
    - 집합에 데이터 추가
    - 명령문 : SADD key member
    - member는 여러개 지정할 수 있으며 중복될 수 없다
- SMEMBERS
    - 집합 데이터 조회
    - 명령문 : SMEMBERS key
    - 조회 순서를 지정할 수 없다
