import smtplib

def sendMailWithGmail(Nombre,Origen,Mensaje):
	
	gmailaddress =("pruebas.sistemas.jm@gmail.com")     
	gmailpassword =("jtsxktgtvkjmzvtq")                 

	destino =  ("juanmanuelchico@hotmail.com")           
	
	msg = ('\nDe: ' + Nombre +'\nDesde: '+ Origen + '\nMensaje: ' + Mensaje)								
	
	mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
	
	mailServer.starttls()
	
	mailServer.login(gmailaddress , gmailpassword)

	mailServer.sendmail(gmailaddress,destino,msg)

	mailServer.quit()