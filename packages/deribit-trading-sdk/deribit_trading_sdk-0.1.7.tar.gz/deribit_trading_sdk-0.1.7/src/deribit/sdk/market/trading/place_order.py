from dataclasses import dataclass

from trading_sdk.types import fmt_num, ApiError
from trading_sdk.market.trading.place_order import (
  SpotPlaceOrder, PerpPlaceOrder, InversePerpPlaceOrder,
  Order as OrderTDK, ResponseModel, OrderState
)

from deribit.core import timestamp as ts
from deribit.trading.buy import Order, LimitOrder, MarketOrder
from deribit.sdk.core import (
  SdkMixin, wrap_exceptions,
  spot_name, perp_name, inverse_perp_name,
  parse_side, parse_status
)

def parse_order(order: OrderTDK) -> Order:
  if order['type'] == 'LIMIT':
    return LimitOrder(
      type='limit',
      price=fmt_num(order['price']),
      amount=fmt_num(order['qty'])
    )
  elif order['type'] == 'MARKET':
    return MarketOrder(
      type='market',
      amount=fmt_num(order['qty'])
    )

@dataclass
class PlaceOrder(SpotPlaceOrder, PerpPlaceOrder, InversePerpPlaceOrder, SdkMixin):
  @wrap_exceptions
  async def _place_order(self, instrument: str, /, *, order: OrderTDK, response: ResponseModel = 'id') -> str | OrderState:
    fn = self.client.buy if order['side'] == 'BUY' else self.client.sell
    r = await fn(instrument, parse_order(order))
    if not 'result' in r:
      raise ApiError(r['error'])
    elif response == 'id':
      return r['result']['order']['order_id']
    else:
      o = r['result']['order']
      return OrderState(
        id=o['order_id'],
        price=o['price'],
        qty=o['amount'],
        filled_qty=o['filled_amount'],
        side=parse_side(o['direction']),
        time=ts.parse(o['creation_timestamp']),
        status=parse_status(o)
      )

  async def _spot_place_order(self, base: str, quote: str, /, *, order: OrderTDK, response: ResponseModel = 'id') -> str | OrderState:
    instrument = spot_name(base, quote)
    return await self._place_order(instrument, order=order, response=response)

  async def _perp_place_order(self, base: str, quote: str, /, *, order: OrderTDK, response: ResponseModel = 'id') -> str | OrderState:
    instrument = perp_name(base, quote)
    return await self._place_order(instrument, order=order, response=response)

  async def _inverse_perp_place_order(self, currency: str, /, *, order: OrderTDK, response: ResponseModel = 'id') -> str | OrderState:
    instrument = inverse_perp_name(currency)
    return await self._place_order(instrument, order=order, response=response)