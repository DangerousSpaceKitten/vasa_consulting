from pathlib import Path
import json

# Adjust these paths as needed; they’re relative to your current working directory.
amounts_path = Path("proposals/week4/amounts_4.json")
prices_path = Path("supplier_prices.json")

def read_json(path: Path):
    try:
        with path.open("r", encoding="utf-8-sig") as f:  # utf-8-sig handles BOM if present
            return json.load(f)
    except FileNotFoundError:
        raise SystemExit(f"File not found: {path.resolve()}\n"
                         f"Tip: current working directory is {Path.cwd()}")
    except json.JSONDecodeError as e:
        raise SystemExit(
            f"Invalid JSON in {path.name} (line {e.lineno}, col {e.colno}): {e.msg}"
        )

amounts = read_json(amounts_path)
prices  = read_json(prices_path)

total_spending = 0

for i in range(len(amounts)):
    product_amount = list(amounts.keys())[i]
    amount_amount = list(amounts.values())[i]
    product_price = prices[product_amount]
    total_price = float(amount_amount) * float(product_price)
    total_spending += total_price

print(total_spending)
