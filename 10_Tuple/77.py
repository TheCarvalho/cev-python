
# * Ex77: Create a program that has a tuple with several words (don't use accents). After that, you must show, for each word, which are its vowels.


tuple = (
    'APRENDER',
    'PROGRAMAR',
    'LINGUAGEM',
    'PYTHON',
    'GRATIS',
    'ESTUDAR',
    'PRATICAR',
    'TRABALHAR',
    'MERCADO',
    'PROGRAMADOR',
    'FUTURO'
)


for x in tuple:
    print(f'\nIn the word {x} we have:', end=' ')
    for i in range(0, len(x)):
        if x[i] in 'AEIOU':
            print((x[i]).lower(), end=' ')
