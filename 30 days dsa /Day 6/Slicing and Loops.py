# 1. Read the number of test cases (Input & Casting)
T = int(input())

# 2. Loop T times (Control Flow)
# We use '_' because we don't care about the loop index, just the repetition.
for _ in range(T):
    
    # 3. Read the string S
    S = input()

    # 4. Separate Even and Odd characters (Slicing)
    # Syntax: string[start : stop : step]
    even_chars = S[::2]   # Start at 0, go to end, step by 2 (0, 2, 4...)
    odd_chars = S[1::2]   # Start at 1, go to end, step by 2 (1, 3, 5...)

    # 5. Print the result (Formatted Output)
    print(f"{even_chars} {odd_chars}")
