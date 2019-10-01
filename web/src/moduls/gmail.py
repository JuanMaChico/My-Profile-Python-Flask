import smtplib

def gmail(Mensaje):
	print ("****enviar email con gmail***")


	gmailaddress =("pruebas.sistemas.jm@gmail.com")     #input("what is your gmail address? \n ")
	gmailpassword =("juliocasares3484")                 #input("what is the password for that email address? \n  ")
	mailto =  ("juanmanuelchico@hotmail.com")                            #input("destino? \n ")
	#asunto=   (Facturacion)                                     #input("asunto?\n ")
	msg = (Mensaje)      #input("mensaje? \n ")
	mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
	mailServer.starttls()
	mailServer.login(gmailaddress , gmailpassword)
	mailServer.sendmail(gmailaddress, mailto , msg)
	print(" \n Enviado...")
	mailServer.quit()
