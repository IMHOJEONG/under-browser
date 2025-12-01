import tkinter
import sys
from shared.url import URL
from shared.config import WIDTH, HEIGHT, HSTEP, VSTEP, SCROLL_STEP
# from shared.font import bi_times
from shared.Element import Text
from shared.Element import Tag
from shared.Layout import Layout


import tkinter.font 

# window = tkinter.Tk()
# bi_times = tkinter.font.Font(
#     family="Times",
#     size=25,
#     weight="bold",
#     slant="italic"
# )


class Browser:
    def __init__(self):
        self.window = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.window, width=WIDTH, height=HEIGHT)
        self.canvas.pack()

        self.scroll = 0
        # 아래 화살표 키 바인딩 
        # self.window.bind("<Down>", self.scrolldown)
        self.display_list = []
    
    # def scrolldown(self, e):
    #     self.scroll += SCROLL_STEP
    #     self.draw()

    def load(self, url):
        body = url.request()
        tokens = lex(body)
        print("Load URL:", url)
        # self.canvas.create_rectangle(10, 20, 400, 300)
        # self.canvas.create_oval(100, 100, 150, 150)
        # self.canvas.create_text(200, 150, text="Hi!")
        self.display_list = Layout(tokens).display_list
        self.draw()
    
    # 루프를 돌리며, 각 문자를 그리는 함수
    
    # font1 = tkinter.font.Font(family="Times", size=16)
    # font2 = tkinter.font.Font(family="Times", size=16, slant="italic")
    # x, y = 200, 225
    # self.canvas.create_text(x, y, text="Hello, ", font=font1, anchor="nw")
    # 아래 줄이 필요
    # x += font1.measure("Hello, ")
    # self.canvas.create_text(x, y, text="overlapping! ", font=font2, anchor="nw")
    def draw(self):
        self.canvas.delete("all")

        for x,y,word,font in self.display_list:

            if y > self.scroll + HEIGHT: continue
            if y + font.metrics("linespace") < self.scroll: continue

            self.canvas.create_text(x, y - self.scroll, text=word, font=font, anchor="nw")


if __name__ == "__main__":
    Browser().load(URL(sys.argv[1]))
    tkinter.mainloop()
