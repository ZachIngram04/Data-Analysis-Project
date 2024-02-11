import args
import pandas as pd
import data_handler

if __name__ == "__main__": 
    arguments = args.parse_args()
    hanlded_data = data_handler.load_file(arguments.input_data)
    print(hanlded_data)