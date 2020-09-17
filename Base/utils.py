import logging.handlers
import os


def get_logger():
    """日志初始化"""
    # 声明日志器
    logger = logging.getLogger()
    # 设置日志器级别
    logger.setLevel(logging.INFO)
    # 处理器 控制台
    sh = logging.StreamHandler()
    # 处理器 文件
    trfh = logging.handlers.TimedRotatingFileHandler(filename='./Log' + os.sep + "hm.log", when='midnight',
                                                     interval=1, backupCount=7, encoding='utf-8')

    # 格式化字符串
    fm = "%(asctime)s %(levelname)s [%(filename)s-%(funcName)s:%(lineno)d] -%(message)s"
    # 格式化器
    formatter = logging.Formatter(fm)
    # 处理器添加到日志器
    logger.addHandler(sh)
    logger.addHandler(trfh)
    # 格式化器添加到处理器
    sh.setFormatter(formatter)
    trfh.setFormatter(formatter)
