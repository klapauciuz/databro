import csv
import pandas as pd
import fasttext
import re


# File paths
v = 0
input_csv = "input_v{}.csv".format(v)
output_csv = "output__v{}.csv".format(v + 1)
filter_file = "keywords.txt"
notfilter_file = "keywords_blacklist.txt"
bl = "usernames_blacklist.txt"

# ## by keywords and nonkeywords

# with open(filter_file, "r", encoding="utf-8") as f:
#     filter_words = {line.strip().lower() for line in f if line.strip()}
# with open(notfilter_file, "r", encoding="utf-8") as f:
#     blacklist_words = {line.strip().lower() for line in f if line.strip()}

# # Open files and stream through CSV
# with open(input_csv, newline="", encoding="utf-8") as csvfile, open(output_csv, "w", newline="", encoding="utf-8") as outfile:
#     reader = csv.reader(csvfile)
#     writer = csv.writer(outfile)

#     # # # Write header
#     # # header = next(reader)
#     # # writer.writerow(header)

#     # keywords
#     for row in reader:
#         # Convert entire row to a single lowercase string to check for any filter word
#         row_text = " ".join(map(str, row)).lower()

#         # Check if any filter word is present
#         if any(word in row_text for word in filter_words) and not any(word in row_text for word in blacklist_words):
#             print(f'found word here - {row_text}')
#             writer.writerow(row)




# ## blacklist

# with open(bl, "r", encoding="utf-8") as f:
#     exclude_lines = [line.strip().lower() for line in f]


# # Process the CSV
# with open(input_csv, "r", encoding="utf-8", newline='') as infile, \
#      open(output_csv, "w", encoding="utf-8", newline='') as outfile:

#     reader = csv.reader(infile)
#     writer = csv.writer(outfile)

#     for row in reader:
#         if len(row) < 2:
#             continue  # skip if row doesn't have at least 2 columns

#         col_text = row[1].strip().lower()
#         if col_text == '' or col_text == ' ':
#             continue
#         if col_text not in exclude_lines:
#             writer.writerow(row)
#         else:
#             print(f'found blacklisted word - {col_text}')



# ## language

# # Load FastText model (only once)
# model = fasttext.load_model("lid.176.bin")

# def clean_text(text):
#     # Optional: remove control chars, leave emojis etc.
#     return str(text).replace('\n', ' ').strip()

# def is_english_fasttext(text):
#     text = clean_text(text)
#     if not text:
#         return False
#     pred = model.predict(text)[0][0]  # e.g., '__label__en'
#     return pred == '__label__en'

# def filter_english_rows(input_csv, output_csv, column_index=10):
#     df = pd.read_csv(input_csv)

#     if column_index >= df.shape[1]:
#         raise IndexError(f"Column index {column_index} is out of range.")

#     df_filtered = df[df.iloc[:, column_index].astype(str).apply(is_english_fasttext)]

#     df_filtered.to_csv(output_csv, index=False)
#     print(f"Saved {len(df_filtered)} English rows to {output_csv}")

# # Run it
# filter_english_rows(input_csv, output_csv, column_index=10)



# #######
# def drop_duplicates_first_column(input_csv, output_csv):
#     df = pd.read_csv(input_csv)

#     # Drop duplicates based on first column (index 0), keeping the first
#     df_cleaned = df.drop_duplicates(subset=df.columns[0], keep='first')

#     df_cleaned.to_csv(output_csv, index=False)
#     print(f"Saved {len(df_cleaned)} rows after removing duplicates in column 0 to {output_csv}")

# # Example usage:
# drop_duplicates_first_column(input_csv, output_csv)


# ## merge
# # Load both CSVs
# df_a = pd.read_csv('file_to_merge_0.csv')  # Original file
# df_b = pd.read_csv('file_to_merge_1.csv')  # File with the extra column

# # Merge on the first column (assumed to be the same)
# df_merged = pd.merge(df_a, df_b, on=df_a.columns[0])

# # Save the result
# df_merged.to_csv('merged.csv', index=False)

# print("Merged file saved as merged.csv")
