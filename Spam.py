p1 = "Make a lot of money"
p2 = "Buy now"
p3 = "Subscribe this" 
p4 = "Click this"

message = input("Enter your Comment here ")

if((message.lower() in p1.lower()) or (message.lower() in p2.lower()) or (message.lower() in p3.lower()) or (message.lower() in p4.lower())):
	print("this messages is spam")

else:
	print("This message is not Spam ")