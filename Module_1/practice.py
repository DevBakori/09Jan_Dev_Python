# try:
#     a=23
#     b=65
#     print("Sum:",a+b)
# except:
#     print("Error!")



# x=34
# y=76
# print("Mul:",x*y)

#--------------------------------------------------------------------------------------------------#

# try:
#     a=int(input("Enter A:"))
#     b=int(input("Enter B:"))
#     print("Sum:",a+B)
# except:
#     print("Error!")

#----------------------------------------------------------------------------------------------------#

# def getdata(id,name,sub='Python',city='Rajkot'): #default arguments
#     print("ID:",id)
#     print("Name:",name)
#     print("Subject:",sub)
#     print("City:",city)


#getdata(101,'Sanket')
    
# getdata(1,'Sanket','Java') #positional arguments
# getdata('Sanket',12,'PHP')
    
# getdata(id=10,name='Ashok',sub='iOS') #keyword arguments

# getdata(sub='PHP',id=12,name='Sanket') #keyword arguments

#-----------------------------------------------------------------------------------------------------#


# def getdata(data):
#     print("ID:",data['id'])
#     print("Name:",data['nm'])
#     print("Subject:",data['sub'])

# getdata({'id':101,'nm':'Sanket','sub':'Python'}) #dict arguments

#-----------------------------------------------------------------------------------------------------#


# def getdata(id,name,sub):
#     print("ID:",id)
#     print("Name:",name)
#     print("Subject:",sub)


# #getdata(101,'Sanket','Python')
    
# stid=input("Enter your ID:")
# stnm=input("Enter your Name:")
# stsub=input("Enter your Subject:")
# getdata(stid,stnm,stsub)

#-----------------------------------------------------------------------------------------------------#
# def myfunc():
#     print("This is user define function!")

# def getsum(a,b):
#     print("Sum:",a+b)

# myfunc()
# getsum(12,34)


#-----------------------------------------------------------------------------------------------------#
# def getdata(id,name,sub):
#     print("ID:",id)
#     print("Name:",name)
#     print("Subject:",sub)


# n=int(input("Enter number of students:"))
# for i in range(n):
#     stid=input("Enter ID:")
#     stnm=input("Enter Name:")
#     stsub=input("Enter Subject:")

#     getdata(stid,stnm,stsub)

#--------------------------------------------------------------------------------------------------#
# x=lambda a,b:a+b

# # print(x(23,56))
# # print("Sum:",x(23,56))

# def answer():
#     # print(x(23,56)) #lambda func
#     # print("Answer is:",x(56,87))
#     n1=int(input("Enter number1:"))
#     n2=int(input("Enter number2:"))
#     print("Answer is:",x(n1,n2))

# answer()

#------------------------------------------------------------------------------------------------#
a=34
b=76

print("A=",a)
print("B=",b)