print "Vanessa Wormer"
print "06/03/2015"
print "Homework 3"

#0. What's the command to make a sample of the first 500 rows of dogs.csv, and save it to thousand.csv?
print "0. What's the command to make a sample of the first 500 rows of dogs.csv, and save it to thousand.csv?"

print "head -n 500 dogs.csv > thousand.csv"

#1. How many registered dogs are in New York City total?
print "1. How many registered dogs are in New York City total?"
# wc -l dogs.csv

import csv
file = open("dogs.csv")

dogs = list(csv.DictReader(file))

print len(dogs)

#2. How many dogs are in each borough?
print "2. How many dogs are in each borough?"

results_mannhattan = 0
results_queens = 0
results_bronx = 0
results_statenisland = 0
results_brooklyn = 0
for dog in dogs:
	if dog["borough"] == "Manhattan":
		results_mannhattan = results_mannhattan + 1
	elif dog["borough"] == "Queens":
		results_queens = results_queens + 1
	elif dog["borough"] == "Bronx":
		results_bronx = results_bronx + 1
	elif dog["borough"] == "Staten Island":
		results_statenisland = results_statenisland + 1
	elif dog["borough"] == "Brooklyn":
		results_brooklyn = results_brooklyn + 1
print "Brooklyn:", results_brooklyn
print "Staten Island:", results_statenisland
print "Bronx:", results_bronx
print "Queens:", results_queens
print "Manhattan:", results_mannhattan


#3. Make a list of every dog's name (duplicates are OK)
print "3. Make a list of every dog's name (duplicates are OK)"

names = []
for dog in dogs:
	print dog["dog_name"]
	names.append(dog["dog_name"])
print names

#4a. How many dogs named "Max" (or any other name of your choosing) are in NYC?
print "4a. How many dogs named Max (or any other name of your choosing) are in NYC?"

name = 0
for dog in dogs:
	if dog["dog_name"] == "Max":
		name = name + 1
print name

#4b. How many dogs named "Max" (or any other name of your choosing) are in each borough?
print "4b. How many dogs named Max (or any other name of your choosing) are in each borough?"

results_mannhattan_max = 0
results_queens_max = 0
results_bronx_max = 0
results_statenisland_max = 0
results_brooklyn_max = 0
for dog in dogs:
	if dog["dog_name"] == "Max" and dog["borough"] == "Manhattan":
		results_mannhattan_max = results_mannhattan_max + 1
	elif dog["dog_name"] == "Max" and dog["borough"] == "Queens":
		results_queens_max = results_queens_max + 1
	elif dog["dog_name"] == "Max" and dog["borough"] == "Bronx":
		results_bronx_max = results_bronx_max + 1
	elif dog["dog_name"] == "Max" and dog["borough"] == "Staten Island":
		results_statenisland_max = results_statenisland_max  + 1
	elif dog["dog_name"] == "Max" and dog["borough"] == "Brooklyn":
		results_brooklyn_max = results_brooklyn_max + 1
print "Manhattan:", results_mannhattan_max
print "Queens:", results_queens_max
print "Bronx:", results_bronx_max
print "Staten Island:", results_statenisland_max
print "Brooklyn:", results_brooklyn_max

#5. How many dogs were registered in 2008? 2011? 
print "5. How many dogs were registered in 2008? 2011?"

results_2008 = 0
for dog in dogs:
	if dog["birth"][-2:] == "08":
		results_2008 = results_2008 + 1
print "In 2008", results_2008, "dogs were registered."

results_2011 = 0
for dog in dogs:
	if dog["birth"][-2:] == "11":
		results_2011 = results_2011 + 1
print "In 2011", results_2011, "dogs were registered."

#6a. What percentage of dogs are spayed/neutered?
print "6a. What percentage of dogs are spayed/neutered?"

results_spayed_neutered = 0
for dog in dogs:
	if dog["spayed_or_neutered"] == "Yes":
		results_spayed_neutered = results_spayed_neutered + 1
print 100*(float(results_spayed_neutered)/float(len(dogs))), "percent of dogs are spayed/neutered."


#6b. What percentage of female dogs are spayed/neutered? Male dogs?
print "6b. What percentage of female dogs are spayed/neutered? Male dogs?"

results_female = 0
for dog in dogs:
	if dog["gender"] == "F":
		results_female = results_female + 1

results = 0
for dog in dogs:
	if dog["gender"] == "F" and dog["spayed_or_neutered"] == "Yes":
		results = results + 1
print 100*(float(results)/float(results_female)), "percent female dogs are spayed/neutered."

results_male = 0
for dog in dogs:
	if dog["gender"] == "M":
		results_male = results_male + 1

results = 0
for dog in dogs:
	if dog["gender"] == "M" and dog["spayed_or_neutered"] == "Yes":
		results = results + 1
print 100*(float(results)/float(results_male)), "male dogs are spayed/neutered."


#7a. What are the per-borough percentages of spayed/neutered dogs?
print "7a. What are the per-borough percentages of spayed/neutered dogs?"

results_mannhattan_sn = 0
results_queens_sn = 0
results_bronx_sn = 0
results_statenisland_sn = 0
results_brooklyn_sn = 0
for dog in dogs:
	if dog["spayed_or_neutered"] == "Yes" and dog["borough"] == "Manhattan":
		results_mannhattan_sn = results_mannhattan_sn + 1
	if dog["spayed_or_neutered"] == "Yes" and dog["borough"] == "Queens":
		results_queens_sn = results_queens_sn + 1
	if dog["spayed_or_neutered"] == "Yes" and dog["borough"] == "Bronx":
		results_bronx_sn = results_bronx_sn + 1
	if dog["spayed_or_neutered"] == "Yes" and dog["borough"] == "Staten Island":
		results_statenisland_sn = results_statenisland_sn + 1
	if dog["spayed_or_neutered"] == "Yes" and dog["borough"] == "Brooklyn":
		results_brooklyn_sn = results_brooklyn_sn + 1
print "Manhattan:", 100*(float(results_mannhattan_sn)/float(results_mannhattan))
print "Queens", 100*(float(results_queens_sn)/float(results_queens))
print "Bronx", 100*(float(results_bronx_sn)/float(results_bronx))
print "Staten Island", 100*(float(results_statenisland_sn)/float(results_statenisland))
print "Brooklyn", 100*(float(results_brooklyn_sn)/float(results_brooklyn))

#7b. Which borough has the lowest % of spayed/neutered dogs?
print "7b. Which borough has the lowest % of spayed/neutered dogs?"

borough_dict = {"Manhattan": 100*(float(results_mannhattan_sn)/float(results_mannhattan)), "Queens": 100*(float(results_queens_sn)/float(results_queens)), "Bronx": 100*(float(results_bronx_sn)/float(results_bronx)), "Staten Island": 100*(float(results_statenisland_sn)/float(results_statenisland)), "Brooklyn": 100*(float(results_brooklyn_sn)/float(results_brooklyn))}

print min(borough_dict, key=borough_dict.get), "is the borough with the lowest percentage of spayed/neutered dogs."

#8. How many ZIP codes are in NYC?
print "8. How many ZIP codes are in NYC?"

zip_code = []
for dog in dogs:
	if dog["zip_code"] not in zip_code:
		zip_code.append( dog["zip_code"] )
print "In NYC there are", len(zip_code), "ZIP codes."

#9. How many are female vs. how many are male?
print "9. How many are female vs. how many are male?"

results_female = 0
for dog in dogs:
	if dog["gender"] == "F":
		results_female = results_female + 1
print "There are", results_female, "female dogs."

results_male = 0
for dog in dogs:
	if dog["gender"] == "M":
		results_male = results_male + 1
print "There are", results_male, "male dogs."

#10. How many different dog names are there in NYC?
print "10. How many different dog names are there in NYC?"

dog_names = []
for dog in dogs:
	if dog["dog_name"] not in dog_names:
		dog_names.append( dog["dog_name"] )
print "In NYC there are", len(dog_names), "dog names."

#11. How many different breeds of dog are in NYC?
print "11. How many different breeds of dog are in NYC?"

breeds = []
for dog in dogs:
	if dog["breed"] not in breeds:
		breeds.append( dog["breed"] )
print "In NYC there are", len(breeds), "different breeds of dog."

#12. What is the most popular breed of dog?
print "12. What is the most popular breed of dog?"

breeds = []
for dog in dogs:
	breeds.append(dog["breed"])

result_dict = dict( [ (i, breeds.count(i)) for i in set(breeds) ] )

print "The most popular breed is", max(result_dict, key=result_dict.get)

#13a. How many dogs are each color? Count only the dominant color.
print "13a. How many dogs are each color? Count only the dominant color."

dominant_color = []
for dog in dogs:
	dominant_color.append(dog["dominant_color"])
result_dict = dict( [(i, dominant_color.count(i)) for i in set(dominant_color) ] )
print result_dict

#13b. How many dogs are each color? Count both dominant, secondary and third colors.
print "13b. How many dogs are each color? Count both dominant, secondary and third colors."

secondary_color = []
for dog in dogs:
	if dog["secondary_color"] != "n/a":
		secondary_color.append(dog["secondary_color"])
result_dict_secondary = dict( [(i, secondary_color.count(i)) for i in set(secondary_color) ] )
print "Second colors:", result_dict_secondary

third_color = []
for dog in dogs:
	if dog["third_color"] != "n/a":
		third_color.append(dog["third_color"])
result_dict_third = dict( [(i, third_color.count(i)) for i in set(third_color) ] )
print "Third colors:", result_dict_third

#13c. What's the most popular color, if counting only dominant? If counting both dominant, secondary, and third colors?
print "13c. What's the most popular color, if counting only dominant? If counting both dominant, secondary, and third colors?"

print "The most popular color, if counting only the dominant color, is", max(result_dict, key=result_dict.get)

print "The most popular color, if counting only the secondary color, is", max(result_dict_secondary, key=result_dict_secondary.get)

print "The most popular color, if counting only the third color, is", max(result_dict_third, key=result_dict_third.get)

#14a. Make the ZIP code results from class into a dictionary, e.g. { '10028': 45, '10099': 120 }
print "14a. Make the ZIP code results from class into a dictionary, e.g. { '10028': 45, '10099': 120 }"

zip_code = []
for dog in dogs:
		zip_code.append( dog["zip_code"] )
result_dict = dict( [ (i, zip_code.count(i)) for i in set(zip_code) ] )
print result_dict

#14b. Prompt the user for a zip code, and use that dictionary to display the number of dogs in that ZIP code.

print "Enter your ZIP code."
zip = raw_input("ZIP code:")

dogs = dict((k, v) for k, v in result_dict.items() if k == zip)

print dogs

### not finished

