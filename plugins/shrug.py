import random

from util import hook

@hook.command
def shrug(inp, say=None):
    shrug_bytes = bytearray([0xE3, 0x83, 0x84])
    macron = bytearray([0xC2, 0xAF])
    shrug = macron.decode('utf-8') + u'\_(' + shrug_bytes.decode('utf-8') + u')_/' + macron.decode('utf-8')
    say(shrug)