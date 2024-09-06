import pandas as pd

class SalesDataAnalysis:
    def __init__(self, file_path):
        """
        Initialize the SalesDataAnalysis class.

        Parameters:
        file_path (str): Path to the CSV file containing sales data.
        """
        self.data = pd.read_csv(file_path)

    def monthly_sales_analysis(self):
        """
        Perform monthly sales analysis for each branch.

        Returns:
        pandas.DataFrame: Monthly sales data for each branch.
        """
        monthly_sales = self.data.groupby(['Branch ID', 'Date'])['Quantity Sold'].sum().reset_index()
        monthly_sales['Date'] = pd.to_datetime(monthly_sales['Date'], format='%Y-%m-%d')
        monthly_sales['Month'] = monthly_sales['Date'].dt.month
        monthly_sales = monthly_sales.groupby(['Branch ID', 'Month'])['Quantity Sold'].sum().reset_index()
        return monthly_sales

    def price_analysis(self):
        """
        Perform price analysis for each product.

        Returns:
        pandas.DataFrame: Price data for each product.
        """
        price_data = self.data.groupby('Product ID')['Price'].mean().reset_index()
        return price_data

    def weekly_sales_analysis(self):
        """
        Perform weekly sales analysis for the supermarket network.

        Returns:
        pandas.DataFrame: Weekly sales data for the supermarket network.
        """
        weekly_sales = self.data.groupby('Date')['Quantity Sold'].sum().reset_index()
        weekly_sales['Date'] = pd.to_datetime(weekly_sales['Date'], format='%Y-%m-%d', errors='coerce')
        weekly_sales['Week'] = weekly_sales['Date'].dt.isocalendar().week
        weekly_sales = weekly_sales.groupby('Week')['Quantity Sold'].sum().reset_index()
        return weekly_sales

    def product_preference_analysis(self):
        """
        Perform product preference analysis.

        Returns:
        pandas.DataFrame: Product preference data.
        """
        product_preference = self.data.groupby('Product ID')['Quantity Sold'].sum().reset_index()
        product_preference = product_preference.sort_values('Quantity Sold', ascending=False)
        return product_preference

    def sales_distribution_analysis(self):
        """
        Perform analysis of the distribution of total sales amount of purchases.

        Returns:
        pandas.DataFrame: Distribution of total sales amount of purchases.
        """
        sales_distribution = self.data['Quantity Sold'].value_counts().reset_index()
        sales_distribution.columns = ['Quantity Sold', 'Frequency']
        return sales_distribution

def main():
    file_path = 'D:\\EDU\\ICT\\4th SEM\\Python\\sales_data.csv'
    analysis = SalesDataAnalysis(file_path)

    while True:
        print("\nSales Data Analysis Menu:")
        print("1. Monthly Sales Analysis")
        print("2. Price Analysis")
        print("3. Weekly Sales Analysis")
        print("4. Product Preference Analysis")
        print("5. Sales Distribution Analysis")
        print("6. Quit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            print("\nMonthly Sales Analysis:")
            print(analysis.monthly_sales_analysis())
        elif choice == "2":
            print("\nPrice Analysis:")
            print(analysis.price_analysis())
        elif choice == "3":
            print("\nWeekly Sales Analysis:")
            print(analysis.weekly_sales_analysis())
        elif choice == "4":
            print("\nProduct Preference Analysis:")
            print(analysis.product_preference_analysis())
        elif choice == "5":
            print("\nSales Distribution Analysis:")
            print(analysis.sales_distribution_analysis())
        elif choice == "6":
            print("\nGoodbye!see you again")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == '__main__':
    main()

