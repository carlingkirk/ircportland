import inspect
import json
import os
from core.irc import SSLIRC, IRC

def find_config():
    # for backwards compatibility, look for either 'config' or 'config.json'
    if os.path.exists('config'):
        return 'config'
    return 'config.json'

def save(conf):
    json.dump(conf, open(find_config(), 'w'), sort_keys=True, indent=2)

if not os.path.exists(find_config()):
    open('config.json', 'w').write(inspect.cleandoc(
        r'''
        {
          "connections":
          {
            "local irc":
            {
              "server": "localhost",
              "nick": "skybot",
              "channels": ["#test"]
            }
          },
          "prefix": ".",
          "disabled_plugins": [],
          "disabled_commands": [],
          "acls": {},
          "api_keys": {},
          "censored_strings":
          [
            "DCC SEND",
            "1nj3ct",
            "thewrestlinggame",
            "startkeylogger",
            "hybux",
            "\\0",
            "\\x01",
            "!coz",
            "!tell /x"
          ]
        }''') + '\n')


def do_config(bot):
    # reload config from file if file has changed
    config_mtime = os.stat(find_config()).st_mtime
    if bot._config_mtime != config_mtime:
        try:
            bot.config = json.load(open(find_config()))
            bot._config_mtime = config_mtime
            for name, conf in bot.config['connections'].items():
                if name in bot.conns:
                    bot.conns[name].set_conf(conf)
                else:
                    if conf.get('ssl'):
                        bot.conns[name] = SSLIRC(bot, conf)
                    else:
                        bot.conns[name] = IRC(bot, conf)
        except ValueError as e:
            print ('ERROR: malformed config!', e)
