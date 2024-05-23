import pandas as pd
import matplotlib.pyplot as plt


def main():
    # Create sample data
    data = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    # Create lag plot
    pd.plotting.lag_plot(data)

    # Display the plot
    plt.title('Example Lag Plot')
    plt.show()


if __name__ == '__main__':
    main()
