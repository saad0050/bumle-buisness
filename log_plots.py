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