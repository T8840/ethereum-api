#   pyinstaller --onefile .\accounts_gui.py

import csv
import tkinter as tk
from tkinter import filedialog, ttk  # ttk is used for the Combobox widget
from web3 import Web3

def load_csv(file_path):
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        addresses = [row[0] for row in reader]  # Assuming one address per row
    return addresses

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        addresses = load_csv(file_path)
        address_combo['values'] = addresses

def run_web3():
    infura_url = f"https://mainnet.infura.io/v3/{infura_api_key_entry.get()}"
    web3 = Web3(Web3.HTTPProvider(infura_url))

    output.delete(1.0, tk.END)  # Clear the existing output
    output.insert(tk.END, f"Connected: {web3.is_connected()}\n")
    output.insert(tk.END, f"Block Number: {web3.eth.block_number}\n")

    selected_wallet = address_combo.get()
    balance = web3.eth.get_balance(selected_wallet)
    output.insert(tk.END, f"Balance for {selected_wallet}: {web3.from_wei(balance, 'ether')} ETH\n")

root = tk.Tk()
root.title("Web3 App")

# INFURA API Key Entry
tk.Label(root, text="INFURA API Key:").pack(pady=5)
infura_api_key_entry = tk.Entry(root, width=50)
infura_api_key_entry.pack(pady=5)

# Load CSV Button
open_button = tk.Button(root, text="Open CSV", command=open_file)
open_button.pack(pady=20)

# Address Dropdown (Combobox)
tk.Label(root, text="Select WALLET_ADDRESS:").pack(pady=5)
address_combo = ttk.Combobox(root)
address_combo.pack(pady=5)

# Run Button
run_button = tk.Button(root, text="Run Web3", command=run_web3)
run_button.pack(pady=20)

# Output Text Area
output = tk.Text(root, height=10, width=50)
output.pack(pady=20)

root.mainloop()
