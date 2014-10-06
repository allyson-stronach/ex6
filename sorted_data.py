rest_scores = open("scores.txt")
restaurant = {}

for line in rest_scores:
    #strip line by \n line
    line = line.rstrip()
    #split data into a list by colon
    entries = line.split(":")
    restaurant_names = entries[0]
    restaurant_scores = int(entries[1])
    #append data into the dictionary using variables above
    restaurant[restaurant_names] = restaurant_scores


#spits out ratings in alph order, by restaurant
for key, value in sorted(restaurant.iteritems()):
    print "%s was rated %r." % (key, value)




