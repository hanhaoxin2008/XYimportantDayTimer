
from ..ui import modifyTimerUi
from PySide6.QtCore import  QTimer,QDateTime
from PySide6.QtWidgets import QMessageBox,QMenu,QSizePolicy,QHBoxLayout,QWidget,QLabel,QVBoxLayout,QPushButton
from  PySide6.QtCore import Qt
from  PySide6.QtGui import QFont,QAction,QCursor
from src.common import Timer
from  PySide6.QtWidgets import QApplication, QMainWindow
class timerWidget(QWidget):
    def __init__(self,timer,parent=None):
        super().__init__(parent=parent)
        # 初始化UI
        self.timer=timer
        self.parent_win=parent
        self.initUi()
        self.qtimer = QTimer()
        self.qtimer.timeout.connect(self.updateDate)
        self.StartTimer()

    def initUi(self):
        #设置窗口高度为100，宽度可拉伸
        self.setMinimumHeight(100)
        self.setMaximumHeight(100)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.root_layout=QHBoxLayout(self)
        self.name_label = QLabel(self.timer.getName(),self)
        self.name_label.setAlignment(Qt.AlignLeft)
        self.name_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.name_label.setFont(QFont('微软雅黑', 20))

        self.date_label= QLabel(self.timer.getDatetime(),self)
        self.date_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.date_label.setAlignment(Qt.AlignLeft)
        self.date_label.setFont(QFont('微软雅黑', 10))


        self.date_d_label= QLabel("00:00:00",self)
        #设置垂直居中
        self.date_d_label.setAlignment(Qt.AlignCenter)
        #self.date_d_label.setAlignment(Qt.AlignRight)
        self.date_d_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        self.date_d_label.setMaximumHeight(100)
        self.date_d_label.setMinimumHeight(100)
        self.date_d_label.setFont(QFont('微软雅黑', 25))

        self.layout_label= QLabel()
        self.layout_label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)

        self.layout1= QVBoxLayout()
        self.layout1.addWidget(self.name_label)
        self.layout1.addWidget(self.date_label)
        self.root_layout.addLayout(self.layout1)
        self.root_layout.addWidget(self.layout_label)
        self.root_layout.addWidget(self.date_d_label)
        #设置右键菜单
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.showMenu)
    def  showMenu(self,pos):
        popMenu = QMenu()
        popMenu.addAction(QAction(u'修改', self, triggered=self.modify))
        popMenu.addAction(QAction(u'删除', self, triggered=self.remove))
        popMenu.exec_(QCursor.pos())
    def modify(self):
        modifyui= modifyTimerUi.modifyTimerUi(self.timer,self.parent_win)
        modifyui.show()
        self.parent_win.hide()
    def remove(self):
        #选择框
        reply = QMessageBox.question(self, 'Message',
                                     "确定删除吗？", QMessageBox.Yes ,QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.timer.remoev()
            self.parent_win.initUI()

    def updateDate(self):
        timeDisplay = self.timer.toStr()
        self.date_d_label.setText(timeDisplay)

    def StartTimer(self):
        # 开启定时器,执行时间/任务的频率是100ms
        self.qtimer.start(100)

"""
app = QApplication([])
window = QMainWindow()
timer=Timer.Timer(1,"高考","2026-6-6 00")
widget = timerWidget(timer)
window.setCentralWidget(widget)
window.show()
app.exec()
"""
