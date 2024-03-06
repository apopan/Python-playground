import os

if __name__ == '__main__':
    print("Welcome to Text to Speech")
    while True:
        x = input("Enter what do you want to say : ")
        if x == "q":
            os.system("say 'Bye, Thanks use again'")   # "say" command only works in mac os 
            break
        command = f"say {x}"
        os.system(command)
            