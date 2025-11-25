# Digit Transition Analysis & Generator

This project analyzes sequences of digits (IDs) to understand the probability of one digit following another. It uses a Markov Chain approach to build a transition matrix and can generate new ID sequences that mimic the patterns found in the input data.

## Files

- **`Transition Matrix.py`**: 
  - Reads IDs from `data.csv`.
  - Calculates the transition matrix (probability of digit $j$ following digit $i$).
  - Identifies and prints the most predictable patterns.
  - Visualizes the transition probabilities using a heatmap.

- **`test_2.py`**:
  - Performs the same transition analysis.
  - Includes a `generate_markov_id(length)` function to generate new synthetic IDs based on the learned probabilities.

- **`data.csv`**: 
  - Input data file containing the IDs to be analyzed.

## Dependencies

This project requires Python and the following libraries:

- pandas
- numpy
- seaborn
- matplotlib

You can install them using pip:

```bash
pip install pandas numpy seaborn matplotlib
```

## Usage

1. **Prepare Data**: Ensure your `data.csv` file is in the same directory. It should have a header row and a column containing the numeric IDs.

2. **Analyze Patterns**: Run the transition matrix script to see the heatmap and probability analysis.
   ```bash
   python "Transition Matrix.py"
   ```

3. **Generate IDs**: You can import the generator from `test_2.py` or run the script to generate new IDs based on the learned patterns.
