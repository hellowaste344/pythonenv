import urllib.request
import urllib.robotparser as rb
from urllib.parse import urlparse, urlunparse

request_url = urllib.request.urlopen("http://zenonai-theta-livid.vercel.app")
print(request_url.read()[:100], end="\n\n")

parse_url = urlparse("http://zenonai.net")
print(parse_url, end="\n\n")

unparse_url = urlunparse(parse_url)
print(unparse_url, end="\n\n")

bot = rb.RobotFileParser()

x = bot.set_url("http://zenonai.net")
print(x)

y = bot.read()
print(y)

z = bot.can_fetch("*", "http://zenonai.net")
print(z)
