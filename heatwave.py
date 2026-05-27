#Niki
#challenge 1
#In this set you will be given arrays linked by index. You must filter the data into an additional array to gain some insight from the data. Each function must have a parameter.
#Init
# The dates as strings
july_days = [ "July 1", "July 2", "July 3", "July 4", "July 5", "July 6", "July 7", "July 8", "July 9", "July 10", "July 11", "July 12", "July 13", "July 14", "July 15", "July 16", "July 17", "July 18", "July 19", "July 20", "July 21", "July 22", "July 23", "July 24", "July 25", "July 26", "July 27", "July 28", "July 29", "July 30", "July 31" ]

# The temperatures in Fahrenheit
july_temps = [
    82, 84, 87, 89, 93, 95, 91, 88, 86, 84,
    86, 89, 95, 97, 98, 101, 97, 93, 89, 87,
    86, 91, 95, 93, 89, 87, 84, 86, 89, 93, 91
]
filtered_days=[]

#Functions
def heatwave(temp):
    for i in range(len(july_temps)):
        if july_temps[i] >= temp:
            filtered_days.append(july_days[i])
    print(filtered_days)
    filtered_days.clear()
#main
heatwave(95)
