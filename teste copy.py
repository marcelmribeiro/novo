import argparse
import sys
from math import factorial as math_factorial
from typing import List

#!/usr/bin/env python3
# teste.py - simple Python test/demo script


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("n must be >= 0")
    return math_factorial(n)

def run_tests() -> None:
    # basic assertions
    assert is_prime(2) and is_prime(3) and not is_prime(1) and not is_prime(4)
    assert factorial(0) == 1 and factorial(5) == 120
    # quick sample list test
    nums: List[int] = [2, 3, 4, 5, 16, 17]
    primes = [n for n in nums if is_prime(n)]
    assert primes == [2, 3, 5, 17]
    print("All tests passed.")

def demo() -> None:
    print("Teste Python - demo")
    print("Primes under 20:", [n for n in range(2, 20) if is_prime(n)])
    print("5! =", factorial(5))

def main(argv=None):
    parser = argparse.ArgumentParser(description="Teste Python - simple utilities")
    parser.add_argument("--test", action="store_true", help="run self-tests")
    parser.add_argument("--demo", action="store_true", help="run demo output")
    parser.add_argument("--prime", type=int, help="check if a number is prime")
    parser.add_argument("--fact", type=int, help="compute factorial of a non-negative integer")
    args = parser.parse_args(argv)

    if args.test:
        run_tests()
        return

    if args.prime is not None:
        n = args.prime
        print(f"{n} is prime: {is_prime(n)}")
        return

    if args.fact is not None:
        try:
            print(f"{args.fact}! = {factorial(args.fact)}")
        except ValueError as e:
            print("Error:", e)
        return

    if args.demo or len(sys.argv) == 1:
        demo()

if __name__ == "__main__":
    main()