import pandas as pd
import sys

if __name__ == "__main__":
    contents = pd.read_csv(sys.argv[1])
    print(contents[0:5])