import pandas as pd
import numpy as np
import random

file_path = 'data.csv'
df = pd.read_csv(file_path)


col_name = df.columns[0]
ids = df[col_name].astype(str).tolist()


counts = np.zeros((10, 10), dtype=int)

for id_str in ids:
    id_str = id_str.strip()
    for i in range(len(id_str) - 1):
        try:
            current = int(id_str[i])
            next_d = int(id_str[i+1])
            counts[current][next_d] += 1
        except ValueError:
            continue


row_sums = counts.sum(axis=1, keepdims=True)

probabilities = np.divide(counts, row_sums, out=np.full_like(counts, 0.1, dtype=float), where=row_sums!=0)


def generate_markov_id(length=13):
    
    current_digit = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    
    generated_id = [str(current_digit)]
    
    
    for _ in range(length - 1):
       
        specific_probs = probabilities[current_digit]
        
        
        # utilizing the exact weights we found 26.7% vs 5%
        specific_probs = specific_probs / specific_probs.sum() 
        
        next_digit = np.random.choice(range(10), p=specific_probs)
        
        generated_id.append(str(next_digit))
        current_digit = next_digit
        
    return "".join(generated_id)

print(f"--- Generated  IDs based on {col_name} patterns ---")
for i in range(40):
    print(generate_markov_id())