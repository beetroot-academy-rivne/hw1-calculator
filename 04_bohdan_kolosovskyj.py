print("Avaliable actions: \n")
print("+ - * / % // **  **2")
action = input("Choose one: ")
error = False
if not action == '+' and not action == '-' and not action == '*' and not action == '/' and not action == '%' and not action == '//' and not action == '**' and not action =='**2':
    result = 'Unsupported operation'
    error = True
if not error:
    firVal = float(input("Enter your first value: "))
if action == '**' and not error:
    st = float(input('Enter level: '))
    result = firVal ** st
elif action == '**2' and not error:
    result = firVal ** 2
elif not action == '**' and not error:
    secVal = float(input('Enter your second value: '))

if action == '+' and not error:
    result = "Result: " + str(firVal) + ' + ' + str(secVal) + ' = ' + str(firVal + secVal)
    # result.format(firVal, secVal, firVal + secVal)
elif action == '-' and not error:
    result = "Result: " + str(firVal) + ' - ' + str(secVal) + ' = ' + str(firVal - secVal)
elif action == '*' and not error:
    result = "Result: " + str(firVal) + ' * ' + str(secVal) + ' = ' + str(firVal * secVal)
elif action == '/' and not error:
    result = "Result: " + str(firVal) + ' / ' + str(secVal) + ' = ' + str(firVal / secVal)
elif action == '%' and not error:
    result = "Result: " + str(firVal) + ' % ' + str(secVal) + ' = ' + str(firVal % secVal)
elif action == '//' and not error:
    result = "Result: " + str(firVal) + ' // ' + str(secVal) + ' = ' + str(firVal // secVal)

print(result)
