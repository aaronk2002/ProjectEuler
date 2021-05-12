def get_fibonacci(current, upper_bound):
    next_num = current[len(current) - 2] + current[len(current) - 1]
    if not next_num > upper_bound:
        current.append(next_num)
        return get_fibonacci(current, upper_bound)
    else:
        return current


if __name__ == "__main__":
    sum = 0
    for i in get_fibonacci([1, 2], 4000000):
        if i % 2 == 0:
            sum += i
    print(sum)
