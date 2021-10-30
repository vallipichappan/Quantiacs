import numpy as np
import pandas as pd

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM

def createAndTrain(DATE, CLOSE, settings):
    lst_dates = DATE.tolist()
    lst_dates = lst_dates[1:]
    price_data = CLOSE[1:, :]
    average = np.average(price_data)
    std_dev = np.std(price_data)
    price_data = (price_data - average) / std_dev

    return_data = (CLOSE[1:, :] - CLOSE[:-1, :]) / CLOSE[:- 1, :]

    trainX = np.reshape(price_data, (price_data.shape[0], price_data.shape[1], 1))
    trainY = return_data

    nMarkets = len(settings['markets'])
    model = Sequential()
    model.add(LSTM(4, input_shape = (nMarkets, 1)))
    model.add(Dense(1))
    model.compile(loss = 'mean_squared_error', optimizer='adam')
    model.fit(trainX, trainY, epochs=50, batch_size=1, verbose=2)

    settings['mean'] = average
    settings['std'] = std_dev
    settings['model'] = model
    return

def myTradingSystem(DATE, CLOSE, exposure, equity, settings):
    lookBack = settings['lookback']
    if 'model' not in settings:
        createAndTrain(DATE[:lookBack - 2], CLOSE[:lookBack - 2], settings)

    model = settings['model']
    average = settings['mean']
    std_dev = settings['std']

    testX = (CLOSE[lookBack - 1:] - average) / std_dev
    testX = np.reshape(testX, (testX.shape[0], testX.shape[1], 1))
    testY = model.predict(testX)

    newDelta = testY[0]
    nMarkets = CLOSE.shape[1]
    pos = np.ones((1, nMarkets))

    if newDelta >= 0:
        pos[0] = 1
    else:
        pos[0] = -1
    
    return pos, settings

def mySettings():
    settings = {}

    # Futures Contracts
    settings['markets'] = ['CASH', 'F_AD', 'F_AE', 'F_AH', 'F_AX', 'F_BC', 'F_BG', 'F_BO', 'F_BP', 'F_C',  'F_CA',
                           'F_CC', 'F_CD', 'F_CF', 'F_CL', 'F_CT', 'F_DL', 'F_DM', 'F_DT', 'F_DX', 'F_DZ', 'F_EB',
                           'F_EC', 'F_ED', 'F_ES', 'F_F',  'F_FB', 'F_FC', 'F_FL', 'F_FM', 'F_FP', 'F_FV', 'F_FY',
                           'F_GC', 'F_GD', 'F_GS', 'F_GX', 'F_HG', 'F_HO', 'F_HP', 'F_JY', 'F_KC', 'F_LB', 'F_LC',
                           'F_LN', 'F_LQ', 'F_LR', 'F_LU', 'F_LX', 'F_MD', 'F_MP', 'F_ND', 'F_NG', 'F_NQ', 'F_NR',
                           'F_NY', 'F_O',  'F_OJ', 'F_PA', 'F_PL', 'F_PQ', 'F_RB', 'F_RF', 'F_RP', 'F_RR', 'F_RU',
                           'F_RY', 'F_S',  'F_SB', 'F_SF', 'F_SH', 'F_SI', 'F_SM', 'F_SS', 'F_SX', 'F_TR', 'F_TU',
                           'F_TY', 'F_UB', 'F_US', 'F_UZ', 'F_VF', 'F_VT', 'F_VW', 'F_VX',  'F_W', 'F_XX', 'F_YM',
                           'F_ZQ']   
    settings['slippage'] = 0.05
    settings['budget'] = 1000000
    settings['lookback'] = 50
    settings['beginInSample'] = '20210101'
    settings['endInSample'] = '20210331'

    return settings

if __name__ == '__main__':
    import quantiacsToolbox

    np.random.seed(98274534)

    results = quantiacsToolbox.runts(__file__)