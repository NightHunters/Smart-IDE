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
# save_name='\\pr_code''.txt'
# full_path=save_path+save_name
# save_name='\\source''.txt'
# full_path=save_path+save_name
# fp=open(full_path,'w',encoding='utf-8')
# fp.close()
# fp=open(full_path,'a+',encoding='utf-8')


url = 'https://github.com/microsoft/vscode/pull/72747/commits'
#'https://bugs.eclipse.org/bugs/buglist.cgi?chfield=%%5BBug%%20creation%%5D&chfieldfrom=7d&columnlist=product%%2Ccomponent%%2Cassigned_to%%2Cbug_status%%2Cresolution%%2Cshort_desc%%2Cchangeddate%%2Cbug_severity&query_format=advanced'
browser = webdriver.Chrome(executable_path='F:\py3.7.4\Scripts\chromedriver.exe')
browser.get(url) #这个就是chrome浏览器中的element的内容了
#browser.find_elements_by_tag_name('td') #获取element中 td下的内容
#fp.write(browser.page_source)
a=browser.find_elements_by_class_name('message')#('blob-code-addition')#('js-comment-body')
#c=browser.find_elements_by_class_name('js-timeline-progressive-focus-container')


# soup = BeautifulSoup(browser.page_source, 'html.parser')
# xml = soup.find_all('a',href='show_bug.cgi?id=55310
# for i in range(len(b)):# 表示从0到xml的len()长度
#     if(b[i].get_attribute('class')=='blob-code blob-code-deletion'):
#         print('-'+b[i].text)
#     elif(b[i].get_attribute('class')=='blob-code blob-code-addition'):
#         print('+'+b[i].text)
#     elif(b[i].get_attribute('class')=='blob-code blob-code-context'):
#         print(' '+b[i].text)
for i in range(len(a)):
    url1=a[i].get_property('href')
    browser1 = webdriver.Chrome(executable_path='F:\py3.7.4\Scripts\chromedriver.exe')
    browser1.get(url1)
    full_path=save_path+str(i)+'.txt'
    b = browser1.find_elements_by_class_name('blob-code')
    fp=open(full_path,'w',encoding='utf-8')
    fp.close()
    fp=open(full_path,'a+',encoding='utf-8')
    for i in range(len(b)):# 表示从0到xml的len()长度
        if(b[i].get_attribute('class')=='blob-code blob-code-deletion'):
            fp.write('-'+b[i].text+'\n')
        elif(b[i].get_attribute('class')=='blob-code blob-code-addition'):
            fp.write('+'+b[i].text+'\n')
        elif(b[i].get_attribute('class')=='blob-code blob-code-context'):
            fp.write(' '+b[i].text+'\n')
    fp.close()
#     fp.write(b[i].text)
#     fp.write('\n')
#
# fp.close()
print('finsh')
