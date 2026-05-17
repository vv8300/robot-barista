
print("hello,welcome to the vv bar!!!" )
name=input("May i know your name? :\n")
print(name+" is a fabulous name ")
menu = ("1.coffee\n2.tea\n3.iced latte\n")
print(("what can i get for today?\n"+menu))
order= input("enter the order you want to order:\n")
if order > "3" or order< "1":
    print("sorry we don't have that item in our menu, please choose from the menu")
else:
    print("Number." + order + " is a great choice, " + name + "! Your order will be ready shortly. Thank you for visiting the vv bar!")
    cups=input("how many cups do you want to order? :\n")
    price=(9,10,12)
    total_price=int(cups)*price[int(order)-1]
    print("the price for your order is $"+str(total_price))
