from socket import * 
print ("You are in the proxy server now! \n")
serverIP = '127.0.0.1'
serverPortNumber = 2020
#to create an INET, STREAMing server socket
SSocket = socket(AF_INET,SOCK_STREAM)
SSocket.bind(('',serverPortNumber))

#listen(1) is the length of the backlog queue, which is the number of incoming connections
SSocket.listen(1)
ConnectionSocket, address = SSocket.accept()

# To create connection with a client waiting to recieve a http request to connect to a client 
connectionRequest = ConnectionSocket.recv(2000)
print("a client has started request: \n")
print(connectionRequest.decode())
# connecting site to our server 
ftp = socket(AF_INET,SOCK_STREAM)
#connecting to web server on port
ftp.connect(('ftp.cdc.gov', 21))
#recieving the reply from 
reply = (ftp.recv(4096)).decode()
print ("FTP ServerResponse:\n",reply)
ServerResponse = "The requested action has been successfully completed.\n"+ reply
ConnectionSocket.send(ServerResponse.encode())
#entering hard coded password for user
def UserPassword(ClientRequest):
    password = 'PASS ' + 'kalbaln@mcmaster.ca' + '\r\n'
    ftp.send(password.encode())
    reply = (ftp.recv(4096)).decode()
    print("FTP request is: "+ ClientRequest+ "FTP ServerResponse: "+reply)
    ServerResponse = "The requested action has been successfully completed.\n"+ reply
    ConnectionSocket.send(ServerResponse.encode())
#entering hard coded user id for the client
def userID(ClientRequest):
    user = 'USER ' + 'anonymous' + '\r\n'
    ftp.send(user.encode())
    reply = (ftp.recv(4096)).decode()
    print("FTP request is: "+ ClientRequest+ "FTP ServerResponse: "+reply)
    ServerResponse = "The requested action has been successfully completed.\n"+ reply
    ConnectionSocket.send(ServerResponse.encode())
# function to implement Print working directory. Returns the current directory of the host.
def pwd(ClientRequest):
    pwd = 'PWD \r\n'
    ftp.send(pwd.encode())
    reply = (ftp.recv(4096)).decode()
    print("FTP request is: "+ ClientRequest+ "FTP ServerResponse: "+reply)
    ServerResponse = "The requested action has been successfully completed.\n"+ reply
    ConnectionSocket.send(ServerResponse.encode())

# function to implement Change working directory.
def cwd(ClientRequest):
    cwd = 'CWD ' + '/pub/' + '\r\n'
    ftp.send(cwd.encode())
    reply = (ftp.recv(4096)).decode()
    print("FTP request is: "+ ClientRequest+ "FTP ServerResponse: "+reply)
    ServerResponse = "The requested action has been successfully completed.\n"+ reply
    ConnectionSocket.send(ServerResponse.encode())

# function to implement change directory to root directory
def cdup(ClientRequest):
    cdup = 'CDUP \r\n'
    ftp.send(cdup.encode())
    reply = (ftp.recv(4096)).decode()
    print("FTP request is: "+ ClientRequest+ "FTP ServerResponse: "+reply)
    ServerResponse = "The requested action has been successfully completed.\n"+ reply
    ConnectionSocket.send(ServerResponse.encode())
#doesnt work ?
def syst(ClientRequest):
    cdup = 'SYST \r\n'
    ftp.send(cdup.encode())
    reply = (ftp.recv(4096)).decode()
    print("FTP request is: "+ ClientRequest+ "FTP ServerResponse: "+reply)
    ServerResponse = "The requested action has been successfully completed.\n"+ reply
    ConnectionSocket.send(ServerResponse.encode())
#doesnt work ?    
def Help(ClientRequest):
    cdup = 'HELP \r\n'
    ftp.send(cdup.encode())
    reply = (ftp.recv(4096)).decode()
    print("FTP request is: "+ ClientRequest+ "FTP ServerResponse: "+reply)
    ServerResponse = "The requested action has been successfully completed.\n"+ reply
    ConnectionSocket.send(ServerResponse.encode())
#closes socket session    
def quitting(ClientRequest):
    quitting = "QUIT\r\n"
    ftp.send(quitting.encode())
    reply = (ftp.recv(4096)).decode()
    print("FTP request is: "+ ClientRequest+ "FTP ServerResponse: "+reply)
    ServerResponse = "The requested action has been successfully completed.\n"+ reply
    connectionSocket.send(ServerResponse.encode())
    ftp.close()
    ConnectionSocket.close()
    SSocket.close()
StayInLoop=True
while StayInLoop==True:
    ClientRequest = ConnectionSocket.recv(2000)
    ClientRequest = ClientRequest.decode()
    print("Server is waiting to receive your FTP commands   \n")
    if ClientRequest == ("pass\n"):
        UserPassword(ClientRequest)
    elif ClientRequest == ("user\n"):
        userID(ClientRequest)
    elif ClientRequest == ("cwd\n"):
        cwd(ClientRequest)
    elif ClientRequest == ("pwd\n"):
        pwd(ClientRequest)
    elif ClientRequest == ("cdup\n"):
        cdup(ClientRequest)
    elif ClientRequest == ("syst\n"):
        syst(ClientRequest)
    elif ClientRequest == ("help\n"):
        Help(ClientRequest)
    elif ClientRequest == ("quit\n"):
        quitting(ClientRequest)
        break
else:
    print ("Invalid command. Please try another command")
        

