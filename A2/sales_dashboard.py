import time
import pandas as pd

FILE_ID = "1Fv_vhoN4sTrUaozFPfzr0NCyHJLIeXEA"
sales_data_URL = f"https://drive.google.com/uc?export=download&id={FILE_ID}"

# Columns the dashboard analytics rely on
REQUIRED_COLUMNS = ["quantity", "unit_price", "sales_region", "order_date"]


def load_csv(source):
    """Load a CSV (path or URL) into a pyarrow-backed dataframe; return None on failure."""
    print(f"Loading {source} ...")
    start = time.time()
    try:
        df = pd.read_csv(source, engine="pyarrow", dtype_backend="pyarrow",
                         on_bad_lines="skip")
    except FileNotFoundError:
        print(f"ERROR: file not found: {source}")
        return None
    except pd.errors.EmptyDataError:
        print(f"ERROR: {source} is empty.")
        return None
    except (pd.errors.ParserError, UnicodeDecodeError, ValueError) as e:
        print(f"ERROR: could not parse CSV data: {e}")
        return None
    except Exception as e:
        print(f"ERROR: failed to load {source}: {e}")
        return None

    print(f"Successfully loaded in {time.time() - start:.2f} seconds.")
    print(f"Rows: {len(df)}")
    print(f"Columns: {list(df.columns)}")

    # Dates arrive in mixed formats (e.g. 9/2/19 and 15/02/2019)
    if "order_date" in df.columns:
        df["order_date"] = pd.to_datetime(
            df["order_date"].astype("string[python]"), format="mixed",
            dayfirst=True, errors="coerce").astype("timestamp[ns][pyarrow]")
        bad = df["order_date"].isna().sum()
        if bad:
            print(f"WARNING: {bad} order_date value(s) could not be parsed.")

    missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing:
        print(f"WARNING: missing required column(s): {missing}. "
              "Some analytics will not function without them.")
    return df


def display_initial_rows(data):
    """Ask the user how many rows to show. Accepts a positive integer, 'all', or 'q' to quit.
    Returns False when the user asks to quit, otherwise True."""
    total = len(data)
    answer = input(f"\nHow many initial rows to display (1-{total}, 'all', or 'q' to quit)? ")
    answer = answer.strip().lower()

    if answer in ("q", "quit", "exit"):
        return False
    if answer == "all":
        n = total
    else:
        try:
            n = int(answer)
        except ValueError:
            print(f"Invalid input '{answer}': enter a whole number, 'all', or 'q'.")
            return True
        if n < 1:
            print("Please enter a number greater than 0.")
            return True
        if n > total:
            print(f"Only {total} rows available; Please enter a number less than or equal to {total}.")
            return True

    print(data.head(n).to_string())
    return True


def show_employees_by_region(data):
    """Print the number of unique employees in each sales region."""
    if "sales_region" not in data.columns or "employee_id" not in data.columns:
        print("Cannot compute employees by region: 'sales_region' or 'employee_id' column is missing.")
        return
    counts = data.groupby("sales_region")["employee_id"].nunique()
    print("\nNumber of employees by region:")
    print(counts.to_string())


def exit_program(data):
    print("Goodbye!")
    raise SystemExit(0)


menu_options = (
    ("Show the first n rows of sales data", display_initial_rows),
    ("Show the number of employees by region", show_employees_by_region),
    ("Exit the program", exit_program),
)


def display_menu():
    """Show the menu and return the user's valid choice as a 0-based index."""
    while True:
        print("\nMenu:")
        for i, (label, _) in enumerate(menu_options, start=1):
            print(f"  {i}. {label}")
        choice = input(f"Select an option (1-{len(menu_options)}): ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(menu_options):
            return int(choice) - 1
        print(f"Invalid selection '{choice}'. Please enter a number from 1 to {len(menu_options)}.")


def main():
    data = load_csv("sales_data_test.csv")
 #   data = load_csv(sales_data_URL)
    if data is None:
        print("No data loaded; exiting.")
        return
    while True:
        choice = display_menu()
        menu_options[choice][1](data)


if __name__ == "__main__":
    main()