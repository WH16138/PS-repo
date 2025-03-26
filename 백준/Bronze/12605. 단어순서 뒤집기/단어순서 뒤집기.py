for T in range(int(input())):
    words = input().split()
    print(f"Case #{T+1}: " + " ".join(words[::-1]))