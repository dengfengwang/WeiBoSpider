'''
Created on 2016年12月1日

@author: Administrator
'''
class weibocontent(object):
    def __init__(self):
        self.userurl=""
        self.content=""
        
    def set_userurl(self,userurl):
        self.userurl=userurl
    def set_content(self,content):
        self.content=content
        
        
    def get_userurl(self):
        return self.userurl
    def get_content(self):
        return self.content