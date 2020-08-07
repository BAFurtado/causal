import pandas as pd


def prob_given_treatment(data, group):
    temp = data[data.A == group]
    print(temp.Y.sum()/len(temp))


if __name__ == '__main__':
    df = pd.read_csv('table2.1.csv', sep=';')
    prob_given_treatment(df, 1)
    prob_given_treatment(df, 0)
