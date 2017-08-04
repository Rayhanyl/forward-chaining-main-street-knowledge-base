#Artificial Intelligence
#Project 1 - Knowledge System (due April 4, 2016)
# A knowledge system using forward chaining designed to make conclusions based off the restaurant knowledge base.

#Myles Johnson-Gray, Kati McLaughlin, Niko Snow

#INFORMATION KEY:
#A - allergy accommodating
#GF - gluten-free
#V - vegan
#VEG - vegetarian
#Prices - either "Low", "Medium", or "High"
#Style - either "Sub", "Pub", "Pizza", "Ethnic", "Mexican"

#import time module
import time

#describes format of user arguments
#           (None?, A?, GF?, V?, VEG?, Price, Takeout?, Alcohol?, Style?)
#           (all values except 'Price' and 'Style' are boolean 0 or 1...if None is 1, A,GF,V,VEG are ignored)
userInput = [1, 0, 0, 0, 0, "Low", 0, 0, "Pub"]

#list that will store keys of restaurants to be deleted
deleteKey = []

#dictionary containing restaurants and all relevant information needed to infer
# Diet(veg, vegan, allergies accommodating?), Price, Distance, Alcohol, TakeOut, style)
d = {'ClaymontSteak': {'Diet': None, 'Price': "Medium", 'Takeout' : 1, 'Alcohol': 1, 'Style' : "Sub", 'Distance': 350},
     'GrottosPizza': {'Diet': {'GF', 'VEG'}, 'Price': "Medium", 'Takeout' : 1, 'Alcohol': 1, 'Style' : "Pizza", 'Distance': 500},
     'NewarkDeli': {'Diet': None, 'Price': "Medium", 'Takeout' : 1, 'Alcohol': 0, 'Style' : "Sub", 'Distance': 550},
     'CalTortilla': {'Diet': {'A', 'GF', 'V', 'VEG'}, 'Price': "Medium", 'Takeout' : 1, 'Alcohol': 1, 'Style' : "Mexican", 'Distance': 600},
     'IndianSizz': {'Diet': {'VEG'}, 'Price': "Medium", 'Takeout' : 0, 'Alcohol': 1, 'Style' : "Ethnic", 'Distance': 650},
     'DelPez': {'Diet': {'A', 'GF', 'V', 'VEG'}, 'Price': "High", 'Takeout' : 1, 'Alcohol': 1, 'Style' : "Mexican", 'Distance': 700},
     'PatsPizza': {'Diet': {'VEG'}, 'Price': "Medium", 'Takeout' : 0, 'Alcohol': 1, 'Style' : "Pizza", 'Distance': 720},
     'CatherineRooneys': {'Diet': None, 'Price': "High", 'Takeout' : 0, 'Alcohol': 1, 'Style' : "Pub", 'Distance': 750},
     'Homegrown': {'Diet': {'A', 'GF', 'V', 'VEG'}, 'Price': "High", 'Takeout' : 1, 'Alcohol': 1, 'Style' : "Sub", 'Distance': 850},
     'Mizu': {'Diet': {'GF', 'VEG'}, 'Price': "Medium", 'Takeout' : 1, 'Alcohol': 0, 'Style' : "Ethnic", 'Distance': 870},
     'Chipotle': {'Diet': {'A', 'GF', 'V', 'VEG'}, 'Price': "Medium", 'Takeout' : 1, 'Alcohol': 0, 'Style' : "Mexican", 'Distance': 880},
     'Margheritas': {'Diet': {'GF', 'VEG'}, 'Price': "Low", 'Takeout' : 1, 'Alcohol': 1, 'Style' : "Pizza", 'Distance': 890},
     'Cheeburger': {'Diet': None, 'Price': "Medium", 'Takeout' : 1, 'Alcohol': 0, 'Style' : "Pub", 'Distance': 900},
     'JimmyJohns': {'Diet': None, 'Price': "Low", 'Takeout' : 1, 'Alcohol': 0, 'Style' : "Sub", 'Distance': 920},
     'Arenas': {'Diet': None, 'Price': "Medium", 'Takeout' : 0, 'Alcohol': 1, 'Style' : "Pub", 'Distance': 950},
     'AliBaba': {'Diet': {'A', 'GF', 'V', 'VEG'}, 'Price': "High", 'Takeout' : 0, 'Alcohol': 1, 'Style' : "Ethnic", 'Distance': 1000},
     'KlondikeKates': {'Diet': {'A', 'GF', 'V', 'VEG'}, 'Price': "High", 'Takeout' : 1, 'Alcohol': 1, 'Style' : "Pub", 'Distance': 1050},
     'Subway': {'Diet': None, 'Price': "Low", 'Takeout' : 1, 'Alcohol': 0, 'Style' : "Sub", 'Distance': 1020},
     'BanhMiBoy': {'Diet': {'V', 'VEG'}, 'Price': "Low", 'Takeout' : 0, 'Alcohol': 1, 'Style' : "Ethnic", 'Distance': 1100},
     'SanteFe': {'Diet': {'V', 'VEG'}, 'Price': "High", 'Takeout' : 0, 'Alcohol': 1, 'Style' : "Mexican", 'Distance': 1150},
     'GreeneTurtle': {'Diet': {'A', 'GF', 'VEG'}, 'Price': "High", 'Takeout' : 0, 'Alcohol': 1, 'Style' : "Pub", 'Distance': 1180},
     'No1Chinese': {'Diet': {'VEG'}, 'Price': "Low", 'Takeout' : 1, 'Alcohol': 0, 'Style' : "Ethnic", 'Distance': 1900},
     'McDonalds': {'Diet': None, 'Price': "Low", 'Takeout' : 1, 'Alcohol': 0, 'Style' : "Pub", 'Distance': 2600},
     'Wawa': {'Diet': {'A', 'VEG'}, 'Price': "Low", 'Takeout' : 1, 'Alcohol': 0, 'Style' : "Sub", 'Distance': 2700},
     'OleTapas': {'Diet': {'A', 'GF', 'V', 'VEG'}, 'Price': "High", 'Takeout' : 1, 'Alcohol': 1, 'Style' : "Ethnic", 'Distance': 5700},
     'Bertuccis': {'Diet': None, 'Price': "High", 'Takeout' : 1, 'Alcohol': 1, 'Style' : "Pizza", 'Distance': 9700},
     'RedRobin': {'Diet': {'A', 'GF', 'VEG'}, 'Price': "Medium", 'Takeout' : 1, 'Alcohol': 1, 'Style' : "Pub", 'Distance': 9800},
     'BorderCafe': {'Diet': None, 'Price': "High", 'Takeout' : 0, 'Alcohol': 1, 'Style' : "Mexican", 'Distance': 12500}
     }

#start timer
start = time.clock()

#DIETARY TRIMMING!!!!!!!!!!!!!!!!!!!!!!!!

#if dietary preference
if userInput[0] !=  1:
    #trimming by diet
    for key, values in d.items():
        for k, v in values.items():
            if k == 'Diet':
                #delete entries with no dietary accommodation
                if v == None:
                    deleteKey.append(key)
                else:
                    #if allergy accommodating
                    if userInput[1] == 1:
                        #if not none
                        if v != None:
                            #delete entries without A...
                            if 'A' not in v:
                                deleteKey.append(key)
                    if userInput[2] == 1:
                        if v != None:
                            if 'GF' not in v:
                                if key not in deleteKey:
                                    deleteKey.append(key)
                    if userInput[3] == 1:
                        if v != None:
                            if 'V' not in v:
                                if key not in deleteKey:
                                    deleteKey.append(key)
                    if userInput[4] == 1:
                        if v != None:
                            if 'VEG' not in v:
                                if key not in deleteKey:
                                    deleteKey.append(key)

#delete entries that don't comply with dietary restrictions
for i in deleteKey:
    del d[i]

#reset deleteKey list
deleteKey = []

#PRICE TRIMMING!!!!!!!!!!!!!!!!!!!!!!!!

#if user wants low budget dining
if userInput[5] ==  "Low":
    #trimming by low priced restaurants
    for key, values in d.items():
        for k, v in values.items():
            if k == 'Price':
                if v != "Low":
                    deleteKey.append(key)
#if user wants medium budget dining
if userInput[5] ==  "Medium":
    #trimming by medium priced restaurants
    for key, values in d.items():
        for k, v in values.items():
            if k == 'Price':
                if v != "Medium":
                    deleteKey.append(key)
#if user wants high budget dining
if userInput[5] ==  "High":
    #trimming by high priced restaurants
    for key, values in d.items():
        for k, v in values.items():
            if k == 'Price':
                if v != "High":
                    deleteKey.append(key)

#delete entries that don't comply with price restrictions
for i in deleteKey:
    del d[i]

#reset deleteKey list
deleteKey = []

#TAKEOUT TRIMMING!!!!!!!!!!!!!!!!!!!!!!!!

if userInput[6] ==  1:
    #trimming by takeout restrictions
    for key, values in d.items():
        for k, v in values.items():
            if k == 'Takeout':
                if v != 1:
                    deleteKey.append(key)

#delete entries that don't comply with takeout restrictions
for i in deleteKey:
    del d[i]

#reset deleteKey list
deleteKey = []

#ALCOHOL TRIMMING!!!!!!!!!!!!!!!!!!!!!!!!

if userInput[7] ==  1:
    #trimming by alcohol restriction
    for key, values in d.items():
        for k, v in values.items():
            if k == 'Alcohol':
                if v != 1:
                    deleteKey.append(key)

#delete entries that don't comply with alcohol restrictions
for i in deleteKey:
    del d[i]

#reset deleteKey list
deleteKey = []

#STYLE TRIMMING!!!!!!!!!!!!!!!!!!!!!!!!

#if user wants sub dining
if userInput[8] ==  "Sub":
    for key, values in d.items():
        for k, v in values.items():
            if k == 'Style':
                if v != "Sub":
                    deleteKey.append(key)
#if user wants pub budget dining
if userInput[8] ==  "Pub":
    for key, values in d.items():
        for k, v in values.items():
            if k == 'Style':
                if v != "Pub":
                    deleteKey.append(key)
#if user wants pizza dining
if userInput[8] ==  "Pizza":
    for key, values in d.items():
        for k, v in values.items():
            if k == 'Style':
                if v != "Pizza":
                    deleteKey.append(key)
#if user wants ethnic dining
if userInput[8] ==  "Ethnic":
    for key, values in d.items():
        for k, v in values.items():
            if k == 'Style':
                if v != "Ethnic":
                    deleteKey.append(key)
#if user wants mexican dining
if userInput[8] ==  "Mexican":
    for key, values in d.items():
        for k, v in values.items():
            if k == 'Style':
                if v != "Mexican":
                    deleteKey.append(key)

#delete entries that don't comply with price restrictions
for i in deleteKey:
    del d[i]

#reset deleteKey list
deleteKey = []

print("--------------------------")

#if the dictionary is not empty...
if d != {}:
    #DISTANCE TIE BREAKER!!!!!!!!!!!!!!!!!!!!!!!!
    #Find the restaurant with the minimum distance.
    temp = 999999
    temp2 = ''
    for key, values in d.items():
        for k, v in values.items():
            if k == 'Distance':
                if temp > v:
                    temp = v
                    temp2 = key
    print("Our system recommends you dine at: " + temp2)
else:
    print("We could not find a restaurant based on your preferences...please try again")

#end timer
print("--------------------------")
end = time.clock()
print("Execution took " + str(end - start) + " seconds")
print("--------------------------")