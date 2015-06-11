from socket import * 
from struct import *


HOST = ''
PORT = 29876
ADDR = (HOST,PORT)
BUFSIZE = 20
# created a small buffer size in order to test to see if my server would continue to 
# get the rest of the message regardless of the buffersize. 

serv = socket(AF_INET, SOCK_STREAM)

serv.bind((ADDR))
serv.listen(5)
print 'listening...'

while True: 
	conn,addr = serv.accept()
	print '... connected!'

	version = unpack("B", conn.recv(1))[0]
	message = unpack("H", conn.recv(2)[::-1])[0]
	userid = unpack("I", conn.recv(4)[::-1])[0]

	# [::-1] this is to deal with network byte order and endianness I had help 
	# with this part as I did not know what big endianness and small endianness 
	# was prior to this coding challenge. 
	payload = ""
	while True:
		buf = conn.recv(BUFSIZE)
		if not buf:
			break
		payload += buf

	print 'Version: %s, Message Type: %s, User id: %s, Payload: %s' %(version, message, userid, payload)
		
 
# Currently my program can only send one message per connection which is inefficient.
# Something that could fix thiswould be to count the length of the payload which 
# will determin how long the variable length ASCII string is. By finding the 
# length we can send multiple messages per connection. 


# Right now my code will only recieve messages from one client at a time 
# then it closes the connection when everything has been sent. given more
# time I would have tried to look into multi threading to try connect to more
# than one client at a time. 
 