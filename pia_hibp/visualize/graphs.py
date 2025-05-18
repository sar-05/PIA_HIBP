import matplotlib.pyplot as plt

def create_pie_graph(title, data_dict):
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_title(title)
    labels = data_dict.keys()
    sizes = data_dict.values()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%')
    return fig

def rates_graphs(path, name, rates_df):
    rates_df = rates_df.sort_values('Breach Rate (%)', ascending=False)
    labels = rates_df['Group']
    heights = rates_df['Breach Rate (%)']
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(labels, heights)
    ax.set_title(f"Tasa de Compromiso por {name}")
    plt.savefig(f"{path}/{name}", dpi=300)
    plt.close(fig)
