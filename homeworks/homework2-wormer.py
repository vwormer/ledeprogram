#Vanessa Wormer
#06/01/2015
#Homework 2

#LISTS
print "LISTS"

#Make a list of the following numbers: 22, 90, 0, -10, 3, 22, and 48

numbers = [22, 90, 0, -10, 3, 22, 48]

#Display the number of elements in the list

print len(numbers)

#Display the 4th element of this list.

print numbers[3]

#Display the sum of the 2nd and 4th element of the list.

print numbers[1] + numbers[3]

#Display the 2nd-largest value in the list.

sorted_numbers = sorted(numbers)
print sorted_numbers[len(sorted_numbers) - 2]

#Display the last element of the original unsorted list

print numbers[len(sorted_numbers) - 1]

#For each number, display a number: if your original number is less than 10, multiply it by thirty. 
#If it's also odd, add six. 
#If it's greater than 50 subtract ten. 
#If it's not negative ten, subtract one. 
#(For example: 2 is less than 10, so 2 * 30 = 60, 2 is also odd, so 60 + 6 = 66, 2 is not negative ten, so 66 - 1 = 65.)

for number in numbers:
	result = number 
	if number < 10:
		result = number * 30
		if number % 2 != 0:
			 result = result + 6
	if number > 50:
		result = number - 10
	if number != -10:
		result = number - 1

#Sum the product of each of the numbers divided by two.

print sum(numbers)/2

#DICTIONARIES
print "DICTIONARIES"

#Define a dictionary called movie that works with the following code.
#print "My favorite movie is", movie['title'], 
#"which was released in", movie['year'], "and was directed by", movie['director']

movie = {"name" : "Walk the line", "year" : "2005", "director" : "James Mangold"}

print "My favorite movie is", movie["name"], "which was released in", movie["year"], "and was directed by", movie["director"]

#Add entries to the movie dictionary for budget and revenue (NOT in the original dictionary definition), 
#and print out the difference between the two.

movie ["budget"] = 28
movie ["revenue"] = 186

print "The movie gained", movie["revenue"] - movie["budget"], "million dollars."

#If the movie cost more to make than it made in theaters, print "It was a flop". 
#If the film's revenue was more than five times the amount it cost to make, print "That was a good investment."

if (movie["revenue"] - movie["budget"]) < 0:
	print "It was a flop"
else:
	print "That was a good investment."

#Sometimes dictionaries are used to describe the same aspects of many different objects. 
#Make a dictionary that describes the population of the boroughs of NYC. 
#Manhattan has 1.6 million residents 
#Brooklyn has 2.6m
#Bronx has 1.4m 
#Queens has 2.3m
#Staten Island has 470,000. (Tip: keeping it all in millions is a good idea)

nyc = {"Manhattan" : 1.6, "Brooklyn" : 2.6, "Bronx" : 1.4, "Queens" : 2.3, "Staten Island" : 0.47}

#Display the population of Brooklyn.

print nyc["Brooklyn"]

#Display the combined population of all five boroughs.

print sum(nyc.values())

#Display what percent of NYC's population lives in Manhattan.

print (nyc["Manhattan"]/sum(nyc.values()))*100

#Display each borough name and population on separate lines (without a for loop) 
#(Hint: You'll just be typing out the name of the borough, this is the "bad" way)

print "Manhattan", nyc["Manhattan"]
print "Brooklyn", nyc["Brooklyn"]
print "Bronx", nyc["Bronx"]
print "Queens", nyc["Queens"]
print "Staten Island", nyc["Staten Island"]

#Print the name of each borough that has more than one million residents.

nyc1 = dict((k, v) for k, v in nyc.items() if v >= 1)

print nyc1

#Print how many boroughs have more than one million residents.

print len(nyc1)

#Print the length of the borough name that comes first in the alphabet.

print len(sorted(nyc.keys())[0])

#Display each borough name and population on separate lines (with a for loop).

for key, value in nyc.iteritems():
	print key, value







