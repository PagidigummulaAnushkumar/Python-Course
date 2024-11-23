# [import any other necessary module(s)]
import sqlite3
from pathlib import Path
from datetime import date
from typing import Optional, List, Any

from p01sc06_OOPDBGUI3tier.p01beg_1da_sales import Sales, Regions


# -------------- Data Access (SQLite) --------------------------
class SQLiteDBAccess:
    SQLITEDBPATH = Path(__file__).parent.parent / 'p01_db'

    def __init__(self):
        self._sqlite_sales_db = 'sales_db.sqlite'
        self._dbpath_sqlite_sales_db = SQLiteDBAccess.SQLITEDBPATH / self._sqlite_sales_db

    def connect(self) -> sqlite3.Connection:
        '''Connect to the SQLite database and return the connection object.'''

        try:
            conn = sqlite3.connect(self._dbpath_sqlite_sales_db)
            print(f"Connected to SQLite database at {self._dbpath_sqlite_sales_db}")
            return conn
        except sqlite3.Error as e:
            print(f"Error connecting to SQLite database: {e}")
            return None

    def retrieve_sales_by_date_region(self, sales_date: date, region_code: str) -> Optional[Sales]:
        '''retrieve ID, amount, salesDate, adn region field from Sales table for the records that have the given salesDate and region values.'''
        connection = self.connect()
        if not connection:
            return None

        cursor = connection.cursor()
        query = '''SELECT id, amount, sales_date, region FROM Sales WHERE sales_date = ? AND region = ?'''
        cursor.execute(query, (sales_date, region_code))

        result = cursor.fetchone()  # Fetch the first matching record
        connection.close()

        if result:
            return Sales(id=result[0], amount=result[1], sales_date=result[2], region=result[3])
        else:
            print("No sales found for the given date and region.")
            return None


    def update_sales(self, sales: Sales) -> None:
        '''update amount, salesDate, and region fields of Sales table for the record with the given ID value. '''
        connection = self.connect()
        if not connection:
            return None

        cursor = connection.cursor()
        query = '''UPDATE Sales SET amount = ?, sales_date = ?, region = ? WHERE id = ?'''
        cursor.execute(query, (sales.amount, sales.sales_date, sales.region, sales.id))

        connection.commit()
        connection.close()
        print(f"Sales record with ID {sales.id} updated successfully.")

    def retrieve_regions(self) -> list[Any] | list[Regions]:
        '''retreive region code and name from Region table'''
        connection = self.connect()
        if not connection:
            return []

        cursor = connection.cursor()
        query = '''SELECT region_code, region_name FROM Regions'''
        cursor.execute(query)

        result = cursor.fetchall()
        connection.close()

        # Return a list of Regions objects
        return [Regions(region_code=row[0], region_name=row[1]) for row in result]