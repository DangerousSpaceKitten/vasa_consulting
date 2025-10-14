"""
Author: Urs Erik Pfrommer
Date:2025-10-11

Preprocessing script for turning data from json files into 
an sql script to insert the data into the db
"""

import json
from pathlib import Path

current_week = 4
import_topic = "schedules"
data = {}

def write_string_to_txt(text: str, subfolder: str, filename: str, base_dir: Path | None = None):
    base = base_dir if base_dir is not None else Path.cwd()
    folder = base / subfolder
    folder.mkdir(parents=True, exist_ok=True)

    file_path = folder / filename
    # 'w' = create if missing, overwrite if existing use 'x' to prevent overwriting
    with file_path.open('w', encoding='utf-8', newline='\n') as f:
        f.write(text)

    print(f"File saved to {file_path}")

def process_amounts():
    for i in range(current_week):
        file = open(f"week{i}/{import_topic}_{i}.json", "r")
        data[f"{i}"] = json.load(file)

    flat_data = {k: [x for kv in v.items() for x in kv] for k, v in data.items()}

    for i in range(len(flat_data)):
        for j in range(len(flat_data[f"{i}"])):
            match flat_data[f"{i}"][j]:
                case "rice_porridge": 
                    flat_data[f"{i}"][j] = 1
                case "hot_dogs":
                    flat_data[f"{i}"][j] = 2
                case "ice_cream":
                    flat_data[f"{i}"][j] = 3
                case "sunscreen":
                    flat_data[f"{i}"][j] = 4
                case "dinosaur":
                    flat_data[f"{i}"][j] = 5
                case "laderhosen":
                    flat_data[f"{i}"][j] = 6
                case "gjokur_ja":
                    flat_data[f"{i}"][j] = 7
                case "batteries":
                    flat_data[f"{i}"][j] = 8
                case "monster":
                    flat_data[f"{i}"][j] = 9
                case "nails":
                    flat_data[f"{i}"][j] = 10
                case "hammer":
                    flat_data[f"{i}"][j] = 11
                case "knives":
                    flat_data[f"{i}"][j] = 12
                case "mattress":
                    flat_data[f"{i}"][j] = 13

    output = ""

    for j in range(0, len(flat_data[f"{0}"]), 2):
        for i in range(0, len(flat_data)):
            output += f"INSERT INTO PURCHASES (WEEK, ARTICLE_ID, AMOUNT) VALUES ({i}, {flat_data[f"{i}"][j]}, {flat_data[f"{i}"][j+1]});\n"

    write_string_to_txt(output, "insert_scripts", "purchases.txt")

def process_prices():
    for i in range(current_week):
        file = open(f"week{i}/{import_topic}_{i}.json", "r")
        data[f"{i}"] = json.load(file)

    flat_data = {k: [x for kv in v.items() for x in kv] for k, v in data.items()}

    for i in range(len(flat_data)):
        for j in range(len(flat_data[f"{i}"])):
            match flat_data[f"{i}"][j]:
                case "rice_porridge": 
                    flat_data[f"{i}"][j] = 1
                case "hot_dogs":
                    flat_data[f"{i}"][j] = 2
                case "ice_cream":
                    flat_data[f"{i}"][j] = 3
                case "sunscreen":
                    flat_data[f"{i}"][j] = 4
                case "dinosaur":
                    flat_data[f"{i}"][j] = 5
                case "laderhosen":
                    flat_data[f"{i}"][j] = 6
                case "gjokur_ja":
                    flat_data[f"{i}"][j] = 7
                case "batteries":
                    flat_data[f"{i}"][j] = 8
                case "monster":
                    flat_data[f"{i}"][j] = 9
                case "nails":
                    flat_data[f"{i}"][j] = 10
                case "hammer":
                    flat_data[f"{i}"][j] = 11
                case "knives":
                    flat_data[f"{i}"][j] = 12
                case "mattress":
                    flat_data[f"{i}"][j] = 13

    output = ""

    for j in range(0, len(flat_data[f"{0}"]), 2):
        for i in range(0, len(flat_data)):
            output += f"INSERT INTO PRICES (WEEK, ARTICLE_ID, ARTICLE_PRICE) VALUES ({i}, {flat_data[f"{i}"][j]}, {flat_data[f"{i}"][j+1]});\n"

    write_string_to_txt(output, "insert_scripts", "prices.txt")

def process_schedules():
    for i in range(current_week):
        file = open(f"week{i}/{import_topic}_{i}.json", "r")
        data[f"{i}"] = json.load(file)
    
    days_of_the_week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]



    flat_data = {k: [x for kv in v.items() for x in kv] for k, v in data.items()}

    print(flat_data["0"][0], flat_data["0"][1][0]["worker_id"], flat_data["0"][1][0]["department"], flat_data["0"][1][0]["shift"])

    
    output = ""
    day = ""

    for i in range(current_week):
        for j in range(len(flat_data[f"{i}"])):
            for k in range(len(flat_data[f"{i}"][j])):
                if j == 0:
                 day = flat_data[f"{i}"][j]
                else:
                    #print({flat_data[f"{i}"][j][k]})
                    output += f"INSERT INTO SCHEDULES (WEEK, DAY, WORKER_ID, DEPARTMENT, SHIFT) VALUES ({i}, {day}, {[flat_data[f"{i}"][j][k]["worker_id"], flat_data[f"{i}"][j][k]["department"], flat_data[f"{i}"][j][k]["shift"]]});\n"
    
    output = output.replace("mondaymondaymondaymondaymondaymonday", "monday")

    print(output)
    


def process_transactions():
    for i in range(current_week):
        file = open(f"week{i}/{import_topic}_{i}.json", "r")
        data[f"{i}"] = json.load(file)

    flat_data = {k: [x for kv in v.items() for x in kv] for k, v in data.items()}


def process_transactions():
    """
    Build INSERT statements for the TRANSACTIONS table from weekN/transactions_N.json files.

    Expected JSON structure per file (example):
    {
        "1": [  # "DAY" key as string (e.g., "1", "2", ...). We preserve it as-is.
            {
                "customer_id": "c_xxx",
                "merch_types": ["laderhosen", "gjokur_ja"],
                "merch_amounts": [1, 2],
                "register_worker": "w_xxx",
                "transaction_type": "customer_sale"
            },
            ...
        ],
        "2": [ ... ],
        ...
    }

    Emits one INSERT per merch item within a transaction (cart line).
    """
    # Load weekly files
    for i in range(current_week):
        with open(f"week{i}/{import_topic}_{i}.json", "r", encoding="utf-8") as file:
            data[f"{i}"] = json.load(file)

    # Article name -> ID mapping (keep in sync with other processors)
    name_to_id = {
        "rice_porridge": 1,
        "hot_dogs": 2,
        "ice_cream": 3,
        "sunscreen": 4,
        "dinosaur": 5,
        "laderhosen": 6,
        "gjokur_ja": 7,
        "batteries": 8,
        "monster": 9,
        "nails": 10,
        "hammer": 11,
        "knives": 12,
        "mattress": 13,
    }

    def q(s: str) -> str:
        # Simple SQL quoting for strings
        return "'" + str(s).replace("'", "''") + "'"

    output_lines = []

    # Iterate: week -> day -> transactions
    for i in range(current_week):
        week_payload = data.get(f"{i}", {})
        # If the file had a flat structure already, ensure we iterate consistently
        if isinstance(week_payload, dict):
            day_items = week_payload.items()
        else:
            # Fallback: assume single day "0"
            day_items = [("0", week_payload)]

        for day_key, tx_list in day_items:
            if not isinstance(tx_list, list):
                continue  # skip malformed

            for tx in tx_list:
                customer_id = tx.get("customer_id", "")
                worker_id = tx.get("register_worker", "")
                tx_type = tx.get("transaction_type", "")
                merch_types = tx.get("merch_types", []) or []
                merch_amounts = tx.get("merch_amounts", []) or []

                # Pair up types and amounts safely
                for idx, art_name in enumerate(merch_types):
                    amount = merch_amounts[idx] if idx < len(merch_amounts) else 0
                    article_id = name_to_id.get(art_name)
                    if article_id is None:
                        # Unknown article name -> skip this line gracefully
                        continue

                    # Compose INSERT
                    line = (
                        "INSERT INTO TRANSACTIONS "
                        "(WEEK, DAY, CUSTOMER_ID, ARTICLE_ID, PURCHASE_AMOUNTS, WORKER_ID, TRANSACTION_TYPE) "
                        f"VALUES ({i}, {q(day_key)}, {q(customer_id)}, {article_id}, {amount}, {q(worker_id)}, {q(tx_type)});"
                    )
                    output_lines.append(line)

    output = "\n".join(output_lines) + ("\n" if output_lines else "")

    # Save to file
    write_string_to_txt(output, "insert_scripts", "transactions.txt")


match import_topic:
    case "amounts":
        process_amounts()
    case "prices":
        process_prices()
    case "schedules":
        process_schedules()
    case "transactions":
        process_transactions()

