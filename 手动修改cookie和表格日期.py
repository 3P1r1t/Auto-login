import  requests

url="http://pubinfo.sdwcvc.cn/xxtb2/saveRecord?id=&fillDate=2020-11-03&mqjk=%E5%81%A5%E5%BA%B7&jrjk=%E5%81%A5%E5%BA%B7&city1=%E5%B1%B1%E4%B8%9C%E7%9C%81&city2=%E6%97%A5%E7%85%A7%E5%B8%82&city3=%E4%B8%9C%E6%B8%AF%E5%8C%BA&sfwc=0&sfjc=1&sfhb=%E5%90%A6&zb=%E4%B8%8D%E6%B8%85%E6%A5%9A&jchz=%E5%90%A6&other=&other1=%E7%A7%A6%E6%A5%BC%E8%A1%97%E9%81%93%E8%81%8A%E5%9F%8E%E8%B7%AF%E5%B1%B1%E4%B8%9C%E6%B0%B4%E5%88%A9%E8%81%8C%E4%B8%9A%E5%AD%A6%E9%99%A2&other2=%E5%90%A6&other3=37.2%E5%BA%A6%E5%8F%8A%E4%BB%A5%E4%B8%8B&other4=37.2%E5%BA%A6%E5%8F%8A%E4%BB%A5%E4%B8%8B&other5=%E5%AD%A6%E6%A0%A1&other6=%E5%90%A6&other7=119.554555%2C35.455762"

header={"Cookie":'JSESSIONID=node0toyrib9hvu0pc7feipvm4z86793898.node0; CTTICKET=web_9a11afe2de2f6008b66c4a0a84a3f73812c580e4'} #cookie值不要泄露
html=requests.get(url,headers=header)
print(html.text)
