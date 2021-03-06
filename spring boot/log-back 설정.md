## Spring Boot LogBack 설정

1. dependency
- spring-boot-starter-web 에 logback-classic, logback-core가 포함되어 있다.

2. properties
```
logback.path=/logs/
logback.level=DEBUG
```

3. logback-spring.xml
```
<?xml version="1.0" encoding="UTF-8"?>
<configuration>

    <springProperty scope="context" name="logging_path" source="logback.path"/>
    <springProperty scope="context" name="logging_level" source="logback.level"/>

    <appender name="Console" class="ch.qos.logback.core.ConsoleAppender">
        <encoder class="ch.qos.logback.classic.encoder.PatternLayoutEncoder">
            <Pattern>
                %d{yyyy-MM-dd HH:mm:ss} [%thread] [%-5level] %logger{36} - %msg%n
            </Pattern>
        </encoder>
    </appender>
    
    <appender name="RollingFile" class="ch.qos.logback.core.rolling.RollingFileAppender">
        <file>${logging_path}/log/fit-food.log</file>
        <encoder class="ch.qos.logback.classic.encoder.PatternLayoutEncoder">
            <Pattern>%d{yyyy-MM-dd HH:mm:ss} [%-5level] %logger{36} - %msg%n</Pattern>
            <charset>UTF-8</charset>
        </encoder>
        
        <triggeringPolicy
            class="ch.qos.logback.core.rolling.SizeBasedTriggeringPolicy">
            <MaxFileSize>10MB</MaxFileSize>
        </triggeringPolicy>

        <rollingPolicy class="ch.qos.logback.core.rolling.FixedWindowRollingPolicy">
            <FileNamePattern>${logging_path}/log/fit-food.%i.log.zip</FileNamePattern>
            <MinIndex>1</MinIndex>
            <MaxIndex>10</MaxIndex>
        </rollingPolicy>
    </appender>   
   
    <appender name="Error" class="ch.qos.logback.core.rolling.RollingFileAppender">
        <filter class="ch.qos.logback.classic.filter.LevelFilter">
            <level>error</level>
            <onMatch>ACCEPT</onMatch>
            <onMismatch>DENY</onMismatch>
        </filter>
        <file>${logging_path}/error/fit-food-error.log</file>
        <encoder class="ch.qos.logback.classic.encoder.PatternLayoutEncoder">
            <Pattern>
                %d{yyyy-MM-dd HH:mm:ss} [%-5level] %logger{36} - %msg%n
            </Pattern>
            <charset>UTF-8</charset>
        </encoder>

        <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">
            <fileNamePattern>${logging_path}/error/fit-food-error.%d{yyyy-MM-dd}.log</fileNamePattern>
            <maxHistory>30</maxHistory>
        </rollingPolicy>
    </appender>
    
    <logger name="org.springframework.web" level="INFO" additivity="false">
        <appender-ref ref="Console"/>
        <appender-ref ref="Error"/>
    </logger>
    
    <logger name="org.apache.ibatis" level="DEBUG" additivity="false">
        <appender-ref ref="Console"/>
        <appender-ref ref="RollingFile"/>
        <appender-ref ref="Error"/>
    </logger>

    <root level="${logging_level}">
        <appender-ref ref="Console"/>
        <appender-ref ref="Error"/>
    </root>

</configuration>
```