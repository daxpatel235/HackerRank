# Read number of entries
n = int(input())

# Create empty dictionary
phone_book = {}

# Read the n entries
for _ in range(n):
    name, number = input().split()
    phone_book[name] = number

# Read queries until EOF (no more input)
while True:
    try:
        query = input()
    except EOFError:
        break  # Stop when there are no more lines

    if query in phone_book:
        print(f"{query}={phone_book[query]}")
    else:
        print("Not found")
