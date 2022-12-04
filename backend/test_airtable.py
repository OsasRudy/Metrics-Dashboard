import unittest
from datetime import date, datetime
import airtable


class EvaluateOrdersFunction(unittest.TestCase):
    def test_format_lst_dic(self):
        unformatted_table = [{'id': 'rec06gvzgqwXmQawF', 'createdTime': '2021-10-06T09:16:38.000Z',
                              'fields': {'order_id': 949, 'order_placed': '2021-06-15',
                                         'product_name': 'mouse earrings', 'price': 143.25,
                                         'first_name': 'Ninnetta', 'last_name': 'Mc Faul',
                                         'address': '1027 Westridge Road',
                                         'email': 'nmcfaulqc@dyndns.org', 'order_status': 'cancelled'}},
                             {'id': 'rec0Az18WIlKvdBrh', 'createdTime': '2021-10-06T09:16:38.000Z',
                              'fields': {'order_id': 881, 'order_placed': '2020-11-19',
                                         'product_name': 'i heart milk brooch',
                                         'price': 73.44, 'first_name': 'Gar', 'last_name': 'Nann',
                                         'address': '2 Hoffman Point',
                                         'email': 'gnannog@1688.com', 'order_status': 'cancelled'}}]

        expected_result = [
            {'order_id': 949, 'order_placed': date(2021, 6, 15), 'product_name': 'mouse earrings', 'price': 143.25,
             'first_name': 'Ninnetta', 'last_name': 'Mc Faul', 'address': '1027 Westridge Road',
             'email': 'nmcfaulqc@dyndns.org', 'order_status': 'cancelled'},
            {'order_id': 881, 'order_placed': date(2020, 11, 19), 'product_name': 'i heart milk brooch',
             'price': 73.44, 'first_name': 'Gar', 'last_name': 'Nann', 'address': '2 Hoffman Point',
             'email': 'gnannog@1688.com', 'order_status': 'cancelled'}]

        result = airtable.filtered_orders_dictionary(unformatted_table)
        self.assertEqual(result, expected_result)

    def test_update_date_day(self):
        result = airtable.update_date_day(date(2022, 5, 10))
        self.assertEqual(result, date(2022, 5, 1))

    def test_count_records(self):
        orders = [{'order_id': 280, 'order_placed': date(2021, 5, 21)},
                  {'order_id': 180, 'order_placed': date(2022, 12, 10)},
                  {'order_id': 180, 'order_placed': date(2022, 12, 30)}]
        result = airtable.count_current_monthly_orders(orders, date(2022, 12, 1))
        self.assertEqual(result, 2)

    def test_revenue(self):
        lst = [
            {'order_id': 726, 'order_placed': date(2021, 10, 5), 'product_name': 'i heart milk brooch', 'price': 181.02,
             'first_name': 'Lindsay', 'last_name': 'Sherrott', 'address': '0 Hovde Junction',
             'email': 'lsherrottk5@cornell.edu', 'order_status': 'placed'},
            {'order_id': 604, 'order_placed': date(2021, 10, 5), 'product_name': 'i heart milk brooch', 'price': 68.83,
             'first_name': 'Janeva', 'last_name': 'Canadine', 'address': '2263 Maple Avenue',
             'email': 'jcanadinegr@sphinn.com', 'order_status': 'in_progress'}]
        result = airtable.calculate_orders_revenue(lst)

        self.assertEqual(result, '249.85')

    def test_display_records(self):
        records = [{'order_id': 280, 'order_placed': date(2021, 5, 21)},
                   {'order_id': 180, 'order_placed': date(2021, 12, 10)},
                   {'order_id': 180, 'order_placed': date(2021, 12, 30)}]

        result = airtable.display_max_records(1, records)
        expected_result = [{'order_id': 280, 'order_placed': date(2021, 5, 21)}]
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
