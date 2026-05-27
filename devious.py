#Niki
#Challenge3
#A tech company’s server was compromised. You are analyzing an annual log to discover the story behind the hack.
#Init
import pandas as pd
data=pd.read_csv('hacker.csv')
log_id=data['Log_ID'].tolist()
ip_address=data['IP_Address'].tolist()
protocol=data['Protocol'].tolist()
data_kb=data['Data_KB'].tolist()
time=data['Time'].tolist()
description=data['Description'].tolist()
filter=[]

#Func
def compromise(take):
    for i in range(len(time)):
        if take in description[i]:
            filter.append([i])
    print(filter)
    filter.clear()

def stolen(have):
    for i in range(len(time)):
        if have in description[i]:
            filter.append([i])
    print(filter)
    filter.clear()

def forced(input):
    for i in range(len(time)):
        if input in description[i]:
            filter.append([i])
    print(len(filter))
    filter.clear()

#Main
compromise("Failed")
print(data.loc[[193,194,195,196]])
stolen('Bulk')
print(data.loc[[199]])
forced('Reset')

