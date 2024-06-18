import random

def repetitive_digits(digits,result_number):
    count = [0] * 10
    res = 0
    
    for i in range(digits):
        n = result_number % 10
        count[n] += 1
        result_number = result_number // 10
        
    for i in range(10):
        if count[i] > 1:
            res += 1
            print('Number of Repetitve Digits : ',count[i])
            
    if res > 0:
        print('Repetitive Digits are present in the result number!')
        return(True)
    else:
        print('No Repetitive Digits found in the result number!')
        return(False)


while True:
    digits = int(input('Enter the number of digits : '))
    guess_number_count = 0
    guess_number = 0
    guess_count = int(input('Enter the maximum number of guesses allowed : '))
    result_number = random.randint(10**(digits - 1) ,10**(digits) - 1)

    while(True):
        if repetitive_digits(digits,result_number) == True:
            break
        else:
            while guess_number_count < guess_count:

                guess_number = int(input('Enter Guess Number : '))
                guess_number_count += 1

                c1 = [0] * digits
                c2 = [0] * digits

                n1 = result_number
                n2 = guess_number

                fermi = 0
                pico = 0
                bagels = 0

                for i in range(digits):
                    c1[digits - (i + 1)] = n1 % 10
                    n1 = n1 // 10

                for i in range(digits):
                    c2[digits - (i + 1)] = n2 % 10
                    n2 = n2 // 10

                for i in c1:
                    if i not in c2:
                        bagels += 1

                if bagels < digits:
                    for i in range(digits):
                        for j in range(digits):
                            if (c1[i] == c2[j]) and (i == j):
                                fermi += 1
                            elif (c1[i] == c2[j]) and (i != j):
                                pico += 1

                if bagels == digits:
                    print('Guess Number :',guess_number,'\tResult : ','Bagels')
                elif fermi == digits:
                    print('Guess Number :',guess_number,'\tResult : ','Fermi '*fermi,'Pico '*pico)
                    break
                else:
                    print('Guess Number :',guess_number,'\tResult : ','Fermi '*fermi,'Pico '*pico)

        if fermi == digits:
            break
        else:
            print('Maximum Number of Guesses reached!')
            break

    if fermi == digits:
        print('Number of Guess Count Taken : ',guess_number_count)
        print('Result Number : Guess Number : ',guess_number)
        print('You Win!')
        break
    else:
        print('Could not guess the Result Number!')
        print('Result Number : ',result_number)
        print('You Lose!')
        break

print('GAME OVER!')