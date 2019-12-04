def bizz_zzuu(num):
    if num % 3 == 0 and num % 5 == 0:
        return str(num) + ' is a multiple of 3 or 5, bizzzzuu'
    elif num % 3 == 0:
        return str(num) + ' is a multiple of 3, bizz!'
    elif num % 5 == 0:
        return str(num) + ' is a multiple of 5, zzuu!'
    else:
        return str(num) + ' is not a multiple of 3 or 5, please try again.'

inputNum = int(input("Enter the number"))
print(bizz_zzuu(inputNum))