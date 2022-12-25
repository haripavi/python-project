
#python project
contacts= {
"HARI": 6305219267,
"HARRY": 7416219267,
"YOGENDAR": 8500710099,
"VARDHAN": 9849036693,
"RESHMI": 9716223666,
"ANVITH": 8328165035,
"UDAY": 9177971960,
"VINAY": 9908491224,
"ANKIT GUPTA": 8081408351,
"VISWAVARDHAN": 9121345262,
"HEMANTH SAI": 8340065854,
"SRISAIMANI": 9059101049,
"KARTHIK": 93947760826,
"MANOJ": 7353916990,
"PORAPUKA": 6989398654,
"HEMANTH": 9502850367,
"SUMANTH": 7981351497,
"SURYANSHU RAI":7878261147,
"SYAMANTH": 97704770968,
"AYUSH": 7991816017,
"PAWAN": 9346204473,
"HEMAHARIKA": 8074838922,
"JOTHAM ROY": 7670892114,
"VISHNU": 8341754832,
"ABHINAV KUMAR": 9119980159,
"SHRAVAN": 9065252026,
"ABHISHEK YADAV":91615011044,
"SHIVAM YADAV": 6003753946,
"VINAYAK CHOUBEY": 6203898793,
"EKTA GUPTA": 7006729398,
"LAKSHYA": 7351081638,
"ARNAV KUMAR": 7455072846,
"FAIZAN": 7497861017,
"ARYAN": 7735684668,
"ROHAN": 77066877045,
"YASHWANTH": 7780441330,
"SUNNY RAJ": 7903405715,
"NIKHIL": 7973206138,
"RISAV": 8002709552,
"RaCHIT SHARMA": 8081450904,
"UJJWAL": 9696492047,
"PRAVEEN MISHRA": 9871433037,
"AMIT KUMAR YADAV": 7380777550
}



def single_search():
	name=input(">>>Enter the name of the contact you wish to search for: ").upper()
	if name in contacts:
		print(f"\n{name}: {contacts[name]}")
	else:
	   b=input("\nNo such contact found\nIf you wish to add one, type 'Yes' else type 'No': ").lower()
	   if b=="yes":
	     new_contact(name)
	     print(f"{name}: {contacts[name]}")
	   elif b=="no":
	     	pass
	   else:
	     print("Enter either yes or no")


def multiple_search():
	     result={}
	     s1=[]
	     s=0
	     name1=input(">>>Enter the names of the contacts seperated by commas: ").split(",")
	     for i in name1:
	     			i=i.upper()
	     			if i in contacts:
	     				result[i]=contacts[i]
	     			else:
	     				s1.append(i)
	     				s+=1
	     			
	     if s>0:
	     	c=(input(f"\nCouldn't find contacts {s1} . \nDo you wish to add them? Enter Yes or no: ")).lower()
	     	if c=="yes":
	     		for i in s1:
	     			new_contact(i)
	     			if i in contacts:
	     				result[i]=contacts[i]
	     		print()
	     		print(result)
	     	elif c=="no":
	     		print()
	     		if result=={}:
	     			pass
	     	else:
	     		print("\n")
	     else:
	     	print()
	     	print(result)

			
	     		
def new_contact(contact_name):
	     print()
	     contact_number=int(input(">>>Enter their contact number: "))
	     contacts[contact_name]=contact_number
	     
choice=int(input("Would you like to: \n\n1. Search for a single contact \n2. List all the contacts \n3. Search for multiple contacts \n \n>>>Enter your choice: "))

if choice==1:
	single_search()
	
elif choice==2:
	print()
	print(contacts)
	
elif choice==3:
	multiple_search()

else:
	print("Choose from the given options!")
