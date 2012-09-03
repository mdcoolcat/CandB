# bits manipulation
# most from CareerCup Ch1

from test_helper import test

def is_power_of_two(n):
    if n < 0:
        return False
    return (n & (n - 1)) == 0

def main():
    test_false = [-3, 43, 10000, pow(3, 20)]
    test_true = [0, 4, 64, 1024, pow(2, 20)]
    for n in test_false:
        test(is_power_of_two(n), False)

    for n in test_true:
        test(is_power_of_two(n), True)

if __name__ == '__main__':
    main()
