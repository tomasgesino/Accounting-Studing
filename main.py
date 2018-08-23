car = 12000
carmarketp = 10000
rescar = car * 0.10

userdepreciationdecision = input()

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
