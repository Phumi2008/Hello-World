import math

p = float(input("Please enter the amount you want to invest:"))
i = float(input("Please enter the interest rate as a percentage:"))
t = float(input("Please enter the number of years of investment:"))



interest = input("Please select the type interest, simple or compounded:")
if interest == "simple":
    simpleAmount = float(p*(1+i*t))
    print(simpleAmount)

elif interest == "compounded":
    compoundAmount = float(p*math.pow((1+i), t))
    print(compoundAmount)

elif interest != "simple" or interest != "compounded": 
    print("Error massage,NOT APPLICABLE")
