# Decompiler
- 이클립스에 decompiler 를 설치해서 .class 파일 보기

## jadClipse eclipse plugin 다운로드
- http://sourceforge.net/projects/jadclipse/
- 이클립스가 설치된 경로의 dropins 폴더에 복사
- 이클립스 restart

## jad.exe 다운로드
- http://varaneckas.com/jad/
- 다운로드 후 압축풀기
- 이클립스에 경로 설정
  - Window / preference / Java / JadClipse
  - Path to decompiler 에 jad.exe 파일 경로 작성

## .class 파일 editors 설정
- Window / preference / General / Editors / File Associations
- *.class, *.class without source
  - 각각 선택 후 Associated editors 에 JadClipse Class File Viewer 를 default 로 설정