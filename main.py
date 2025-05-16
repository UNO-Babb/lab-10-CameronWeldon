#MapPlot.py
#Name: Cameron Weldon
#Date:
#Assignment: Lab 10

import coffee
import pandas
import matplotlib.pyplot as plt

#I made a graph of Coffee Beans showing the Year and Sweetness score.

coffee = coffee.get_coffee()

print(coffee[0]["Data"]["Scores"]["Sweetness"])

years = []
scores = []
for bean in coffee:
    year = bean["Year"]
    score = bean["Data"]["Scores"]["Sweetness"]
    years.append(year)
    scores.append(score)
    

df = pandas.DataFrame({"Year": years,
                        "Score": scores})

print(df)
df.plot(kind = 'scatter', x = 'Year', y = 'Score')

plt.savefig("output")
