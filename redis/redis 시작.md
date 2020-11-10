## Redis 사용

### Redis 란
- REmote DIctionary Server
- 오픈소스
- 공통으로 사용되는 데이터를 캐시로 저장해둠으로써 리소스를 효율적으로 이용할 수 있음
- In-Memory 데이터베이스 : 모든 데이터를 메모리에 저장 및 조회
    - 메모리 접근은 디스크 접근보다 빠르기 때문에, 기존 RDBMS 보다 훨씬 빠름
- 다양한 자료구조를 Key-Value 형태로 지원함으로써 개발의 편의성을 높이고 난이도를 낮춤

### Redis key
- 문자열
- 모든 이진 시퀀스 사용 가능
- 빈 문자열도 사용 가능
- 최대 키 크기는 512MB
- 긴 키를 사용해야 할 때는 hash의 member로 저장하는 것이 더 효율적
- object-type:id 형태를 권장
- ., -, : 등의 부호를 사용해 관계를 나타낼 수 있음

### Redis 자료구조

#### String
- 레디스의 키가 문자열이며, 문자열을 다른 문자열에 매핑하는 것
```
    > set hello world
    OK
    > get hello
    "world"
```
- 이진 데이터를 포함한 모든 종류의 문자열을 저장할 수 있으며, JPEG 이미지를 저장하거나 HTML fragment를 캐시하는 용도로 자주 사용
- 최대 저장 사이즈 : 512MB
- string 을 정수로 파싱 후 atomic 증감
```
    > set counter 100
    OK
    > incr counter
    (integer) 101
    > incr counter
    (integer) 102
    > incrby counter 50
    (integer) 152

```
- 키를 새 값을 변경하고 이전 값을 반환
```
    > incr mycounter
    (interger) 1
    > getset mycounter "0"
    "1"
    > get mycounter
    "0"
```
- 키가 이미 존재하거나, 존재하지 않을 때에만 데이터를 저장하게 하는 옵션
```
    > set mykey newval nx
    (nil)
    > set mykey newval xx
    OK
```

#### List
- 일반적인 linked list의 특징을 가짐
- list 내에 수백만 개의 아이템이 있더라도 head와 tail에 값을 추가할 때 동일한 시간이 소요됨
- 특정 값이나 인덱스로 데이터를 찾거나 삭제 가능
```
    LPUSH mylist A      # now the list is "A"
    LPUSH mylist B      # now the list is "B", "A"
    RPUSH mylist A      # now the list is "A", "B", "A"
```
- list blocking
    - list가 비어있을 때 pop을 시도하면 대개 NULL을 반환. 이 경우 일정시간을 기다린 후 다시 pop 시도 (=polling)
    - BRPOP을 사용하면 새로운 아이템이 리스트에 추가될 때에만 응답하므로 불필요한 polling 프로세스를 줄일 수 있음

#### Hash
- field-value 쌍을 이용한 해시
- key에 대한 filed의 갯수는 제한이 없음
- RDB의 table과 비슷
    - hash key는 table의 PK, field는 column, value 는 vlaue로 볼 수 있음
    - key와 PK가 같은 역할을 하기 때문에, key 하나는 table의 한 row와 같음
```
    > hmget user-2 email country
    1) "giantpengsoo@ebs.com"
    2) "Antarctica"
```
- atomic 조작
```
    > hincrby user : 1000 birthyear 10
    (interger) 1987
    > hincrby user : 1000 birthyear 10
    (interger) 1997
```

#### Set
- 정렬되지 않은 문자열의 모음
- 중복될 수 없음
- redis 에서 교집합, 합집합, 차집합 연산을 수행할 수 있으며, 객체 간의 관계를 표현할 때 좋음
- EX. ID가 1000인 프로젝트에 1,2,5,77번의 태그ID를 연결
```
    > sadd project:1000:tags 1 2 5 77
    (integer) 4

    > smembers project:1000:tags
    1. 5
    2. 1
    3. 77
    4. 2
```

### Expire
- 메모리에 저장할 수 있는 데이터가 한정적이기 때문에 더 이상 데이터 저장이 불가할 경우, 가장 먼저 혹은 가장 나중에 들어온 데이터를 삭제하거나 더 이상 데이터를 입력받지 못하게 된다.
- 삭제되는 데이터를 레디스에 맡기지 않고, 직접 설정 가능
- 데이터 입력 시 이 데이터의 사용 기한 설정 가능 (timeout)
- 동일한 키가 다시 들어오면 timeout 재설정 됨 (자주 사용되는 데이터는 계속 남아있게 됨)
- 모든 키에 expire 값을 추가하는 것을 권장