from socket import *

HOST = 'localhost'
PORT = 29876
ADDR = (HOST,PORT)
BUFSIZE = 4096

cli = socket(AF_INET, SOCK_STREAM)

cli.connect ((ADDR))

# data = cli.recv(BUFSIZE)
# print data
cli.send('H')
cli.send('12')
cli.send('1234')
cli.send('this is my test thing that i feel like sending at the moment yea...')
cli.send('ahhhhh real monsters')

cli.close()


