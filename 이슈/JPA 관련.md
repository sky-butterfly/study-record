- 이슈
```
    'com.querydsl.jpa.impl.JPAQueryFactory' that could not be found.
```

- JPA Config 파일 필요
```
    @Configuration
    @EnableJpaAuditing
    @EnableJpaRepositories(basePackages = "com.forj.plan")
    public class JPAConfig {
        
        @PersistenceContext
        private EntityManager entityManager;
        
        @Bean
        public JPAQueryFactory queryFactory() {
            return new JPAQueryFactory(entityManager);
        }
    }

```

- 참고 : https://abbo.tistory.com/321