from ui import addTimerUi
from PySide6.QtWidgets import QApplication
import sys
from common import TimerManager
if __name__ == '__main__':
    app = QApplication(sys.argv)
    tm=TimerManager.TimerManager()
    win=addTimerUi.addTimerUi(tm)
    win.show()
    sys.exit(app.exec())