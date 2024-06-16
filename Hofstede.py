import numpy as np
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt

pd.plotting.register_matplotlib_converters()
# %matplotlib inline

# Path of the CSV file to read
hofstede_model_path = "6-dimensions-for-website-2015-08-16.csv"

# Read the file into a variable hofstede_model
hofstede_model = pd.read_csv(hofstede_model_path, sep=';', index_col="country")

# Replace '#NULL!' values with NaNs
hofstede_model = hofstede_model.replace('#NULL!', np.nan)

# Drop the rows where at least one element is NaN
hofstede_model = hofstede_model.dropna()

# Convert numerical values from String to Int
exclude = ['ctr']
for col in hofstede_model.columns:
    if col not in exclude:
        hofstede_model[col] = hofstede_model[col].astype(int)

# The first five rows of the data
print(hofstede_model.head())

# Define a function to create bar plots
def create_bar_plot(sorted_data, index, title, ylabel):
    plt.figure(figsize=(10, 30))
    plt.title(title)
    plt.ylabel("Nations")
    plt.xlabel(ylabel)
    sns.barplot(x=sorted_data[index], y=sorted_data.index)
    plt.show()

# Plotting each index
indices = {
    'pdi': "Power distance index",
    'idv': "Individualism-collectivism index",
    'uai': "Uncertainty avoidance index",
    'mas': "Femininity-masculinity index",
    'ltowvs': "Long-term orientation - Short-term orientation index",
    'ivr': "Indulgence - Restraint index"
}

for index, ylabel in indices.items():
    sorted_data = hofstede_model.sort_values([index], ascending=False)
    create_bar_plot(sorted_data, index, f"Hofstede’s {ylabel} ({index.upper()})", ylabel)
