## version 변경 중 에러 발생

### 동작
-  ./gradlew wrapper --gradle-version 7.6 --stacktrace

### 에러
```
    Caused by: java.lang.ExceptionInInitializerError: Exception java.lang.NoClassDefFoundError: Could not initialize class org.codehaus.groovy.reflection.ReflectionCache [in thread "Daemon worker"]
```

### 해결방법
- gradle 과 java 버전이 맞지 않다는 말도 있었지만, gradle/wrapper/gradle-wrapper.properties 의 distributionUrl 의 gradle 버전을 수정해주었더니 에러가 사라졌다.

