import pandas as pd


excel_file = "HR_Employee_Data.xlsx"
xls = pd.ExcelFile(excel_file)

header = xls.parse(xls.sheet_names[0], header=None).iloc[0]

chunk_size = 1000
start_row = 1  # Skip the header row initially

while True:
    chunk = pd.read_excel(excel_file, header=None, skiprows=start_row, nrows=chunk_size)
    if chunk.empty:
        break

    output_file = f"output_file_{start_row // chunk_size + 1}.xlsx"

    with pd.ExcelWriter(output_file, engine='xlsxwriter') as writer:
        header_df = pd.DataFrame(header)
        header_df.to_excel(writer, sheet_name='Sheet1', index=False, header=False)
        chunk.to_excel(writer, sheet_name='Sheet1', index=False, header=False, startrow=1)
    print(f"{output_file} saved.")
    start_row += chunk_size

print("Done, Son")
