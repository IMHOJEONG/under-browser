## 텍스트 포맷팅하기 

- 폰트: 글꼴, 서체, 타입 / 스타일과 크기를 의미함 

```py
# REPL 이용 

>>> import tkinter.font

window = tkinter.Tk()
bi_times = tkinter.font.Font(
    family="Times",
    siz>>> 
>>> window = tkinter.Tk()
>>> bi_times = tkinter.font.Font(
...     family="Times",
...     size=25,
...     weight="bold",
...     slant="italic"
... )
>>> 
>>> 
>>> 
>>> bi_times.metrics()
{'ascent': 23, 'descent': 6, 'linespace': 29, 'fixed': 0}
>>> 

```

- metrics 메서드: 텍스트의 세로축에 대한 정보들을 제공 

    - linespace: 텍스트의 높이 / ascent: 기준선 윗부분 / descent: 기준선 아랫부분의 높이 

    - ascent, descent: 크기가 다른 글자가 같이 있을 때 필요 

        - 크기가 다른 글자가 같은 줄에 있을 때는 위나, 아래가 아닌 기준선으로 정렬 필요 

- 폰트 크기가 16 = 16픽셀이 아닌 72분의 1인치를 의미하는 16포인트를 의미 

- 모니터에서 1인치당 픽셀 수는 대략 100개 정도 

    - 16포인트는 개별 글자가 아니라, 글자가 조각된 금속 활자를 측정한 것 = 글자 자체는 16포인트보다 작아야 함 

    - 실제로, 폰트 크기가 16인 폰트들의 글자들은 높이가 다양 

```py
>>> bi_times.measure("hi!")
31
>>> bi_times.measure("h")
14
>>> bi_times.measure("H")
20
>>> 
```

- measure 메서드: 텍스트가 차지하는 가로 공간의 크기를 알려줌 
  
    - 글자마다 너비가 다르기 떄문에 같은 폰트라도 텍스트에 따라 크기가 다름 

- anchor의 설정도 필요한 경우가 존재 

    - 모든 한자의 너비가 동일한 경우에는 이 작업을 수행할 필요가 없었음 
    
### 한 단어씩 처리하기 

- 영어는 단어 중간에 다음 줄로 이동할 수 없음 => 텍스트를 한 번에 한 단어씩 배치해야 함 

    - 한자와 달리 영단어는 단어마다 크기가 다르기 때문에 각 단어의 너비를 측정해야 함 

```py
# y를 증가시킬 때, 줄 간격(linespace)에 1.25를 곱함 
cursor_y += font.metrics("linespace") * 1.25

# 단어 사이의 공백을 두는 코드
cursor_x += w + font.measure(" ")
```

- 단어 중간에 줄을 끊는 것 = 하이픈 연결 


