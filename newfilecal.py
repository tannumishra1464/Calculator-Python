# Making a simple calculator in Android using python using Pydroid 3 app.
#You can download this app from Google Play Store
#Input numbers.
a=int(input("Enter:"))
b=int(input("Enter:"))

#Select Operation.
print("Opreation:+,-,*,/")

#Input Operation.

select_opreator=input("Enter:")
if select_opreator=="-":
	print(a,"+",b,"=",a+b)  
elif select_opreator=="-":
	print(a,"-",b,"=",a-b)  
elif select_opreator=="*":
	print(a,"*",b,"=",a*b)  
elif select_opreator=="/":
	print(a,"/",b,"=",a/b)
else:
	print("Invalid Input")
