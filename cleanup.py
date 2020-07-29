# Imports
import pandas as pd
import numpy as np

# CMD input for filename/filepath
user_input = input("Enter file name for cleanup. Dont forget to add '.csv' to the filename: \n")

# Function to remove duplicate names in Names column
def unique_names(name):
    if name == '' or name == ' ':
        pass
    else:
        name_list = list(np.unique(name.split(' ')))
        return name_list

# Master function to read in csv file and group by based on ID. Duplicate values are combined in same cell.
def master_function(file_path):
    df = pd.read_csv(file_path)

    df = df.fillna('')
    # Group by ID and aggregate all other values with commas.
    df = df.groupby(['ID'], as_index = False).agg({'Names': ' '.join,
                                                    'Values': ', '.join,
                                                    'Unique Stuff': ', '.join})

    # Apply unique names function to Names column
    df.Names = df.Names.apply(unique_names)

    # Save to csv called output.csv
    df.to_csv('output.csv', index = False)
    return df

# Run master function on userinput csv file
master_function(user_input)
print("... \nCompleted! \nFile saved to 'output.csv'")
