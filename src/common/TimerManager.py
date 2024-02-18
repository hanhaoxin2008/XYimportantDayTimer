"""
@author: hanhaoxin
@file: TimerManager.py.py
@time: 2024/2/15
@desc: 定时器管理器
"""
from src.config import config
from src.common import Timer
import os
import json
class TimerManager:
    def __init__(self):
        """
        @desc: 初始化定时器管理器
        """

        self.timers=[]
        #检查timers.json是否存在
        if not os.path.exists(config.TIMERS_JSON_DIR):
            with open(config.TIMERS_JSON_DIR, 'w') as f:
                json.dump({"timers":[]}, f)
        self.readTimers()

    def addTimer(self,name,datetime):
        """
        @desc: 添加定时器
        :param name: 定时器名称
        :param datetime: 定时器时间
        :return:
        """
        try:
            newTimer={
                "name":name,
                "datetime":datetime
            }
            if self.timers==[]:
                newTimer["id"]=1
            else:
                #寻找最大的id
                maxId=max([timer["id"] for timer in self.timers])
                newTimer["id"]=maxId+1
            self.timers.append(newTimer)
            with open(config.TIMERS_JSON_DIR, 'w') as f:
                json.dump({"timers":self.timers}, f)
        except Exception as e:
            return False
        return  True
    def readTimers(self):
            """
            @desc: 读取定时器
            :return:
            """
            with open(config.TIMERS_JSON_DIR, 'r') as f:
                data=json.load(f)
                self.timers=data["timers"]

    def getTimers(self):
        """
        @desc: 获取定时器列表
        :return: Timer类列表
        """
        self.readTimers()
        TimerList=[]
        for  timer in self.timers:
            TimerList.append(Timer.Timer(timer["id"],timer["name"],timer["datetime"]))
        return TimerList
