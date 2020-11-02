## Future
- 참고 : https://gunju-ko.github.io/java/2018/07/05/Future.html

### Future
- 비동기 처리 결과를 표현하기 위해 사용
- 비동기 처리 완료되었는지 확인, 처리 완료 대기, 처리 결과 리턴 메소드 제공
- 비동기 결과는 완료 후 get을 사용해 얻을 수 있음
- get 메소드는 비동기 처리가 완료될 때까지 blocking 처리
- 취소하려면 cancel 메소드 사용

### CompletableFuture
- Future의 결과를 명시적으로 쓸 수 있음 (명시적으로 Future를 완료할 수 있음)
- 만약 2개 이상의 스레드에서 CompleteFuture에 결과를 쓰려고 하는 경우에는 그 중 1개의 스레드만 성공

```
CompletableFuture<String> futrue = CompletableFuture.completedFuture("test");
assertThat(future.isDone()).isTure();

String result = future.get();
assertThat(result).isEqualTo("test");

```