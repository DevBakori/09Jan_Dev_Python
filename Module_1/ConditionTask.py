Maths=int(input("Enter Your Maths Marks:"))
Science=int(input("Enter Your Science Marks:"))
Bio=int(input("Enter Your Bio Marks :"))
Physics=int(input("Enter Your Physics Marks :"))

Total = Maths+Science+Bio+Physics

print("Total Marks Is :" ,Total)

pr=Total/4
print("parcentage is :" ,pr)
    
if(Maths<25 or Physics<25 or Bio<25 or Science<25):
    print("Fail")
elif(pr>=70):
    print("Dist")
elif(pr>=60):
    print("First Class")
elif(pr>=50):
    print("Second Class")
elif(pr>=40):
    print("Third Class")
elif(pr>=35):
    print("Pass")


    
