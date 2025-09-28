i = 0   
started = False                                                                 # command = "" (empty string)
while i < 2:                                                             # while command != "quit": 
        command = input("> ")  
        if command == "help":                                          #(while command is not qual to quit, the loop will go on)                                                                                               # because we had to take to take care abt upper and lower cases
            print(''' 
        start- to start car                                    
        stop - to stop car
        quit - to exit''')
        elif command == "start":
            if started:
                 print(" your car is already started")
            else:
                 started = True
                 print("car started.. ready to go")                               # while command.lower() != "quit":
        elif command == "stop":  
            if not started:
                 print                                                       #OR
            print("car stopped")                                             # while command.upper() != "quit":
        elif command == "quit":
              break                                                            #while True:
        else:                                                                #(another way of starting this code, 
            print("i dont understand that..")  
            break                                                   # the code runs until we explicitly break out of it)



    