# coding: utf-8

from comtypes.client import CreateObject
import speech
import synthDriverHandler, os, config, re, logging
from logHandler import log
from synthDriverHandler import SynthDriver,VoiceInfo,BooleanSynthSetting
import languageHandler
from collections import OrderedDict

minValue = 0
maxValue = 10
XV = None
SI = None

def InitializeXVSynth():
	global XV, SI
	try:
		obj = CreateObject('SenseReader.Application')
		XV = obj.SpeechControlers.Add('test')
		XV.Init('')
		SI = XV.NewSpeakInfo()
	except:
		pass



class SynthDriver(synthDriverHandler.SynthDriver):
 supportedSettings = [SynthDriver.PitchSetting()]
# supportedSettings=(SynthDriver.VoiceSetting(),SynthDriver.VariantSetting(),SynthDriver.RateSetting(), SynthDriver.PitchSetting(), SynthDriver.InflectionSetting(), SynthDriver.VolumeSetting())
 description = 'SenseReader Synth'
 name = 'XVSynth'
 speakingLanguage=""

 @classmethod
 def check(cls):
  global XV, SI
  InitializeXVSynth()
  if XV is not None:
   return True
  else:
   return False


 def __init__(self):
  lang = languageHandler.getLanguage()
  self.rate = 4
  self.speakingLanguage=lang


 def speak(self,speechSequence):
  for item in speechSequence:
   if isinstance(item, basestring):
    XV.Speak(item, SI)

 def speakText(self, test, index=None):
  if isinstance(text, basestring):
   XV.Speak(text, SI)



 def pause(self,switch):
  XV.Stop()

 def cancel(self):
  XV.Stop()


 def _get_rate(self):
  pass

 def _set_rate(self, vl):
  pass

 def terminate(self):
  XV = SI = None
