import pandas as pd
from dfs import count_islands
import argparse

def main(input_path):
    # reading our data
    test_cases = pd.read_json(input_path)
    
    for test_case in test_cases['test_cases']:
        dim = test_case['input']['dimensions']
        matrix = test_case['input']['matrix']
        ground_truth = test_case['output']

        answer = count_islands(matrix, dim)
        print(f"The answer is {answer}, while ground truth is {ground_truth}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Processing test cases for island counting')
    parser.add_argument('input_path', type=str, help='Path to the input JSON file')
    
    args = parser.parse_args()
    main(args.input_path)