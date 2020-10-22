## git diff
- 참고 : https://blog.outsider.ne.kr/1011
- 두 커밋간이나 HEAD와 워킹 디렉토리의 차이점을 보여주는 명령어
- --color-words 옵션
    - git diff --color-words
    - 변경된 단어(공백으로 구분)로 표시
- --word-diff
    - git diff --word-diff
    - 보다 명시적으로 변경된 단어 표시
- diff-highlight
    - git config --global pager.diff 'diff-highlight | less'
    - ~/.gitconfig 파일 설정 추가 방법도 있음 (위 명령어와 같은 역할)
        - ```
            [pager]
                diff = diff-highlight | less
          ```
    - 변경된 라인 표시와 함께 단어도 표시 됨