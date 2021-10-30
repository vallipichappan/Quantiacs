# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 20:07:00 2021

@author: valli
"""


import numpy as np
from statsmodels.tsa.api import Holt

def myTradingSystem(DATE, OPEN, HIGH, LOW, CLOSE, VOL, OI, P, R, RINFO, exposure, equity, settings):
    nMarkets=len(settings['markets'])
    threshold=settings['threshold']

    pos=np.zeros(nMarkets, dtype=np.float)

    for market in range(nMarkets):
        # double exponential
        # fine tuned
        
        reg = Holt(np.asarray(CLOSE[:, market])).fit(smoothing_level = 0.1,smoothing_slope=0.4)    
        trend = reg.forecast(1)

        if abs(trend[0])<threshold:
            trend[0] = 0

        pos[market]=np.sign(trend)

    return pos, settings


def mySettings():
    """ Define your trading system settings here """

    settings = {}

    # Futures Contracts
    settings['markets'] = ['CASH', 'F_AD', 'F_AE', 'F_AH', 'F_AX', 'F_BC', 'F_BG', 'F_BO', 'F_BP', 'F_C',  'F_CA',
                           'F_CC', 'F_CD', 'F_CF', 'F_CL', 'F_CT', 'F_DL', 'F_DM', 'F_DT', 'F_DX', 'F_DZ', 'F_EB',
                           'F_EC', 'F_ED', 'F_ES', 'F_F',  'F_FB', 'F_FC', 'F_FL', 'F_FM', 'F_FP', 'F_FV', 'F_FY',
                           'F_GC', 'F_GD', 'F_GS', 'F_GX', 'F_HG', 'F_HO', 'F_HP', 'F_JY', 'F_KC', 'F_LB', 'F_LC',
                           'F_LN', 'F_LQ', 'F_LR', 'F_LU', 'F_LX', 'F_MD', 'F_MP', 'F_ND', 'F_NG', 'F_NQ', 'F_NR',
                           'F_NY', 'F_O',  'F_OJ', 'F_PA', 'F_PL', 'F_PQ', 'F_RB', 'F_RF', 'F_RP', 'F_RR', 'F_RU',
                           'F_RY', 'F_S',  'F_SB', 'F_SF', 'F_SH', 'F_SI', 'F_SM', 'F_SS', 'F_SX', 'F_TR', 'F_TU',
                           'F_TY', 'F_UB', 'F_US', 'F_UZ', 'F_VF', 'F_VT', 'F_VW', 'F_W', 'F_XX', 'F_YM', 'F_VX',
                           'F_ZQ']

    settings['lookback']= 20
    settings['budget']= 10**6
    settings['slippage']= 0.05


    settings['threshold'] = 0.2
    settings['dimension'] = 3
    settings['beginInSample'] = '20210101'
    settings['endInSample']   = '20210331'
    return settings


# Evaluate trading system defined in current file.
if __name__ == '__main__':
    import quantiacsToolbox
    results = quantiacsToolbox.runts(__file__)