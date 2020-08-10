import pandas as pd


def prob_given_treatment(data, treatment, outcome):
    temp = data[data[treatment] == 1]
    prob = temp[outcome].sum() / len(temp)
    print(f'{prob:.4f}')
    return prob


def weighted(data, strata):
    a1 = prob_given_treatment(data[data[strata] == 0], 'A', 'Y')
    a2 = prob_given_treatment(data[data[strata] == 1], 'A', 'Y')
    out = (a1 * len(data[data[strata] == 0]) / len(data)) + (a2 * len(data[data[strata] == 1]) / len(data))
    print(f'{out:.4f}')


if __name__ == '__main__':
    # 'A': received heart transplant -- treatment or not
    # 'Y': ouctome -- died or not
    # 'L': prognostic -- critical condition or not

    # df = pd.read_csv('table2.1.csv', sep=';')
    # prob_given_treatment(df, 'A', 'Y')
    # prob_given_treatment(df, 'A', 'Y')

    df2 = pd.read_csv('table2.2.csv', sep=';')
    # Causal risk ratio Pr[Ya=1 = 1]/Pr[Ya=0 = 1]
    weighted(df2, 'L')


