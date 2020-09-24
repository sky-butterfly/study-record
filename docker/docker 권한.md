## Docker 권한

### docker 실행 권한
- 도커의 명령은 항상 root 권한으로 실행해야 한다.
- sudo를 사용하지 않고 docker 실행하기 위한 명령어
    - > sudo usermmod -aG docker $USER

### volumne 폴더 소유권
- 기본적으로 root로 생성됨