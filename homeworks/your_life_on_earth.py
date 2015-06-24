#Vanessa Wormer
#05/27/2015
#Homework 1

#Prompt the user for their year of birth
print "Enter your birth day"
year_of_birth = raw_input("year_of_birth:")

#and tell them (approximately) how old they are
age = 2015 - int(year_of_birth)
print "You are approximately", age, "years old"

#How many times their heart has beaten
#one year has 525600 minutes, 100 heartbeats per minute
heartbeat = int(age * 52560000)
print "Your heart has beaten", heartbeat, "times"

#How many times a blue whale's heart has beaten
#one year has 525600 minutes, 6 heartbeats per minute
heartbeat_whale = int(age * (525600 * 6))
print "A blue whale's heart has beaten", heartbeat_whale, "times"

#How many times a rabbit's heart has beaten
#one year has 525600 minutes, 120 heartbeats per minute
heartbeat_rabbit = int(age * (525600 * 120))
print "A rabbit's heart has beaten", heartbeat_rabbit, "times"

#If the answer to (19) is more than a billion, say "XXX billion" instead of the very long raw number
if heartbeat_rabbit > 1000000000:
	print round(float(heartbeat_rabbit)/1000000000,1),"billion"
else:
	print heartbeat_rabbit
#How old they are in Venus years
#1 year on Earth == 1.63 years on Venus
venus = int(age * 1.63)
print "You are", venus, "years old on Venus."

#How old they are in Neptune years
#1 year on Earth == 0.006 years on Neptune
neptune = age * 0.006
print "You are", neptune, "years old on Neptune."

#Whether they are the same age as you, older or younger
#I'm 27 years old
if age == 27:
	print "You are the same age as me."
if age > 27:
	print "You are older than me."
if age < 27:
	print "You are younger than me."

#If older or younger, how many years difference
age_older = age - 27
if age > 27:
	print "You are", age_older, "older than me."
age_younger = 27 - age
if age < 27:
	print "You are", age_younger, "younger than me."

#If they were born in an even or odd year
if int(year_of_birth) % 2 == 0:
	print "You were born in an even year."
else:
	print "You were born in an odd year."

#How many times the Pittsburgh Steelers have won the Superbowl.
#superbowl = 1974,1975,1978,1979,2005,2008
if int(year_of_birth) > 2008:
	print "The Pittsburgh Steelers have won 0 times the Superbowl."
elif int(year_of_birth) > 2005:
	print "The Pittsburgh Steelers have won 1 time the Superbowl."
elif int(year_of_birth) > 1979:
	print "The Pittsburgh Steelers have won 2 times the Superbowl."
elif int(year_of_birth) > 1978:
	print "The Pittsburgh Steelers have won 3 times the Superbowl."
elif int(year_of_birth) > 1975:
	print "The Pittsburgh Steelers have won 4 times the Superbowl."
elif int(year_of_birth) > 1974:
	print "The Pittsburgh Steelers have won 5 times the Superbowl."
elif int(year_of_birth) < 1975:
	print "The Pittsburgh Steelers have won 6 times the Superbowl."
	
#Which US President was in office when they were born (FDR onward)
#Franklin D. Roosevelt = 1933 - 1945
#Harry S. Truman = 1945 - 1953
#Dwight D. Eisenhower = 1953 - 1961
#John F. Kennedy = 1961 - 1963
#Lyndon B. Johnson = 1963 - 1969
#Richard Nixon = 1969 - 1974
#Gerald Ford = 1974 - 1977
#Jimmy Carter = 1977 - 1981
#Ronald Reagan = 1981 - 1989
#George H. W. Bush = 1989 - 1991
#Bill Clinton = 1993 - 2001
#George W. Bush = 2001 - 2009
#Barack Obama = 2009 - 2015

if int(year_of_birth) > 2009:
	print "Barack Obama was President when you was born."
elif int(year_of_birth) > 2001:
	print "George W. Bush was President when you was born."	
elif int(year_of_birth) > 1993:
	print "Bill Clinton was President when you was born."	
elif int(year_of_birth) > 1989:
	print "George H. W. Bush was President when you was born."	
elif int(year_of_birth) > 1981:
	print "Ronald Reagan was President when you was born."	
elif int(year_of_birth) > 1977:
	print "Jimmy Carter was President when you was born."	
elif int(year_of_birth) > 1974:
	print "Gerald Ford was President when you was born."	
elif int(year_of_birth) > 1969:
	print "Richard Nixon was President when you was born."	
elif int(year_of_birth) > 1963:
	print "Lyndon B. Johnson was President when you was born."	
elif int(year_of_birth) > 1961:
	print "John F. Kennedy was President when you was born."	
elif int(year_of_birth) > 1953:
	print "Dwight D. Eisenhower was President when you was born."	
elif int(year_of_birth) > 1945:
	print "Harry S. Truman was President when you was born."	
elif int(year_of_birth) < 1933:
	print "Franklin D. Roosevelt was President when you was born."	


#If someone gives you a year in the future, try asking them again 
if int(year_of_birth) > 2015:
	print "You have to enter a real date. Please try again."
	year_of_birth = raw_input("year_of_birth:")
