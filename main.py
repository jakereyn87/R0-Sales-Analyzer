"""
main.py

Sales Data Processing Program

This program:
1. Accepts an input CSV file from the command line.
2. Validates the file.
3. Reads sales data.
4. Performs calculations.
5. Writes the results to an output file.

Author: Your Name
"""

import sys

from file_handler import read_csv, write_report
from validator import validate_file
from calculations import (
    calculate_total_sales,
    calculate_average_sale,
    calculate_highest_sale,
    calculate_lowest_sale,
    calculate_total_quantity,
    calculate_category_sales,
    best_selling_product,
)


def main():
    """Main function that controls the program."""

    # Check command-line arguments
    if len(sys.argv) != 2:
        print("Usage: python main.py input.csv")
        return

    input_file = sys.argv[1]

    # Validate input file
    if not validate_file(input_file):
        return

    # Read data
    sales_data = read_csv(input_file)

    if not sales_data:
        print("No data found in the file.")
        return

    # Perform calculations
    total_sales = calculate_total_sales(sales_data)
    average_sale = calculate_average_sale(sales_data)
    highest_sale = calculate_highest_sale(sales_data)
    lowest_sale = calculate_lowest_sale(sales_data)
    total_quantity = calculate_total_quantity(sales_data)
    category_sales = calculate_category_sales(sales_data)
    top_product = best_selling_product(sales_data)

    # Create report
    report = []
    report.append("=" * 50)
    report.append("SALES ANALYSIS REPORT")
    report.append("=" * 50)
    report.append(f"Total Transactions : {len(sales_data)}")
    report.append(f"Total Quantity Sold : {total_quantity}")
    report.append(f"Total Revenue : ${total_sales:.2f}")
    report.append(f"Average Sale : ${average_sale:.2f}")
    report.append(f"Highest Sale : ${highest_sale:.2f}")
    report.append(f"Lowest Sale : ${lowest_sale:.2f}")
    report.append("")
    report.append(f"Best Selling Product : {top_product}")
    report.append("")
    report.append("Revenue by Category")
    report.append("-" * 25)

    for category, revenue in category_sales.items():
        report.append(f"{category}: ${revenue:.2f}")

    report.append("=" * 50)

    # Display report
    for line in report:
        print(line)

    # Save report
    write_report("output.txt", report)

    print("\nAnalysis completed successfully.")
    print("Results saved to output.txt")


if __name__ == "__main__":
    main()