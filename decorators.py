def greeting(func):
    def wrapper(*args):
        print("Welcome")
        func(args[0],args[1])
        print("Enjoy your stay")
    return wrapper

def roundNum(func):
    def wrapper(*args):
        if len(str(args[0])) > 5:
            rounded = round(args[0], 3)
            print("Your number is ", rounded)
        else:
            func(args[0])
    return wrapper


@greeting
def printName(first, last):
    print(last + ", " + first)
    return

@roundNum
def printNum(userNum):
    print(userNum)

printName("Isaac", "Mutschler")

printNum(5.967819)
