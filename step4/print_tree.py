import sys
import sys
from shared.url import URL
from shared.HTMLParser import HTMLParser, print_tree

body = URL(sys.argv[1]).request()
# print(body)
nodes = HTMLParser(body).parse()
print_tree(nodes)