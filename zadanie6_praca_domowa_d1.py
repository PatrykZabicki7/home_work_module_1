def is_divided_by_4(x):
    y = x % 4
    if y==0:
        return True
    else:
        return False

print(is_divided_by_4(15))