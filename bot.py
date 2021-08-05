#!/usr/bin/env python

import os
import sqlite3
import queue
import sys
import traceback
import time
from core import reload
from core.config import do_config
from core.main_input import mainInput

class Bot(object):
    def __init__(self):
        self.conns = {}
        self.persist_dir = os.path.abspath('persist')
        if not os.path.exists(self.persist_dir):
            os.mkdir(self.persist_dir)
        self._config_mtime = 0
        
bot = Bot()

def main():
    sys.path += ['plugins']  # so 'import hook' works without duplication
    sys.path += ['lib']
    os.chdir(os.path.dirname(__file__) or '.')  # do stuff relative to the install directory

    print ('Loading plugins')

    # bootstrap the reloader
    eval(compile(open(os.path.join('core', 'reload.py'), 'U').read(),
                 os.path.join('core', 'reload.py'), 'exec'),
         globals())
    reload(bot, init=True)

    print ('Connecting to IRC')

    try:
        do_config(bot)
        if not hasattr(bot, 'config'):
            exit()
    except Exception as e:
        print ('ERROR: malformed config file:', e)
        traceback.print_exc()
        sys.exit()

    print ('Running main loop')

    while True:
        reload(bot)  # these functions only do things
        do_config(bot)  # if changes have occured

        for conn in bot.conns.values():
            try:
                out = conn.out.get_nowait()
                mainInput(bot, conn, out)
            except queue.Empty:
                pass
        while all(conn.out.empty() for conn in bot.conns.values()):
            time.sleep(.1)

if __name__ == '__main__':
    main()
