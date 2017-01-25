# -*- coding: utf-8 -*-

version = 'v2.0.4'

sampleConfStr = '''{

    # QQBot 的配置文件
    
    # 用户 somebody 的配置
    "nagizero" : {
        
        # QQBot-term 服务器端口号
        "termServerPort" : 8188,
        
        # http 服务器 ip，请设置为公网 ip
        # 注意本 ip 不是用来设置服务器的监听 ip 的，只是用来向用户显示图片链接地址的
        # 服务器的监听 ip 永远是 0.0.0.0 ，只要本 ip 不为空，服务器就会开启
        "httpServerIP" : "",
        
        # http 服务器端口号
        "httpServerPort" : 8189,
        
        # 自动登录的 QQ 号
        "qq" : "3164531174",
        
        # 接收二维码图片的邮箱账号
        "mailAccount" : "2569375308@qq.com",
        
        # 该邮箱的 IMAP/SMTP 服务授权码
        "mailAuthCode" : "kxwuwgskjrhadigd",
    
        # 显示/关闭调试信息
        "debug" : False,

        # QQBot 掉线后自动重启
        "restartOnOffline" : True,
    
    },
    
    # 请勿修改本项中的设置
    "默认配置" : {
        "termServerPort" : 8188,
        "httpServerIP" : "",
        "httpServerPort" : 8189,
        "qq" : "3164531174",
        "mailAccount" : "2569375308@qq.com",
        "mailAuthCode" : "kxwuwgskjrhadigd",
        "debug" : False,
        "restartOnOffline" : True,
    },

}
'''

import os, sys, ast, argparse
from utf8logger import SetLogLevel, INFO, RAWINPUT, utf8Stdout

class ConfError(Exception):
    pass

class QConf:
    def __init__(self, qq=None, user=None):        
        self.qq = None if qq is None else str(qq)
        self.user = None if user is None else str(user)
        self.version = version
        # self.readCmdLine()
        self.readConfFile()
        self.configure()
 
    def readConfFile(self):
        conf = ast.literal_eval(sampleConfStr)['默认配置']
        
        for k, v in conf.items():
            if not hasattr(self, k):
                setattr(self, k, v)
        
        if self.mailAccount and not self.mailAuthCode:
            msg = '请输入 %s 的 IMAP/SMTP 服务授权码： ' % self.mailAccount
            self.mailAuthCode = RAWINPUT(msg)

    def configure(self):
        SetLogLevel(self.debug and 'DEBUG' or 'INFO')

    def Display(self):
        INFO('QQBot-%s', self.version)
        INFO('配置完成')
        INFO('用户名： %s', self.user or '无')
        INFO('登录方式：%s', self.qq and ('自动（qq=%s）' % self.qq) or '手动')        
        INFO('命令行服务器端口号：%s', self.termServerPort)       
        INFO('HTTP 服务器 ip ：%s', self.httpServerIP or '无')       
        INFO('HTTP 服务器端口号：%s',
             self.httpServerIP and self.httpServerPort or '无')
        INFO('用于接收二维码的邮箱账号：%s', self.mailAccount or '无')
        INFO('邮箱服务授权码：%s', self.mailAccount and '******' or '无')
        INFO('调试模式：%s', self.debug and '开启' or '关闭')
        INFO('掉线后自动重启：%s', self.restartOnOffline and '是' or '否')
    
    tmpDir = os.path.join(os.path.expanduser('~'), '.qqbot-tmp')
    
    @classmethod
    def absPath(cls, rela):
        return os.path.join(cls.tmpDir, rela)

    def ConfPath(self):
        return self.absPath('%s.conf' % self.version[:4])

    def PicklePath(self):
        return self.absPath('%s-%s.pickle' % (self.version, self.qq))
    
    @classmethod
    def QrcodePath(cls, qrcodeId):
        return cls.absPath(qrcodeId+'.png')

if not os.path.exists(QConf.tmpDir):
    os.mkdir(QConf.tmpDir)

if __name__ == '__main__':
    QConf().Display()
    QConf(user='somebody').Display()
