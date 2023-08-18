def sito(n):
    numbers = [True for _ in range(n)]
    primers = []

    for i in range(len(numbers)): 
        if i <= 1:
            numbers[i] = False
        else:
            if numbers[i] == True:
                primers.append(i)
                for j in range(i, len(numbers) ,i):
                    numbers[j] = False
    return primers

# wyświetlanie wszystkich z zakresu
print(sito(1000))
print()


# sprawdzanie danej liczby
primers = sito(100)

if 12 in primers:
    print("Jest")
else: 
    print("Nie jest")