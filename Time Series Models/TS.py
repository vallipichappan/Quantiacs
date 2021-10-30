from statsmodels.graphics.tsaplots import plot_pacf
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from statsmodels.tsa.stattools import adfuller
import matplotlib.pyplot as plt
from tqdm import tqdm_notebook
import numpy as np
import pandas as pd
from itertools import product
import warnings
warnings.filterwarnings('ignore')
# %matplotlib inline

data = pd.read_csv('C:/Users/valli/tickerData/F_AD.txt', sep=",", header=None)
print(data)
data.columns = ["DATE", "OPEN", "HIGH", "LOW", "CLOSE", "VOL", "OI", "P", "R", "RINFO"]
#data = data.CLOSE.fillna(value=0,inplace=True)
print(len(data))

plt.figure(figsize=[15, 7.5]); # Set dimensions for figure
plt.plot(data['DATE'], data['CLOSE'])
plt.title('Quarterly EPS for Johnson & Johnson')
plt.ylabel('EPS per share ($)')
plt.xlabel('Date')
plt.xticks(rotation=90)
plt.grid(True)
plt.show()
