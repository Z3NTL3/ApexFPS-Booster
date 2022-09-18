import os
from stat import S_IWRITE,S_IREAD
import shutil
import sys

'''
    Best automated Apex Video Config Tool

    RES: 1680x1050

    FPS BOOSTED TILL MAX !!!!!
'''

USER_DIR = os.getenv('UserProfile')
APEX_DIR = "{userdir}\\{saved_path}".format(
    userdir = USER_DIR,
    saved_path= 'Saved Games\\Respawn\\Apex\\local\\videoconfig.txt'
)
PATH = os.path.dirname(__file__)

def activateReadMode(path):
    '''
        This activates read mode for file video.config.txt
    '''
    os.chmod(path, S_IREAD)
    return 1

def activateWriteMode(path):
    '''
        This activates write mode for file video.config.txt
    '''
    os.chmod(path, S_IWRITE)
    return 1

def create(path):
    shutil.copyfile(f'{PATH}\\config\\videoconfig.txt', path)
    return

def Start():
    '''
        Start installing config
    '''
    activateWriteMode(APEX_DIR)
    create(APEX_DIR)

    activateReadMode(APEX_DIR)
    
    sys.stdout.write('Completed. You can launch Apex now')
    sys.stdout.flush()
    return

if __name__ == '__main__':
    Start()
