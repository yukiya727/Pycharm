import shelve

filehandler = open("Video_Games_Sales.csv")
filehandler.readline()
data = []
for line in filehandler:
    items = line.strip().split(';')
    Name = str(items[0])
    Global_sales = float(items[5])
    data.append([Name,Global_sales])
import random
import shelve
# Import the compatibility chart and the years table into dictionaries, and the sentences into a list
phrases = open("silly.txt").read().splitlines()
years = open("years.txt").read().splitlines()
signs = open("signs.txt").read().splitlines()
yearSign= {}
for iin range(len(years)):
yearSign[years[i].rstrip()] = signs[i].rstrip()
compatible = {}
file = open("signCompatibilities.csv")
file.readline()
for line in file:
items = line.strip().split(',')
compatible[items[0]] = [items[1], items[2], items[3]]
file.close()import random
import shelve
# Import the compatibility chart and the years table into dictionaries, and the sentences into a list
phrases = open("silly.txt").read().splitlines()
years = open("years.txt").read().splitlines()
signs = open("signs.txt").read().splitlines()
yearSign= {}
for iin range(len(years)):
yearSign[years[i].rstrip()] = signs[i].rstrip()
compatible = {}
file = open("signCompatibilities.csv")
file.readline()
for line in file:
items = line.strip().split(',')
compatible[items[0]] = [items[1], items[2], items[3]]
file.close()import random
import shelve
# Import the compatibility chart and the years table into dictionaries, and the sentences into a list
phrases = open("silly.txt").read().splitlines()
years = open("years.txt").read().splitlines()
signs = open("signs.txt").read().splitlines()
yearSign= {}
for iin range(len(years)):
yearSign[years[i].rstrip()] = signs[i].rstrip()
compatible = {}
file = open("signCompatibilities.csv")
file.readline()
for line in file:
items = line.strip().split(',')
compatible[items[0]] = [items[1], items[2], items[3]]
file.close()