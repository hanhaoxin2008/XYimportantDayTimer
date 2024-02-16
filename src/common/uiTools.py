from src.config import config
from src.common.setting import setting
def readQss(classname):
    filename=config.QSS_DIR+classname +"_"+setting.getUiTheme()+ '.qss'
    with open(filename,encoding='utf-8') as f:
        return f.read()