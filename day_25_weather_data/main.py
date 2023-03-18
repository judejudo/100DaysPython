# with open("day_25_weather_data/weather_data.csv") as csv_data:
#     list_of_data = csv_data.readlines()
#     print(list_of_data)

# import csv

# with open("day_25_weather_data/weather_data.csv") as csv_data:
#     data = csv.reader(csv_data)
#     temperatures = []  
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
    
import pandas
data = pandas.read_csv("day_25_weather_data/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(type(data))
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# # print(data["temp"].max())
# print(data.condition)

# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp) *9/5 + 32
# print(monday_temp)

#Create a dataframe from scratch
# data_dict = {
#     "students":["Amy","James", "Angela"],
#     "scores":[76,56,65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
count = 0
grey_squirrels = data[data["Primary Fur Color"] == "Gray"]
print(len(grey_squirrels))

red_squirrels = data[data["Primary Fur Color"] == "Cinnamon"]
print(len(red_squirrels))

black_squirrels = data[data["Primary Fur Color"] == "Black"]
print(len(black_squirrels))

data_dict ={
    "Primary Fur Color":["Gray","Cinnamon","Black"],
    "Count":[len(grey_squirrels), len(red_squirrels),len(black_squirrels)]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_squrrel_data.csv")