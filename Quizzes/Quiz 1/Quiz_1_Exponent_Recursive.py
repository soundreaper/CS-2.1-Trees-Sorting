# Recursive Function to take power
def raise_power(base, exponent):
    # Special case where exponent is 0
    if exponent == 0:
        return 1

    elif exponent == 1:
        return base

    elif exponent > 1:
        return base * raise_power(base, exponent - 1)

# Tests that cover all edge cases
def test_sort_on_empty_list():
    assert raise_power(4,2) == 16
    assert raise_power(2,2) == 4
    assert raise_power(2,8) == 256
    assert raise_power(10,10) == 10000000000
    assert raise_power(0,0) == 1