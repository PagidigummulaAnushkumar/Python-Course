# [import classes date and datetime from datetime library]
from datetime import datetime
from typing import Optional

from pathlib import Path
import csv

from p01sc01_control_structures.p01m_sales_input import amount, entry_item, region_code, sales_date

# Regions
VALID_REGIONS = {"w": "West", "m": "Mountain", "c": "Central", "e": "East"}
# Sales date
DATE_FORMAT = "%Y-%m-%d"
MIN_YEAR, MAX_YEAR = 2000, 2_999
# files
FILEPATH = Path(__file__).parent.parent / 'p01_files'
IMPORTED_FILES = 'imported_files.txt'
ALL_SALES = 'all_sales.csv'
NAMING_CONVENTION = "sales_qn_yyyy_r.csv"


# [Add code to handle possible exception(s)]
def input_amount() -> float:
    while True:
        try:
            entry = float(input(f"{'Amount:':20}"))
            if entry > 0:
                return entry
            else:
                print(f"Amount must be greater than zero.")
        except(ValueError, entry.InvalidOperation):
            print("Please enter a valid monetary value.")


# [Add code to handle possible exception(s)]
def input_int(entry_item: str, high: int, low: int = 1, fmt_width: int = 20) -> int:
    prompt = f"{entry_item.capitalize()} ({low}-{high}):"
    while True:
        try:
            entry = int(input(f"{prompt:{fmt_width}}"))
            if low <= entry <= high:
                return entry
            else:
                print(f"{entry_item.capitalize()} must be between {low} and {high}.")
        except ValueError:
            print(f"Please enter a valid integer for {entry_item}.")

def input_year() -> int:
    return input_int('year', MAX_YEAR, MIN_YEAR)


def input_month() -> int:
    return input_int("month", 12, fmt_width=20)


def is_leap_year(year: int) -> bool:
    if year % 400 == 0:  # divisible by 400 --> leap year
        return True
    elif year % 100 == 0:  # not divisible by 400, but by 100 --> not leap year
        return False
    elif year % 4 == 0:  # not divisible by 100, but by 4,  --> leap year
        return True
    else:
        return False


def cal_max_day(year: int, month: int) -> int:
    if is_leap_year(year) and month == 2:  # short-circuit
        return 29
    elif month == 2:
        return 28
    elif month in (4, 6, 9, 11):
        return 30
    else:
        return 31


def input_day(year: int, month: int) -> int:
    max_day = cal_max_day(year, month)
    parameters = {"entry_item": "day", "high": max_day}
    return input_int(**parameters)


def is_valid_region(region_code: str) -> bool:
    return tuple(VALID_REGIONS.keys()).count(region_code) == 1


def get_region_name(region_code: str) -> str:
    return VALID_REGIONS[region_code]


def input_region_code() -> str:
    while True:
        fmt = 20
        valid_codes = tuple(VALID_REGIONS.keys())
        prompt = f"{f'Region {valid_codes}:':{fmt}}"
        code = input(prompt)
        if valid_codes.count(code) == 1:
            return code
        else:
            print(f"Region must be one of the following: {valid_codes}.")


# [Modify the code to use date and datetime from datetime library]
# [Add code to handle exception ValueError]
def input_date() -> str:
    while True:
        entry = input(f"{'Date (yyyy-mm-dd):':20}").strip()
        try:
            parsed_date = datetime.strptime(entry, DATE_FORMAT)
            if MIN_YEAR <= parsed_date.year <= MAX_YEAR:
                return parsed_date.strftime(DATE_FORMAT)
            # if len(entry) == 10 and entry[4] == '-' and entry[7] == '-' \
            #     and entry[:4].isdigit() and entry[5:7].isdigit() \
            #     and entry[8:].isdigit():
            # yyyy, mm, dd = int(entry[:4]), int(entry[5:7]), int(entry[8:])
            # if (1 <= mm <= 12) and (1 <= dd <= cal_max_day(yyyy, mm)):
            #     if MIN_YEAR <= yyyy <= MAX_YEAR:
            #         return entry
            else:
                 print(f"Year of the date must be between {MIN_YEAR} and {MAX_YEAR}.")
        except ValueError:
                    print(f"'{entry}' is not valid date or is in wrong format. please use yy-mm-dd.")

        #     else:
        #         print(f"{entry} is not in a valid date format.")
        # else:
        #     print(f"{entry} is not in a valid date format.")


def cal_quarter(month: int) -> int:
    if month in (1, 2, 3):
        quarter = 1
    elif month in (4, 5, 6):
        quarter = 2
    elif month in (7, 8, 9):
        quarter = 3
    elif month in (10, 11, 12):
        quarter = 4
    else:
        quarter = 0
    return quarter


def correct_data_types(row):
    try:  # amount
        row[0] = float(row[0])  # convert to float
    except ValueError:
        row[0] = "?"  # Mark invalid amount as bad
    try:  # date
        sales_date = datetime.strptime(row[1], DATE_FORMAT)
        row[1] = sales_date.date()  # convert to date
    except ValueError:
        row[1] = "?"  # Mark invalid date as bad


def has_bad_amount(data: dict) -> bool:
    return data["amount"] == "?"  # or data["amount"] < 0


def has_bad_date(data: dict) -> bool:
    return data["sales_date"] == "?"  # or not isinstance(self.sales_date, date)


def has_bad_data(data: dict) -> bool:
    return has_bad_amount(data) or has_bad_date(data)


def from_input1(sales_data):
    amount = input_amount()
    year = input_year()
    month = input_month()
    day = input_day(year, month)
    sales_date = input_date(year, month, day)
    region_code = input_region_code()
    return {"amount": amount,
            "sales_date": sales_date,
            "region": region_code,
            }


def from_input2():
    amount = input_amount()
    sales_date = input_date()
    region_code = input_region_code()
    return {"amount": amount,
            "sales_date": sales_date,
            "region": region_code,
            }


def is_valid_filename_format(sales_filename: str) -> bool:
    if len(sales_filename) == len(NAMING_CONVENTION) and \
       sales_filename[:7] == NAMING_CONVENTION[:7] and \
       sales_filename[8] == NAMING_CONVENTION[8] and \
       sales_filename[13] == NAMING_CONVENTION[-6] and \
       sales_filename[-4:] == NAMING_CONVENTION[-4:]:
        return True
    return False


def get_region_code(sales_filename: str) -> str:
    return sales_filename[sales_filename.rfind('.') - 1]


# [Add code to handle exception FileNotFoundError]
def already_imported(filepath_name: Path) -> bool:
    try:
        with open(FILEPATH / IMPORTED_FILES) as file:
            files = [line.strip() for line in file.readlines()]  # Strip newlines
            return str(filepath_name) in files
    except FileNotFoundError:
        print(f"File '{IMPORTED_FILES}' not found.")
        return False


# [Add code to handle exception Exception by printing the type of exception]
def add_imported_file(filepath_name: Path):
    try:
        with open(FILEPATH / IMPORTED_FILES, "a") as file:
            file.write(f"{filepath_name}")
    except Exception as e:
        print(f"An error occurred while trying to write to '{IMPORTED_FILES}': {type(e).__name__} - {e}")


def import_sales(filepath_name: Path, delimiter: str=',') -> list:
    try:
        # Convert filepath_name to a Path object if it's a string
        if isinstance(filepath_name, str):
            filepath_name = Path(filepath_name)

        # Check if the Path object exists
        if not filepath_name.exists():
            raise FileNotFoundError(f"The file {filepath_name} does not exist.")

        # Open the CSV file
        with open(filepath_name, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=delimiter)
            filename = filepath_name.name
            region_code = get_region_code(filename)  # Assuming this function is defined elsewhere

            imported_sales_list = []

            # Read and process each row from the CSV file
            for amount_sales_date in reader:
                correct_data_types(amount_sales_date)  # Assuming this function is defined elsewhere
                amount, sales_date = amount_sales_date[0], amount_sales_date[1]

                # Store the data in a dictionary
                data = {
                    "amount": amount,
                    "sales_date": sales_date,
                    "region": region_code,
                }
                imported_sales_list.append(data)

        # Return the list of imported sales data
        return imported_sales_list

    except FileNotFoundError as e:
        # Handle file not found error
        print(f"Error: {e}")

    except Exception as e:
        # Handle other unforeseen errors
        print(f"An unexpected error occurred: {e}")

        # Return an empty list in case of error
    return []


def main():
  '''
  Write code to test the functions in this module
  '''

  sales_data = {}
  try:
      amount = input_amount()
      date = input_date()
      region_code = input_region_code()

      sales_data = {
          "amount": amount,
          "sales_date":sales_date,
          "region":region_code,
      }
      #from_input1(sales_data)

      #sales_data.append(from_input1)
      print(f"Sales data added: {sales_date}")

  except ValueError as ve:
      print(f"Error: {ve}")

  sales_file = Path("sales_data.csv")
  try:
      # if not already_imported(sales_file):
      #     sales_list = import_sales(sales_file)
      #     for sales in sales_list:
      #         from_input1(sales)
      #     add_imported_file(sales_file)

      if not already_imported(sales_file):
          sales_data_from_file = import_sales(sales_file)
          for sales in sales_data_from_file:
              sales_data.update(sales)
              add_imported_file(sales_file)
  except Exception as e:
      (print(f"Error during file operations: {e}"))


if __name__ == "__main__":
    main()

  
