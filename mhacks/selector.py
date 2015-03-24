import time
from twilio.rest import TwilioRestClient 
 

ACCOUNT_SID = "" 
AUTH_TOKEN = "" 
report = open("C:\\Users\\Abhishek\\Desktop\\MHacksIV\\report.txt", "w+")


number = "";
found = 0;
time.sleep(1)

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
 

#Haven't decided on authentication mehtod as yet
#this file should only invoke methods to send auth prompts


def sendYo():
	#this message should simply invoke the yo.py file
	#providing the user's information.


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
	#note that in the interest of simplicity, if a particular preffers to be
	#notifed by more than one method, method.json will simply have multipe entries
	#associated with his account.
	#NOTE: this is an O(N) operation. We should replce this with a hash table when time permits
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
