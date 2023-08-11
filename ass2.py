#1
def strint(s, i):
    if i == "":
        return ""
    else:
        nreverse = "".join(reversed(s))*i
        return nreverse

print(strint("hello",2))
################################
#2
def UpLow(s):
    upper=""
    lower=""
    for i in s:
        if i.isupper():
            upper +=i
        else:
            lower+=i
    s2=upper+lower
    return s2
print(UpLow("AliKandil"))
################################################################
#3
def reorder(s1,s2):
    s3="".join(sorted(s2))
    if s1 ==s3:
        return True
    else:
        return False

print(reorder('abcde','bdcea'))
##########################################################
#4
def Max(l):
    max=0
    min=0
    for i in l:
        if i>max:
            max=+i

        elif(i<min):
          min=+i

    print("the highest value in the list is " + str(max) + " in index " + str(l.index(max)))
    print("the lowest value in the list is " + str(min) + " in index " + str(l.index(min)))

lsit1=[5,6,3,2,7,2,0,1,6]
Max(lsit1)
############################################
#5
def counts(n):
    return print(len(n))

print("enter a number")
x=input()
counts(x)
###############################################
#6
def list_jumps(jumps):
    for i in jumps+1:
        pass
  


###################################################
#7
def total(items, barcode, quantity):
    if barcode in items:
        item_name, item_price = items[barcode]
        total_cost = item_price * quantity
        return item_name, quantity, total_cost


def receipts(receipt):
    total_amount = 0
    print("\nReceipt:")
    for item in receipt:
        name, quantity, total_cost = item
        receipt_line = "Name: " + name + "\n" + " - Quantity: " + str(quantity) + "\n" + " - Total Cost: " + str(total_cost)
        print(receipt_line)
        total_amount += total_cost

    print("Total:", total_amount)


def POS():
    items = {
        123: ("apple", 1.5),
        456: ("banana", 2.5)
    }

    while True:
        receipt = input("Start a new receipt? (yes/no): ")
        if receipt == "no":
            break
        elif receipt == "yes":
            l = []
            while True:
                barcode = input("Enter the item barcode (0 to see receipt): ")
                if not barcode.isdigit():
                    print("Invalid input. Please enter a valid number.")
                    continue
                barcode = int(barcode)
                if barcode == 0:
                    break
                if barcode not in items:
                    print("Invalid barcode. Item not found!")
                    continue
                quantity = input("Enter the quantity purchased: ")
                if not quantity.isdigit():
                    print("Invalid input. Please enter a valid number.")
                    continue
                quantity = int(quantity)
                item = total(items, barcode, quantity)
                if item:
                    l.append(item)

            receipts(l)

POS()

