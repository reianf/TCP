For my Networks and Distributed Systems course, I implemented both a TCP server and a TCP client using my macOS Terminal app.
<br><br>
<b>tcpserver.py</b><br>
The server accepts a connection from a client and receives a text message of no more than 256
characters. The server converts each character by replacing it with the next character in the ASCII sequence. 
<br><br>
<b>tcpclient.py</b><br>
The client connects to the server using the same port and passes the message to the server. 
The client will then display the converted message from the server.<br><br>
Example input: <b>Hello World</b><br>
Example output: <b>Ifmmp!Xpsme</b><br><br>
<b>Execution:</b><br><br>
![Picture1](https://user-images.githubusercontent.com/34120074/57265041-77103900-702a-11e9-8994-86895dcb4def.png)
