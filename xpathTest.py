import urllib
url='http://www.ppvke.com'
res=urllib.request.urlopen(url)
text=res.read()
res.close()
txt=text.decode("utf-8")
from lxml import etree
htm=etree.HTML(txt)
result = htm.xpath('//*[@id="linkcolor"]/text()')
