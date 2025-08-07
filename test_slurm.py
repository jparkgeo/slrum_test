import multiprocessing as mp
import time
import os

# 제곱 연산을 하는 함수
def square(number):

    time.sleep(1)
    return number * number

if __name__ == '__main__':
    numbers = range(1, 10)

    print("--- Pool과 map을 사용한 병렬 처리 시작 ---")
    start_time = time.time()
    
    pool = mp.Pool(mp.cpu_count())  # 시스템의 CPU 코어 수를 자동으로 가져옵니다.
    print(f"Multiprocessing started with {pool._processes} processes.")
    results = pool.map(square, numbers)

    end_time = time.time()
    
    print("\n--- 결과 ---")
    print(f"병렬 처리 결과: {results}")
    print(f"총 소요 시간: {end_time - start_time:.2f}초")
    print("--- 병렬 처리 종료 ---\n")