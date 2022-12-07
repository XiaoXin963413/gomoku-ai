def check_all(list, val):
    return all(x == val and x is not True for x in list)

a = [1, 0, 0, 0, 0]

print(check_all(a, 0))