from main import run_instance
import os, csv

SIZES = [3, 4, 5, 6, 7, 8]
DIFFICULTIES = {'easy': 10, 'medium': 20, 'hard': 50}
REPETITIONS = 100
OUTPUT_DIR = 'results'
FIELD_NAMES = ['n', 'k', 'difficulty', 'solved', 'cost', 'time']

os.makedirs(OUTPUT_DIR, exist_ok=True)

def benchmark():
    for n in SIZES:
        with open(os.path.join(OUTPUT_DIR, f'{n}x{n}_results.csv'), 'w', newline='') as csvfile:
            csv_writer = csv.DictWriter(csvfile, fieldnames=FIELD_NAMES, extrasaction='ignore') 
            csv_writer.writeheader()
            for difficulty, k in DIFFICULTIES.items():
                for i in range(REPETITIONS):
                    result = run_instance(n, k)
                    result['difficulty'] = difficulty
                    csv_writer.writerow(result)
                    print(f"Completed: n={n}, difficulty={difficulty}, repetition={i+1}/{REPETITIONS}")


if __name__ == "__main__":
    benchmark()