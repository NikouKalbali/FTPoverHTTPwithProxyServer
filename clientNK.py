from socket import * 
serversIP = '127.0.0.1'
serverPortNumber = 2020
CSocket = socket(AF_INET,SOCK_STREAM)

#entering hard coded password for user
def UserPassword(parameter):
    ClientRequest = ("pass\n")
    CSocket.sendall(ClientRequest.encode())
    print ('Your request has been sent: \n')
    ServerResponse = CSocket.recv(2000)
    print('The Servers Response to command:')
    print(ServerResponse.decode())
#entering hard coded user id for the client   
def userID(parameter):
    ClientRequest = ("user\n")
    CSocket.sendall(ClientRequest.encode())
    print ('Your request has been sent: \n')
    ServerResponse = CSocket.recv(1024)
    print('The Servers Response to command:')
    print(ServerResponse.decode())
# function to implement Print working directory. Returns the current directory of the host.    
def pwd(parameter):
    ClientRequest = ("pwd\n")
    CSocket.sendall(ClientRequest.encode())
    print ('Your request has been sent: \n')
    ServerResponse = CSocket.recv(1024)
    print('The Servers Response to command:')
    print(ServerResponse.decode())
# Change working directory
def cwd(parameter):
    ClientRequest = ("cwd\n")
    CSocket.sendall(ClientRequest.encode())
    print ('Your request has been sent: \n')
    ServerResponse = CSocket.recv(1024)
    print('Server Response:\n')
    print(ServerResponse.decode())
# function to implement change directory to root directory
def cdup(parameter):
    ClientRequest = ("cdup\n")
    CSocket.sendall(ClientRequest.encode())
    print ('Your request has been sent: \n')
    ServerResponse = CSocket.recv(1024)
    print('The Servers Response to command:')
    print(ServerResponse.decode())
#doesnt work ?
def Help(parameter):
    ClientRequest = ("help\n")
    CSocket.sendall(ClientRequest.encode())
    print ('Your request has been sent: \n')
    ServerResponse = CSocket.recv(1024)
    print('The Servers Response to command:')
    print(ServerResponse.decode())
#doesnt work ?
def syst(parameter):
    ClientRequest = ("syst\n")
    CSocket.sendall(ClientRequest.encode())
    print ('Your request has been sent: \n')
    ServerResponse = CSocket.recv(1024)
    print('The Servers Response to command:')
    print(ServerResponse.decode())
#closes socket session  
def quitting(parameter):
    ClientRequest = ("POST /quit \r\n")
    CSocket.sendallall(ClientRequest.encode())
    print ('Your request has been sent: \n')
    ServerResponse = CSocket.recv(1024)
    print('The Servers Response to command:')
    print(ServerResponse.decode())
    CSocket.close()
def CreateConnection(parameter):
    CSocket.connect((serversIP,serverPortNumber))
    print ("connected to serve!!")
    ClientRequest = ("GET /" + 'ftp.cdc.gov')
    CSocket.sendall(ClientRequest.encode())
    print ('Your request has been sent: \n')
    ServerResponse = (CSocket.recv(1024)).decode()
    print ('Response of proxy server is:\n')
    print(ServerResponse)
    return
ForeverLOOP= True
while ForeverLOOP==True:
    UserCommand = input("Please enter a FTP command ")
    print ("Client is sending your request to the server...\n")
    #Connect to the given host and port.
    UserCommand = UserCommand.lower()
    if UserCommand == "user":
        userID(UserCommand)
    elif UserCommand == "ftp ftp.cdc.gov":
        CreateConnection(UserCommand)
    elif UserCommand == "pass":
        UserPassword(UserCommand)
    # pwd()Return the pathname of current directory on the server side
    elif UserCommand == "cwd":
        cwd(UserCommand)
    elif UserCommand == "pwd":
        pwd(UserCommand)
    # Set the current directory on to the server.
    #navigate back to root directory
    elif UserCommand == "cdup":
        cdup(UserCommand)
    elif UserCommand == "help":
        Help(UserCommand)
    elif UserCommand == "syst":
        syst(UserCommand)
    # Sendall a QUIT command to the server and close the connection
    elif UserCommand == "quit":
        quitting(UserCommand)
        break
else:
    print ("Invalid Command. Try Again.")

