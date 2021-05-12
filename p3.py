if __name__ == "__main__":
    num = 600851475143
    prime_factors = []

    for i in range(num // 2, 0, -1):
        if num % i == 0:
            print(i)
