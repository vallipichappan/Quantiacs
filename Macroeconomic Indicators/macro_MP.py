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
    settings['lookback'] = 50
    #settings['threshold']=0.2
    settings['dimension'] = 3

    #train set
    #settings['beginInSample'] = '19900101'
    #settings['endInSample'] = '20201231'
    #test set
    settings['beginInSample'] = '20210101'
    settings['endInSample'] = '20210331'


    return settings


def myTradingSystem(DATE, OPEN, HIGH, LOW, CLOSE, USA_MP, settings):
    nMarkets = len(settings['markets'])
    pos = np.zeros(nMarkets, dtype=np.float)
    data = USA_MP
    array = []
    for i in data:
        array.append(i[0])
    min_x = min(array)
    max_x = max(array)
    normalized_weights = []
    for x in array:
        normalized_weights.append(2*((x-min_x)/(max_x-min_x))-1)
    normalized_weights = np.array(normalized_weights)
    
    for market in range(nMarkets):
        if normalized_weights[-1] > 0:
            pos[market] = 1
        elif normalized_weights[-1] < 0:
            pos[market] = -1
    return pos, settings
        

    
##    dimension = settings['dimension']
##    lookback = settings['lookback']
##    threshold = settings['threshold']
##    poly = PolynomialFeatures(degree=dimension)
##
##   
##    diff = []
##    for i in range(1, 504):
##        diff.append(data[i]-data[i-1])
##    #print(np.sign(diff))
##    macro_indicator = np.sign(diff[-1])
##    print(macro_indicator)
##   
##    for market in range(nMarkets):
##        if diff > 0:
##            pos[market] = 1
##        elif diff < 0:
##            pos[market] = -1
##
##    return pos, settings

    #return pos, settings

# Evaluate trading system defined in current file.
if __name__ == '__main__':
    import quantiacsToolbox
    results = quantiacsToolbox.runts(__file__)
