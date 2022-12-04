import os
import requests
from pyairtable import Table
from pyairtable.formulas import match
from datetime import date, datetime
from itertools import islice
from dotenv import load_dotenv

load_dotenv()

AIRTABLE_TOKEN = os.getenv("AIRTABLE_TOKEN")
AIRTABLE_BASE_ID = os.getenv("AIRTABLE_BASE_ID")
AIRTABLE_TABLE_NAME = os.getenv("AIRTABLE_TABLE_NAME")
AIRTABLE_URL = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}"

table = Table(AIRTABLE_TOKEN, AIRTABLE_BASE_ID, AIRTABLE_TABLE_NAME)

"""VARIABLES"""
total_orders = 0
total_monthly_orders = 0
orders_in_progress = 0
orders_revenue = 0
orders_in_progress_lst = []
orders_shipped_lst = []
total_orders_lst = []
recent_orders_lst = []

""" The function returns a list of dictionary containing the following keys 
order_id: int
order_placed: datetime 
product_name: string  
price: float
first_name: string  
last_name: string
address: string
email:string 
"""

# The function converts the table records into a list of dictionaries with appropriate datatype
def filtered_orders_dictionary(table_to_filter):
    filtered_dic = []
    for dic in table_to_filter:
        for dic_key in dic:
            if dic_key == 'fields':
                # print(dic[dic_key])
                filtered_dic.append(dic[dic_key])
                for key in dic[dic_key]:
                    if key == 'order_placed':
                        # print(dic[dic_key])
                        dic[dic_key].update(
                            {'order_placed': datetime.strptime(dic[dic_key].get(key), '%Y-%m-%d').date()})
    return filtered_dic


"""TOTAL ORDERS"""
total_orders_lst = filtered_orders_dictionary(table.all())
total_orders = len(total_orders_lst)
# print(total_orders_lst)
print("Total Orders: ", total_orders)

"""TOTAL MONTHLY ORDERS"""
date_current = date.today()


# function to replace every order date day to 1 to ease off the date comparison
def update_date_day(update_day):
    return update_day.replace(day=1)


def count_current_monthly_orders(lst_dic, current_date):
    count = 0
    for dic in lst_dic:
        for dic_key in dic:
            if dic_key == 'order_placed':
                new_date = update_date_day(dic.get('order_placed'))
                # print(new_date)
                if new_date == current_date:
                    count += 1
    return count


total_monthly_orders = count_current_monthly_orders(total_orders_lst, date_current)
print("Monthly orders:", total_monthly_orders)

"""ORDERS IN PROGRESS """
formula_in_progress = match({"order_status": "in_progress"})
table_orders_in_progress = table.all(formula=formula_in_progress)

# print(formula)
orders_in_progress_lst = filtered_orders_dictionary(table_orders_in_progress)
# print(orders_in_progress_lst)
orders_in_progress = len(orders_in_progress_lst)
print("Orders in progress: ", orders_in_progress)
# print(convert_list_dict(orders_in_progress_lst))

""""ORDERS' REVENUE"""
# Function to calculate the total revenue of the orders
def calculate_orders_revenue(lst_dict):
    revenue = 0
    for dic in lst_dict:
        for dic_key in dic:
            if dic_key == 'price':
                revenue += dic[dic_key]
    return '{0:.2f}'.format(revenue)


formula_shipped = match({"order_status": "shipped"})
table_orders_shipped = table.all(formula=formula_shipped)
orders_shipped_lst = filtered_orders_dictionary(table_orders_shipped)
orders_revenue = calculate_orders_revenue(orders_shipped_lst)
print("Revenue:", orders_revenue)
"""RECENT ORDERS"""


# Function to sort out the recent orders
def sort_orders(lst_dic, key_to_sort):
    return lst_dic.sort(key=lambda x: x[key_to_sort], reverse=True)


sort_orders(total_orders_lst, 'order_placed')

recent_orders_lst = total_orders_lst.copy()


# Displays the first n values
def display_max_records(n, list_dic):
    return list(islice(list_dic, n))


display_recent_orders = display_max_records(5, recent_orders_lst)
print(display_recent_orders)

# def get_orders():
#     """Retrieve orders from airtable."""
#     url = f"{AIRTABLE_URL}/Orders"
#     headers = {
#         'Authorization': f'Bearer {AIRTABLE_TOKEN}',
#         'Content-Type': 'application/json'
#     }
#
#     response = requests.request("GET", url, headers=headers)
#     # print(response.json())
#     return response
#
# get_orders()
