import socket, sys, re
from math import *
import base64

server = "irc.root-me.org"  # settings
channel = "#root-me_challenge"
botnick = "yckai"
#input('wait1')
irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # defines the socket

#input('wait2')
print ("connecting to:" + server)

#input('wait3')
irc.connect((server, 6667))

#input('wait4')  # connects to the server
msg = "USER "+ botnick +" "+ botnick +" "+ botnick +" :Beter than Enigma\n"
irc.send(msg.encode("Utf8"))  # user authentication
text = irc.recv(4096)  # receive the text
print(text)

#input('wait5')
msg = "NICK " + botnick + "\n"
irc.send(msg.encode("Utf8"))  # sets nick
text = irc.recv(4096)  # receive the text
print(text)

#input('wait6')
msg = "JOIN " + channel + "\n"
irc.send(msg.encode("Utf8"))  # join the chan
text = irc.recv(4096)  # receive the text
print(text)

msg = "PRIVMSG candy !ep2 \n"
irc.send(msg.encode("Utf8"))  # auth

while 1:
    text = irc.recv(4096)  # receive the text
    print(text)
    PRIVMSG = re.search("PRIVMSG", str(text))
    if PRIVMSG is not None :
        a = str(text).split(":")
        b = str(a[2]).replace("\\r\\n'", "")
        print(str(b))
        b=base64.b64decode(str(b))
        b=b.decode("utf-8")
        print(str(b))
        msg= "PRIVMSG candy !ep2 -rep " + str(b) +" \n"
        irc.send(msg.encode("Utf8"))