import pandas as pd

def get_power(df):
    val_counts = df.apply(pd.Series.value_counts)
    gamma = int(''.join(map(str, list(val_counts.idxmax()))), 2)
    epsilon = int(''.join(map(str, list(val_counts.idxmin()))), 2)
    return gamma * epsilon

if __name__ == "__main__":

    # Read in the input ... always called `input`
    # Customize depending on the type of data structure required

    # Day 03: Binary but treat as pandas columns of ints
    df = pd.read_csv('input', dtype=object, header=None)
    df = df[0].str.split('',expand=True)
    df = df.drop(columns=[0, 13])
    df = df.astype(int)

    print(f'Power Consumption is: {get_power(df)}')
