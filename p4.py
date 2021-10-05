import time

if __name__ == "__main__":
    start = time.time()

    min_num = 100
    max_num = 1000

    palindromes = []

    for x in range(min_num, max_num):
        for y in range(x, max_num):
            num = x * y

            if str(num) == str(num)[::-1]:
                palindromes.append(num)

    print(max(palindromes))
    print(time.time() - start)
