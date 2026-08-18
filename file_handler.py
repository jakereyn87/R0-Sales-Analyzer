"""
file_handler.py

Handles reading sales data from a CSV file
and writing the analysis report to an output file.

Author: Your Name
"""

import csv


def read_csv(filename):
    """
    Reads the CSV file and returns a list of sales records.

    Parameters:
        filename (str): Path to the CSV file.

    Returns:
        list: List of dictionaries containing sales data.
    """

    sales_data = []

    try:
        with open(filename, mode="r", newline="", encoding="utf-8-sig") as csv_file:
            reader = csv.DictReader(csv_file)

            for row in reader:
                sales_data.append({
                    "SaleID": int(row["SaleID"]),
                    "Product": row["Product"],
                    "Category": row["Category"],
                    "Quantity": int(row["Quantity"]),
                    "UnitPrice": float(row["UnitPrice"])
                })

    except FileNotFoundError:
        print(f"Error: '{filename}' not found.")

    except ValueError:
        print("Error: Invalid numeric value found in the CSV file.")

    except KeyError as error:
        print(f"Error: Missing required column {error}")

    except Exception as error:
        print(f"Unexpected Error: {error}")

    return sales_data


def write_report(filename, report_lines):
    """
    Writes the sales report to a text file.

    Parameters:
        filename (str): Output filename.
        report_lines (list): List of report lines.

    Returns:
        None
    """

    try:
        with open(filename, mode="w", encoding="utf-8") as output_file:
            for line in report_lines:
                output_file.write(line + "\n")

    except Exception as error:
        print(f"Error writing report: {error}")