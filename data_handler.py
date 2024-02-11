import pandas as pd
import argparse

"""
This script contains the functions for loading and processing the input data into a pandas dataframe.
"""

def load_file(filename) -> pd.DataFrame:
    """
    filename: path of desired .txt file for loading
    """
    processed_data = {"Potential/V": [],
                      "Current/A": []
                      }
    print("loading file...")
    try:
        with open(filename) as file:
            lines = file.readlines()
        found_header = False
        for i, line in enumerate(lines):
            print(f"data: {i}, {found_header}, {line}")
            if found_header == False:
                if line == "Potential/V, Current/A\n":
                    found_header = True
                    print("header found!")
                    continue
                else:
                    continue
            else: #if header has already been found
                if line != "\n":
                    extracted_data = line.split(",")
                    processed_data['Potential/V'].append(float(extracted_data[0]))
                    processed_data['Current/A'].append(float(extracted_data[1])) 
    except:
        "Error loading/parsing file. Quitting."
        quit()
    return(pd.DataFrame.from_dict(processed_data))
    