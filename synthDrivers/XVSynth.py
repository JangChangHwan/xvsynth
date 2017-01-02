# coding: utf-8
# ver 0.1.1

import xv
import speech
import synthDriverHandler, os, config, re, logging
from logHandler import log
from synthDriverHandler import SynthDriver,VoiceInfo,BooleanSynthSetting
import languageHandler
from collections import OrderedDict

minValue = 0
maxValue = 10

class SynthDriver(synthDriverHandler.SynthDriver):
 supportedSettings = [SynthDriver.PitchSetting()]
# supportedSettings=(SynthDriver.VoiceSetting(),SynthDriver.VariantSetting(),SynthDriver.RateSetting(), SynthDriver.PitchSetting(), SynthDriver.InflectionSetting(), SynthDriver.VolumeSetting())
 description = 'SenseReader Synth'
 name = 'XVSynth'
 speakingLanguage=""

 @classmethod
 def check(cls):
  return xv.InitializeXVSynth()

 def __init__(self):
  try:
   lang = languageHandler.getLanguage()
   self.speakingLanguage=lang
   xv.si.Speed = 2
   xv.si.Volume = 4
   xv.si.Pitch = 4
  except:
   pass

 def speak(self,speechSequence):
  try:
   for item in speechSequence:
    if isinstance(item, basestring):
     xv.ctrl.Speak(item, xv.si)
  except:
   pass

 def speakText(self, test, index=None):
  try:
   if isinstance(text, basestring):
    xv.ctrl.Speak(text, xv.si)
  except:
   pass

 def pause(self,switch):
  try:
   if not xv.ctrl.Speaking: return
   xv.ctrl.Stop()
  except:
   pass
 def cancel(self):
  try:
   if not xv.ctrl.Speaking: return
   xv.ctrl.Stop()
  except:
   pass

 def _get_rate(self):
  pass

 def _set_rate(self, vl):
  pass
