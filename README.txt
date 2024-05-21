In this assignment, we modify the second assignment to communicate with a server and post messages to it
The programs commands are the same: 

Q -- Quit the program
C -- Create a new file in a specified path
D -- Deleted a file
R -- Read a file
O -- Open a file
E -- Edit a file
P -- Print a file

The only difference is that there is a web server that the profile and messages are pushed to
The UI module is modified to send the profiles and messages to the server
using ds_client and ds_protocol the communication with the server is possible