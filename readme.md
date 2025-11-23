## Python 기본 

- 아주 핵심적인 두 가지 질문이야. 둘 다 Python을 제대로 이해하는 데 매우 중요한 개념이어서 자세히 설명해줄게.

---

# ✅ 1. `python -m step2.main` 은 **모듈 실행 방식**

## 🔥 이것이 의미하는 것:

* **Python이 현재 디렉토리를 “프로젝트 루트”로 보고 패키지 구조를 인식한 채 실행해라** 라는 뜻.
* `step2/main.py`를 **패키지 내부의 모듈**로 실행하는 방식.

즉:

```
python -m step2.main
```

은 실제로 내부적으로 다음을 실행함:

* `project/`를 **sys.path[0] (= import root)** 로 설정
* `step2.main` 모듈을 로드
* `main.py` 안의 코드를 실행

그래서

```python
from shared.url import URL
```

이 **정상적으로 작동하는 것**.

---

## ❌ 왜 `python step2/main.py` 로 실행하면 문제인가?

이렇게 실행하면:

* Python은 **현재 디렉토리 = step2** 를 import root로 설정
* 그러면 `shared/` 폴더를 못 찾음 → `ModuleNotFoundError`

즉, import 경로가 달라진 것.

---

# 🏆 결론

### `python -m`은:

**“프로젝트 루트 기준의 패키지 import 규칙을 지켜서 모듈을 실행하라”**
이런 뜻이며, 패키지 기반 개발에서는 거의 표준 실행 방식.

---

# ✅ 2. `__pycache__` 폴더가 생기는 이유

Python 파일(.py)을 실행하면 Python 인터프리터는 다음을 함:

### 🔹 1) `.py`를 **바이트코드(.pyc)** 로 컴파일

### 🔹 2) 컴파일된 결과를 `__pycache__/파일명.cpython-XX.pyc` 에 저장

### 🔹 3) 다음 실행부터는 `.pyc`를 즉시 로드 → 실행 속도 향상

그래서 **각 폴더에 `__pycache__`가 생기는 게 정상**.

---

# 📌 왜 각 폴더마다 생길까?

파이썬은 “모듈 단위로” 캐시를 만드는 언어임.

* `shared/url.py` → `shared/__pycache__/url.cpython-XX.pyc`
* `step2/main.py` → `step2/__pycache__/main.cpython-XX.pyc`

물리적으로 모듈이 있는 폴더에 pycache를 남기는 것이 규칙이기 때문.

---

# 🧹 pycache는 지워도 되나?

네. 지워도 문제 없음.

다음 실행 때 Python이 다시 만든다.

---

# ✔ 요약

| 개념                     | 설명                                                           |
| ---------------------- | ------------------------------------------------------------ |
| `python -m step2.main` | 패키지 구조를 유지한 상태로 모듈 실행, import 문제 해결                          |
| `__pycache__`          | Python이 `.py` → `.pyc` 바이트코드를 저장하는 캐시 폴더, 실행 속도 향상을 위해 자동 생성 |

---

원하면:

* 너의 프로젝트 구조에 맞는 “권장 실행 방식”
* pycache를 자동으로 무시하는 `.gitignore`
* VSCode에서 `python -m`을 기본 실행으로 맞추는 설정

까지 모두 설정해줄 수 있어.
