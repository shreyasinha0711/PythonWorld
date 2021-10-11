#ask user for a list of 3 friends
#for each fiends, we'll tell the user wheather they are nearby
#for each nearby friend, we'll save their name to `nearby_friends.txt
#hint:readlines()

friends = input('Enter 3 friends, separated by commas(no spaces):').split(',')
print(friends)

people = open('file/people.txt', 'r')
#people_nearby = people.readlines()
people_nearby = people.read().splitlines()
print(people_nearby)

people.close()

friends_set = set(friends)
people_nearby_set = set(people_nearby)
print(friends_set)
print(people_nearby_set)

friends_nearby_set = friends_set.intersection(people_nearby_set)
print(friends_nearby_set)
nearby_friends_file = open('file/nearby_friend.txt', 'w')

for friend in friends_nearby_set:
    print(f'{friend} is nearby!!')
    nearby_friends_file.write(f'{friend}\n')

nearby_friends_file.close()
