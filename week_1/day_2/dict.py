user: dict[str, str | int | float | bool] = {
    "name": "Arnaldo",
    "age": 30,
    "height": 1.75,
    "is_active": True,
}

for key, value in user.items():
    print(f"{key}: {value}")

users: list[dict[str, str | int]] = [
    {"id": 1, "name": "Arnaldo", "active": True},
    {"id": 2, "name": "Beatrice", "active": False},
    {"id": 3, "name": "Carla", "active": True},
]

for u in users:
    print(u["id"], u["name"])

active_users = [u["name"] for u in users if u["active"]]
print(active_users)
# for u in active_users:
    # print(u["id"], u["name"])   