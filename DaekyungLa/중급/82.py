import sys

p, q = map(int, sys.stdin.readline().split())

def fraction_to_decimal(p, q):
    integer_part = p // q
    remainder = p % q
    if remainder == 0:
        return str(integer_part)
    
    result = str(integer_part) + "."
    remainder_map = {}
    decimal_part = ""
    index = 0

    while remainder and remainder not in remainder_map:
        remainder_map[remainder] = index
        remainder *= 10
        decimal_digit = remainder // q
        decimal_part += str(decimal_digit)
        remainder = remainder % q
        index += 1

    if remainder == 0:
        return result + decimal_part.rstrip('0')

    repeat_start = remainder_map[remainder]
    non_repeat_part = decimal_part[:repeat_start]
    repeat_part = decimal_part[repeat_start:]
    return result + non_repeat_part + "{" + repeat_part + "}"

print(fraction_to_decimal(p, q))
