# coding: utf-8
import os
import globalPluginHandler
from synthDriverHandler import *

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def __init__(self):
		super(GlobalPlugin, self).__init__()

		obj = getSynth()
		if obj.name != 'XVSynth': return
		setSynth('espeak')
