import pandas as pd

test_df = pd.read_excel("test.xlsx", sheet_name=0, skiprows=None)


# Split the long date column into two separate columns - date and time

test_df["Date_clear"], test_df["Time_clear"] = test_df["Submitted date"].str.split(" ").str

test_df.to_excel("test_ready.xlsx", index=False)










# import pandas as pd
# import numpy as np
#
# all_fifths = pd.DataFrame()
#
# all_emails = pd.read_excel("test4.xlsx", sheet_name=0, skiprows=None)
#
# unique_emails = pd.read_excel("test4.xlsx", sheet_name=0, skiprows=None)
#
# unique_emails.drop_duplicates(["Emails"], keep="first", inplace=True)
#
# for email in unique_emails["Emails"]:
#     all_selected = all_emails[all_emails["Emails"] == email]
#     all_selected.index = np.arange(1, len(all_selected) + 1)
#     each_fifth = all_selected[(all_selected.index % 5 == 0)]
#     all_fifths = all_fifths.append(each_fifth)
#
# #all_fifths = all_fifths.sample(n=10)
#
# #print("Winners:")
# print(all_fifths)