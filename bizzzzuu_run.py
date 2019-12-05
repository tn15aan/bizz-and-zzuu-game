from bizzzzuu_functions import *

while num % 5 != 0 and num % 3 != 0:
    print(bizz_zzuu(num))
    num = int(input('Please choose a number: '))

final_output = run(num)
print(final_output)