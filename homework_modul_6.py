import numpy as np

def game_got_number(number: int = 1) -> int:
    min_value = 1
    max_value = 100
    secret_number = np.random.randint(min_value, max_value + 1)
    attempts = 0

    while True:
        guessed_number = np.random.randint(min_value, max_value + 1)
        attempts += 1

        if guessed_number == secret_number:
            print(f'Программа угадала/нашла число {secret_number} в {attempts} прыжка/прыжков.')
            return attempts
        elif guessed_number < secret_number:
            min_value = guessed_number + 1
        else:
            max_value = guessed_number - 1

if __name__ == "__main__":
    game_got_number()
    
# Любовь Скибина    
#программа использует метод бинарного поиска, чтобы угадать число за минимальное число попыток. 
#Она начинает с середины диапазона возможных значений и сужает его с каждой попыткой, исходя из ответа (больше или меньше) до тех пор, 
#пока не угадает число.

