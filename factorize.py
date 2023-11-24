import time
from multiprocessing import Pool, cpu_count


def factorize(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors


def synchronous_factorize(*digit):
    start_time = time.time()
    results = [factorize(num) for num in digit]
    end_time = time.time()
    print(f"Synchronous execution time: {end_time - start_time} seconds")
    return results


def parallel_factorize(*dig):
    start_time = time.time()
    cores_number = cpu_count()
    with Pool(cpu_count()) as pool:
        results = pool.map(factorize, dig)
    end_time = time.time()
    print(f"Parallel execution time: {end_time - start_time} seconds")
    print(f"Number of cores on your machine: {cores_number}")
    return results


if __name__ == "__main__":
    a, b, c, d = (128, 255, 99999, 10651060)

    # Synchronous version
    result_sync = synchronous_factorize(a, b, c, d)

    # Parallel version
    result_parallel = parallel_factorize(a, b, c, d)

    # Check correctness
    assert result_sync[0] == [1, 2, 4, 8, 16, 32, 64, 128]
    assert result_sync[1] == [1, 3, 5, 15, 17, 51, 85, 255]
    assert result_sync[2] == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert result_sync[3] == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790,
                              1065106, 1521580, 2130212, 2662765, 5325530, 10651060]

    assert result_sync == result_parallel
