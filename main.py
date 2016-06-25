import socket
import string
import time

host = 'irc.snoonet.org'
port = 6667
nick = 'PredditBot'
ident = 'PredditBot'
realname = 'PredditBot'
bot_owner = 'IRCPortland'
room = '#portland'
read = ' '
password = 'O5nuOpB7pAHxy2VsRK1X'

irc_sock = socket.socket()
irc_sock.connect((host, port))
#irc_sock.send('/msg NickServ IDENTIFY ' + nick + ' ' + password + '\r\n')
#irc_sock.send('PASS ' + password + '\r\n')
irc_sock.send('USER ' + nick + ' 0 * :' + bot_owner + '\r\n')
irc_sock.send('NICK ' + nick + '\r\n')
time.sleep(5)
#irc_sock.send('USER ' + ident + ' ' + host + ' bla : ' + realname + 'n\r\n')
irc_sock.send('JOIN ' + room + '\r\n')


while True: #infinite loop to keep gathering text

    read = irc_sock.recv(500) #gets line of text
    if read:
        print(read) #prints it

       # if (if(line[0]=="PING"):
       #     s.send("PONG %s\r\n" % line[1]))

    #if read.find('Generic Intro Message') != -1: #if server intro message, join a channel

        #irc_sock.send('JOIN #portland \r\n')