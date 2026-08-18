"""
validator.py

Validates the input CSV file before processing.

Checks:
1. File exists
2. File is a CSV
3. File is not empty
4. Required columns exist
5. Numeric values are valid

Author: Jake Reynolds
"""

import os
import csv


# Required columns in the CSV file
REQUIRED_COLUMNS = [
    "SaleID",
    "Product",
    "Category",
    "Quantity",
    "UnitPrice"
]


def validate_file(filename):
    """
    Validates the input CSV file.

    Parameters:
        filename (str): Path to the CSV file.

    Returns:
        bool: True if valid, False otherwise.
    """

    # Check if file exists
    if not os.path.exists(filename):
        print(f"Error: '{filename}' does not exist.")
        return False

    # Check file extension
    if not filename.lower().endswith(".csv"):
        print("Error: Input file must be a CSV file.")
        return False

    # Check file is not empty
    if os.path.getsize(filename) == 0:
        print("Error: The CSV file is empty.")
        return False

    try:
        with open(filename, mode="r", newline="", encoding="utf-8-sig") as csv_file:

            reader = csv.DictReader(csv_file)

            # Check required columns
            if reader.fieldnames is None:
                print("Error: CSV file has no header.")
                return False

            for column in REQUIRED_COLUMNS:
                if column not in reader.fieldnames:
                    print(f"Error: Missing required column '{column}'.")
                    return False

            # Check every row
            for row_number, row in enumerate(reader, start=2):

                # Empty field check
                for column in REQUIRED_COLUMNS:
                    if row[column].strip() == "":
                        print(f"Error: Empty value in '{column}' at row {row_number}.")
                        return False

                # Numeric validation
                try:
                    int(row["SaleID"])
                except ValueError:
                    print(f"Error: Invalid SaleID at row {row_number}.")
                    return False

                try:
                    quantity = int(row["Quantity"])

                    if quantity < 0:
                        print(f"Error: Quantity cannot be negative (row {row_number}).")
                        return False

                except ValueError:
                    print(f"Error: Invalid Quantity at row {row_number}.")
                    return False

                try:
                    price = float(row["UnitPrice"])

                    if price < 0:
                        print(f"Error: UnitPrice cannot be negative (row {row_number}).")
                        return False

                except ValueError:
                    print(f"Error: Invalid UnitPrice at row {row_number}.")
                    return False

    except Exception as error:
        print(f"Validation Error: {error}")
        return False

    print("Input file validation successful.")

    return True
