
"""
@author: hanhaoxin
@file: uiTools.py
@time: 2024/2/16
@desc: ui工具
"""
from ..config import config
from ..common.setting import setting
def readQss(classname):
    """
    读取qss文件
    :param classname: ui类的名称
    :return: qss文本
    """
    filename=config.QSS_DIR+classname +"_"+setting.getUiTheme()+ '.qss'
    with open(filename,encoding='utf-8') as f:
        return f.read()