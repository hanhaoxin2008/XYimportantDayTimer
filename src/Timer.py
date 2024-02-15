"""
@author: hanhaoxin
@file: TimerManager.py.py
@time: 2024/2/15
@desc: 定时器
"""
import json
import time
class Timer:
    def __init__(self,id,name,datetime):
        """
        :param id: 定时器id
        :param name: 定时器名称
        :param datetime: 时间
        """
        self.id = id
        self.name = name
        self.datetime = datetime
    def getName(self):
        return self.name
    def getDatetime(self):
        return self.datetime

    def getTimestamp(self):
        """
        @desc: 获取时间戳
        :return: 时间戳
        """
        return int(time.mktime(time.strptime(self.datetime, "%Y-%m-%d %H")))

    def getSecond(self):
        """
        @desc: 获取秒数
        :return: 秒数
        """
        if time.time()>self.getTimestamp():
            return int(time.time()) - self.getTimestamp()
        else:
            return self.getTimestamp() - int(time.time())

    def getDiff(self):
        """
        @desc: 获取时间差
        :return: 时间差字典
        """
        s=self.getSecond()
        diff={
            "year":int(s/(60*60*24*365)),
            "month":int((s%(60*60*24*365)/(60*60*24*30))),
            "day":int((s%(60*60*24*365)%(60*60*24*30))/(60*60*24)),
            "hour":int((s%(60*60*24*365)%(60*60*24*30)%(60*60*24))/(60*60)),
            "minute":int((s%(60*60*24*365)%(60*60*24*30)%(60*60*24)%(60*60))/(60)),
            "second":int(s%(60*60*24*365)%(60*60*24*30)%(60*60*24)%(60*60)%(60))
        }
        return diff
    def toStr(self):
        """
        @desc: 转换为字符串
        :return :字符串 格式：
        距离xx还剩xx年xx月xx天xx小时xx分xx秒
        """
        return "距离%s还剩%s年%s月%s天%s小时%s分钟%s秒"%(self.name,self.getDiff()["year"],self.getDiff()["month"],self.getDiff()["day"],self.getDiff()["hour"],self.getDiff()["minute"],self.getDiff()["second"])
    def remoev(self):
        """
        @desc: 删除计时器
        """
        #删除这个计时器
        with  open("timers.json","r") as f:
            data=json.load(f)
            for timer in data["timers"]:
                if timer["id"]==self.id:
                    data["timers"].remove(timer)
        with open("timers.json","w") as f:
            json.dump(data,f)
    def updateName(self,name):
        """
        @desc: 修改计时器名称
        :param name: 新的名称
        """
        with open("timers.json","r") as f:
            data=json.load(f)
            for timer in data["timers"]:
                if timer["id"]==self.id:
                    timer["name"]=name
        with open("timers.json","w") as f:
            json.dump(data,f)
    def updateDate(self,datetime):

        """
        @desc: 修改计时器时间
        :param datetime: 新的时间
        """
        with open("timers.json","r") as f:
            data=json.load(f)
            for timer in data["timers"]:
                if timer["id"]==self.id:
                    timer["datetime"]=datetime
        with open("timers.json","w") as f:
            json.dump(data,f)



