from rich.table import Table
from rich.console import Console
from rich.live import Live
from rich.text import Text
import time

table = Table(title="Wifi hack")


words = [str(chr(x) + chr(x) + chr(x)) for x in range(128)]

byte_data = ''.join(words).encode()

console = Console()
table.add_column("WPA2 data")
table.add_column("Test password")
table.add_column("Success")

passText = Text("passwd", style="green")

i = 0

console.print(table)
