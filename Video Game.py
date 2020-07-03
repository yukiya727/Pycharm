import shelve

filehandler = open("Video_Games_Sales.csv")
filehandler.readline()
data = []
for line in filehandler:
    items = line.strip().split(';')
    Name = str(items[0])
    Global_sales = float(items[5])
    data.append([Name,Global_sales])
filehandler.close()
data.sort()

shelfFile = shelve.open('Video_game', 'w')
shelfFile['video_game'] = data
shelfFile.close()

shelfFile = shelve.open('Video_game', 'r')
for key in shelfFile.keys():
    print(shelfFile[key])
shelfFile.close()