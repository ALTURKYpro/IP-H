import socket
import os
import time
import sys
#######
print ('ALturky pro')
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(00000.015)
jalan ("Welcome to ALturky pro followers, I present to you a site ip extraction tool")
print ("YouTube   : https://youtube.com/alturkypro") 
print ("telegram    : https://t.me/ALturky_pro") 
print ("Facebook  : https://www.facebook.com/ALturkypro1") 
print ("Website   : https://www.mohamedsaed.tk") 
print ("Twitter   : https://twitter.com/ALTURKY_pro") 
test = str(input("enter domin name: "))
test0 = socket.gethostbyaddr(test)
print (test0)
