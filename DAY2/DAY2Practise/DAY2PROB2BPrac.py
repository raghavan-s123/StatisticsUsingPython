import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Excel file (update file name if needed)
df = pd.read_excel("ML374_S2_DeliverybyZone_Data_Practice.xlsx")

# Column containing delivery time
col = "Delivery_Time_Hours"   # change if your column name is different

# Population = whole data
population = df[col]

# Sample = random 50 rows (you can change n= )
sample = df[col].sample(n=50, random_state=42)

# Plot settings
sns.set(style="whitegrid")

plt.figure(figsize=(15, 6))

# --------------------------
# LEFT PLOT – Population
# --------------------------
plt.subplot(1, 2, 1)
sns.histplot(population, bins=20, kde=True, color="blue",
             edgecolor="black", stat="density", alpha=0.6)
plt.title("Population Delivery Times", fontsize=14)
plt.xlabel("Delivery_Time_Hours")
plt.ylabel("Density")

# --------------------------
# RIGHT PLOT – Sample
# --------------------------
plt.subplot(1, 2, 2)
sns.histplot(sample, bins=20, kde=True, color="orange",
             edgecolor="black", stat="density", alpha=0.6)
plt.title("Sample Delivery Times", fontsize=14)
plt.xlabel("Delivery Time (Hours)")
plt.ylabel("Density")
plt.legend(["Sample"], loc="upper right")

plt.tight_layout()
plt.show()
