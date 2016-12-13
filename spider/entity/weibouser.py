'''
Created on 2016年11月30日

@author: Administrator
'''
class weibouser(object):
    def __init__(self):
        self.username = ""
        self.weibonum=""
        self.follownum=""
        self.fannum=""
        self.url=""
        self.host=""
        self.type=""
        
    def set_username(self,username):
        self.username = username
    def set_weibonum(self,weibomum):
        self.weibonum = weibomum
    def set_follownum(self,follownum):
        self.follownum = follownum
    def set_fannum(self,fansnum):
        self.fannum = fansnum
    def set_url(self,url):
        self.url=url
    def set_host(self,host):
        self.host=host
    def set_type(self,type):
        self.type=type        
        
    def get_username(self):
        return self.username
    def get_weibonum(self):
        return self.weibonum
    def get_follownum(self):
        return self.follownum
    def get_fannum(self):
        return self.fannum
    def get_url(self):
        return self.url
    def get_host(self):
        return self.host
    def get_type(self):
        return self.type