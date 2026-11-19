p=float(input("enter the principal amount in rupees:"))
r=float(input("enter the rate of interest in rupees:"))
t=float(input("enter time in years"))
amount=p*(1+r/100)**t
ci=amount-p
print("compound interest=",ci)
print("total amount=",amount)