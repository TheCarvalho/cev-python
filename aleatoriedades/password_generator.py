from random import SystemRandom
import string

abc = string.ascii_letters
numbers = string.digits
punctuation = string.punctuation

tamanho = int(input('Tamanho da senha: '))

ok = abc + punctuation + numbers

input(
    ''.join(
        SystemRandom().choices(
            ok, k=tamanho
        )
    )
)

# python -c "import string as s;from random import SystemRandom as sr;print(''.join(sr().choices(s.ascii_letters + s.punctuation +s.digits,k=12)))"