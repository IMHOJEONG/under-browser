import tkinter
import sys
from shared.url import URL
from shared.config import WIDTH, HEIGHT, HSTEP, VSTEP, SCROLL_STEP

def layout(text):

    display_list = []
    cursor_x, cursor_y = HSTEP, VSTEP
    for c in text:
        display_list.append((cursor_x, cursor_y, c))
        cursor_x += HSTEP
        if cursor_x >= WIDTH - HSTEP:
            cursor_y += VSTEP
            cursor_x = HSTEP

    return display_list

class Browser:
    def __init__(self):
        self.window = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.window, width=WIDTH, height=HEIGHT)
        self.canvas.pack()

        self.scroll = 0
        # 아래 화살표 키 바인딩 
        self.window.bind("<Down>", self.scrolldown)
    
    def scrolldown(self, e):
        self.scroll += SCROLL_STEP
        self.draw()

    def lex(self, body):
        text = ""
        in_tag = False
        for c in body:
            if c == "<":
                in_tag = True
            elif c == ">":
                in_tag = False
            elif not in_tag: 
                text += c
        return text

    def load(self, url):
        body = url.request()
        text = self.lex(body)

        print("Load URL:", url)
        # self.canvas.create_rectangle(10, 20, 400, 300)
        # self.canvas.create_oval(100, 100, 150, 150)
        # self.canvas.create_text(200, 150, text="Hi!")
        
        
        self.display_list = layout(text)
        self.draw()
    
    # 루프를 돌리며, 각 문자를 그리는 함수
    def draw(self):
        self.canvas.delete("all")
        for x,y,c in self.display_list:

            # if y > self.scroll + HEIGHT: continue
            # if y + VSTEP < self.scroll: continue

            self.canvas.create_text(x, y - self.scroll, text=c)



if __name__ == "__main__":
    Browser().load(URL(sys.argv[1]))
    tkinter.mainloop()
