## h2 database

### dependencies
- runtimeOnly 'com.h2database:h2'

### properties
```
spring.h2.console.enabled=true
spring.h2.console.path=/h2-console
spring.datasource.generate-unique-name=false
```

or

```
spring.datasource.url=jdbc:h2:mem:testdb  
spring.datasource.driverClassName=org.h2.Driver  
spring.datasource.username=sa  
spring.datasource.password=  
spring.h2.console.enabled=false  
spring.datasource.generate-unique-name=false
```

### H2 console
- Saved Settings : Generic H2 (Embedded)
- Driver Class : org.h2.Driver
- JDBC URL : jdbc:h2:mem:testdb
- User Name : sa

### sql file path
- src/main/resources/data.sql
(위 경로의 파일에 sql 문을 작성해 놓으면, 서버 시작 시 실행된다.)
