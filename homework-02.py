# SHIVANGI BISHNOI
# 11/5/2023
# Homework 2



import datetime
import csv

# Q1 & Q10: prompting the user for their age

current_year = datetime.datetime.now().year

while True:
    yob = int(input ('What is your year of birth?'))
    # check if year is valid
    if yob <= current_year:
        break
    else:
        yob = int(input('Invalid entry: please enter the correct year of birth'))
    break

age = current_year-yob


print ('Your age is ' + str(age))

# Q2: Human heart Rate
# Taking midpoint of average range (60-100 bpm= 80) (source: https://www.health.harvard.edu/heart-health/what-your-heart-rate-is-telling-you)
minutes_in_year = 60*24*365
human_heart = int((80* age * minutes_in_year)/1000000)
print ('Your heart has beaten ' + str (human_heart)+ ' million times')

# Q3: Blue Whale's Heart Rate
# Taking the midpoint of the heart beat range (2-40 bpm = 19) (source: https://www.pnas.org/doi/10.1073/pnas.1914273116)
bw_heart = int((19 * age *minutes_in_year)/1000000)
print ('A blue whales heart has beaten ' + str(bw_heart)+ ' million times')

# Q4: Rabbit's Heart Rate
# Taking the midpoint of average range (120-180 bpm = 150) (source: https://rabbit.org/2013/02/temperature-and-respiration-rates/)

rabbit_heart = int((150*age * minutes_in_year)/1000000)
print ('A rabbits heart has beaten ' + str(rabbit_heart) + ' million times')

# Q5
# Using fstring
print  (f'A rabbits heart has beaten {rabbit_heart:,} million times')

## The f string seems a more intuitive option when spaces are involved

# Q6
# Part 1: my age= 30

age_diff = age - 30
if age_diff < 0:
    print ('You are ' + str(-1*age_diff) + ' years younger to me.')
elif age_diff>0:
    print ('You are ' + str(age_diff) + ' years older to me.')
elif age_diff == 0:
    print ('You are the same age as me')

# Part 2: odd/even

if (yob % 2) == 0:
    print ('Year of birth is even')
else:
    print ('Year of birth is odd')

# Q7 & Q8

# Compare the yob to the year in the csv 

# open csv for reading
with open('/Users/shivangibishnoi/Library/CloudStorage/Dropbox/J School/Foundations/Week 1/presidents.csv', 'r') as csv_file:
    #create csv reader which will iterate over rows and return a string
    csv_reader = csv.reader(csv_file)
    #iterate through the rows to find year of birth
    for row in csv_reader:
        #check if first column matches yob
        if row and row[0] == str(yob):
            print (f'The president of the U.S. was {row[1]} and the President has been from the Democratic Party {row[3]} times')
            break
    else:
            print('You are too old for this to work.')


# Q9 
# I manually counted the number of times democratic party was in the office. Since we were restricted to 1980 onwards, that was easy.
#  I tried working in pandas and something broke. In fact, as soon as I import pandas I cant get anything to work.

import pandas as pd

# loading csv file in memory since its small
presidents = pd.read_csv('/Users/shivangibishnoi/Library/CloudStorage/Dropbox/J School/Foundations/Week 1/presidents.csv')
# sorting for good practice
presidents = presidents.sort_values(by=["year"])
#restricting data set upto the year of birth
presidents = presidents[presidents["year"]<=yob]


            








