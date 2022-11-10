def silnia(x:int) -> int:
    
    # Funkcja liczaca silnie
    if x <= 1:
        return 1
    else:
        return x * silnia(x - 1)

nums_before = list()
nums_after  = list()

print("Obliczanie silni ")
while True:
    user_input = input("Podaj liczbe z ktorej chcesz obliczyc silnie lub Q, by wyjsc: ")
    for i in user_input:
        if i not in '0123456789qQ':
            print('Podaj poprawny numer')
            break
    else:
        if user_input.lower() == 'q':
            print("Podsumowanie dzialania programu:\n")
            
            for num, tuple_num in enumerate(zip(nums_before, nums_after)):
                print("[Nr.{}] Wartosc: {}, Silnia: {}.".format(num +1, tuple_num[0], tuple_num[1]))
            exit()
        else:
            result = silnia(int(user_input))
            print("Silnia z {}, wynosi {}".format(int(user_input),result))
            nums_before.append(user_input)
            nums_after.append(result)


