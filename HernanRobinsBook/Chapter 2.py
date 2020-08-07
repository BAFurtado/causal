import pandas as pd


def prob_given_treatment(data, treatment, outcome, group):
    temp = data[data[treatment] == group]
    prob = temp[outcome].sum() / len(temp)
    print(f'{prob:.4f}')
    return temp


if __name__ == '__main__':
    # 'A': received heart transplant -- treatment or not
    # 'Y': ouctome -- died or not
    # 'L': prognostic -- critical condition or not
    df = pd.read_csv('table2.1.csv', sep=';')
    prob_given_treatment(df, 'A', 'Y', 1)
    prob_given_treatment(df, 'A', 'Y', 0)

    df2 = pd.read_csv('table2.2.csv', sep=';')
    # Causal risk ration Pr[Ya=1 = 1]/Pr[Ya=0 = 1]
