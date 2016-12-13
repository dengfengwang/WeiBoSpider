'''
Created on 2016年11月29日

@author: Administrator
'''
from bs4 import BeautifulSoup
import requests
from spider.entity.weibouser import weibouser
from spider.entity.weibocontent import weibocontent
from spider.db.dbutil import dao
from spider.db import dbutil
try:
    import cookielib
except:
    import http.cookiejar as cookielib

agent = 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36'
global headers
global user_Url
headers = {
    'User-Agent': agent
}
baseUrl = "http://weibo.cn"

# 使用登录cookie信息
session = requests.session()
session.cookies = cookielib.LWPCookieJar(filename='cookies')
try:
    session.cookies.load(ignore_discard=True)
except:
    print("Cookie 未能加载")
    
def getPage(url):
    response= session.get(url,headers=headers)
    html = response.text
    return html

def parseFansListPage(fansListPageUrl):
    fansPageHtml =getPage(fansListPageUrl)
    soup = BeautifulSoup(fansPageHtml, 'html.parser', from_encoding='utf-8')
    tableTags = soup.find_all('table')
    #粉丝列表
    for tbodyTag in tableTags:
        fansName = tbodyTag.find_all('a')[1].text
        fansUrl = tbodyTag.find_all('a')[1].get('href')
        fanHomePageHtml = getPage(fansUrl)
        
    nextPage = soup.findAll('a',text='下页')
    if nextPage:
        nextPageUri = nextPage[0].get('href')
        url = baseUrl+nextPageUri
        parseFansListPage(url)

#获取用户的微博内容并保存到数据库中
def parseWeiboContentPage(url):
    html = getPage(url)
    soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
    contentTags = soup.find_all('div','c')
    for contentTag in contentTags[:-2]:
        wc = weibocontent()
        wc.set_content(contentTag.text)
        wc.set_userurl(user_Url)
        dao = dbutil.dao()
        dao.save_weibo(wc)
        print(contentTag.text)
    nextPage = soup.findAll('a',text='下页')
    if nextPage:
        nextPageUri = nextPage[0].get('href')
        url = baseUrl+nextPageUri
        parseWeiboContentPage(url)
        
def parseUserHomePage(userurl):
    user_Url = userurl
    html = getPage(userurl)
    print(userurl)
    soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
    #微博url
    personInfoTag = soup.find("div", "tip2")
    #微博条数
    weiboNum = personInfoTag.find('span','tc').text
    #微博名
    userName = soup.find('title').text[:-3]
#     print(weiboNum)
    atag = personInfoTag.findAll("a")
    #关注人数
    followNum = atag[0].text
    #粉丝数
    fanNum = atag[1].text
    #保存微博用户的基本信息到数据库
    user = weibouser()
    user.set_fannum(fanNum)
    user.set_follownum(followNum)
    user.set_username(userName)
    user.set_weibonum(weiboNum)
    dao = dbutil.dao()
    dao.user_dao(user)
    #获取微博
    parseWeiboContentPage(userurl)
    
#     contentTags = soup.find_all('div','c')
#     for contentTag in contentTags[:-2]:
#         wc = weibocontent()
#         wc.set_content(contentTag.text)
#         wc.set_userurl(userurl)
#         dao.save_weibo(wc)
#         print(contentTag.text)
    

#     #跳转到粉丝页面的url
#     uri = atag[1].get('href')
#     fansListPageUrl = baseUrl+uri
#     parseFansListPage(fansListPageUrl)


if __name__ == "__main__":
    #http://weibo.cn/u/1851853163+
    url = "http://weibo.cn/u/5953608036"
    user_Url = url
    parseUserHomePage(url)