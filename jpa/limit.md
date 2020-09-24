## Limit 쿼리를 써야할 때
- JPA, JPQL 에서 limit 을 사용하면 에러가 발생한다.

### Pageable 사용하기
- Repository 호출 부분
```
menuRepo.findByRandom(PageRequest.of(0, 1));
```

- Repository
```
@Query("select name from Menu order by random()")
String findByRandom(PageRequest limit);
```