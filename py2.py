#!/usr/bin/env python3
import time
import os
import sys

# ------Greeting------
print("Enter your name: ")
name=input()

print("Hello, " +name+"! Welcome to MY WORLD!")

#------CommandLine------
def main():
    while True:
        command = input("Enter a command: ")
        
        if command.lower() == "exit":
            return True
        elif command.lower()== "quit":
            return False

#------time------
        elif command=="time":
            print("Current time:" +time.strftime("%I:%M:%S:%p"))
            
#------date------
        elif command== "date":
            print("Current date:" +time.strftime("%d-%m-%y"))
        
#------math------
        elif command=="math":
            print("Entering math mode...")
            print("\nEnter first number: ")
            num1 = input()
            if num1 == "exit":
                continue
            
            num1= float(num1)
            
            print("Enter second number: ")
            num2 = input()
            if num2 == "exit":
                continue
            
            num2= float(num2)
                
            print("Enter operattion(+,-,*,/): ")
            op= input()
            if op== "+":
                print("Result: " +str(num1+num2))
            elif op== "-":
                print("Result: " +str(num1-num2))
            elif op== "*":
                print("Result: " +str(num1*num2))
            elif op== "/":
                if num2 !=0:
                    print("Result: " +str(num1/num2))
                else:
                    print("Error: Division by zero is not allowed.")
            

            else:
                print("Invalid operation. Please enter +, -, *, or /.")

#------notes------
        elif command== "notes":
            print("Opening notes...")
            print("Enter notes command: ")
            nCommand= input()
            
            if nCommand == "exit":
                continue
            
            elif nCommand== "create":
                print("Enter file name(with .txt): ")
                fname= input()

                open(fname,"w").close()
            
            if nCommand== "write":
                print("Enter file name(with .txt): ")
                fname= input()
                with open(fname,"w") as file:
                    print("Write your notes here: ")
                    wNotes = input()
                    file.write(wNotes)
                    file.close()

            elif nCommand== "read":
                print("Enter file name: ")
                fname= input()
                with open(fname,"r") as file:
                    print(file.read())
        
            elif nCommand== "delete":
                print("Enter file name: ")
                fPath=input()
                if os.path.exists(fPath):
                    os.remove(fPath)
                    print("File deleted succesfully...")
                else:
                    print("File does not exist...")
                    
            
        else:
            print("Unknown command, Try again") 

while True:
    quit=main()
    if not quit:
     break
            
            