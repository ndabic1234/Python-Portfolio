#Niki
#challenge1
#A new indie game  just received feedback on their beta test. You have the data and need to analyze it to see where the team could make improvements.
#Init
import pandas as pd
data = pd.read_csv("gamedev.csv")
level=data['Level'].tolist()
time=data['Time'].tolist()
rating=data['Rating'].tolist()
summary=data['Summary'].tolist()
feedback=data['Feedback'].tolist()
filter=[]
#Functions
def find_problems(level_rating):
    for i in range(len(level)):
        if rating[i]<=level_rating:
            filter.append([i])
    print(filter)
    filter.clear()

def high_time(timing,review):
    for i in range(len(time)):
        if time[i]>=timing and rating[i]>=review:
            filter.append([i])
    print(filter)
    filter.clear()

def hidden(message):
    for i in range(len(feedback)):
        if message in feedback[i]:
            filter.append([i])
    print(filter)
    filter.clear()

#Main
find_problems(2)
print(data.loc[[14,34,77]])
high_time(700,4)
print(data.loc[79])
hidden("secret")
print(data.loc[66])
