from rich.table import Table
from rich.live import Live

# Create a table instance
table = Table()

# Add columns to the table
table.add_column("Name", justify="center", style="cyan")
table.add_column("Age", justify="center", style="magenta")
table.add_column("City", justify="center", style="green")

# Define some data for the table
data = [
    {"Name": "Alice", "Age": 28, "City": "New York"},
    {"Name": "Bob", "Age": 32, "City": "Los Angeles"},
    {"Name": "Charlie", "Age": 22, "City": "Chicago"},
    {"Name": "David", "Age": 35, "City": "San Francisco"},
]

# Function to update the table with new data


def update_table(data):
    for row in data:
        table.add_row(row["Name"], str(row["Age"]), row["City"])


# Create a Live instance to continuously display the table
with Live(table, refresh_per_second=1):
    while True:
        # In this example, we update the table with the same data repeatedly,
        # but in a real application, you would replace this with your own data source.
        update_table(data)
