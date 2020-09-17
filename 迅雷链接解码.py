import base64

# 迅雷地址转普通地址过程：
# 1，将迅雷地址去掉thunder://，得到base64编码后的字符串
# 2，将字符串解码，得到一个字节对象
# 3，将字节对象转成字符串对象
# 4，将字符串对象去掉前缀'AA'和后缀'ZZ'

url = 'thunder://QUFodHRwOi8vZGwwMi55dXRvdS50djo5MjAvMTExMC9bMDHniYjlgJrlpKnlsaDpvpnorrBd56ysNDLpm4YvWzAx54mI5YCa5aSp5bGg6b6Z6K6wXeesrDQy6ZuGLm1wNFpa'
strb = url.lstrip('thunder://')
urlb = base64.b64decode(strb)
strurl = urlb.decode('utf-8')
zsurl = strurl.strip('AZ')
print(zsurl)
