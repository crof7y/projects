#!/usr/bin/python
money = float(input("Enter an amount of money: "))
dollars = int(money)
change = (money - dollars)
quarters = (change / 0.25)
change = change % 0.25
dimes = (change / 0.1)
change = change % 0.1
nickels = (change / 0.05)
change = change % 0.05
pennies = (change / 0.01)
print("Your amount of $%.2f consists of;\
\n\t%i dollars\n\t%i quarters\n\t%i dimes\n\t%i nickels\n\t%i pennies"\
% (money, dollars, quarters, dimes, nickels, pennies))
