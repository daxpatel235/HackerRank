if __name__ == '__main__':
    n = int(input("enter value of n: ").strip())

    # Rule 1: Odd
    if n % 2 != 0:
        print("Weird")
    
    # Rule 2: Even & 2-5
    elif n % 2 == 0 and 2 <= n <= 5:
        print("Not Weird")
    
    # Rule 3: Even & 6-20
    elif n % 2 == 0 and 6 <= n <= 20:
        print("Weird")
    
    # Rule 4: Even & >20
    else:   
        print("Not Weird")
