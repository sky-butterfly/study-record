## Syntax Error

### Non-ASCII character
SyntaxError: Non-ASCII character '\xeb' in file xxx.py on line 1, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details
- 한글 인코딩 에러이다. 한글을 사용하는 윗 라인에 '# -*- coding: utf-8 -*-' 을 추가해주면 에러가 사라진다. python3 에서는 기본적으로 utf-8 을 사용하기 때문에 이러한 설정을 할 필요가 없다.

