import sys

if __name__ == '__main__':
    n = int(input().strip())

    # Loop from 1 to 10 (11 is excluded)
    for i in range(1, 11):
        result = n * i
        # Use an f-string to format the output exactly as requested
        print(f"{n} x {i} = {result}")
