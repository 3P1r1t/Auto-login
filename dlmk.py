import  requests

url="sso.sdwcvc.cn/index.php?rid=verifyWebUser"     #action属性
params={
   "username":"2020145335",               #input标签下的name
   "password":"Zxcv1234@"              #input标签下的name
}
html=requests.post(url,data=params)
print(html.text)