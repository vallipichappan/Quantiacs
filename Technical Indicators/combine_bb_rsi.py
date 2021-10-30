import numpy as np
from scipy.signal import lfilter

def mySettings():

    settings = {}
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
    settings['beginInSample'] = '20210101'
    settings['endInSample'] = '20210331'
    settings['lookback'] = 20
    settings['threshold']=0.2
    #threshold = 0.418 -> 0.2594
    return settings


def myTradingSystem(DATE, OPEN, HIGH, LOW, CLOSE, settings):
    period1 = 14
    nMarkets = len(settings['markets'])
    
    data =  np.zeros((1, nMarkets), dtype=np.float)

##    -----Bollinger Bands------
    def bollingerBands(a, n=20):
        sma = np.nansum(a[-n:]) / n 
        std = np.std(a[-n:], ddof=1) #finding standard deviation -> measure of volatility
        return sma, sma + 2 * std, sma - 2 * std
    
    threshold=settings['threshold']
    for market in range(nMarkets):
        rsi1=RSI(CLOSE[:, market], period1)
        sma, upperBand, lowerBand=bollingerBands(CLOSE[:, market])
        currentPrice = CLOSE[-1, market]

        if currentPrice >= upperBand + (upperBand-lowerBand)*threshold and rsi1>70:
                data[0, market] = -1

        elif currentPrice <= lowerBand - (upperBand - lowerBand)*threshold and rsi1<30:
                data[0,market]= 1
                
    return data, settings   
    #70->overbought, 30->oversold

def RSI(CLOSE,period):
    closeMom = CLOSE[1:]- CLOSE[:-1]   
    upPosition = np.where(closeMom >= 0)
    downPosition = np.where(closeMom < 0)

    upMoves = closeMom.copy()
    upMoves[downPosition] = 0

    downMoves = np.abs(closeMom.copy())
    downMoves[upPosition] = 0

    out = 100 - 100 / (1 + (np.mean(upMoves[-(period+1):], axis=0) / np.mean(downMoves[-(period+1):], axis=0)))
     #RSI formula = 100 - 100/(1+(avg gain/avg loss))
    #avg gain/loss -> average percentage gain or loss during a look-back period
    
    return out

# Evaluate trading system defined in current file.
if __name__ == '__main__':
    import quantiacsToolbox
    results = quantiacsToolbox.runts(__file__)
