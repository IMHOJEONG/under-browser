import socket
import ssl

class URL:
    # init 메서드 : 클래스 생성자를 위한 파이썬의 독특한 구문 
    def __init__(self, url) -> None:
        self.scheme, url = url.split("://", 1)
        assert self.scheme in ["http", "https"]

        # HTTP 연결 
        if self.scheme == "http":
            self.port = 80
        elif self.scheme == "https":
            self.port = 443

        # 호스트와 경로를 분리 

        if "/" not in url:
            url = url + "/"
        self.host, url = url.split("/", 1)
        self.path = "/" + url
    pass

    def request(self):
        # import ssl
        # ctx = ssl.create_default_context()

        s = socket.socket(
            family=socket.AF_INET,
            type=socket.SOCK_STREAM,
            proto=socket.IPPROTO_TCP
        )

        s.connect((self.host, self.port))

        if self.scheme == "https":
            ctx = ssl.create_default_context()
            s = ctx.wrap_socket(s, server_hostname=self.host)

        if ":" in self.host:
            self.host, port = self.host.split(":", 1)
            self.port = int(port)

        # 
        request = "GET {} HTTP/1.0\r\n".format(self.path)
        request += "Host: {}\r\n".format(self.host)
        request += "\r\n"
        s.send(request.encode("utf8"))

        response = s.makefile("r", encoding="utf8", newline="\r\n")
        statusline = response.readline()
        version, status, explanation = statusline.split(" ", 2)

        # 
        response_headers = {}
        while True:
            line = response.readline()
            if line == "\r\n": break
            header, value = line.split(":", 1)
            response_headers[header.casefold()] = value.strip()

        # 
        assert "transfer-encoding" not in response_headers
        assert "content-encoding" not in response_headers

        # 
        body = response.read()
        s.close()

        return body

def show(body):
    in_tag = False
    for c in body:
        if c == "<":
            in_tag = True
        elif c == ">":
            in_tag = False
        elif not in_tag:
            print(c, end="")

def load(url):
    body = url.request()
    show(body)

if __name__ == "__main__":
    import sys 
    load(URL(sys.argv[1]))