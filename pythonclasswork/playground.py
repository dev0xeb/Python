language = input("enter your preferred language: ")

match language:
        case "java":
            print("you are a java programmer")
        case "python":
            print("you are a python programmer")
        case _:
           print("you are not a software enginner")


name = 'clinton'
print(id(name))

name = name + ' ayo'
print(id(name))

total = 0
for number in range(100):
    print(number, end=')
    total += number
print(total)
