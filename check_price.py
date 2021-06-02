import urllib.request,smtplib,ssl
from bs4 import BeautifulSoup


def sendmail():
	smtp_server = "smtp.gmail.com"
	sender_address=''               #Enter the email id from which you want to send the mail
	receiver_address=''             #Enter receiver's email address
	message="""\
	Hi There


	The prices went beyond the limit"""

	port=465
	password=input("Enter your password: ")
	# Create a secure SSL context
	context = ssl.create_default_context()
	with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
		server.login(sender_address, password)
		server.sendmail(sender_address, receiver_address, message)
		server.quit()



if __name__=='__main__':
	url="https://www.moneycontrol.com/india/stockpricequote/food-processing/britanniaindustries/BI"
	source=urllib.request.urlopen(url).read()
	soup=BeautifulSoup(source,"lxml")
	div_tag=soup.find('div',id='nsecp')
	price=div_tag.text
	print(price)
	if float(price)>3000:
		sendmail()
