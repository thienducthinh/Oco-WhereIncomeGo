import csv

# Define the path to your CSV file
csv_file = 'uszips.csv'  # Update this with your CSV file's path
insert_template = "INSERT INTO us_zip_codes VALUES (\"{}\", \"{}\", \"{}\", \"{}\", \"{}\", \"{}\");"

# Open the CSV file and process its contents
with open(csv_file, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row if it exists
    for row in reader:
        zip, city, state_id, state_name, county_name, timezone = row
        # Generate the INSERT statement
        insert_statement = insert_template.format(zip, city, state_id, state_name, county_name, timezone)
        with open('insert_statement.sql', 'a') as file: 
                file.write(insert_statement + '\n')