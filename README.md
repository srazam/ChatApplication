# Chat Application

## Purpose of the Program
This is a chat application in which the client and server will be able to communicate with each other, using a socket module.

## Compiling/Running the Program on VS Code
You will first compile/run the server and then compile/run the client

### How to Compile/Run the Server
**First, compile/run the Server.py file by clicking the "Run Python File" in the top right-hand corder.**
In the terminal, it will then inquire to an enter an IP address so make sure that you enter a valid IP address or just press enter to set it to local host. Next it will inquire a port nunber so make sure that you enter a valid port number (greater than 1023) or just hit enter to have the default port of 8000. Make sure to also enter then wait for the client to connect. The client will be the first one to send the message.

### How to Compile/Run the Client 
**Next, compile/run the Client.py file by by selecting "Run without debugging"**
It will then inquire an IP address so make sure it's the same one you entered for the server. When it inquires the port number, make sure it's the same port number you entered for the server as well. The username you put for the client side should be different than the username for the server side, as to help you distinguish between the messages. The client has to be the first one to send a message. 

## Important Information
If there are different port numbers and/or IP addresses inputted in the client side, then there will be an error, stopping the client side but continuing the server side.

Make sure that the message you enter is not blank, for that is considered an invalid message and will stop the program entirely

In order to stop messaging each other, send "end" either on the client or server side and the program will end. 

## Example Terminal/Output (Using Default IP Address/Port)
#### Server Side 
Input an IP address or press enter for localhost: 
Input a port number or press enter for the default port: 
Enter your username: userOne
Ready to recieve/send messages via the server (wait for client): 

#### Client Side
Input an IP address or press enter for localhost: 
Input a port number or press enter for default port: 
Enter your username: userTwo35
Ready to recieve/send messages via the client: 
Enter a message: Hi there!

#### Server Side
userTwo35: Hi there!
Enter a message: Hello!

#### Client Side
userOne: Hello!
Enter a message: end
[Program would end for both client and server side]

## Acknolwedgments
### Resources
Geeks for Geeks: Extracting numbers from strings
W3Schools: For Python Basics
