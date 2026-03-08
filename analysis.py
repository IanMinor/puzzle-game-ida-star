import pandas as pd
import matplotlib.pyplot as plt
import os
from benchmark import OUTPUT_DIR, SIZES

PLOTS_DIR = os.path.join(OUTPUT_DIR, 'plots')
DIFFICULTIES = ['easy', 'medium', 'hard']
COLORS = {'easy': 'green', 'medium': 'orange', 'hard': 'red'}


def load_data():
    data_frames = []
    for file in os.listdir(OUTPUT_DIR):
        if file.endswith('.csv'):
            df = pd.read_csv(os.path.join(OUTPUT_DIR, file))
            data_frames.append(df)
    return pd.concat(data_frames, ignore_index=True)


def calculate_stats(df):
    stats = df.groupby(['n', 'difficulty']).agg(
        avg_time=('time', 'mean'),
        median_time=('time', 'median'),
        solved_rate=('solved', 'mean'),
        total=('solved', 'count')
    ).reset_index()
    return stats


def plot_avg_time(stats):
    plt.figure(figsize=(10, 6))
    for difficulty in DIFFICULTIES:
        subset = stats[stats['difficulty'] == difficulty].sort_values('n')
        plt.plot(subset['n'], subset['avg_time'], label=difficulty,
                 marker='o', color=COLORS[difficulty])
    plt.xlabel('Board size (n)')
    plt.ylabel('Average time (s)')
    plt.title('IDA* Average Execution Time by Board Size')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.savefig(os.path.join(PLOTS_DIR, 'avg_time.png'), dpi=150)
    plt.close()
    print('Saved: avg_time.png')


def plot_solved_rate(stats):
    pivot = stats.pivot(index='n', columns='difficulty', values='solved_rate') * 100
    pivot = pivot[DIFFICULTIES]  # orden consistente
    pivot.plot(kind='bar', figsize=(10, 6), color=[COLORS[d] for d in DIFFICULTIES])
    plt.xlabel('Board size (n)')
    plt.ylabel('Solved rate (%)')
    plt.title('IDA* Solution Rate by Board Size and Difficulty')
    plt.xticks(rotation=0)
    plt.legend(title='Difficulty')
    plt.grid(True, axis='y', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.savefig(os.path.join(PLOTS_DIR, 'solved_rate.png'), dpi=150)
    plt.close()
    print('Saved: solved_rate.png')


def plot_boxplots(df):
    for difficulty in DIFFICULTIES:
        plt.figure(figsize=(10, 6))
        data = [df[(df['n'] == n) & (df['difficulty'] == difficulty)]['time'].values
                for n in SIZES]
        plt.boxplot(data, labels=SIZES, patch_artist=True,
                    boxprops=dict(facecolor=COLORS[difficulty], alpha=0.5))
        plt.xlabel('Board size (n)')
        plt.ylabel('Time (s)')
        plt.title(f'IDA* Time Distribution — {difficulty.capitalize()} (k={dict(easy=10, medium=20, hard=50)[difficulty]})')
        plt.grid(True, axis='y', linestyle='--', alpha=0.5)
        plt.savefig(os.path.join(PLOTS_DIR, f'boxplot_{difficulty}.png'), dpi=150)
        plt.close()
        print(f'Saved: boxplot_{difficulty}.png')


if __name__ == '__main__':
    os.makedirs(PLOTS_DIR, exist_ok=True)
    df = load_data()
    stats = calculate_stats(df)

    print('\n--- Statistics ---')
    print(stats.to_string(index=False))

    plot_avg_time(stats)
    plot_solved_rate(stats)
    plot_boxplots(df)