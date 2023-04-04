first_name = input("Enter the first name:")
last_name = input("Enter the last name:")
ZIP_code = input("Enter the ZIP code:")
employee_ID = input("Enter an employee ID:")

len1 = len(first_name)
len2 = len(last_name)
len4 = len(employee_ID)


if len1 == 0:
    print("The first name must be filled in.")
elif len1 == 1:
    print('"{}" is not a valid first name. It is too short.'.format(first_name))

if len2 == 0:
    print("The last name must be filled in.")
elif len2 == 1:
    print('"{}" is not a valid last name. It is too short.'.format(last_name))#在字符串里穿插输出变量

if ZIP_code.isnumeric() == False: #判断是不是数字，用现成的函数，注意区分isdecimal、isdight
    print("The ZIP code must be numeric.")

if len4 != 7 or employee_ID[2] != '-':
    print('{} is not a valid ID.'.format(employee_ID))
