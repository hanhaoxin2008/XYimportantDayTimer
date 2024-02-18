"""
@author: hanhaoxin
@file: addTierUi.py
@time: 2024/2/17
@desc: 主界面ui
"""

from PySide6.QtWidgets import QListWidget,QListWidgetItem,QHBoxLayout,QPushButton,QFrame,QWidget,QLabel,QMainWindow,QVBoxLayout,QSizePolicy
from  PySide6.QtCore import Qt
from  PySide6.QtGui import QFont
from src.common import uiTools
from src.ui import addTimerUi,timerWidget
class mainUi(QMainWindow):

    def __init__(self,tm):
        """
        @desc:添加定时器界面
        :param tm: 计时器管理器对象
        """
        super().__init__()
        self.timerm=tm
        self.initUI()

    def initUI(self):
        """
        @desc:初始化界面
        :return:
        """
        #设置默认大小
        self.resize(800,600)

        #设置central widegt
        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)
        self.centralWidget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.centralWidget.setObjectName("centralWidget")
        #添加样式
        self.centralWidget.setStyleSheet(uiTools.readQss(self.__class__.__name__))
        #设置窗口标题
        self.setWindowTitle('重要日计时器')

        #添加标题标签
        self.title_label=QLabel('重要日',self.centralWidget)
        self.title_label.setSizePolicy(QSizePolicy.Preferred,QSizePolicy.Fixed)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setFont(QFont("微软雅黑",25))

        #添加按钮区域
        self.button_frame=QFrame(self.centralWidget)
        self.button_frame.setSizePolicy(QSizePolicy.Preferred,QSizePolicy.Fixed)

        #添加重要日按钮
        self.add_timer_button=QPushButton("添加重要日",self.button_frame)
        self.add_timer_button.setObjectName("add_timer_button")
        self.add_timer_button.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
        self.add_timer_button.setMinimumSize(100,30)
        self.add_timer_button.clicked.connect(self.add_tier_button_clicked)
        self.button_frame.setLayout(QHBoxLayout())
        self.button_frame.layout().addWidget(self.add_timer_button)
        self.button_frame.layout().setAlignment(Qt.AlignLeft)

        #重要日列表区域
        self.list_frame=QFrame(self.centralWidget)
        self.list_frame.setSizePolicy(QSizePolicy.Preferred,QSizePolicy.Preferred)
        self.timer_list=QListWidget(self.list_frame)
        self.timer_list.setSizePolicy(QSizePolicy.Preferred,QSizePolicy.Preferred)
        self.list_frame.setLayout(QVBoxLayout())
        self.list_frame.layout().addWidget(self.timer_list)
        self.tw_list = []

        t_list = self.timerm.getTimers()
        print(t_list)
        for timer in t_list:
            iteam=QListWidgetItem()

            self.timer_list.addItem(iteam)
            tw = timerWidget.timerWidget(timer, self)
            #tw.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
            #self.list_frame.layout().addWidget(tw)
            self.timer_list.setItemWidget(iteam, tw)
            iteam.setSizeHint(tw.sizeHint())
            self.tw_list.append(tw)
        self.list_frame_layout_label=QLabel()
        self.list_frame_layout_label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        #self.list_frame.layout().addWidget(self.list_frame_layout_label)
        #设置窗口布局
        self.root_layout=QVBoxLayout(self.centralWidget)
        self.root_layout.addWidget(self.title_label)
        self.root_layout.addWidget(self.button_frame)
        self.root_layout.addWidget(self.list_frame)





    def add_tier_button_clicked(self):
        """
        @desc:添加重要日按钮被点击时
        :return:
        """
        #初始化addtimerui
        add_timer_ui=addTimerUi.addTimerUi(self.timerm,self)
        add_timer_ui.show()
        #隐藏本窗口
        self.hide()