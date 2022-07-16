import math
#A program allowing users to access a financial calculator for investments and home loan repayments.
#First the user chooses between a bond calculation and an investment calculation.
#All of the calculations will be done based on the users' input

print("Choose either 'investment' or 'bond' to proceed:")
print('\n'"investment     - to calculate the amount of interest you'll earn on interest")
print("bond           - to calculate the amount you'll have to pay on a home loan")
user_input = input('\n'"Enter your choice here:")
choice = user_input.lower()

#This calculation that will be done if the user chooses 'bond'
if choice == "bond":
    value = input("What is the current value of the house? R")
    int_rate = input("Enter the interest rate: NOTE: Do not add the '%' symbol at the end.")
    months = input("Enter the number of months you need to take to repay the bond:")
    p = int(value)
    i = int(int_rate)/12
    n = int(months)
    amt = round((i) * (1/(1-(1+i)**(-n)))*p,2)
    print(f"The amount to be repaid monthly is: R{amt}")

#This calculation that will be performed if the user chooses 'interest'
elif choice == "investment":
    amount = input("Enter the amount of money you are depositing:R")
    rate = input("Enter the interest rate: NOTE: Do not add the'%' symbol at the end:")
    years = input("How many years would you like to invest for:")
    INTEREST = input("Do you want 'simple' or 'compound' interest:")
    interest = INTEREST.lower()
    P = int(amount)
    r = int(rate)/100
    t = int(years) 
#calculation for simple interest
    if interest == "simple":
        total = round(P*(1+r*t),2)
        print(f"Your total amount is: R{total}")
#calculation for compound interest
    elif interest == "compound":
        total = round(P*math.pow((1+r),t),2)
        print(f"Your total amount is: R{total}")
else:
    print("ERROR! Please choose one of the options. Make sure your spelling is correct!")
