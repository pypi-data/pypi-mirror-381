from typing_extensions import Callable, Awaitable, TypeVar
from dataclasses import dataclass
from datetime import datetime, timedelta

from trading_sdk.types import ApiError, UserError
from trading_sdk.wallet.withdrawal_methods import WithdrawalMethod, Network, WithdrawalMethods as WithdrawalMethodsTDK

from deribit.sdk.core import SdkMixin, wrap_exceptions

T = TypeVar('T')

def currency_network(currency: str) -> Network:
  match currency:
    case 'XRP':
      return 'XRP'
    case 'BNB':
      return 'BSC'
    case 'BTC':
      return 'BTC'
    case 'SOL':
      return 'SOL'
    case _:
      return 'ETH'

def cacher(ttl: timedelta = timedelta(seconds=10)):
  value = None
  last = None
  async def cached_fn(fn: Callable[[], Awaitable[T]]) -> T:
    nonlocal value, last
    if last is None or datetime.now() - last > ttl:
      value = await fn()
      last = datetime.now()
    return value # type: ignore

  return cached_fn

get_currencies_cached = cacher()

@dataclass
class WithdrawalMethods(WithdrawalMethodsTDK, SdkMixin):
  @wrap_exceptions
  async def withdrawal_methods(self, asset: str):
    r = await get_currencies_cached(self.client.get_currencies)
    if not 'result' in r:
      raise ApiError(r['error'])
    for c in r['result']:
      if c['currency'] == asset:
        return [WithdrawalMethod(
          network=currency_network(asset),
          fee=WithdrawalMethod.Fee(asset=asset, amount=fee) if (fee := c.get('withdrawal_fee')) else None,
        )]
    
    raise UserError(f'Currency {asset} not found')