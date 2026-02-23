users = ["Ana", "Carlos", "Maria"]
transactions = [100, 250.5, -20]

enum_users = enumerate(users)
enum_transactions = zip(users, transactions)

for index, user in enum_users:
    print(f"{index}: {user}")

for user, transaction in enum_transactions:
    print(f"{user}: {transaction}")

for user, transaction in zip(enumerate(users), transactions):
    if transaction < 0:
        continue

    index, name = user
    print(f"{index}: {name} - {transaction}")

# ✅ VERSÃO PYTHONIC E PROFISSIONAL
for index, (name, amount) in enumerate(zip(users, transactions), start=1):
    if amount < 0:
        continue
    print(f"{index} - {name}: {amount}")    

# 🧪 ALTERNATIVA (UM POUCO MAIS FUNCIONAL)
valid_pairs = [
    (i, name, amount)
    for i, (name, amount) in enumerate(zip(users, transactions), start=5)
    if amount > 0
]

for i, name, amount in valid_pairs:
    print(f"{i} - {name}: {amount}")