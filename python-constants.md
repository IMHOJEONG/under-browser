### Python에서 공유할 변수는 어떻게 관리하는 게 좋은가?

👉 config.py 또는 constants.py를 만들어 공유하는 방식
shared/
 └─ constants.py

# constants.py
WIDTH = 800
HEIGHT = 600

from shared.constants import WIDTH, HEIGHT


구조도 깔끔하고, Python 프로젝트에서 가장 널리 쓰는 패턴이야.