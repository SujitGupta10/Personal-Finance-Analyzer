import json
from datetime import datetime
Expenses={}

def SaveExpenses():
   with open("expenses.json","w") as file:
      json.dump(Expenses,file,indent=4)
      
   
def LoadExpense():
   global Expenses

   try:
      with open("expense.json","r")as file:
         Expenses =json.load(file)
         

   except FileNotFoundError:
      Expenses ={}


def AddExpense():

    date = datetime.now().strftime("%d-%m-%Y")

    while True:
        try:
            n = int(input("Enter number of items:"))
            break
        except ValueError:
            print("Please enter a valid number.")

    for i in range(n):
      while True:
        Item = input("Enter the item name: ")
        if Item =="":
            print("Item cannot be empty")
            continue
        break
      while True:
        Category = input("Enter category: ")
        if Category =="":
           print("Category cannot be empty")
           continue
        break

      while True:
            try:
                Amount = float(input("Enter amount: "))

                if Amount <= 0:
                    print("Amount must be greater than 0.")
                    continue

                break

            except ValueError:
                print("Enter valid amount")

      if date not in Expenses:
         Expenses[date]={
            "expenses":[],
            "total":0
         }

      Expense = {
            "Item": Item,
            "Category": Category,
            "Amount": Amount
        }

      Expenses[date]["expenses"].append(Expense)
      Expenses[date]["total"] += Amount
      SaveExpenses()

      print("Expense Added Succesfully!")

def ViewExpense():
   for  date ,data  in Expenses.items():
      print(f"\n Date:{date}")

      for expense in data["expenses"]:
               print(f"Item:{expense['Item']}")
               print(f"Category:{expense["Category"]}")
               print(f"Amount:{expense["Amount"]}")
               print("-----------------------------")
      print(f"Total:{data["total"]}")
         
      
def TotalExpense():
   total=0
   for expense in Expenses:
         total += expense["Amount"]
   print(f"Total Expense:{total}")
   
def CategoryTotal():
   Category_Total={}

   for expense in Expenses:
      category =expense["Category"]
      amount = expense["Amount"]

      if category in Category_Total:
         Category_Total[category]+= amount
      else :
         Category_Total[category]= amount

   for category,total in Category_Total.items():
      print(f"{category}:{total}")


LoadExpense()

      

while True:
    print("EXPENSE TRACKER")
    print("1. Add Expense")
    print("2. View Expense")
    print("3. Total Expense")
    print("4. Total  Category Expense")
    print("5. Exit")

    choice =input("Choose an option:")

    if(choice=="1"):
       AddExpense()
    elif(choice=="2"):
       ViewExpense()
    elif(choice=="3"):
       TotalExpense()
    elif(choice=="4"):
        CategoryTotal()
    elif(choice=="5"):
       SaveExpenses()
       print("Thanku for using Expense Analyzer !")
       break
       
    else:
       print("invalid choice ")
    

    
   




    
