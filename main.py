car = 12000
carmarketp = 10000
rescar = car * 0.10

userdepreciationdecision = input("What type of depresciation do you want? ")

def straightln():
    b = car - rescar
    print(b)
    print("Prov. for depresciation Vehicle in Credit to Assets & Depreciation in Debit to Income St. (Expenses)")

def reducingbl():
    a = car - rescar
    print(a)
    print("Prov. for depresciation Vehicle in Credit to Assets & Depreciation in Debit to Income St. (Expenses)")

def revl():
    depri = car - carmarketp
    c = car - depri
    print(c)
    print("On good T Credit & on depresciation Debit")

if userdepreciationdecision == 1:
    straightln()
elif userdepreciationdecision == 2:
    reducingbl()
elif userdepreciationdecision == 3:
    revl()
else:
    print("Error 404 ; Command not found")


userpruchase = input("What where your purchases? ")
userpruchasesreturns = input("What where your purchases returns? ")
useropeningstock = input("What was your opening stock? ")
userclosingstock = input("What was your closing stock? ")
usercarrigeinwards = input("What where your carrige inwards? ")

usersales = input("What where your sales? ")
usersalesreturns = input("What where your sales returns? ")

userinsurance = input("What is the cost of insurance? ")
userrent = input("What is the cost of rent? ")
userwages = input("What is the cost of wages? ")

def incomestate():
    costofsales = userpruchase - userpruchasesreturns + useropeningstock - userclosingstock + usercarrigeinwards
    sales = usersales - usersalesreturns
    grossprofit = costofsales - sales
    expenses = userinsurance + userrent + userwages
    netprofit = grossprofit - expenses
    print("Cost of Sales: ")
    print(costofsales)
    print("Sales: ")
    print(sales)
    print("Gross Profit: ")
    print(grossprofit)
    print("Expenses: ")
    print(expenses)
    print("Net Profit: ")
    print(netprofit)

incomestate()
