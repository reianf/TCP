For my Networks and Distributed Systems course, I implemented both a TCP server and a TCP client using my macOS Terminal app.
<br><br>
<b>tcpserver.py</b><br>
The server accepts a connection from a client and receives a text message of no more than 256
characters. The server converts each character by replacing it with the next character in the ASCII sequence. 
<br>
<b>tcpclient.py</b><br>
The client connects to the server using the same port and passes the message to the server. 
The client will then display the converted message from the server.<br>
Example input: <b>Hello World</b><br>
Example output: <b>Ifmmp!Xpsme</b><br><br>
Execution:<br>
![image](/uploads/7ddea27337201e04f7f4ce6339ca58b6/image.png)
