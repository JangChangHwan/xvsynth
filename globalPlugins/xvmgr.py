# coding: utf-8

import globalPluginHandler
from synthDriverHandler import setSynth, getSynth

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def __init__(self):
		super(GlobalPlugin, self).__init__()

		obj = getSynth()
		if obj.name == 'XVSynth' and obj.xv.ctrl == None:
			setSynth('espeak')
