
#load CSV file
with open("user.csv", "r") as f:
    lines = f.readlines()

try:
    users = []
    for line in lines[1:]:  # Skip header
        name, age = line.strip().split(";")
        users.append({"name": name, "age": int(age)})

except Exception as e:
    print(f"Error processing file: {e}")
    exit(1)
    
print(users)