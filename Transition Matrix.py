import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


file_path = 'data.csv'
df = pd.read_csv(file_path)


id_column_name = df.columns[0] 
ids = df[id_column_name].astype(str).tolist()

print(f"Analyzing {len(ids)} IDs from column: '{id_column_name}'...")

# Transition Matrix
# count how many times digit x is followed by digit y
counts = np.zeros((10, 10), dtype=int)

for id_str in ids:
    id_str = id_str.strip() 
    for i in range(len(id_str) - 1):
        try:
            current_d = int(id_str[i])
            next_d = int(id_str[i+1])
            counts[current_d][next_d] += 1
        except ValueError:
            continue

# convert counts to Probabilities

row_sums = counts.sum(axis=1, keepdims=True)
with np.errstate(divide='ignore', invalid='ignore'):
    probabilities = counts / row_sums
probabilities = np.nan_to_num(probabilities) 


print("\n--- Top 3 Most Predictable Patterns ---")
for i in range(10):
    
    best_next = np.argmax(probabilities[i])
    chance = probabilities[i][best_next]
    
    
    if chance > 0.20: 
        print(f"If we see '{i}', the next digit is likely '{best_next}' ({chance*100:.1f}% probability)")

plt.figure(figsize=(10, 8))
sns.heatmap(probabilities, annot=True, fmt=".2f", cmap="Blues", cbar=True)
plt.title(" View: Probability of Next Digit")
plt.xlabel("Next Digit")
plt.ylabel("Current Digit")
plt.show()