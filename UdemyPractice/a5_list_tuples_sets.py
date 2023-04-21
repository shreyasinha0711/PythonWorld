#list
friends = ["Rolf", "Bob", "Anne", "Jef"]
friends.append("Ael")
print(friends[0])
print(len(friends))
friends = [
    ["Rolf", 24], 
    ["Bob", 30],
    ["Anne", 27]
]
friends.remove(["Anne", 27])
print(friends[1])
print(friends[0][1])

#list slicing
print("-----LIST SCLICING----")
friends = ["Rolf", "Bob", "Anne", "Jef"]
print(friends[2:4])
print(friends[1:]) #except 1st one
print(friends[:4]) #start and end at 4
print(friends[:]) #gives a new list with all elements
print(friends[-3:]) #
print(friends[-3:4]) #
print(friends[:-2]) #
print(friends[-3:-1]) #

#list comprehensions
print("-----LIST COMPREHENSIONS----")
numbers = [0, 1, 2, 3, 4]
double_nums = [ number * 2 for number in numbers]
print(double_nums)

friend_ages = [22, 31, 35,37]
age_strings = [f"My firend is {age} years old." for age in friend_ages]
print(age_strings)

lower = [name.lower() for name in friends]
print(lower)

#list comprehensions with conditionals
print("-----LIST COMPREHENSIONS WITH CONDITIONS----")
ages = [22, 31, 35, 37, 20, 21]
odds = [age for age in ages if age % 2 == 1]
print(odds)


friends = ["Rolf", "ruth", "Charlie", "Jen"]
guests = ["jose", "Bob", "Rolf", "Charlie", "michael"]

friends_lower = set([f.lower() for f in friends])
guest_lower = set([g.lower() for g in guests])
print(friends_lower.intersection(guest_lower))

present_friends = [
    name 
    for name in guests 
    if name.lower() in friends_lower
]

print(present_friends)

#tuples
print("-----TUPLES EXAMPLES----")
short_tupe = "Rolf", "Bob"
a_bit_clear = ("Rolf", "Bob") #used mostly like this
tuple_in_list = [("Rolf", "Bob")]

not_string = "Rold", #its a tuple

friends = ("Rolf", "Bob", "Anne")
friends = friends + ("Ann",) #tuple don't change it created new tuples
print(friends)

#tuples don't change, list changes


#sets
#don't hold order and are unique

art_friends = {"Rolf", "Anne"}
science_friends = {"Jen","Charlie"}
art_friends.add(("Jen"))
print(art_friends)
print("-----")
print(len(art_friends))
art_friends.remove("Jen")
print(art_friends)

art_friends = {"Rolf", "Anne", "Jen"}
science_friends = {"Jen", "Charlie"}
art_but_no_science = art_friends.difference(science_friends)
print(art_but_no_science)
sci_but_no_art = science_friends.difference(art_friends)
print(sci_but_no_art)

not_in_both = art_friends.symmetric_difference(science_friends)
print(not_in_both)

art_and_science = art_friends.intersection(science_friends)
print(art_and_science)

all_friends = art_and_science.union(science_friends)

#set comprehensions
print("-----SET COMPREHENSIONS----")

friends = ["Rolf", "ruth", "Charlie", "Jen"]
guests = ["jose", "Bob", "Rolf", "Charlie", "michael"]

friends_lower = {f.lower() for f in friends}
guest_lower = {g.lower() for g in guests}

#sum and avg

grades = [80,75,90,100]
total = sum(grades)
length = len(grades)
print(total/length)

grades = [80,75,90,100] #best
grades = {80,75,90,100} #set can't have unqiue worst
grades = (80,75,90,100) #tuple can't add new grades


#join

friends = ["Rolf", "Bob", "Anne"]
comma_separated = ",".join(friends)
print(f"My friends are {comma_separated}")