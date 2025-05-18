import matplotlib.pyplot as plt

def create_pie_graph(title, data_dict):
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_title(title)
    labels = data_dict.keys()
    sizes = data_dict.values()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%')
    return fig
