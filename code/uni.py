
import requests
import pyquery

url = "https://www.un.org/zh/sections/un-charter/preamble/index.html"

req = requests.get(url)
req.encoding = 'utf8'
text = req.text
qd = pyquery.PyQuery(text)
sep = "\n" + "*-" * 10 + '*'
lmd = lambda i, v: ("" if v.tag == "h3" else '  ') + v.text + (sep if v.tag == "h3" else "  " ) 
lines = qd(".content h3, .content li, .content p").map(lmd)
print("\r\n".join(lines))
