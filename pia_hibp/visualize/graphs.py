from matplotlib.cm import get_cmap
import matplotlib.pyplot as plt

def create_pie_graph(title, data_dict):
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_title(title)
    labels = data_dict.keys()
    sizes = data_dict.values()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%')
    return fig

def rates_graphs(path, name, rates_df):
    labels = rates_df['Group']
    heights = rates_df['Breach Rate (%)']
    plt.style.use('seaborn-v0_8-whitegrid')
    colormap = get_cmap('YlOrRd')
    colors = colormap(heights / 100) 
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(labels, heights,
    edgecolor='black', linewidth=1, color=colors)
    ax.set_ylabel('Tasa de Compromiso (%)',
    fontsize=12, fontweight='bold')
    ax.set_title(f"Tasa de Compromiso por {name}",
    fontsize=16, fontweight='bold', pad=20)
    plt.tight_layout()
    plt.savefig(f"{path}/{name}", dpi=300)
    plt.close(fig)
