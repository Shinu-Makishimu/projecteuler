import requests
from bs4 import BeautifulSoup as BS


def second():
    total = 0
    a, b = 1, 2

    while b <= 4000000:
        if b % 2 == 0:
            total += b
        a, b = b, a + b

    print(
        f"The sum of the even-valued terms in the Fibonacci sequence whose values do not exceed four million is {total}")


def fourth():
    def is_palindrome(n: int) -> bool:
        s = str(n)
        return s == s[::-1]

    largest_palindrome = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            product = i * j
            if is_palindrome(product) and product > largest_palindrome:
                largest_palindrome = product

    print(f"The largest palindrome made from the product of two 3-digit numbers is {largest_palindrome}")


def sixth():
    sum_of_squares = 0
    sum = 0

    for i in range(1, 101):
        sum_of_squares += i ** 2
        sum += i

    difference = sum_of_squares - sum ** 2

    print(
        f"The difference between the sum of the squares of the first one hundred natural numbers and the square of the sum is {difference}")


def eighth():
    def get_number() -> str:
        pars = requests.get('https://projecteuler.net/problem=8')
        soup = BS(pars.content, 'html.parser')
        for i in soup.find_all('p'):
            if len(i.text.strip()) > 1000:
                b = i.text.strip().replace("\n", "")
                return b

    number = get_number()
    greatest_product = 0
    n = 13
    for i in range(len(number) - n):
        product = 1
        for j in range(i, i + n):
            product *= int(number[j])
        if product > greatest_product:
            greatest_product = product

    print(f"Thirteen adjacent digits that have the greatest product {greatest_product}")


def tenth():
    def sieve(n) -> list[bool]:
        s = [True] * (n + 1)
        s[0] = s[1] = False
        for k in range(2, int(n ** 0.5) + 1):
            if s[k]:
                s[k * k::k] = [False] * len(s[k * k::k])
        return s

    primes = sieve(2000000)

    total_sum = 0
    for i in range(2, len(primes)):
        if primes[i]:
            total_sum += i
    print(f"Sum of all the primes below two million {total_sum}")


if __name__ == '__main__':
    second()
    fourth()
    sixth()
    eighth()
    tenth()
