from bizzzzuu_functions import *
# def bizz_zzuu(num):
#     if num % 3 == 0 and num % 5 == 0:
#         return str(num) + ' is a multiple of 3 or 5, bizzzzuu'
#     elif num % 3 == 0:
#         return str(num) + ' is a multiple of 3, bizz!'
#     elif num % 5 == 0:
#         return str(num) + ' is a multiple of 5, zzuu!'
#     else:
#         return str(num) + ' is not a multiple of 3 or 5, please try again.'
print("Welcome to the bizzzzuu game")
inputNum = int(input("Enter the number"))
print(bizz_zzuu(inputNum))

# Test driven development
# def div_by_3(num):
#    if num % 3 == 0:
#        return True
#    else:
#        return False
# Testing function div_by_3 (in theory), expected Bizz (expect true since I entered 3)
# print(div_by_3(3) == 'bizz') can use True or False instead of Bizz