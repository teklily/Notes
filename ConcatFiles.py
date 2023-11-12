import pandas as pd
import os

path = "SplitFiles"
files = os.listdir(path)
files_xlsx = [f for f in files if f[-4:] == 'xlsx']

myconcat_df = pd.DataFrame()

for f in files_xlsx:
    data = pd.read_excel(os.path.join(path,f))
    myconcat_df = pd.concat([myconcat_df, data], ignore_index=True)

myoutput_path = "SplitFiles/Splitfiles.xlsx"
myconcat_df.to_excel(myoutput_path, index=False)

print("The files have been joined into the file SplitFiles.xlsx :)")
