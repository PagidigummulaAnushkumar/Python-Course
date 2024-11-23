# [import p01_1da_sales and use alias sd]

import csv
# [import class Decimal and constant ROUND_HALF_UP from decimal library]
import locale as lc
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

from p01sc01_control_structures.p01m_sales_input import sales_date, sales_list
from p01sc02_function_files.p01beg_m_sales_g17 import view_sales, import_all_sales, add_sales1, add_sales2, \
    save_all_sales
from p01sc04_exception_libraries_3tier.p01beg_1da_sales import import_sales as sd, import_sales

import p01sc04_exception_libraries_3tier.p01beg_1da_sales as sd
from p01sc06_OOPDBGUI3tier.p01beg_1da_sales import DataFileAccess

lc.setlocale(lc.LC_ALL, "en_US")
111
FILEPATH = Path(__file__).parent.parent / 'p01_files'
ALL_SALES = "all_sales.csv"


class SalesManager:
    def __init__(self, filepath=None):
        self._datafileaccess = None
        self._sales_list = self._datafileaccess.import_all_sales()
        self._datafileaccess = DataFileAccess(filepath)
        self.sales_list = self._datafileaccess.import_sales()


def import_all_sales(self) -> list:
        """Import all sales from the CSV file."""
        sales_list = []
        try:
            with open(FILEPATH / ALL_SALES, newline='') as csvfile:
                reader = csv.reader(csvfile)
                for line in reader:
                    if len(line) == 3:  # Adjust based on your CSV structure
                        amount, sales_date, region = line
                        sales_list.append({
                            "amount": Decimal(amount),
                            "sales_date": sales_date,
                            "region": region
                        })
            return sales_list
        except FileNotFoundError:
            print("Sales file not found. Starting with an empty sales list.")
            return []
        except Exception as e:
            print(f"An error occurred while importing sales: {e}")
        return []

    # def view_sales(self) -> None:
    #
    #     """Display all sales data."""
    #     if not self._sales_list:
    #         print("No sales records available.")
    #         return
    #         print(f"{'Amount':<15}{'Sales Date':<15}{'Region'}")
    #         print("-" * 40)
    #     for sale in self._sales_list:
    #         # print(f"{sale['amount']:<15}{sale['sales_date']:<15}{sale['region']}")
    #         print(f"{sale['amount']:<15}{sale['sales_date']:<15}{sale['region']}")
    #         print("-" * 40)


def view_sales(self) -> None:
    """Display all sales data."""
    if not sales_list:
        print("No sales records available.")
        return

    print(f"{'Amount':<15}{'Sales Date':<15}{'Region'}")
    print("-" * 40)

    for sale in sales_list:
        print(f"{sale['amount']:<15}{sale['sales_date']:<15}{sale['region']}")
        print("-" * 40)

    def add_sales1(self) -> None:
        """Add sales data manually by typing amount, year, month, day, and region."""
        amount = input("Enter sales amount: ")
        sales_date = input("Enter sales date (YYYY-MM-DD): ")
        region = input("Enter region code: ")

        # Append the new sales entry to the sales list
        self._sales_list.append({
            "amount": Decimal(amount),
            "sales_date": sales_date,
            "region": region
        })
        print(f"Sales for {sales_date} added.")

    def add_sales2(self) -> None:
        """Add sales data by typing sales amount, date (YYYY-MM-DD), and region."""
        amount = input("Enter sales amount: ")
        sales_date = input("Enter sales date (YYYY-MM-DD): ")
        region = input("Enter region code: ")

        # Append the new sales entry to the sales list
        self._sales_list.append({
            "amount": Decimal(amount),
            "sales_date": sales_date,
            "region": region
        })
        print(f"Sales for {sales_date} added.")

    def import_sales(self) -> None:
        """Import sales from a file (implementation details may vary)."""
        filename = input("Enter the file name to import sales from: ")
        # Implement the logic to import from a specified file

    # [Add code to handle exception FileNotFoundError by displaying "Sales file not found"]
    def import_all_sales(self) -> list:
        sales_list = []
        try:
            with (open(sd.FILEPATH / sd.ALL_SALES, newline='') as csvfile):
                reader = csv.reader(csvfile)
                sales_list = []
                for line in reader:
                    if len(line) == 3:
                        amount, sales_date, region = line
                        sales_list.append({
                            "amount": Decimal(amount),
                            "sales_date": sales_date,
                            "region": region
                        })
                # *amount_sales_date, region_code = line
                # sd.correct_data_types(amount_sales_date)
                # amount, sales_date = amount_sales_date[0], amount_sales_date[1]
                # data = {"amount": amount,
                #         "sales_date": sales_date,
                #         "region": region_code,
                #         }
                # sales_list.append(data)
                return sales_list  # within with statement
        # except FileNotFoundError:
        #     print("Sales file not found.")
        #     return []
        except FileNotFoundError:
            print("Sales file not found. Starting with an empty sales list.")
            return []
        except Exception as e:
            print(f"An error occurred while importing sales: {e}")
            return []


# [Modify the code to use Decimal of decimal library and currency function of the locale library ]
    def view_sales(sales_list: list, self:None) -> bool:
        bad_data_flag = False

        if not sales_list:  # check if the list is empty or None
            print("No sales to view.\n")
            return bad_data_flag  # Early return if no sales to view

        # if len(self.sales_list) == 0:  # sales_list could be [] or None
        #     print("No sales to view.\n")

        # else:  # not empty

            col1_w, col2_w, col3_w, col4_w, col5_w = 5, 15, 15, 15, 15
            total_w = col1_w + col2_w + col3_w + col4_w + col5_w

            print(f"{' ':{col1_w}}"
                  f"{'Date':{col2_w}}"
                  f"{'Quarter':{col3_w}}"
                  f"{'Region':{col4_w}}"
                  f"{'Amount':>{col5_w}}")
            # print(horizontal_line := f"{'-' * total_w}")
            print("-" * total_w)
            total = 0.0

            # for idx, sales in enumerate(sales_list, start=1):
            #     if sd.has_bad_data(sales):
            #         bad_data_flag = True
            #         num = f"{idx}.*"  # add period and asterisk
            #     else:
            #         num = f"{idx}."  # add period only

            for idx, sales in enumerate(sales_list, start=1):
                # Check for bad data in each sale
                if has_bad_data(sales):  # Assuming `has_bad_data` is a valid function
                    bad_data_flag = True
                    num = f"{idx}.*"  # Indicate bad data
                else:
                    num = f"{idx}."  # Normal entry

                amount = Decimal(sales["amount"]).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
                # if not sd.has_bad_amount(sales):
                #     total += amount

                if not has_bad_amount(sales):  # Assuming `has_bad_amount` is a valid function
                    total += amount

                sales_date = sales["sales_date"]

                # if sd.has_bad_date(sales):
                #     bad_data_flag = True
                #     month = 0

                if has_bad_date(sales):  # Assuming `has_bad_date` is a valid function
                    bad_data_flag = True
                    month = 0  # Placeholder for invalid date
                else:
                    month = int(sales_date.split("-")[1])

                region = sd.get_region_name(sales["region"])
                # quarter = f"{sd.cal_quarter(month)}"

                quarter = cal_quarter(month)
                print(f"{num:<{col1_w}}"
                      f"{sales_date:{col2_w}}"
                      f"{quarter:<{col3_w}}"
                      f"{region:{col4_w}}"
                      f"{amount:>{col5_w}}")

            print(horizontal_line)
            print(f"{'TOTAL':{col1_w}}"
                  f"{' ':{col2_w + col3_w + col4_w}}"
                  f"{total:>{col5_w}}\n")
            return bad_data_flag


    def add_sales1(sales_list) -> None:
        sales_list.append(data := sd.from_input1())
        print(f"Sales for {data["sales_date"]} is added.\n")


    def add_sales2(sales_list) -> None:
        sales_list.append(data := sd.from_input2())
        print(f"Sales for {data["sales_date"]} is added.\n")


    # [Modify the code accordingly to use objects from other module]
    # def import_sales(sales_list) -> None:
    #     # get filename from user
    #     filename = input("Enter name of file to import: ")
    #     filepath_name = sd.FILEPATH / filename
    #     # check if filename is valid
    #     if not sd.is_valid_filename_format(filename):
    #         print(f"Filename '{filename}' doesn't follow the expected",
    #               f"format of '{sd.NAMING_CONVENTION}'.")
    #     # check if region code (the 5th character from end) is valid.
    #     elif not sd.is_valid_region(sd.get_region_code(filename)):
    #         print(f"Filename '{filename}' doesn't include one of",
    #               f"the following region codes: {list(sd.VALID_REGIONS.keys())}.")
    #     # check if file has already been imported
    #     elif sd.already_imported(filepath_name):
    #         filename = filename.replace("\n", "")  # remove new line character
    #         print(f"File '{filename}' has already been imported.")
    #     elif:
    #         #import sales data from file
    #        try:
    #             imported_sales_list = import_sales(filepath_name)  # function in the imported module
    #         except Exception as e:
    #             print(f"{type(e)}. Fail to import sales from '{filename}'.")
    #     else:
    #     # display imported sales
    #         bad_data_flag = view_sales(imported_sales_list)
    #
    #     if bad_data_flag:
    #         print(f"File '{filename}' contains bad data.\n"
    #                       "Please correct the data in the file and try again.")
    #     elif len(imported_sales_list) > 0:
    #         (sales_list.extend(imported_sales_list))
    #     print("Imported sales added to list.")
    #     sd.add_imported_file(filepath_name)

    def save_all_sales(sales_list: list, delimiter: str = ',') -> None:
        # convert the list of Sales to a list of lists of sales data (amount, sales_date, region.code), using comprehension
        sales_records = [[sales["amount"], f"{sales["sales_date"]:{sd.DATE_FORMAT}}", sales["region"]]
                         for sales in sales_list]
        try:
            with open(sd.FILEPATH / sd.ALL_SALES, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=delimiter)

                ''' The following additional code is only for practicing raising 
                exception for testing purpose, and will be commented out for 
                testing whether the function can save data successfully.
                You will write code to do the following:
                - Write a try clause in which raise an OSError.
                - Reraise the OSError in the except clause that handles the OSError exception.
                - Write code to make sure the csvfile is closed no matter an exception occurs or not.
                - Optionally, you may also add code to roll back the change to the imported_files]
                '''
                ...

            try:
                raise OSError("Simulated OSError for testing.")
                writer.writerows(sales_records)
                print("Saved sales records.")
            except OSError as e:
                print("Caught OSError:", e)
                raise
            finally:
                print("csvfile is closed automatically by the 'with' statement.")
        except Exception as e:
            print(type(e), "Sales data could not be saved.")

    # [Modify the code to raise and handle exception(s)]
    def main(self):
        '''
        Write code to test the functions in this module
        '''
        ...

        # Initialize an empty sales list to work with
        sales_list = []

        # Test importing sales data from a file (simulated)
        print("Testing import_all_sales() function:")
        try:
            sales_list = import_all_sales()
            print(f"Imported {len(sales_list)} sales records.\n")
        except FileNotFoundError:
            print("Sales file not found.\n")

        # Test viewing sales (including potential bad data)
        print("Testing view_sales() function:")
        bad_data_flag = view_sales(sales_list)
        if bad_data_flag:
            print("Some sales records contain bad data.\n")

        # Test adding sales manually (simulate user input)
        print("Testing add_sales1() function (manual sales entry):")
        add_sales1(sales_list)

        print("Testing add_sales2() function (manual sales entry):")
        add_sales2(sales_list)

        # View the updated sales list
        print("Sales list after adding new records:")
        view_sales(sales_list)

        # Test saving all sales to a file (with exception handling)
        print("Testing save_all_sales() function:")
        try:
            save_all_sales(sales_list)
        except OSError as e:
            print(f"Error during saving: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

        print("\nTests completed.")

    def import_sales(sales_list) -> None:
        # get filename from user
        filename = input("Enter name of file to import: ")
        filepath_name = Path(sd.FILEPATH) / filename

        filepath_name = filepath_name.resolve()

        if not filepath_name.exists():
            print(f"Error: The file {filepath_name} does not exist. Please check the file path and try again.")
            return

        # check if filename is valid
        if not sd.is_valid_filename_format(filename):
            print(f"Filename '{filename}' doesn't follow the expected format of '{sd.NAMING_CONVENTION}'.")
            return  # Exit early if the filename is invalid

        # check if region code (the 5th character from end) is valid
        region_code = sd.get_region_code(filename)
        if not sd.is_valid_region(region_code):
            print(
                f"Filename '{filename}' doesn't include one of the following region codes: {list(sd.VALID_REGIONS.keys())}.")
            return  # Exit early if the region code is invalid

        # check if file has already been imported
        if sd.already_imported(filepath_name):
            filename = filename.replace("\n", "")  # remove newline character
            print(f"File '{filename}' has already been imported.")
            return  # Exit early if the file was already imported

        # Now try importing sales data from file
        try:
            imported_sales_list = sales_list.read_sales_from_file(
                filepath_name)  # You should have a function to read data from the file
        except Exception as e:
            print(f"{type(e).__name__}: Failed to import sales from '{filename}'.")
            return  # Exit early if there's an error during file import

        # Now display imported sales
        bad_data_flag = view_sales(imported_sales_list)

        if bad_data_flag:
            print(f"File '{filename}' contains bad data.\nPlease correct the data in the file and try again.")
            return  # Exit early if bad data is found
        elif len(imported_sales_list) > 0:
            sales_list.extend(imported_sales_list)
            print("Imported sales added to list.")
        else:
            print(f"No sales data found in '{filename}'.")

        # Mark the file as imported
        sd.add_imported_file(filepath_name)


    if __name__ == "__main__":
        main()


    def read_sales_from_file(filepath_name):
        """
        Reads sales data from the given file. This is a placeholder for actual file reading logic.
        You would need to implement this function based on the format of your file.
        """
        imported_sales_list = []
        try:
            # Example: Read the CSV file (assuming CSV format for simplicity)
            with open(filepath_name, "r") as file:
                for line in file:
                    # Assuming the file format is comma-separated, and each line is a sale record.
                    parts = line.strip().split(",")  # Example: "200,2024-10-01,North"
                    if len(parts) == 3:  # If the line has the expected format
                        try:
                            amount = float(parts[0])
                            sales_date = parts[1]
                            region = parts[2]
                            imported_sales_list.append({
                                "amount": amount,
                                "sales_date": sales_date,
                                "region": region,
                            })
                        except ValueError:
                            print(f"Invalid data format in line: {line.strip()}")
                    else:
                        print(f"Skipping invalid line: {line.strip()}")
        except FileNotFoundError:
            raise Exception(f"File {filepath_name} not found.")
        return imported_sales_list