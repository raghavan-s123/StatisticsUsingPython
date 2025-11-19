import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import sys

# --- Constants ---
RANDOM_SEED = 42
SIMPLE_SAMPLE_SIZE = 50

def load_data(file_name):
    """Loads an Excel file into a pandas DataFrame."""
    file_path = os.path.join(sys.path[0], file_name)

    try:
        df = pd.read_excel(file_path)
        print(f"File loaded successfully: {file_name}")
        return df
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        sys.exit()
    except Exception as e:
        print(f"Error loading Excel file: {e}")
        sys.exit()

def part1_compare_population_vs_sample(population_df):
    """
    Part 1: Plots the population distribution vs. a single sample distribution.
    """
    print(f"\n--- Part 1: Population vs. Sample (n={SIMPLE_SAMPLE_SIZE}) ---")
    
    if len(population_df) < SIMPLE_SAMPLE_SIZE:
        print(f"Not enough rows to sample {SIMPLE_SAMPLE_SIZE} rows. Total rows: {len(population_df)}")
        return

    simple_sample_df = population_df.sample(n=SIMPLE_SAMPLE_SIZE, random_state=RANDOM_SEED)

    plt.figure(figsize=(10, 6))
    sns.set_style("whitegrid")
    
    # --- MODIFIED PLOTTING ---
    # Plot the entire population distribution (Filled)
    sns.kdeplot(population_df['Height_cm'], 
                color="blue", 
                label='Population', 
                fill=True,  # Fill the population curve
                common_norm=False)
    
    # Overlay the sample distribution (Line only)
    sns.kdeplot(simple_sample_df['Height_cm'], 
                color="green", 
                label=f'Sample (n={SIMPLE_SAMPLE_SIZE})', 
                fill=False, # Do not fill the sample curve
                linestyle='--', # Add dashed line to match sample
                common_norm=False)
    # --- END MODIFICATION ---
    
    plt.title('Population vs. Simple Sample Distribution (Height)', fontsize=16)
    plt.xlabel('Height (cm)', fontsize=12)
    plt.ylabel('Density') # Kdeplot shows density, not count
    plt.legend()
    plt.show()

def part2_increasing_sample_sizes(population_df):
    """
    Part 2: Plots distributions for multiple increasing sample sizes.
    """
    print("\n--- Part 2: Effect of Increasing Sample Sizes ---")
    
    sample_sizes = [5, 15, 25, 35]
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    axes = axes.flatten()
    sns.set_style("darkgrid") # Match the style for this specific chart

    fig.suptitle('Distribution Shape by Increasing Sample Size', fontsize=18)

    for i, size in enumerate(sample_sizes):
        ax = axes[i]
        
        if len(population_df) < size:
            ax.set_title(f"Sample Size = {size} (Not enough data)")
            continue

        sample_df = population_df.sample(n=size, random_state=RANDOM_SEED)
        
        # This plot (histplot with KDE) already matches your screenshot
        sns.histplot(sample_df['Height_cm'], 
                     ax=ax, 
                     kde=True, 
                     stat='density',
                     common_norm=False)
        
        ax.set_title(f'Sample Size = {size}')
        ax.set_xlabel('Height (cm)')
        ax.set_ylabel('Density')

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()

# --- Main Execution ---
if __name__ == "__main__":
    file_name = "ML374_S2_Height_Weight_Data_Concept.xlsx"
    
    population_df = pd.read_excel(file_name)
    
    print(f"Data shape: {population_df.shape}")
    print("Preview of Loaded Data:")
    print(population_df.head())

    # Run Part 1
    part1_compare_population_vs_sample(population_df)
    
    # Run Part 2
    part2_increasing_sample_sizes(population_df)