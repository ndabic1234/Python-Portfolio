#Niki
#Challenge2
#A top-tier creator’s channel is dying, and they don’t know why. You have 10 years of monthly data tracking views and dislikes etc...
#Init
import pandas as pd
data = pd.read_csv("influencer.csv")
month=data['Month'].tolist()
views=data['Views'].tolist()
dislikes=data['Dislikes'].tolist()
subscriber=data['Subscriber(+-)'].tolist()
revenue=data['Revenue'].tolist()
filter=[]
#Func
def humble_begin(input):
    for i in range(len(month)):
        if views[i]<=input:
            filter.append(month[i])
    print(filter)
    filter.clear()

def golden_age(climb):
    for i in range(len(month)):
        if subscriber[i]>climb:
            filter.append(month[i])
    print(filter)
    filter.clear()

def scandal(done):
    for i in range(len(month)):
        if revenue[i]==done:
            filter.append(month[i])
    print(filter)
    filter.clear()
#Main
humble_begin(2000)
golden_age(50000)
scandal(0)
