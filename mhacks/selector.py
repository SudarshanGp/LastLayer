import time
from twilio.rest import TwilioRestClient 
 

ACCOUNT_SID = "AC5e89975323b46e4d820390f8ad591339" 
AUTH_TOKEN = "836c46b0edb008a44a980fde1ce77d7a" 
report = open("C:\\Users\\Abhishek\\Desktop\\MHacksIV\\report.txt", "w+")


number = "";
found = 0;
time.sleep(1)

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
 

#Haven't decided on authentication mehtod as yet
#this file should only invoke methods to send auth prompts


def sendMessage_simp():
	report.write("message sent to ")
	report.write(number)
	report.close()
	print number
	client.messages.create(
		to=number, 
		from_="+16092566342", 
		body="MHacks IV - Last Layer alert.\nA request to be access has been made by your account. Please reply Y to authenticate if this is you.",  
	)


def getMethod():
	print "This method is supposed to find this user\'s preffered\n"
	print "choice(s) of authentication\n"
	print "this is still to be implemented\n"


def getID():
	scan = open("C:\\Users\\Abhishek\\Desktop\\MHacksIV\\scan.json", "r")
	global number
	jsRead = scan.readlines()
	number = jsRead[1]
	number = number[8:]
	number = number[:number.index("\"")]
	print number
	scan.close()

	numb = open("C:\\Users\\Abhishek\\Desktop\\MHacksIV\\mapping.json")
	jsRead = numb.readlines()
	numb.close()
	x = 1;
	while (jsRead[x] != "}"):
		print jsRead[x]
		if (jsRead[x].find(number) != -1):
			number = jsRead[x][21:33]
			global found
			found = 1;
		x+=1
	report.write("end of getID")



def main():
	getID()
	getMethod()
	if (found != 0):
		sendMessage_simp()
	#the if found statement will most likely be removed
	#from this function. It should be shifted to the getMethod function
	#getmethon can iteratively go through the multiple
	#set preferences and invoke them as required


if __name__ == "__main__":
	main()