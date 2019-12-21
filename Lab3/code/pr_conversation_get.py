# 需要调用的requests 库和 BeautifulSoup库中的bs4工具
import requests
import soup as soup
import re
from bs4 import BeautifulSoup
from selenium import webdriver

#num = 0  # 定义条数的初始值
# 定义一个变量url，为需要爬取数据的网页网址

#输出到文件的信息定义
save_path='F:\\'
save_name='\\pr_conversation''.txt'
full_path=save_path+save_name
# save_name='\\source''.txt'
# full_path=save_path+save_name
fp=open(full_path,'w',encoding='utf-8')
fp.close()
fp=open(full_path,'a+',encoding='utf-8')

# for page in range(2):
# url = 'https://bugs.eclipse.org/bugs/buglist.cgi?chfield=%%5BBug%%20creation%%5D&chfieldfrom=7d&columnlist=product%%2Ccomponent%%2Cassigned_to%%2Cbug_status%%2Cresolution%%2Cshort_desc%%2Cchangeddate%%2Cbug_severity&query_format=advanced'
# # 获取这个网页的源代码，存放在req中，{}中为不同浏览器的不同User-Agent属性，针对不同浏览器可以自行百度
# req = requests.get(url, {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'})
# # 生成一个Beautifulsoup对象，用以后边的查找工作
# print(req.text)
# soup = BeautifulSoup(req.text, 'html.parser')
# 找到所有p标签中的内容并存放在xml这样一个类似于数组队列的对象中
# xml = soup.find_all()
# print(len(xml))
url = 'https://github.com/microsoft/vscode/pull/72747'
#'https://bugs.eclipse.org/bugs/buglist.cgi?chfield=%%5BBug%%20creation%%5D&chfieldfrom=7d&columnlist=product%%2Ccomponent%%2Cassigned_to%%2Cbug_status%%2Cresolution%%2Cshort_desc%%2Cchangeddate%%2Cbug_severity&query_format=advanced'
browser = webdriver.Chrome(executable_path='F:\py3.7.4\Scripts\chromedriver.exe')
browser.get(url) #这个就是chrome浏览器中的element的内容了
#browser.find_elements_by_tag_name('td') #获取element中 td下的内容
#fp.write(browser.page_source)
a=browser.find_elements_by_class_name('timeline-comment-group')#('blob-code-addition')#('js-comment-body')
c=browser.find_elements_by_class_name('js-timeline-progressive-focus-container')
#b=browser.find_elements_by_css_selector('td')


#print(len(b))

# soup = BeautifulSoup(browser.page_source, 'html.parser')
# xml = soup.find_all('a',href='show_bug.cgi?id=553101')
fp.write(a[0].text+'\n')
fp.write('\n')
for i in range(len(c)):# 表示从0到xml的len()长度
    fp.write(c[i].text+'\n')
    fp.write('\n')



# print(str(page+1))
fp.close()
print('finsh')
