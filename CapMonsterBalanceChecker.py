import time
import requests
import os

while True:
    api_key = input("Enter your CapMonster API key: ")
    try:
        response = requests.post("https://api.capmonster.cloud/getBalance", json={"clientKey": api_key}).json()
        if response['errorId'] == 0:
            balance = response['balance']
            break
    except:
        print("Incorrect API key. Please try again.")

print(f"Press Enter to refresh your balance.\n You currently have ${balance:.3f}")

while True:
    command = input()
    if command.lower() == "quit":
        break
    elif command == "":
        print("Refreshing balance", end="", flush=True)
        for _ in range(6):
            time.sleep(0.1)
            print(".", end="", flush=True)
        print()
        os.system("cls" if os.name == "nt" else "clear")
        try:
            response = requests.post("https://api.capmonster.cloud/getBalance", json={"clientKey": api_key}).json()
            if response['errorId'] == 0:
                balance = response['balance']
                print(f"Your balance is: {balance:.3f}")
            else:
                print("Failed to get balance.")
        except:
            print("Incorrect API key. Please try again.")
        print("Press Enter to refresh the balance")
    else:
        print("Invalid command.")
