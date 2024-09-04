import socket as s
import io

invalidInput = True #Used for keeping the user input in a loop

#Asking the user to input an IP Address and checking to make sure it's valid
#If it's invalid, the user will be prompted to enter another IP address
while (invalidInput):
    server_ip = input("Input an IP address or press enter for localhost: ")

    #If the user enters/leaves the input blank, then the IP address is localhost 
    if (server_ip == ""):
        server_ip = "localhost"
        invalidInput = False
    #If the user enters an actual IP address...
    else:
        #Get all integers from the string
        allNums = [int(i) for i in server_ip.split(".") if i.isdigit()]

        #If there are more/less than 4 integers in the string, it's an invalid IP address
        if (len(allNums) > 4 or len(allNums) < 4):
            print("Invalid IP Address. Try again!\n")
            continue

        #If any of the integers are greater than 255 or less than 0, it's an invalid IP address
        for x in range(len(allNums)):
            if (allNums[x] > 255 or allNums[x] < 0):
                print("Invalid IP Address. Try again!\n")
                break
            else:
                pass
        
        #If there's a valid IP address, break the loop by setting the invalidInput var to False
        invalidInput = False


#Asking the user to input a port number and checking to make sure it's valid
#If it's invalid, the user will be prompted to enter another port address
invalidInput = True
while(invalidInput):
    server_port = input("Input a port number or press enter for default port: ")

    #If the user hits enter/leaves the input empty, set the port address to 8000
    if (server_port == ""):
        server_port = 8000
        invalidInput = False
    #If the user enters a specific port number, make sure that it's over 1023, or else it's an error
    else:
        server_port = int(server_port)
        if(server_port <= 1023):
            print("Invalid port number. Try again\n")
        #Breaking the loop if the port address is valid 
        else:
            invalidInput = False

#Checking to make sure the username the user entered isn't an empty string
#If it is, then prompt the user again 
invalidInput = True
while(invalidInput):
    client_username = input("Enter your username: ")
    if(client_username == ""):
        print("Invalid username. Try again\n")
        break
    else:
        invalidInput = False

try:
    #Connect client socket to the server IP and port
    client_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    #Client is ready to send a message now since it's connected
    print("Ready to recieve/send messages via the client. Enter 'end' to stop messaging: ")

    while True:
        #Prompt the server user to enter a message
        client_message = input("Enter a message: ")

        #If the user enters "end", send "end" to the client, stop the socket connection, and end the program
        if (client_message == "end"):
            client_socket.send("end".encode())
            client_socket.close()
            break
        #If a blank message is entered, this is considered invalid and will end the program
        elif(client_message == ""):
            print("This is an invalid message. Ending program. \n")
            client_socket.send("end".encode())
            client_socket.close()
            break
        
        #Otherwise, send the message to the client with the username of the server-side user
        msg_to_server = client_username + ": " + client_message
        client_socket.send(msg_to_server.encode())  
        
        #Recieved and decoded the message from the server
        server_message = client_socket.recv(2048)  
        server_message = server_message.decode()

        #If the server sent "end", then stop the socket connection and end the program
        if(server_message == "end"):
            client_socket.close() 
            break
        
        #Otherwise, print the server message
        print(server_message)
except:
    #Display this if there are any errors, specifically with the socket bind, connect, accept, send, 
    #or recv operations, then this will be displayed to the terminal and will end the program
    print("Error occurred with the socket. Ending program.")
