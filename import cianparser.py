import cianparser
import pandas as pd

moscow_parser = cianparser.CianParser(location=("Руза"))
data = moscow_parser.get_flats(deal_type="sale", rooms=("all"), with_saving_csv=True, additional_settings={"start_page":1, "end_page":1000})

print(data[0])
file_list = ["zxcqwe.csv","qwezxc.csv"]

combined_df = pd.DataFrame()

for file in file_list:
   
    df = pd.read_csv(file,on_bad_lines='skip')
   
    combined_df = pd.concat([combined_df, df], ignore_index=True)
combined_df.to_csv('combined_file.csv', index=False)

