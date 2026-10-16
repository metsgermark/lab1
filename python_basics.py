"""Заготовки задач на базовый Python."""

from grader_contracts.python_basics import PositiveIntegerInput, TextInput, VectorPairInput


def count_vowels(data: TextInput) -> int:
    text = data.value
    return sum(1 for i in text.lower() if i in 'aeiou')

def has_unique_characters(data: TextInput) -> bool:
    text = data.value
    return len(set(text)) == len(text)


def count_one_bits(data: PositiveIntegerInput) -> int:
    number = data.value
    if number<0:
        return 'число отрицательное'
    return bin(number).count('1')


def multiplicative_persistence(data: PositiveIntegerInput) -> int:
    number = data.value
    count = 0
    while number >= 10:
        product = 1
        for digit in str(number):
            product *= int(digit)
        number = product
        count += 1
    return count


def mse(data: VectorPairInput) -> float:
    predicted, expected = data.predicted, data.expected
    n = len(predicted)
    return sum((p - e) ** 2 for p, e in zip(predicted, expected)) / n


def prime_factorization(data: PositiveIntegerInput) -> str:
    number = data.value
    factors = {}
    d = 2
    while d * d <= number:
        while number % d == 0:
            factors[d] = factors.get(d, 0) + 1
            number //= d
        d += 1
    if number > 1:
        factors[number] = factors.get(number, 0) + 1

    parts = []
    for base in sorted(factors):
        exp = factors[base]
        if exp == 1:
            parts.append(f"({base})")
        else:
            parts.append(f"({base}**{exp})")
    return ''.join(parts)

def pyramid(data: PositiveIntegerInput) -> int | str:
    cube_count = data.value
    total = 0
    k = 0
    while total < cube_count:
        k += 1
        total += k * k
    if total == cube_count:
        return k
    return "It is impossible"


def is_balanced_number(data: PositiveIntegerInput) -> bool:
    number = data.value
    s = str(number)
    length = len(s)
    mid = length // 2
    if length % 2 == 0:
        left = s[:mid - 1]
        right = s[mid + 1:]
    else:
        left = s[:mid]
        right = s[mid + 1:]
    return sum(int(d) for d in left) == sum(int(d) for d in right)

# проверка функции count_vowels 

#print (count_vowels(TextInput('abcdefghi'))) = 3
#print (count_vowels(TextInput('ABFsaifpacx9hio'))) = 6
#print (count_vowels(TextInput(''))) = 0
#print (count_vowels(TextInput('bgbgbgplt'))) = 0

# проверка функции has_unique_characters

#print (has_unique_characters(TextInput('bgbgbgplt'))) = False
#print (has_unique_characters(TextInput('Dd'))) = True
#print (has_unique_characters(TextInput(''))) = True
#print (has_unique_characters(TextInput('@#$%^ads'))) = True

# проверка функции count_one_bits

#print(count_one_bits(PositiveIntegerInput(10))) = 2
#print(count_one_bits(PositiveIntegerInput(-10))) = число отрицательное

# проверка функции multiplicative_persistence

#print(multiplicative_persistence(PositiveIntegerInput(39))) = 3 
#print(multiplicative_persistence(PositiveIntegerInput(4))) = 0
#print(multiplicative_persistence(PositiveIntegerInput(999))) = 4

# проверка функции mse

#print(mse(VectorPairInput([1,2,3], [1,2,3]))) = 0.0
#print(mse(VectorPairInput([5], [3]))) = 4.0
#print(mse(VectorPairInput([-1,-2], [1,2]))) = 10.0

# проверка функции prime_factorization

#print(prime_factorization(PositiveIntegerInput(86240))) = (2**5)(5)(7**2)(11)

# проверка функции pyramid

#print(pyramid(PositiveIntegerInput(14))) = 3
#print(pyramid(PositiveIntegerInput(10))) = It is impossible

# проверка функции is_balanced_number

#print(is_balanced_number(PositiveIntegerInput(1234006))) = True
#print(is_balanced_number(PositiveIntegerInput(123456))) = False
