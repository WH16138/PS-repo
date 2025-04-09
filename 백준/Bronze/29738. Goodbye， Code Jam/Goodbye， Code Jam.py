for i in range(int(input())):
    n = int(input())
    if n > 4500:
        print(f"Case #{i+1}: Round 1")
    elif n > 1000:
        print(f"Case #{i+1}: Round 2")
    elif n > 25:
        print(f"Case #{i+1}: Round 3")
    else:
        print(f"Case #{i+1}: World Finals")