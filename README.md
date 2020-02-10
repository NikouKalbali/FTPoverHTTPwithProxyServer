# FTPoverHTTPwithProxyServer
There are two modules the first is a FTP client which accepts FTP commands and send them as HTTP messages to the second program. 
The second program works like a proxy server.  It accepts HTTP messages from the client program, unwrap the  FTP command and forward it to the actual intended FTP server. Similarly, it relays the reply ofthe FTP server wrapped in an HTTP message to the client program
