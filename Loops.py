# Ex.1

myList = [5, 7, 3, 1]
listLenght = len(myList) - 1
index = 1
result = True
while index < listLenght:
    if myList[index] > myList[index + 1]:
        result = False
        break
    index += 1

print(result)

print("________________________________")

# Ex.2

# def foonction():
#    for i in range(int(input("please input the number: "))):
#      print(i+1, end=".")

# foonction()

# ex.3

myList = [1, 1, 2, 2, 3, 3]


def unicElements(myList):
    print(set(myList))


unicElements(myList)


def my_function(fname, lname):
    print(fname + " " + lname)


my_function("john", "Smith")

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

