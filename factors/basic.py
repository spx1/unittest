from typing import List

def calc_factors(val: int) -> List[int]:
    factors = []
    for i in range(1,val+1):
        if val % i == 0:
            factors.append(i)
    return factors

