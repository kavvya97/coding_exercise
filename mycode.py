import csv
import sys
def fetch_code_exercise(amount, transactions):
    output = {}
    # sorting the transactions based on time
    transactions.sort(key=lambda x: x[2])
    for (payer, points, timestamp) in transactions:
        if payer not in output:
            output[payer] = points
        else:
            output[payer] += points
        if amount > 0:
            if output[payer] >= amount:
                output[payer] -= amount
                amount = 0
            else:
                amount -= output[payer]
                output[payer] = 0
    return output   
    

def main():
    if len(sys.argv) < 2:
        print("Please provide amount to spend")
        return
    points_spent = int(sys.argv[1])
    transactions = []
    with open('./data/transactions.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader) # we are going to skip the frist row which is the header row .
        for row in reader:
            payer, points, timestamp = row
            transactions.append((payer, int(points), timestamp))
    result = fetch_code_exercise(points_spent, transactions)
    print(result)

if __name__ == '__main__':
    main()


# import csv
# import sys

# def spend_points(amount, transactions):
#     payer_balances = {}
#     transactions.sort(key=lambda x: x[2])  # sort transactions by timestamp
#     for payer, points, timestamp in transactions:
#         if payer not in payer_balances:
#             payer_balances[payer] = 0
#         payer_balances[payer] += points
#         if amount > 0:
#             if payer_balances[payer] >= amount:
#                 payer_balances[payer] -= amount
#                 amount = 0
#             else:
#                 amount -= payer_balances[payer]
#                 payer_balances[payer] = 0
#     return payer_balances

# if __name__ == "__main__":
#     amount = int(sys.argv[1])
#     transactions = []
#     with open("transactions.csv") as file:
#         reader = csv.reader(file)
#         next(reader)  # skip header row
#         for row in reader:
#             payer, points, timestamp = row
#             transactions.append((payer, int(points), timestamp))
#     payer_balances = spend_points(amount, transactions)
#     print("Balance:", payer_balances)