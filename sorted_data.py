#opening text without hard coding it into our program
txt = open("scores.txt")

def main(txt):
    #rest_scores = open("scores.txt")
    restaurant = {}

    for line in txt:
        #strip line by \n line
        line = line.rstrip()
        #split data into a list by colon
        entries = line.split(":")
        restaurant_name = entries[0]
        restaurant_score = int(entries[1])
        #append data into the dictionary using variables above
        restaurant[restaurant_name] = restaurant_score

    for key in sorted(restaurant.keys()):
        print "%s was rated %r." % (key, restaurant[key])
    #spits out ratings in alph order, by restaurant
    # for key, value in sorted(restaurant.iteritems()):
    #     print "%s was rated %r." % (key, value)

if __name__ == "__main__":
    main(txt)


