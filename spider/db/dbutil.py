'''
Created on 2016年11月30日

@author: Administrator
'''
from spider import config
import  mysql.connector
from spider.entity.weibouser import weibouser
from spider.entity.weibocontent import weibocontent
class dao(object):
    try:
        cnn = mysql.connector.connect(
                                      user=config.DbConfig.get('user'),
                                      password=config.DbConfig.get('password'),
                                      host=config.DbConfig.get('host'),
                                      database=config.DbConfig.get('database'),
                                      charset=config.DbConfig.get('charset')
                                      )
    except Exception as e:
        print("连接出错")
    cursor = cnn.cursor()
     
    def user_dao(self, user):
        sql_insert = "insert into weibouser(username,weibonum,follownum,fannum)values('" + user.get_username() + "','" +user.get_weibonum() + "','" + user.get_follownum()+ "','" + user.get_fannum() + "')"
        print(sql_insert)
        self.cursor.execute(sql_insert)
        self.cnn.commit()
    def save_weibo(self,content):
        print(content.get_content())
        print(content.get_userurl())
        sql_insert = "insert into weibocontent(userurl,content)values('"+content.get_userurl()+"','"+content.get_content()+"')"
        print(sql_insert)
        self.cursor.execute(sql_insert)
        self.cnn.commit()
    
    def test(self, user):
        print(user.get_fannum())
        print(user.get_username())
        print(user.get_follownum())
        print(user.get_weibonum())
if __name__ == "__main__":
    dao = dao()
    content = weibocontent()
    content.set_content("123")
    content.set_userurl("www.baidu.com")
    dao.save_weibo(content)
