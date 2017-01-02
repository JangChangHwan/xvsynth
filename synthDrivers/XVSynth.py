# coding: utf-8
# ver 0.2.0

from comtypes.client import CreateObject
import math
import speech
import synthDriverHandler, os, config, re, logging
from logHandler import log
from synthDriverHandler import SynthDriver, VoiceInfo, BooleanSynthSetting
import languageHandler
from collections import OrderedDict



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



class SynthDriver(synthDriverHandler.SynthDriver):
 supportedSettings = [SynthDriver.PitchSetting(), SynthDriver.RateSetting(), SynthDriver.VolumeSetting()]

# supportedSettings=(SynthDriver.VoiceSetting(),SynthDriver.VariantSetting(),SynthDriver.RateSetting(), SynthDriver.PitchSetting(), SynthDriver.InflectionSetting(), SynthDriver.VolumeSetting())
 description = 'SenseReader Synth'
 name = 'XVSynth'
 speakingLanguage=""

 @classmethod
 def check(cls):
  return InitializeXVSynth()

 def __init__(self):
  lang = languageHandler.getLanguage()
  self.speakingLanguage=lang

 def speak(self,speechSequence):
  try:
   for item in speechSequence:
    if isinstance(item, basestring):
     ctrl.Speak(item, si)
  except:
   pass

 def speakText(self, test, index=None):
  try:
   if isinstance(text, basestring):
    ctrl.Speak(text, si)
  except:
   pass

 def pause(self,switch):
  try:
   if not ctrl.Speaking: return
   ctrl.Stop()
  except:
   pass
 def cancel(self):
  try:
   if not ctrl.Speaking: return
   ctrl.Stop()
  except:
   pass

 def _get_rate(self):
  try:
   return si.Speed * 5
  except:
   pass


 def _set_rate(self, vl):
  try:
   si.Speed = int(math.ceil(vl * 0.2))
  except:
   pass
 


 def _get_volume(self):
  try:
   return si.Volume * 5
  except:
   pass


 def _set_volume(self, vl):
  try:
   si.Volume = int(math.ceil(vl * 0.2))
  except:
   pass



 def _get_pitch(self):
  try:
   return si.Pitch * 5
  except:
   pass


 def _set_pitch(self, vl):
  try:
   si.Pitch = int(math.ceil(vl * 0.2))
  except:
   pass
