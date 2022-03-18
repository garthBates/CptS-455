################################
## Name: Garth Bates
## SID: 11473063
## Project: Programing Project 1
## Class: CptS 455
## Date: 10/11/21
################################

#imports
import http.server
import socketserver

#socket
PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

#server
with socketserver.TCPServer(("",PORT), Handler) as http:
	print("serving at port:", PORT)
	http.serve_forever()