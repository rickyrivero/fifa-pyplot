import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

fifa = pd.read_csv('fifa_data.csv')

left = fifa.loc[fifa['Preferred Foot'] == 'Left'].count()[0]
right = fifa.loc[fifa['Preferred Foot'] == 'Right'].count()[0]

colors = ['blue', 'green']

plt.pie([left, right], labels=['Left', 'Right'], autopct='%.2f %%', colors=colors)

plt.title('Foot Preference of FIFA Players')

plt.show()