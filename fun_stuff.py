from datetime import datetime
from matplotlib import pyplot as plt

def index_lookup(header_row):
    """Finds the index containing the given name and returns
    the index value.
    """
    keywords = ['DATE', 'TMIN', 'TMAX']
    indicies = []
    indicies = [i for key in keywords
                for i, column_header in enumerate(header_row)
                if column_header == key]
    return indicies

def gather_temperatures(reader, indicies):
    """Collects the dates and temperatures in the reader from the given 
    indicies and stores them into a dictionary to return.
    """
    data = {
        'dates': [],
        'lows': [],
        'highs': [],
        }
    for row in reader:
        date = datetime.strptime(row[indicies[0]], '%Y-%m-%d')
        try:
            low_temperature = int(row[indicies[1]])
            high_temperature = int(row[indicies[2]])
        except ValueError:
            print("Missing value.")
        else:
            data['dates'].append(date)
            data['lows'].append(low_temperature)
            data['highs'].append(high_temperature)
    return data

def show_figure(data1, data2):
    """Generates the figure."""

    plt.style.use('seaborn-v0_8')
    fig, ax = plt.subplots()
    ax.plot(data1['dates'], data1['lows'], color='red', alpha=0.5)
    ax.plot(data1['dates'], data1['highs'], color='blue', alpha=0.5)
    ax.plot(data2['dates'], data2['lows'], color='red', alpha=0.5)
    ax.plot(data2['dates'], data2['highs'], color='red', alpha=0.5)
    ax.fill_between(data1['dates'], data1['lows'], data1['highs'],
                    facecolor='blue', alpha=0.1)
    ax.fill_between(data2['dates'], data2['lows'], data2['highs'],
                    facecolor='blue', alpha=0.1)

    ax.set_title("Temperatures", fontsize=24)
    ax.set_xlabel('', fontsize=16)
    fig.autofmt_xdate()
    ax.set_ylabel("Temperature (F)", fontsize=16)
    ax.tick_params(labelsize=16)

    plt.show()
