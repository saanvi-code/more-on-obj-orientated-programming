class Employee():
    def __init__(self):
       print("Employee introduced")

    def __del__(self):
       print("employee removed")

def Employ():
   print("callin class")
   obj=Employee()
   print("endin function")
   return obj

print("calling function")
obj2=Employ()
print("program end")

