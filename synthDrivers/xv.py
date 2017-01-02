# coding: utf-8

from comtypes.client import CreateObject

ctrl = None
si = None

def InitializeXVSynth():
	try:
		global ctrl, si
		obj = CreateObject('SenseReader.Application')
		ctrl = obj.SpeechControlers.Add('test')
		ctrl.Init('')
		si = ctrl.NewSpeakInfo()
		if ctrl is not None and si is not None:
			return True
		else:
			return False
	except:
		return False

