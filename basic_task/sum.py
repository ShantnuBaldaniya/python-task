def single_digit_sum(a):
    total = 0
    for i in a:
        total += i

   
    while total >= 3:
        s = 0
        while total > 0:
            s += total % 10
            total //= 10
        total = s

    return total


a = [1, 2, 3, 4, 5, 6, 7]
print(single_digit_sum(a))
