"""
@author: hanhaoxin
@file: addTierUi.py
@time: 2024/2/15
@desc: 添加计时器页面
"""

from PySide6.QtWidgets import QMessageBox,QHBoxLayout,QLineEdit,QPushButton,QWidget,QVBoxLayout,QSizePolicy, QFrame,QLabel, QMainWindow
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from src.common import  uiTools

class addTimerUi(QMainWindow):
    def __init__(self,tm,parent=None):
        """
        @desc:添加定时器界面
        :param tm: 计时器管理器对象
        :param parent: 父元素
        """
        super().__init__(parent=parent)
        self.timerManager=tm
        self.initUI()
    def initUI(self):
        self.centralWidget= QWidget(self)
        self.setCentralWidget(self.centralWidget)
        self.centralWidget.setObjectName("centralWidget")
        self.centralWidget.setStyleSheet(uiTools.readQss((self.__class__.__name__)))

        self.setWindowTitle('添加重要日')
        #设置窗口大小不可变
        self.setFixedSize(400,400)
        self.centralWidget.setContentsMargins(10,10,10,10)

        self.title_label=QLabel("添加重要日",self.centralWidget)
        self.setObjectName("title_label")
        self.title_label.setAlignment(Qt.AlignCenter)
        title_label_font=QFont("微软雅黑",20)
        self.title_label.setFont(title_label_font)

        self.title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.data_entry=QFrame(self.centralWidget)
        self.data_entry.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.name_label=QLabel("名称",self.data_entry)
        self.name_entry=QLineEdit()
        self.name_entry.setMinimumSize(0,30)

        self.name_entry_layout=QHBoxLayout()
        self.name_entry_layout.addWidget(self.name_label)
        self.name_entry_layout.addWidget(self.name_entry)

        self.date_label=QLabel("日期",self.data_entry)
        self.date_year_entry=QLineEdit()
        self.date_year_entry.setMinimumSize(0,30)
        self.date_year_entry.setPlaceholderText("年")
        self.date_month_entry=QLineEdit()
        self.date_month_entry.setMinimumSize(0,30)
        self.date_month_entry.setPlaceholderText("月")
        self.date_day_entry=QLineEdit()
        self.date_day_entry.setMinimumSize(0,30)
        self.date_day_entry.setPlaceholderText("日")
        self.date_hour_entry=QLineEdit()
        self.date_hour_entry.setMinimumSize(0,30)
        self.date_hour_entry.setPlaceholderText("时")


        self.date_entry_layout=QHBoxLayout()
        self.date_entry_layout.addWidget(self.date_label)
        self.date_entry_layout.addWidget(self.date_year_entry)
        self.date_entry_layout.addWidget(self.date_month_entry)
        self.date_entry_layout.addWidget(self.date_day_entry)
        self.date_entry_layout.addWidget(self.date_hour_entry)


        self.data_entry_layout=QVBoxLayout()
        #self.data_entry_layout.addWidget(self.title_label)
        self.data_entry_layout.addLayout(self.name_entry_layout)
        self.data_entry_layout.addLayout(self.date_entry_layout)
        self.data_entry.setLayout(self.data_entry_layout)



        self.submit_button=QPushButton("提交",self.centralWidget)
        self.submit_button.setObjectName("submit_button")
        self.submit_button.setMaximumSize(9999999,50)
        self.submit_button.setMinimumSize(0,50)
        self.submit_button.clicked.connect(self.submit_data)
        self.submit_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.layout=QVBoxLayout(self.centralWidget)
        #self.layout.setContentsMargins(10,10,10,10)
        self.layout.addWidget(self.title_label)
        self.layout.addWidget(self.data_entry)
        self.layout.addWidget(self.submit_button)


        #设置窗口被关闭时的事件

    def closeEvent(self, event):
        self.close()
        self.parent().show()
    def submit_data(self):
        name=self.name_entry.text()
        year=self.date_year_entry.text()
        month=self.date_month_entry.text()
        day=self.date_day_entry.text()
        hour=self.date_hour_entry.text()

        if name=="" or year=="" or month=="" or day=="" or hour=="":
            QMessageBox.warning(self,"警告","输入不能为空")
            return

        #检测year,moth,day,hour是否是数字
        if  not year.isdigit() or not month.isdigit() or not day.isdigit() or not hour.isdigit():
            QMessageBox.warning(self,"警告","输入必须为数字")
            return

        #将year，month，day，hour转换为整数
        year=int(year)
        month=int(month)
        day=int(day)
        hour=int(hour)

        #检测year，month，day，hour是否在合理范围内
        if year<1900 or year>2099:
            QMessageBox.warning(self,"警告","年份必须在1900到2099之间")
            return
        if month<1 or month>12:
            QMessageBox.warning(self,"警告","月份必须在1到12之间")
            return

        if hour<0 or hour>23:
            QMessageBox.warning(self,"警告","小时必须在0到23之间")
            return

        #检测是否是闰年
        if month==2:
            if (year%4==0 and year%100!=0) or year%400==0:
                if day>29:
                    QMessageBox.warning(self,"警告","闰年2月份日期必须在1到29之间")
                    return
            else:
                if day>28:
                    QMessageBox.warning(self,"警告","闰年2月份日期必须在1到28之间")
                    return
        elif  month in [1,3,5,7,8,10,12]:
            if day>31:
                QMessageBox.warning(self,"警告","月份日期必须在1到31之间")
                return
        else:
            if day>30:
                QMessageBox.warning(self,"警告","月份日期必须在1到30之间")
                return

        #将year，month，day，hour转换为字符串
        year=str(year)
        month=str(month)
        day=str(day)
        hour=str(hour)

        #将year，month，day，hour转换为字符串，并在前面补0
        if len(month)==1:
            month="0"+month
        if len(day)==1:
            day="0"+day
        if len(hour)==1:
            hour="0"+hour
        datestr="%s-%s-%s %s"%(year,month,day,hour)

        if self.timerManager.addTimer(name,datestr):
            QMessageBox.information(self,"提示","添加成功")
            self.close()
        else:
            QMessageBox.warning(self,"警告","添加失败")
            self.initUI()




