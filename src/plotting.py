import matplotlib.pyplot as plt

def plot_cumulative_results(cumulative_dict):
    """
    Plot cumulative portfolio value for multiple strategies.
    """
    plt.figure(figsize=(14, 7))
    line_styles = ['-', '--', '-.']
    markers = ['o', 's', 'D']
    colors = ['blue', 'orange']

    for i, (label, series) in enumerate(cumulative_dict.items()):
        series_norm = series / series.iloc[0] * 100
        color = colors[0] if "Markowitz" in label else colors[1]
        linestyle = line_styles[i % len(line_styles)]
        marker = markers[i % len(markers)]
        plt.plot(series.index, series_norm, label=label, color=color, linestyle=linestyle,
                 marker=marker, markevery=len(series)//20)

    plt.title("Portfolio Value Comparison (Normalized to 100)")
    plt.xlabel("Date")
    plt.ylabel("Normalized Portfolio Value")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()
