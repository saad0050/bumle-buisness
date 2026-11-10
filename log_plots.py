import matplotlib.pyplot as plt


def plot_scatter(table, x_column, y_column):
    """Viser et scatter-plot af to kolonner mod hinanden."""
    plt.figure(figsize=(10, 6))
    # alpha gør prikkerne gennemsigtige, så man kan se, hvor mange der ligger oven på hinanden
    plt.scatter(table[x_column], table[y_column], alpha=0.5)
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.title(f"{y_column} mod {x_column}")
    plt.xticks(rotation=45)   # drej teksten, så den kan læses
    plt.tight_layout()
    plt.show()


def plot_bar(counts, title, x_label, y_label):
    """Viser et søjlediagram. counts er en pandas-serie med antal pr. kategori."""
    plt.figure(figsize=(12, 6))
    plt.bar(counts.index.astype(str), counts.values)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.xticks(rotation=90)   # drej teksten, så den kan læses
    plt.tight_layout()
    plt.show()