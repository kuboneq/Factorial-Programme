class Math:
    @classmethod
    def factorial(cls, x):
        if x <= 1:
            return 1
        else:
            return x * cls.factorial(x - 1)
    
    @classmethod
    def power(cls, x, n):
        if n <= 0:
            return 1
        else:
            return x * cls.power(x, n - 1)



dict_power = {}
dict_factorial = {}

while True:
    user_input = input('What do u want to do? [F] Factorial, [P], Power, [Q] to Quit: ')
    for i in user_input:
        if i in '1234567890':
            print('Type in the letter')
            break
        else:
            if user_input.lower() == 'q':
                if dict_factorial:
                    print('Factorials:')
                    for (key, value) in dict_factorial.items():
                        print('{}! is {}'.format(key, value))
                else:
                    print("No factorials were found!")
                if dict_power: 
                    print('Powers:')
                    for (key, value) in dict_power.items():
                        print('{}^{} is {}'.format(key[0],key[3],value))
                else:
                    print("No powers were found!")
                exit()
                    
            elif user_input.lower() == 'f':
                user_input_factorial = input("Enter the number you want to factorize: ")
                for i in user_input_factorial:
                    if i not in '0123456789':
                        print('Invalid value')
                        break
                    else:
                        result_factorial = Math.factorial(int(user_input_factorial))
                        print("The factorial of {}, is equal to {}".format(int(user_input_factorial),result_factorial))
                        dict_factorial.update({int(user_input_factorial): result_factorial})

            elif user_input.lower() == 'p':
                user_input_power = input("Enter a base of the power: ") 
                user_input_power_exponent = input("Enter an exponent: ")
                for i in user_input_power_exponent and user_input_power:
                    if i not in '0123456789':
                        print('Invalid value')
                        break
                    else:
                        result_power = Math.power(int(user_input_power), int(user_input_power_exponent))
                        print("{} raised to the power of {}, is equal to {}".format(user_input_power, user_input_power_exponent, result_power))
                        dict_power.update({'{}, {}'.format(user_input_power, user_input_power_exponent):result_power})
            else:
                print('Enter a valid value')
                break

