import csv
import json
import argparse

parser = argparse.ArgumentParser(description='Convert a CSV file to JSON format for CreateML image classification.')
parser.add_argument('csv_file', nargs='?', default='./_classes.csv', help='Path to the input CSV file (default: ./_classes.csv)')
parser.add_argument('json_file', nargs='?', default='./annotations.json', help='Path to the output JSON file (default: ./annotations.json)')
args = parser.parse_args()

# Paths to CSV and JSON files
csv_file = args.csv_file
json_file = args.json_file

data = []

try:
    with open(csv_file, newline='') as file:
        reader = csv.reader(file)
        
        headers = [header.strip() for header in next(reader)]
        
        for row in reader:
            if row:
                image_file = row[0].strip()
                
                annotations = []
                for i in range(1, len(row)):
                    if row[i].strip() == '1':
                        annotations.append(headers[i])
                
                if annotations:
                    data.append({
                        "image": image_file,
                        "annotations": annotations
                    })

    with open(json_file, 'w') as json_out:
        json.dump(data, json_out, indent=4)

    print(f'JSON data has been saved to {json_file}')

except FileNotFoundError:
    print(f"The file {csv_file} was not found.")
