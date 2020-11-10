## Redis 와 Spring boot 연동하기
- 참고 : https://engkimbs.tistory.com/796

### 의존성 추가
- implementation 'org.springframework.boot:spring-boot-starter-data-redis'

### 레디스 실행
- 도커를 이용한 레디스 실행
> docker run -p 6379:6379 --name redis -d redis

- 실행 확인
> docker exec -it redis redis-cli
> keys *

### 레디스 
- 예제
```
    @Component
    public class RedisRunner implements ApplicationRunner {

        @Autowired
        StringRedisTemplate redisTemplate;

        @Override
        public void run(ApplicationArguments args) throws Exception {
            ValueOperations<String, String> values = redisTemplate.opsForValue();
            values.set("name", "saelobi");
            values.set("framework", "spring");
            values.set("message", "hello world");
        }
    }
```

- 확인
> get name
> get framework
> get message

### 레디스를 이용 스프링 저장소

- 예제소스
```
    @RedisHash("accounts")
    public class Account {

    @Id
    String id;

    private String username;

    private String email;

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
}
```

- @RedisHash : 해당 클래스의 인스턴스가 레디스에 적재될 때, @RedisHash의 인수를 키로 사용

```
public interface AccountRepository extends CrudRepository<Account, String> {

}
```

- CrudRepository : 저장소 접근 및 처리 위한 인터페이스 제공
```
    @Component
    public class RedisRunner implements ApplicationRunner {

    @Autowired
    StringRedisTemplate redisTemplate;

    @Autowired
    AccountRepository accountRepository;

    @Override
    public void run(ApplicationArguments args) throws Exception {
        ValueOperations<String, String> values = redisTemplate.opsForValue();
        values.set("name", "saelobi");
        values.set("framework", "spring");
        values.set("message", "hello world");

        Account account = new Account();
        account.setEmail("eng.kimbs@gmail.com");
        account.setUsername("saelobi");

        accountRepository.save(account);

        Optional<Account> byId = accountRepository.findById(account.getId());
        System.out.println(byId.orElse(new Account()).getUsername());
        System.out.println(byId.orElse(new Account()).getEmail());
    }
}
```