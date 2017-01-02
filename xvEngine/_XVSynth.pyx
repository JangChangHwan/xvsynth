# coding: utf-8

from comtypes.client import CreateObject

class xvEngine(object):
	ctrl = None
	si = None

	def __init__(self):
		self.Initialize()

	def Initialize(self):
		try:
			app = CreateObject('SenseReader.Application')
			self.ctrl = app.SpeechControlers.Add('test')
			self.ctrl.Init('')
			self.si = self.ctrl.NewSpeakInfo()
			return True
		except:
			return False
