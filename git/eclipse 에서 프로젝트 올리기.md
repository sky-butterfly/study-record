## eclipse 에서 처음으로 git 에 프로젝트를 올릴 때

1. eclipse 에 git 레파지토리 생성
    - 프로젝트에서 오른쪽 마우스 클릭
    - Team -> Share Project 선택
    - Use or create repository in parent folder of project 체크박스 체크
    - Create Repository 버튼 클릭

2. remote 생성
    - git repository 의 Remotes 에서 오른쪽 마우스 클릭
    - Configure push 라디오 선택
    - OK 버튼 클릭
    - Change 버튼 클릭
    - github 정보 입력하고 Finish 클릭
    - Save 버튼 클릭

3. fetch
    - git repository 의 Remotes 클릭
    - origin 클릭
    - 첫번째 항목에서 오른쪽 마우스 클릭 후 Configure Fetch 클릭
    - Advanced... 클릭
    - Source ref: 에서 master[branch] 선택
    - Destination ref: 에서 origin/master [tracking branch] 선택
    - + Add Spec 클릭
    - Finish 클릭
    - Save 클릭
    - 다시 첫번째 항목에서 오른쪽 마우스 클릭 후 Fetch 클릭
    - Fetch 된 소스를 Pull 받는다

4. commit/push
    - 생성된 프로젝트 소스를 push 한다