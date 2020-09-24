# Jenkins update
- 참고 https://medium.com/@jimkang/how-to-start-a-new-jenkins-container-and-update-jenkins-with-docker-cf628aa495e9

1. jenkins 컨테이너로 진입
2. wget http://updates.jenkins-ci.org/download/war/2.150.1/jenkins.war
3. mv ./jenkins.war /usr/share/jenkins
4. chown jenkins:jenkins /usr/share/jenkins/jenkins.war
5. 호스트로 나오기
6. docker restart jenkins