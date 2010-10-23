'''
this is blipcleaner

@author: fri
'''
from waveapi import events
from waveapi import robot
from waveapi import appengine_robot_runner
from waveapi.events import Context
import logging

BOT_ADDRESS='blipcleaner@appspot.com'

def OnWaveletSelfAdded(event, wavelet):
    """Invoked when the robot has been added.""" 
    logging.info("OnWaveletSelfAdded called")
    wavelet.reply("""
    hiho - blipcleaner here
     
    use <forcedelete> to delete a blip and all its childs
    
    use <delete> and </delete> to delete all blips between those tags
    
    IMPORTANT set the </delete> tag first (or you will purge all childs...)""")

def OnBlibSubmitted(event, wavelet):
    logging.info("OnBlipSubmitted called")

    # deletes all blips until the </delete> tag is found
    if '<delete>' in event.blip.text:
        deleteRec(event.blip, wavelet, True)
    elif '<forcedelete>' in event.blip.text and not BOT_ADDRESS in event.blip.contributors:
        #  on <forcedelete> we delete the blip and its childs recursively
        deleteRec(event.blip, wavelet)
        
def deleteRec(blip, wavelet, search_for_end_tag=False):
    """
    deletes recursively a blip and all its childs
    if search_for_end_tag is set to True, the function stops
    as soon as there is a blip with </delete> in it
    """
    if len(blip.child_blips) > 0:
        for c in blip.child_blips:
            if search_for_end_tag:
                # if there is an end tag, stop the iteration and return
                if '</delete>' in c.text:
                    wavelet.delete(c)
                    return
            deleteRec(c, wavelet)
            
    # never delete the root blip!
    if not blip.is_root():
        wavelet.delete(blip)

if __name__ == '__main__':
    myRobot = robot.Robot('blipcleaner',
                          image_url='http://blipcleaner.appspot.com/assets/icon.jpg',
                          profile_url='http://frickler.ch')
    myRobot.register_handler(events.WaveletSelfAdded, OnWaveletSelfAdded)
    myRobot.register_handler(events.BlipSubmitted, OnBlibSubmitted, Context.ALL)
    appengine_robot_runner.run(myRobot)
