import random
 
from util import hook
 
butts = ["(_|_)", "(_o_)", "(‿ˠ‿)", "(‿.ꜟ‿)","(   ㅅ   )","(‿|‿)"]
 
@hook.command
def butt(inp):
    returnedbutt = random.choice(butts)
    return returnedbutt