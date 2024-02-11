import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        prog = "ZAP",
        description = "Program to do certain functions on data" #Make this more descriptive
    )

    parser.add_argument('--input_data', type=str, required=True,
                        help="Exported text data from CHI Butler")
    
    args = parser.parse_args()

    return args