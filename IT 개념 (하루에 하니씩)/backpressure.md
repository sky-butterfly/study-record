## Back Pressure

## 참고 https://sjh836.tistory.com/182
- 빠른 Publisher - 느린 Subscriber 문제를 해결하는 원리
- Subscriber 가 처리할 수 있을 만큼의 데이터만 전달
    - 중간에 Queue 가 필요없어짐
    - dynamic pull 이라고 부름
- 리액티브 스트림에서는 Subscription 의 request 메소드로 요청량 조절
    - LONG.MAX 씩 요청하면 순수 push 모델이 됨
    - onNext 당 1개씩 요청하면 pull 모델이 됨??
    


## 참고 백기선님 강의
- 얼마나 많은 데이터를 받기 원하는 지 신호를 보내는 것.
> backpressure 에 대한 설정값을 매번 설정해줘야 하는 가?
    - Spring Webflux 에서 적절한 양만큼 자동조절
    - 리액터 자체는 자동조절 해주지 않음
> 숫자가를 30으로 설정했다해도 그게 과하다면 동적으로 바뀌어야 하는 것이 아닌가?
