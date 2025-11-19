import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load CSV file
file_name = "ML374_S2_DeliverybyZone_Data_Practice.xlsx"

try:
    df = pd.read_excel(file_name)

    if 'Delivery_Time_Hours' not in df.columns:
        print("CSV must contain 'Delivery_Time_Hours' column.")
        exit()

    population_data = df['Delivery_Time_Hours']

    # Draw 200 repeated samples of size 30 with replacement
    sample_size = 30
    num_samples = 200
    sample_means = []

    for _ in range(num_samples):
        sample = np.random.choice(population_data, size=sample_size, replace=True)
        sample_means.append(sample.mean())

    # Plot histogram with KDE
    sns.histplot(sample_means, bins=15, color='skyblue', edgecolor='black', kde=True)
    plt.title('Sampling Distribution of Sample Means (CLT Demonstration)')
    plt.xlabel('Sample Mean Delivery Time (Hours)')
    plt.ylabel('Count')
    plt.show()

except FileNotFoundError:
    print(f"File '{file_name}' not found.")
except Exception as e:
    print("Error:", e)
