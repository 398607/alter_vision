# - coding:gbk
from qqbot import QQBot
from qqbot.qconf import QConf

class AlterVision(object):

	def __init__(self):
		self.bot = QQBot()
		# print(globals()['sampleConfStr'])
		self.bot.Login()


	def vision(self, msg):
		self.bot.Send('buddy', qq='2569375308', content=msg)

if __name__ == '__main__':
	alter = AlterVision()
	alter.vision('test 1')
	alter.vision('test 2')
