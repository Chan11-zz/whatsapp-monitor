import datetime from datetime as dt
class Person:
    def __init__(self):
        self.name=None
        self.status=None
        self.lastseen_ts=[]
        self.ls=None
        self.td=None
        self.online_ts=[]
        self.td={}
    def add_name(self,name):
        self.name=name
    def status(self,status):
        self.status=status
    def lastseen(self,ls):
        print("in last seen")
        if(ls==self.ls):
            return
        self.lastseen_ts.append(ls)
        self.ls=ls
        self.total_duration(ls)
    def total_duration(self,ls):
        td=self.ls-self.online_ts[-1]
        self.td[self.online_ts[-1]]="Online from " + self.online[-1].strftime("%H:%M")+" to "+ self.ls.strftime("%H:%M") + ":"+td.strftime("%H:%M")
        print(self.td)
    def online(self,ol):
        self.online_ts.append(ol)
        
        
        
        
        
    
