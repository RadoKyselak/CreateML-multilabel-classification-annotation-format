# CreateML Multi-Label Classification Annotation Format

This script converts a multi-label CSV file with annotations into a JSON file compatible with [Apple's CreateML](https://developer.apple.com/machine-learning/create-ml/). The CSV file must contain image filenames and their corresponding labels. The output JSON file will list the image filenames with their associated labels.

## Requirements

- Python 3.0+
- Standard Python libraries: `csv`, `json`, and `argparse` (all three are included in Python)

## Files

You can specify custom file paths for the input CSV and output JSON files when running the script. Use the following command structure:

```terminal
python formatconvert.py <path_to_csv_file> <path_to_json_file>
```

Default file names:
- `_classes.csv`: The input CSV file containing image filenames and labels.
- `annotations.json`: The output JSON file where the processed data will be saved.

### CSV File Format


The CSV file should be structured as follows:

- The **first row** must contain headers representing labels.

- Each **subsequent row** represents an image and its annotations.

- The **first column** of each row should contain the image filename.

- Each subsequent cell in a row should contain either `1` (if the label applies to the image) or `0` (if the label does not apply)

## Usage

1. **Clone this Repo:**
   If you haven't already cloned the repository, use the following command to download it to your local machine:

   ```terminal
   git clone https://github.com/RadoKyselak/CreateML-multilabel-classification-annotation-format
   ```

2. **Navigate to the Directory:**
   Move into the directory where the script is located:

   ```terminal
   cd CreateML-multilabel-classification-annotation-format
   ```
   
3. **Ensure Python is Installed:**
   Make sure you have Python 3.x installed. Check the version with:

   ```terminal
   python --version
   ```

   or

   ```terminal
   python3 --version
   ```
   
4. **Run the Script:**
   You can now execute the script using Python. If you want to use the default file paths ( CSV file: `./_classes.csv`, JSON file: `./annotations.json`), simply run:

   ```terminal
   python formatconvert.py
   ```

   To use custom file paths, specify them as arguments:

   ```terminal
   python formatconvert.py ./path/to/your/input.csv ./path/to/your/output.json
   ```

6. **Review the Output:**
   After running the script, the output JSON file will be saved in the specified location. You should see a message in the terminal confirming that the JSON data has been saved.

## Script Overview

- **Imports:**
  - `csv`: To read data from the CSV file.
  - `json`: To write data to the JSON file.
  - `argparse`: To handle command-line arguments for easy use.

- **Arguments:**
  - `csv_file`: Path to the input CSV file (default: `./_classes.csv`).
  - `json_file`: Path to the output JSON file (default: `./annotations.json`).

- **Process:**
  1. **Read CSV File:**
     - The script opens the CSV file and reads its content.
     - The first row is treated as headers representing the labels for each column.
     - Each of the rows below represents an image and its annotations.
     - If a cell contains `'1'`, the corresponding label is added to the list of annotations for that image. A `'0'` indicates the label is not part of the image's annotations.

  2. **Write JSON File:**
     - The collected data is converted into JSON format and saved to the specified JSON file.

- **Error Handling:**
  - If the CSV file is not found, a `FileNotFoundError` message is printed.

## Example

### CSV Input:

![image](https://github.com/user-attachments/assets/7ff8d48a-d4cd-41d4-a34c-05c06d04122f)

### JSON Output:

The script will convert the above CSV input into the following JSON format:

```json
[
    {
        "image": "Screen-Shot-2024-png.rf.ms5jw5pllak4k9qa9ajjr556.jpg",
        "annotations": [
            "animal",
            "grass",
            "elephant"
        ]
    },
    {
        "image": "Screen-Shot-2024-png.rf.tz8je3xo05ak2p0a2qwji182.jpg",
        "annotations": [
            "animal",
            "fox"
        ]
    }
]
```

## Troubleshooting

- **File Not Found Error:**
  Ensure that the file paths are correct and that the specified files exist.

- **General Errors:**
  Check that the CSV file is properly formatted and free of unexpected characters or structures.

  The correct format:

  - The first row contains headers.

  - The first column of each row contains the image filename.

  - All subsequent columns contain only `1` or `0`.

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](https://github.com/RadoKyselak/CreateML-multilabel-classification-annotation-format/blob/main/LICENSE) file for details.
