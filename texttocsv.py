import string
from string import digits
import re
def hw_stats (file_name, n):
    with open(file_name) as in_file:
        outputfile = "CS485_Edward3_" + str(n) + ".csv"
        f_out = open(outputfile,"w")
        for line in in_file:
            line = line.strip()
            if (len(line) > 30):
                line = line.translate(str.maketrans('', '', string.punctuation))
                line = line.translate(str.maketrans('', '', digits))
                # line = line.translate(str.maketrans("", "", "False"))
                line = re.sub(r'[A-Z]+(?![a-z])', '', line)
                # label = False
                # line = line[:-1]
                result = "{},".format(line)
                print(result,file=f_out)
        f_out.close()

    
for i in range(1, 16):
    inputfile = str(i) + ".txt"
    hw_stats(inputfile, i)

# import csv
# import random
# import pandas as pd

# df = pd.read_csv('CS485_Shakespeare.csv', header=0)
# ds = df.sample(frac=1)
# ds.to_csv('newfile.csv')