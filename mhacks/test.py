from twilio.rest import TwilioRestClient 

ACCOUNT_SID = "AC5e89975323b46e4d820390f8ad591339" 
AUTH_TOKEN = "836c46b0edb008a44a980fde1ce77d7a" 

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 

x = 0;

while (x != 1):
	client.messages.create(
		to="+16177840260", 
		from_="+16092566342", 
		body="MHacks IV - 2nd Fact alert.\nThis is a courtesy message.", 
		x = x + 1 
	)