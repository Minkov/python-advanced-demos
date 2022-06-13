from PyP100 import PyP100

p100 = PyP100.P100("192.168.X.X", "email@gmail.com", "Password123")
p100.handshake()  # Creates the cookies required for further methods
p100.login()  # Sends credentials to the plug and creates AES Key and IV for further methods
