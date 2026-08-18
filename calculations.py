"""
calculations.py

Contains all functions used to perform
sales calculations.

Author: Your Name
"""


def calculate_total_sales(sales_data):
    """
    Calculates the total revenue.

    Returns:
        float
    """

    total = 0

    for sale in sales_data:
        total += sale["Quantity"] * sale["UnitPrice"]

    return total


def calculate_average_sale(sales_data):
    """
    Calculates the average sale value.

    Returns:
        float
    """

    if len(sales_data) == 0:
        return 0

    total = calculate_total_sales(sales_data)

    return total / len(sales_data)


def calculate_highest_sale(sales_data):
    """
    Finds the highest sale value.

    Returns:
        float
    """

    if len(sales_data) == 0:
        return 0

    highest = 0

    for sale in sales_data:
        value = sale["Quantity"] * sale["UnitPrice"]

        if value > highest:
            highest = value

    return highest


def calculate_lowest_sale(sales_data):
    """
    Finds the lowest sale value.

    Returns:
        float
    """

    if len(sales_data) == 0:
        return 0

    lowest = sales_data[0]["Quantity"] * sales_data[0]["UnitPrice"]

    for sale in sales_data:
        value = sale["Quantity"] * sale["UnitPrice"]

        if value < lowest:
            lowest = value

    return lowest


def calculate_total_quantity(sales_data):
    """
    Calculates total quantity sold.

    Returns:
        int
    """

    total_quantity = 0

    for sale in sales_data:
        total_quantity += sale["Quantity"]

    return total_quantity


def calculate_category_sales(sales_data):
    """
    Calculates total revenue for each category.

    Returns:
        dict
    """

    category_totals = {}

    for sale in sales_data:

        category = sale["Category"]

        revenue = sale["Quantity"] * sale["UnitPrice"]

        if category not in category_totals:
            category_totals[category] = 0

        category_totals[category] += revenue

    return category_totals


def best_selling_product(sales_data):
    """
    Finds the product with the highest quantity sold.

    Returns:
        str
    """

    product_totals = {}

    for sale in sales_data:

        product = sale["Product"]

        quantity = sale["Quantity"]

        if product not in product_totals:
            product_totals[product] = 0

        product_totals[product] += quantity

    best_product = ""
    highest_quantity = 0

    for product, quantity in product_totals.items():

        if quantity > highest_quantity:
            highest_quantity = quantity
            best_product = product

    return best_product