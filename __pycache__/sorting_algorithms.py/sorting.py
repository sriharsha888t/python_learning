from random import randint
from timeit import repeat

def run_sorting_algorithm(algorithm,array):
    setup_code = f"from__main__import{algorithm}"\
        if algorithm != "sorted"else ""

    stmt = f"{algorithm}({array})"

    times = repeat(setup = setup_code,stmt = stmt,repeat = 3,number = 10)

    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")

ARRAY_LENGTH = 10000


if __name__ == "__main__":
    array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]
    run_sorting_algorithm(algorithm="sorted", array=array)
