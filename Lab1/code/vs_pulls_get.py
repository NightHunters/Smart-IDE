# 需要调用的requests 库和 BeautifulSoup库中的bs4工具
import requests
import soup as soup
from bs4 import BeautifulSoup

num = 0  # 定义条数的初始值
# 定义一个变量url，为需要爬取数据的网页网址

#输出到文件的信息定义
save_path='F:\\'
save_name='\\pullswithlink_2''.txt'
full_path=save_path+save_name
fp=open(full_path,'w',encoding='utf-8')
fp.close()
fp=open(full_path,'a+',encoding='utf-8')

for page in range(6):
    url = 'https://github.com/microsoft/vscode/pulls?page=%s&q=is%%3Aopen+is%%3Apr' %str(page+1)
# 获取这个网页的源代码，存放在req中，{}中为不同浏览器的不同User-Agent属性，针对不同浏览器可以自行百度
    req = requests.get(url, {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'})
# 生成一个Beautifulsoup对象，用以后边的查找工作
    soup = BeautifulSoup(req.text, 'html.parser')
# 找到所有p标签中的内容并存放在xml这样一个类似于数组队列的对象中
    xml = soup.find_all('a',class_='link-gray-dark v-align-middle no-underline h4 js-navigation-open')


# 利用循环将xml[]中存放的每一条打印出来

    for i in range(len(xml)):  # 表示从0到xml的len()长度
        msg = xml[i].string
        if not msg is None:
            num += 1
        #print('第', num, '条', msg)
        t3 = xml[i].get('href')
        url2='https://github.com'+str(t3)
        fp.write('第'+str(num)+'条\t'+msg + '\n')
        fp.write(url2+'\n')

    print(str(page+1))

for page1 in range(237):
    url1 = 'https://github.com/microsoft/vscode/pulls?page=%s&q=is%%3Apr+is%%3Aclosed' %str(page1+1)
# 获取这个网页的源代码，存放在req中，{}中为不同浏览器的不同User-Agent属性，针对不同浏览器可以自行百度
    req1 = requests.get(url1, {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'})
# 生成一个Beautifulsoup对象，用以后边的查找工作
    soup1 = BeautifulSoup(req1.text, 'html.parser')
# 找到所有p标签中的内容并存放在xml这样一个类似于数组队列的对象中
    xml1 = soup1.find_all('a',class_='link-gray-dark v-align-middle no-underline h4 js-navigation-open')


# 利用循环将xml[]中存放的每一条打印出来

    for i in range(len(xml1)):  # 表示从0到xml的len()长度
        msg1 = xml1[i].string
        if not msg1 is None:
            num += 1
        #print('第', num, '条', msg)
        t4 = xml1[i].get('href')
        url4 = 'https://github.com' + str(t4)
        fp.write('第'+str(num)+'条\t'+msg1 + '\n')
        fp.write(url4 + '\n')
    print(str(page1+1))

fp.close()
print('finsh')
