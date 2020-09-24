# Spring 프로젝트 구성

## Dynamic Web Project 생성
- 프로젝트 생성 시 설정
  - /src/main/java 폴더 생성
  - Content directory 를 webapp 으로 설정
  - Generate web.xml deployment descriptor 를 체크해서 web.xml 파일 자동 생성

## Maven 프로젝트로 변환
- 우클릭 / Configure / Convert to Maven Project 선택
  - Group Id 는 com.xxx
- 변환되면 pom.xml 생성됨

## Pom.xml 에 라이브러리 추가
- 스프링 개발 시 필요한 라이브러리
  - spring-context
  - spring-web
  - spring-webmvc
```
	<properties>
		<org.springframework-version> 5.1.5.RELEASE </org.springframework-version>
	</properties>
	
	<dependencies>
		<dependency>
			<groupId>org.springframework</groupId>
			<artifactId>spring-context</artifactId>
			<version>${org.springframework-version}</version>
		</dependency>
		<dependency>
			<groupId>org.springframework</groupId>
			<artifactId>spring-web</artifactId>
			<version>${org.springframework-version}</version>
		</dependency>
		<dependency>
			<groupId>org.springframework</groupId>
			<artifactId>spring-webmvc</artifactId>
			<version>${org.springframework-version}</version>
		</dependency>
	</dependencies>
```

## Web.xml 설정 추가
- DispatcherServlet
  - url / servlet 매핑
```
<servlet>
    <servlet-name>spring</servlet-name>
    <servlet-class>org.springframework.web.servlet.DispatcherServlet</servlet-class>
    <init-param>
        <param-name>contextConfigLocation</param-name>
        <param-value>/WEB-INF/spring/servlet-context.xml</param-value>
    </init-param>
</servlet>
<servlet-mapping>
    <servlet-name>spring</servlet-name>
    <url-pattern>*.do</url-pattern>
</servlet-mapping>
```

## servlet.xml 파일 생성
- web.xml 에서 설정한 servlet-name 을 이용해서 xml 파일 생성
  - ex). spring-servlet.xml
- <context:annotation-config />
  - bean 의 어노테이션 활성화
  - @Autowired 와 같은 어노테이션 활성화
- <context:component-scan>
  - @Controller, @Service, @Configuration 와 같은 어노테이션을 스캔
- jsp 뷰 리졸버
```
<bean class="org.springframework.web.servlet.view.InternalResourceViewResolver">
    <property name="prefix" value="/WEB-INF/views/" />
    <property name="suffix" value=".jsp" />
</bean>
```