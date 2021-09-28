"""
Part 2a Tutorial: Creating a bar chart using the csv file
"""

import csv   # To work with csv file
# To count total number of item appeared repeatedly
from collections import Counter
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

plt.style.use('fivethirtyeight')

#  Loading data from csv file
"""with open('data.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    for row in csv_reader:
    language_counter.update(row['LanguagesWorkedWith'].split(';'))
    """

# Importing data using pandas
data = pd.read_csv('data.csv')
ids = data['Responder_id']
lang_responses = data['LanguagesWorkedWith']

# Initializing the Counter
language_counter = Counter()

# Taking out the languages used by the developers (as per survey)
for response in lang_responses:
    language_counter.update(response.split(';'))

#   Getting top 15 languages and total users from the total list
languages = []
popularity = []
for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

# To reverse the chart according to the popularity
languages.reverse()
popularity.reverse()

# For Horizontal bar graph the first parameter is of Y axis
plt.barh(languages, popularity)

plt.xlabel('Number of Users')
# plt.ylabel('Programming Languages')
plt.title('Most Popular Languages')

plt.legend()

plt.tight_layout()

plt.show()
