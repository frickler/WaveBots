'''
this is pylurinator

@author: fri
'''
from waveapi import events
from waveapi import robot
from waveapi import appengine_robot_runner
from waveapi.events import Context
import logging

def OnWaveletSelfAdded(event, wavelet):
    """Invoked when the robot has been added.""" 
    logging.info("OnWaveletSelfAdded called")

def OnBlibSubmitted(event, wavelet):
    #logging.info("OnBlipSubmitted called")
    blip = event.blip

    # ha ha
    blip.all('f').replace('')
    blip.all('F').replace('')
    #if 'proprietary' not in blip.text:
    #    blip.append('\nPS: proprietary software rulez...\n')

if __name__ == '__main__':
    myRobot = robot.Robot('pyLurinator',
                          image_url='http://pylurinator.appspot.com/icon.png',
                          profile_url='http://frickler.ch')
    myRobot.register_handler(events.WaveletSelfAdded, OnWaveletSelfAdded)
    myRobot.register_handler(events.BlipSubmitted, OnBlibSubmitted, Context.ALL)
    appengine_robot_runner.run(myRobot)
