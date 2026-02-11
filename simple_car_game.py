command=""
start =False
stop=False
while command != "quit":
    command=input().lower()
    if command=="start" :
        if start == False:
            print("Car started.")
            start=True
        else :
            print("Car already started.")
    elif command=="stop" :
        if stop == False:
            print("Car stopped.")
            stop = True
        else:
            print("Car already stopped.")
    elif command=="quit":
        print("out of the game.")
        break
    elif command=="help":
        print("""start : To start the car
stop : To stop the car
quit : To exit the car""")
    else :
        print("Please enter a valid input.")
