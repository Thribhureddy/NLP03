import re

sample_text = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
The meeting is scheduled for 2024-03-21. Please arrive on time.
"""

pattern = r'\b\d{4}-\d{2}-\d{2}\b'  # Regular expression pattern to match dates in YYYY-MM-DD format

dates = re.findall(pattern, sample_text)

print("Extracted dates:")
for date in dates:
    print(date)

print("\nValidation:")
for date in dates:
    if re.fullmatch(pattern, date):
        print(f"{date}: Valid")
    else:
        print(f"{date}: Invalid")
