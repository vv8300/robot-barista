
print("hello,welcome to the vv bar!!!" )
name=input("May i know your name? :\n")
if name =="ten":
    evil_status =input("are you a supporter of the evil states? (yes/no):\n")
    if evil_status == "yes":
     print ("your not allowed to enter the bar")
     exit()
    else:
     evil_status == "no"
     print ("your welcaome to the bar the choicen one") 
if name =="mkmk":
     print("we're not a dm* supporter ****,so you can't enter the bar")
     exit()
else:
    print(name+" is a fabulous name ")
    menu = ("1.coffee\n2.tea\n3.iced latte\n4.cappuccino\n5.americano\n6.mocha")
    print(("what can i get for today and please enter the number of your choice?\n"+menu))
    order= input("enter the order you want to order:\n")
    if order > "6" or order< "1":
        print("sorry we don't have that item in our menu, please choose from the menu")
    else:
        print("Number." + order + " is a great choice, " + name + "! Your order will be ready shortly. Thank you for visiting the vv bar!")
        cups=input("how many cups do you want to order? :\n")
        if order == "4" or order == "5" or order == "6":
            price={3:15, 4:18, 5:20}
            total_price=int(cups)*price[int(order)-1]
            print("the price for your order is $"+str(total_price))
        else:
            price=(9,10,12)
            total_price=int(cups)*price[int(order)-1]
            print("the price for your order is $"+str(total_price))