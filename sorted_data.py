# with open("scores.txt") as restfile:
#     rest_scores = restfile.readlines()

# print rest_scores


rest_scores = open("scores.txt")
restaurant = {}

for line in rest_scores:
    line = line.rstrip()
    entries = line.split(":")
    restaurant_names = entries[0]
    restaurant_scores = int(entries[1])
    restaurant[restaurant_names] = restaurant_scores

print restaurant



# while line:
#     values = line.split('\n')
    
#     print values
#     line = rest_scores.read()

# rest_scores.close()

# # rest_scores = open("scores.txt", 'r')
# restaurant_entries = line.split(':')

   # restaurant_score = restaurant_entries[1]

# print "%s was rated %r." % ()






    #need to strip \n char from rest list



#open and reads file
#strip data
#split data into a list by colon
#generate a dictionary of restaurants by scores


#spits out ratings in alph order, by restaurant





