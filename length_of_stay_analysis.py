# Module 9
import pandas as pd
import numpy as np
from scipy.stats import skew, norm
import matplotlib.pyplot as plt

# Load data from the "Data" sheet of the Excel file with the first row as headers
df = pd.read_excel('Myocardial_infarction.xlsx', sheet_name='Data', header=None, names=['Country', 'Length_of_Stay'])

# Clean the 'Length_of_Stay' column by converting it to numeric, handling errors as 'coerce'
df['Length_of_Stay'] = pd.to_numeric(df['Length_of_Stay'], errors='coerce')

# Drop rows with NaN values in the 'Length_of_Stay' column
df.dropna(subset=['Length_of_Stay'], inplace=True)

# a) Find the Mean, Mode, and Median of the data
mean = df['Length_of_Stay'].mean()
mode = df['Length_of_Stay'].mode().values[0] # In case there are multiple modes
median = df['Length_of_Stay'].median()

print("Mean:", mean)
print("Mode:", mode)
print("Median:", median)

# b) Apply Gaussian Distribution and find the skewness of the data
skewness = skew(df['Length_of_Stay'])

print("Skewness:", skewness)

# Visualization
plt.figure(figsize=(10, 6))

# Calculate the histogram separately
hist_data, bins, _ = plt.hist(df['Length_of_Stay'], bins=10, density=True, alpha=0.7, color='blue', label='Data')
plt.xlabel('Length of Stay (in days)')
plt.ylabel('Density of Observations (Length of Stay)')
plt.title('Average Length of Stay Distribution for Acute Myocardial Infarction (2020)')

# Create a range of values for the Gaussian distribution within the same range as the data
x = np.linspace(min(df['Length_of_Stay']), max(df['Length_of_Stay']), 100)

# Fit Gaussian distribution to the data
pdf = norm.pdf(x, mean, df['Length_of_Stay'].std())

# Plot the Gaussian distribution curve on top of the histogram in red
plt.plot(x, pdf, color='red', label='Fitted Gaussian Distribution')

plt.legend(loc='best')
plt.grid(True)

plt.show()