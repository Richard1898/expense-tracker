#   _____                                       _____               _             
#  | ____|_  ___ __   ___ _ __  ___  ___  ___  |_   _| __ __ _  ___| | _____ _ __ 
#  |  _| \ \/ / '_ \ / _ \ '_ \/ __|/ _ \/ __|   | || '__/ _` |/ __| |/ / _ \ '__|
#  | |___ >  <| |_) |  __/ | | \__ \  __/\__ \   | || | | (_| | (__|   <  __/ |   
#  |_____/_/\_\ .__/ \___|_| |_|___/\___||___/   |_||_|  \__,_|\___|_|\_\___|_|   
#             |_|                                                                 
import json
#
# Uzdevums:
# Uzrakstīt programmu, kas ļauj
# - ievadīt izdevumus: nosaukumu, summu un kategoriju
# - atspoguļot uz ekrāna visus izdevumus
# - iespēja atlasīt 10 lielākus izdevumus
# - iespēja atlasīt 10 mazākus izdevumus
# - iespēja apskatīt vidējo izdevumu summu
# [!] Programmai jaglabā izdevumu stāvokli kad programma ir izslēgta palaista no jauna
#
expenses_file = open('expenses.json') # opening JSON file
expenses = json.load(expenses_file) # returns JSON object as a dictionary

m ={}
# load expenses from expenses.json file here
# https://www.geeksforgeeks.org/read-write-and-parse-json-using-python/ (Python read JSON file)
pass
def Summa(n):
            return int(n["Summa"])
while True:
    command = input("\nChoose command:")
    if command == "1":
        m = {
        "Nosaukums": input("Uzrakstiet Nosaukumu: "),
        "Summa": int(input("Uzrakstiet Summu: ")),
        "Kategorija": input("Uzrakstiet Kategoriju: ")
        }
        expenses.append(m)
        with open('expenses.json', 'w') as outfile:
             json.dump(expenses, outfile)
    if command == "2":
        print(expenses)
    if command == "3":
        expenses.sort(key = Summa, reverse=True)
        print(expenses[:10])
    if command == "4":
        expenses.sort(key = Summa, reverse=False)
        print(expenses[:10])
    if command == "5":
        summ = 0
        o=0
        for x in expenses:
             summ += x['Summa'] 
             o += 1
        Videja = summ / o
    print(Videja)
    if command == "e":
        print("Exiting...")
        break

# save expenses to expenses.json file here
# https://www.geeksforgeeks.org/read-write-and-parse-json-using-python/ (Writing JSON to a file in Python)
pass

