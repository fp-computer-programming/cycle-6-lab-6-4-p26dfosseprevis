#Create a Python file named lab_6-4

#*** You must write a comment for every chunk of code you write from now on along with your author tag***

#Create a list of 3 subjects that you have studied at Prep and store it as a variable.
list = ["math","hystory","bio"]
#Use a method to add a fourth subject you have studied to the end of the list.
list.append("West_Civ")
#Use a method to return the index of one of the subjects in your list.
print(list.index("math"))
#Order the subjects alphabetically using a method.
list.sort()
#Use a method to make a copy of this list and store it in a different variable.
list2 = list[:]
#Use a method to order this second list in reverse alphabetical order.
list2.reverse()
print(list)
print(list2)

