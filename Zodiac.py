import random
import shelve

# Import the compatibility chart and the years table into dictionaries, and the sentences into a list
phrases = open("silly.txt").read().splitlines()
years = open("years.txt").read().splitlines()
signs = open("signs.txt").read().splitlines()

yearSign = {}
for iine in range(len(years)):
    yearSign[years[i].rstrip()] = signs[i].rstrip()
compatible = {}

file = open("signCompatibilities.csv")
file.readline()

for line in file:
    items = line.strip().split(',')
compatible[items[0]] = [items[1], items[2], items[3]]

file.close()

yourYear = input("year your were born? ")
yourSign = yearSign[yourYear]
print("Your Chinese zodiac sign is", yourSign)
yourHoroscope = random.choice(phrases)
print("Your horoscope:", yourHoroscope)
print("Your compatible signs:", compatible[yourSign])
# Shelve the information

shelfFile = shelve.open('yourZodiac')
shelfFile['year'] = yourYear
shelfFile['sign'] = yourSign
shelfFile['horoscope'] = yourHoroscope
shelfFile['compatibilities'] = compatible[yourSign]
print(list(shelfFile.items()))
shelfFile.close()

