import self

# [Import all objects from the p01_2bl_salesmanager module]
from p01sc04_exception_libraries_3tier.p01beg_2bl_salesmanager import  *
import os

# def display_title(self):
#     print("SALES DATA IMPORTER\n")


def display_menu(self):
    cmd_format = "6"  # ^ center, < is the default for str.
    print("COMMAND MENU",
          f"{'view':{cmd_format}} - View all sales",
          f"{'add1':{cmd_format}} - Add sales by typing sales, year, month, day, and region",
          f"{'add2':{cmd_format}} - Add sales by typing sales, date (YYYY-MM-DD), and region",
          f"{'import':{cmd_format}} - Import sales from file",
          f"{'menu':{cmd_format}} - Show menu",
          f"{'exit':{cmd_format}} - Exit program", sep='\n')


# [Write code to ask user to enter a command and call corresponding functions[ 
def execute_command(sales_list) -> None:
    while True:
        command = input("\nEnter command: ").strip().lower()
        if command == "view":
            view_sales(sales_list)
        elif command == "add1":
            add_sales1(sales_list)
        elif command == "add2":
            add_sales2(sales_list)
        elif command == "import":
            # Get file path input from user
            file_path = input("Enter the file path to import sales data: ").strip()

            # Debug: Print the type and value of file_path
            print(f"Debug: file_path is of type {type(file_path)} and value {file_path}")

            # Convert file_path from str to Path
            file_path = Path(file_path)
            print(f"Debug: Converted file_path is {file_path}")

            # Check the current working directory
            print(f"Current working directory: {os.getcwd()}")
            #
            if not file_path.is_absolute():
               file_path = Path(os.getcwd()) / file_path

            # Now check if the file exists
            if not file_path.exists():
                print(f"Error: The file {file_path} does not exist. Please check the file path and try again.")
                continue  # Skip this iteration and prompt again

            # Now pass the Path object to import_sales
            import_sales(file_path)  # Pass the Path object to import_sales
        elif command == "menu":
            display_menu(self)
        elif command == "exit":
            break
        else:
            print(f"Filename {file_path} doesn't include one of the following region codes: ['w', 'm','c', 'e']. ")

def main(self):
    # display_title(self)
    display_menu(self)

    # get all original sales data from a csv file
    try:
        sales_list = import_all_sales(self)
        print(f"Loaded {len(sales_list)} sales records.\n")
    except FileNotFoundError:
        print("Sales file not found. Starting with an empty sales list.")
        sales_list = []

    execute_command(sales_list)

    print("Bye!")


# if started as the main module, call the main function
if __name__ == "__main__":
    main(self)

  


  
