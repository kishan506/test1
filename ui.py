from AdminScreen import AdminMenu
from UserScreen import UserMenu


while True:	
	print("""
		1. Admin
		2. User
		0. Exit
	"""
	)
	n = int(input("\tEnter your choice: "))
	if(n==1):
		print("\tWELCOME TO ADMIN\t")
		AdminMenu()
	elif(n==2):
		UserMenu()
		print("\tWELCOME TO USER\t")
	elif(n==0):
		print("BYE BYE!!!")
		break
	else:
		print("INVALID CHOICE...")
	