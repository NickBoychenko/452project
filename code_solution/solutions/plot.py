import pandas as pd
import matplotlib.pyplot as plt

def plot_graph_from_csv(csv_file, output_file):
    df = pd.read_csv(csv_file, header=None, names=['X', 'Y'])
    
    plt.figure(figsize=(8, 6))
    plt.plot(df['X'], df['Y'], marker='o', linestyle='-', linewidth=2)
    plt.title('Approximate Solution to String', fontsize=16)
    plt.xlabel('Edges', fontsize=14)
    plt.ylabel('Seconds', fontsize=14)
    plt.xscale('log')
    plt.grid(visible=True, which='both', linestyle='--', linewidth=0.5)
    plt.tight_layout()
    
    plt.savefig(output_file, format='png')
    print(f"Graph saved as {output_file}")

csv_file = 'approxStr.csv'
output_file = 'approxStr.png'
plot_graph_from_csv(csv_file, output_file)
