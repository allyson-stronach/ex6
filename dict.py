phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781


for name, number in phonebook.iteritems():
    print "Phone number of %s is %d" % (name, number)


phonebook.pop("John")

print phonebook

phonebook["Jake"] = 938273443

print phonebook

