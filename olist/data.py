import os
import pandas as pd
import pandas_profiling

class Olist:
    def get_data(self):
        """
        This function returns a Python dict.
        Its keys should be 'sellers', 'orders', 'order_items' etc...
        Its values should be pandas.DataFrames loaded from csv files
        """
        # Hints: Build csv_path as "absolute path" in order to call this method from anywhere.
        # Do not hardcode your path as it only works on your machine ('Users/username/code...')
        # Use __file__ as absolute path anchor independant of your computer
        # Make extensive use of `import ipdb; ipdb.set_trace()` to investigate what `__file__` variable is really
        # Use os.path library to construct path independent of Unix vs. Windows specificities
        csv_path = os.path.join(
            "/Users/nathan/code/Nath301/data-challenges/04-Decision-Science/data/csv/archive"
        )
        #pd.read_csv(os.path.join(csv_path, 'olist_sellers_dataset.csv')).head()
        file_names = os.listdir(csv_path)
        key_names = [
            str(x).replace("_dataset.csv", "").replace("olist_",
                                                       "").replace(".csv", "")
            for x in file_names
        ]
        data = {
            x: pd.read_csv(os.path.join(csv_path, y))
            for (x, y) in zip(key_names, file_names)
        }
        return data

    def get_matching_table(self):
        """
        This function returns a matching table between
        columns [ "order_id", "review_id", "customer_id", "product_id", "seller_id"]
        """
        data = Olist().get_data()
        datasets_to_profile = [
            'orders', 'products', 'sellers', 'customers', 'order_reviews',
            'order_items'
        ]

        columns_matching_table = [
            "order_id",
            "review_id",
            "customer_id",
            "product_id",
            "seller_id",
        ]
        matching_table = pd.DataFrame()
        matching_table = pd.merge(data['order_items'], data['sellers'], on='seller_id', how='outer' )
        matching_table = pd.merge(matching_table, data['orders'], on='order_id', how='outer')
        matching_table = pd.merge(matching_table, data['customers'], on='customer_id', how='outer')
        matching_table = pd.merge(matching_table, data['order_reviews'], on='order_id', how='outer')
        for x in matching_table.keys():
            if x not in columns_matching_table:
                matching_table.drop(x, axis=1, inplace=True)
        matching_table.drop_duplicates(inplace=True)
        return matching_table

    def ping(self):
        """
        You call ping I print pong.
        """
        print("pong")
