from bs4 import BeautifulSoup
import requests
import time
#签到的页面
url = ' http://pubinfo.sdwcvc.cn/xxtb2/saveRecord?id=&fillDate=2020-10-16&mqjk=%E5%81%A5%E5%BA%B7&jrjk=%E5%81%A5%E5%BA%B7&city1=%E5%B1%B1%E4%B8%9C%E7%9C%81&city2=%E6%97%A5%E7%85%A7%E5%B8%82&city3=%E4%B8%9C%E6%B8%AF%E5%8C%BA&sfwc=0&sfjc=1&sfhb=%E5%90%A6&zb=%E4%B8%8D%E6%B8%85%E6%A5%9A&jchz=%E5%90%A6&other=&other1=%E7%A7%A6%E6%A5%BC%E8%A1%97%E9%81%93%E8%81%8A%E5%9F%8E%E8%B7%AF%E5%B1%B1%E4%B8%9C%E6%B0%B4%E5%88%A9%E8%81%8C%E4%B8%9A%E5%AD%A6%E9%99%A2&other2=%E5%90%A6&other3=37.2%E5%BA%A6%E5%8F%8A%E4%BB%A5%E4%B8%8B&other4=37.2%E5%BA%A6%E5%8F%8A%E4%BB%A5%E4%B8%8B&other5=%E5%AD%A6%E6%A0%A1&other6=%E5%90%A6&other7=119.554555%2C35.455762 HTTP/1.1 '
header = {
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate',
'Host': 'pubinfo.sdwcvc.cn',
'Connection': 'keep-alive',
'Accept':'*/*',
'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
'X-Requested-With': 'XMLHttpRequest',
'Referer': 'http://pubinfo.sdwcvc.cn/xxtb2/dailyRecord?submitDate=2020-10-16',
'Accept-Encoding':' gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
'Cookie': 'JSESSIONID=node01hl8fetjjuyns1fx5zp5s1jsrp793776.node0; CTTICKET=web_0ba36a54601070872370aabb225fa0fd45fbb054',
}
#记得写上headers=header,通过键名匹配
web_data = requests.get("url",headers=header)