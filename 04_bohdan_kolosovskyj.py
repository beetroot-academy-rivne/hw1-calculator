# TortosiseGit

print("Avaliable actions: \n")
print("+ - * / % // **  **2")
action = input("Choose one: ")
error = False
if not action == '+' and not action == '-' and not action == '*' and not action == '/' and not action == '%' and not action == '//' and not action == '**' and not action =='**2':
    result = 'Unsupported operation'
    error = True

firVal = float(input('Enter your first value: '))

if firVal == int(firVal):
    firVal = int(firVal)

if action == '**' and not error:
    st = int(input('Enter level: '))
    result = firVal ** st
    secVal = st
elif action == '**2' and not error:
    secVal = ' '
    result = firVal ** 2
elif not action == '**' and not error:
    secVal = float(input('Enter your second value: '))
    if secVal == int(secVal):
        secVal = int(secVal)    


if action == '+' and not error:
    result = firVal + secVal
elif action == '-' and not error:
    result = firVal - secVal
elif action == '*' and not error:
    result = firVal * secVal
elif action == '/' and not error:
    result = firVal / secVal
elif action == '%' and not error:
    result = firVal % secVal
elif action == '//' and not error:
    result = firVal // secVal

print('Your result: \n')
print(str(firVal), action, str(secVal) + ' = ' + str(result))
