# types of var :-   # int 
                    # float
                    # string
                    # boolean 
                    # complex


# a=345
# print(a)                                     <<< cast
# print(float(a))

# a="22"
# b="44"                                           <<< cast 
# print(a+b)
# print (int(a)+int(b))



# print ("Hello",end=" ")                          <<< end 
# print("Dev")


# print("hello \npython")
# print("he\bllo\bpython")                       <<< escape
# print(r"hello\tpython")


# Mobile_No=input("Enter Your Number:")                  <<< input
# print("My Number Is",Mobile_No)


# a=input("Enter value of A:")
# b=input ("Enter value of B:")                           <<< input
# print("sum:",int(a)+int(b))


# a=int(input ("Enter value of A:"))
# b=int(input ("Enter value of B:"))                     <<< input
# print("sum:",(a%b))


# print(hello python!
# goodbye python!                          <<< print
# the last line)


# print("hiii","hello", "my name is dev",sep="``")            <<<  seprate 


# a=22
# b=44
# print("A",a)                  <<< print 2 var.
# print ("B",b)


# a=22
# b=44
# tamp=a 
#                               <<<<  using 3rd var. swaping
# a=b
# b=tamp    
# print("A =",a)
# print("B =",b)


# a=22
# b=44
# a,b=b,                         <<<<  using just 2 var. swaping
# print('A =',a)
# print("B =",b)


# a=22                       
# b=44
# print("Add:",a+b)  
# print("Sub:",a-b)                 <<<  vars
# print("Mul:",a*b)
# print("Div:",a/b)





# <---------------------------------------------Formate Function------------------------------------------------>
# id=78
# name="Sanket"
#print("My ID is {} and Name is {}".format(id,name))

# print(f"My ID is {id} and Name is {name}")


# a=int(input("Enter value of A:"))
# b=int(input("Enter value of B:"))
# print(f"Valuue of A={a}, Value of B={b} and Sum of {a}+{b}={a+b}")





# <-----------------------------------------if---------------------------------------------->
# a=int(input("Enter value of A:"))
# b=int(input("Enter value of B:"))

# if a<b: #TRUE
#     print("A is min")
    
    
    
# <--------------------------------------------if_elif------------------------------------------->    
# a=int(input("Enter value of A:"))
# b=int(input("Enter value of B:"))

# if a<b:
#     print("A is min")
# elif a>b:
#     print("A is max")
# #elif a==b:
# else:
#     print("Both are equal...")




# <-----------------------------------------if_else-------------------------------------------->
# a=int(input("Enter value of A:"))
# b=int(input("Enter value of B:"))

# if a<b: #TRUE
#     print("A is min")
# else: #FALSE
#     print("A is max")



# <--------------------------------------------Split Function-------------------------------------------->
mystr="This is Python!"
print(mystr)
print(mystr.split())
print(mystr.split('i'))