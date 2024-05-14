import unittest
from database.data_loading import connect_to_database, load_data

class TestDataLoading(unittest.TestCase):

    def setUp(self):
        # Initialize test database connection parameters
        self.db_params = {
            'dbname': 'test_youtube_data',
            'user': 'test_user',
            'password': 'test_password',
            'host': 'localhost',
            'port': '5432'
        }
        
        # Create test tables or clear existing tables if needed
        
    def test_connect_to_database(self):
        # Test connection to the database
        connection = connect_to_database(self.db_params)
        self.assertIsNotNone(connection)

    def test_load_data(self):
        # Test loading data into tables
        table_name = 'test_table'
        csv_file = 'test_data.csv'
        load_data(table_name, csv_file, self.db_params)
        
        # Connect to the database to verify data insertion
        connection = connect_to_database(self.db_params)
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute(f'SELECT COUNT(*) FROM {table_name}')
                count = cursor.fetchone()[0]
                # Add more assertions to verify data integrity if needed
                self.assertTrue(count > 0, "No data inserted into the table.")
                print(f"Test load_data passed. {count} rows inserted into '{table_name}'.")
            except Exception as e:
                self.fail(f"Error: {e}")
            finally:
                if connection:
                    connection.close()
        else:
            self.fail("Error: Unable to establish database connection.")

if __name__ == '__main__':
    unittest.main()
