## Topic, Partition, Segment

### 카프카의 주요요소
- Topic : 카프카내에서 전송되는 메세지가 저장되는 논리적 장소
- Producer : 메세지 생성하여 Topic으로 전송하는 앱
- Consumer : Topic의 메세지를 가져가 소비하는 앱
- Consumer Group : 하나의 Consumer 는 하나의 Consumer Group 에 포함, Group 내에서는 Topic 의 메세지를 병렬 처리

### Producer 와 Consumer 의 기본동작방식
- P 와 C 는 서로 알지 못하며, 각각의 고유 속도로 Commit Log 에 Write 및 Read 수행

### Commit Log
- 추가만 가능하며 변경이 불가한 데이터 스트럭처
- 데이터(Event)는 항상 로그 끝에 추가 됨
- Offset : Commit Log 에서 Event 의 위치
- LOG-END-OFFSET : 커밋로그의 마지막 offset
- CURRENT-OFFSET : 컨슈머가 마지막으로 읽어간 곳
- Consumer Lag : LOG-END-OFFSET 과 CURRENT-OFFSET 의 사이

### Partition 
- Commit Log
- 하나의 토픽은 하나 이상의 파티션으로 구성되며 서로 독립적
- 병렬처리를 위해 다수의 파티션 사용
- 번호는 0부터 오름차순으로 생성
- Segment : 메세지(데이터)가 저장되는 실제 물리 File. 크기, 기간 설정하여 파일 Rolling (log.segment.bytes, log.roll.hours)
- Partition 에 저장된 데이터는 변경 불가 (Immutable)

### 구조
- 생성 시 Partition 개수 지정, 추후 변경 가능하나 운영중에는 변경 비권장
- 각 Partition은 Broker 들에 분산되며, Segment File들로 구성되어 있음


