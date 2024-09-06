import unittest
import pandas as pd
import os
from sales_data_analysis import SalesDataAnalysis

class TestSalesDataAnalysis(unittest.TestCase):

    def setUp(self):
        """
        Set up the test case environment before each test method is run.
        """
        file_path = 'd:/EDU/ICT/4th SEM/Python/sales_data.csv'
        self.analysis = SalesDataAnalysis(file_path=file_path)

    def test_monthly_sales_analysis(self):
        result = self.analysis.monthly_sales_analysis()
        self.assertIsInstance(result, pd.DataFrame)

    def test_price_analysis(self):
        result = self.analysis.price_analysis()
        self.assertIsInstance(result, pd.DataFrame)

    def test_weekly_sales_analysis(self):
        result = self.analysis.weekly_sales_analysis()
        self.assertIsInstance(result, pd.DataFrame)

    def test_product_preference_analysis(self):
        result = self.analysis.product_preference_analysis()
        self.assertIsInstance(result, pd.DataFrame)

    def test_sales_distribution_analysis(self):
        result = self.analysis.sales_distribution_analysis()
        self.assertIsInstance(result, pd.DataFrame)

if __name__ == '__main__':
    unittest.main()
