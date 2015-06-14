print "Vanessa Wormer"
print "06/09/2015"
print "Homework 4"


import csv

file = open("dogs.csv")
dogs = list(csv.DictReader(file))

#1
print "Make a dictionary where every dog's name maps to the number of dogs with that name."

names = []

for dog in dogs:
	names.append(dog["dog_name"])

unames = list(set(names))

namecountdict = {}
for uname in unames:
	namecountdict[uname] = 0

for name in names:
	namecountdict[name] = namecountdict[name] + 1

print namecountdict

#print namecountdict

#2
print "2. How many dogs are named Danger?"

#name_danger = [dog["dog_name"] for dog in dogs if dog["dog_name"] == "Danger"]
#print len(name_danger)

print "There are", namecountdict["Danger"], "dogs named Danger in nyc"

#3
print "3. Find the ratio of dogs name Spot to dogs name Spike."

print float(namecountdict["Spot"])/float(namecountdict["Spike"])

#4
print "4a. Make a list of all of the names that only appear once in the list."

single_names = []
for name in namecountdict:
	if namecountdict[name] == 1:
		single_names.append(name)

print single_names

#4b
print "Display them in alphabetical order."

#print sorted.namecountdict

list = single_names
single_names.sort()
for item in single_names:
	print item


#5
#print "5. Which borough loves dogs the most? Use the following dictionary to tell me the ratio of dogs to people in each borough."

#population = { 'Staten Island': 468000, 'Brooklyn': 2504000, 'Bronx': 1385000, 'Manhattan': 1585000, 'Queens': 2231000 }

#for dog in dogs:
#	print dog

#	print dog["dog_name"]
#	print dog ["borough"]


### not finished

