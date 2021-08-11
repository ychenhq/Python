def giveBankofEmily():
    global money
    print("thanks for:", money)
    money = money *1.01 #adds one percent
    print ("now you have:", money)
    

money = input("How much money are you depositing?")
money = float(money)

giveBankofEmily()

print("Finally you have:", money)
