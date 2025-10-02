import pandas as pd
from finlab import config
from finlab.ml.utils import resampler


def align_to_feature(index: pd.Index, df: pd.DataFrame) -> pd.Series:
    ret: pd.Series = df.unstack().swaplevel(0, 1).reindex(index)
    ret.index = ret.index.set_names(['datetime', 'instrument'])
    return ret

def daytrading_percentage(index: pd.Index, **kwargs) -> pd.Series:
    """Calculate the percentage change of market prices over a given period.

    Args:
        index (pd.Index): A multi-level index of datetime and instrument.
        resample (Optional[str]): The resample frequency for the output data. Defaults to None.
        period (int): The number of periods to calculate the percentage change over. Defaults to 1.
        trade_at_price (str): The price for execution. Defaults to `close`.
        **kwargs: Additional arguments to be passed to the resampler function.

    Returns:
        pd.Series: A pd.Series containing the percentage change of stock prices.

    """

    market = config.get_market()
    assert market is not None

    adj_close = market.get_price('close', adj=True).shift(-1)
    adj_open = market.get_price('open', adj=True).shift(-1)
    uadj_close = resampler(adj_close, 'D', **kwargs)
    uadj_open = resampler(adj_open, 'D', **kwargs)

    ret = (uadj_close / uadj_open) - 1
    return align_to_feature(index, ret)

def return_percentage(index: pd.Index, resample=None, period=1, trade_at_price='close', bfill=False, **kwargs) -> pd.Series:

    """Calculate the percentage change of market prices over a given period.

    Args:
        index (pd.Index): A multi-level index of datetime and instrument.
        resample (Optional[str]): The resample frequency for the output data. Defaults to None.
        period (int): The number of periods to calculate the percentage change over. Defaults to 1.
        trade_at_price (str): The price for execution. Defaults to `close`.
        **kwargs: Additional arguments to be passed to the resampler function.

    Returns:
        pd.Series: A pd.Series containing the percentage change of stock prices.

    """

    market = config.get_market()
    assert market is not None

    adj = market.get_price(trade_at_price, adj=True).shift(-1)

    if bfill:
        not_listed = adj.notna().cumsum() == 0
        removed = (adj.notna()[::-1].cumsum() == 0)[::-1]
        adj = adj.bfill().where(~not_listed & ~removed)

    uadj = resampler(adj, resample, **kwargs)
    ret = (uadj.shift(-period) / uadj) - 1
    return align_to_feature(index, ret)


def maximum_adverse_excursion(index: pd.Index, period=1, trade_at_price='close') -> pd.Series:

    """Calculate the maximum adverse excursion of market prices over a given period.

    Args:
        index (pd.Index): A multi-level index of datetime and instrument.
        resample (Optional[str]): The resample frequency for the output data. Defaults to None.
        period (int): The number of periods to calculate the percentage change over. Defaults to 1.
        trade_at_price (str): The price for execution. Defaults to `close`.
        **kwargs: Additional arguments to be passed to the resampler function.

    Returns:
        pd.Series: A pd.Series containing the percentage change of stock prices.

    """

    market = config.get_market()
    assert market is not None
    adj = market.get_price(trade_at_price, adj=True).shift(-1)
    ret = adj.shift(-period).rolling(period).min() / adj - 1
    ret = ret.reindex(index.levels[0], method='ffill')
    return align_to_feature(index, ret)


def maximum_favorable_excursion(index: pd.Index, period=1, trade_at_price='close') -> pd.Series:

    """Calculate the maximum favorable excursion of market prices over a given period.

    Args:
        index (pd.Index): A multi-level index of datetime and instrument.
        resample (Optional[str]): The resample frequency for the output data. Defaults to None.
        period (int): The number of periods to calculate the percentage change over. Defaults to 1.
        trade_at_price (str): The price for execution. Defaults to `close`.
        **kwargs: Additional arguments to be passed to the resampler function.

    Returns:
        pd.Series: A pd.Series containing the percentage change of stock prices.

    """

    market = config.get_market()
    assert market is not None
    adj = market.get_price(trade_at_price, adj=True).shift(-1)
    ret = adj.shift(-period).rolling(period).max() / adj - 1
    ret = ret.reindex(index.levels[0], method='ffill')
    return align_to_feature(index, ret)


def excess_over_median(index: pd.Index, resample=None, period=1, trade_at_price='close', **kwargs) -> pd.Series:

    """Calculate the excess over median of market prices over a given period.

    Args:
        index (pd.Index): A multi-level index of datetime and instrument.
        resample (Optional[str]): The resample frequency for the output data. Defaults to None.
        period (int): The number of periods to calculate the percentage change over. Defaults to 1.
        trade_at_price (str): The price for execution. Defaults to `close`.
        **kwargs: Additional arguments to be passed to the resampler function.

    Returns:
        pd.Series: A pd.Series containing the percentage change of stock prices.

    """

    market = config.get_market()
    adj = market.get_price(trade_at_price, adj=True).shift(-1)
    uadj = resampler(adj, resample, **kwargs)
    ret = (uadj.shift(-period) / uadj) - 1
    ret = ret.subtract(ret.median(axis=1), axis=0)
    return align_to_feature(index, ret)


def excess_over_mean(index: pd.Index, resample=None, period=1, trade_at_price='close', **kwargs) -> pd.Series:

    """Calculate the excess over mean of market prices over a given period.

    Args:
        index (pd.Index): A multi-level index of datetime and instrument.
        resample (Optional[str]): The resample frequency for the output data. Defaults to None.
        period (int): The number of periods to calculate the percentage change over. Defaults to 1.
        trade_at_price (str): The price for execution. Defaults to `close`.
        **kwargs: Additional arguments to be passed to the resampler function.

    Returns:
        pd.Series: A pd.Series containing the percentage change of stock prices.

    """
    market = config.get_market()
    adj = market.get_price(trade_at_price, adj=True).shift(-1)
    uadj = resampler(adj, resample, **kwargs)
    ret = (uadj.shift(-period) / uadj) - 1
    ret = ret.subtract(ret.mean(axis=1), axis=0)
    return align_to_feature(index, ret)
