import time
from twilio.rest import TwilioRestClient 
 
# put your own credentials here 
ACCOUNT_SID = "AC5e89975323b46e4d820390f8ad591339" 
AUTH_TOKEN = "836c46b0edb008a44a980fde1ce77d7a" 
report = open("C:\\Users\\Abhishek\\Desktop\\MHacksIV\\report.txt", "w+")


number = "";
found = 0;
time.sleep(1)

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
 

def sendMessage_simp():
	report.write("message sent to ")
	report.write(number)
	report.close()
	print number
	client.messages.create(
		to=number, 
		from_="+16092566342", 
		body="Last Layer alert.\nThis is a courtesy message. Please reply Y to authenticate.",  
	)

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
	if (found != 0):
		sendMessage_simp()

if __name__ == "__main__":
	main()