import pandas as pd
import matplotlib.pyplot as plt
import mplcursors


def main():
    # Create sample data
    data = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    additional_data = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

    # Create lag plot
    fig, ax = plt.subplots()
    scatter = ax.scatter(data[:-1], data[1:])

    # Annotate each point with the corresponding additional data
    for i, txt in enumerate(additional_data[1:]):  # Exclude the first element since there's no previous data
        ax.annotate(txt, (data[i], data[i+1]))

    # Add tooltips using mplcursors
    mplcursors.cursor(hover=True).connect("add", lambda sel: sel.annotation.set_text(additional_data[sel.target.index]))

    # Display the plot
    plt.title('Example Lag Plot with Hover Tooltips')
    plt.xlabel('Current Value')
    plt.ylabel('Previous Value')
    plt.show()


if __name__ == '__main__':
    main()
