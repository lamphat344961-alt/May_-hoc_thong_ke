import pandas as pd
from statsmodels.tsa.stattools import adfuller, kpss


def adf_test(x):
    indices = ['ADF: Test statistic', 'p value', '# of Lags', '# of Observations']

    test = adfuller(x, autolag='AIC') # Perform

    #Dickey-Fuller test

    results = pd.Series(test[:4], index=indices)
    
    for key, value in test[4].items():

        results[f'Critical Value ({key})'] = value
    if results[1] <= 0.05: # (p-value < 0.05 (alpha=5%))

        print("Reject the null hypothesis (H0), \nthe data is stationary.")

    else:

        print("Fail to reject the null hypothesis (HO), \nthe data is not stationary.")
    
    return results

def kpss_test(x):
    indices = ['KPSS: Test statistic', 'p value', '# of Lags']

    test = kpss(x)

    results = pd.Series(test[:3], index=indices)

    for key, value in test[3].items():

        results[f'Critical Value ({key})'] = value

    if results[1] <= 0.05: # (p-value < 0.05 (alpha=5%))

        print("Reject the null hypothesis (H0), \nthe data is not stationary.")

    else:

        print("Fail to reject the null hypothesis (HO), \nthe data is stationary.")


