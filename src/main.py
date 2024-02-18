from ui import mainUi
from common import TimerManager
from PySide6.QtWidgets import QApplication
import sys
if __name__ == '__main__':
    app = QApplication(sys.argv)
    tm=TimerManager.TimerManager()
    #win=addTimerUi.addTimerUi(tm)
    win=mainUi.mainUi(tm)
    win.show()
    sys.exit(app.exec())