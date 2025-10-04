from typing_extensions import Literal, overload, AsyncIterable, NotRequired
from dataclasses import dataclass
from decimal import Decimal
from datetime import datetime

from deribit.core import (
  TypedDict, ApiResponse, validator,
  ClientMixin, timestamp as ts, raise_on_error
)

class Funding(TypedDict):
  index_price: Decimal
  interest_1h: Decimal
  interest_8h: Decimal
  prev_index_price: NotRequired[Decimal|None]
  timestamp: int

validate_response = validator(list[Funding])

@dataclass(frozen=True)
class GetFundingRateHistory(ClientMixin):
  @overload
  async def get_funding_rate_history(
    self, instrument_name: str, *,
    start: datetime, end: datetime,
    validate: bool = True,
    unsafe: Literal[True] = True
  ) -> list[Funding]:
    ...
  @overload
  async def get_funding_rate_history(
    self, instrument_name: str, *,
    start: datetime, end: datetime,
    validate: bool = True,
  ) -> ApiResponse[list[Funding]]:
    ...
  async def get_funding_rate_history(
    self, instrument_name: str, *,
    start: datetime, end: datetime,
    validate: bool = True,
    unsafe: bool = False
  ) -> ApiResponse[list[Funding]] | list[Funding]:
    """Retrieves hourly historical interest rate for a perpetual instrument.
    
    - `instrument_name`: The name of the instrument to get the funding rate history for.
    - `start`: The start timestamp to get the funding rate history for.
    - `end`: The end timestamp to get the funding rate history for.
    - `validate`: Whether to validate the response against the expected schema.
    - `unsafe`: Whether to raise an exception in case of an error.
    
    > [Deribit API docs](https://docs.deribit.com/#public-get_funding_rate_history)
    """
    params: dict = {
      'instrument_name': instrument_name,
      'start_timestamp': ts.dump(start),
      'end_timestamp': ts.dump(end),
    }
    r = await self.get('/public/get_funding_rate_history', params)
    if self.validate(validate) and 'result' in r:
      r['result'] = validate_response(r['result'])
    return raise_on_error(r) if unsafe else r
    

  async def get_funding_rate_history_paged(
    self, instrument_name: str, *,
    start: datetime, end: datetime,
    validate: bool = True,
  ) -> AsyncIterable[list[Funding]]:
    last = None
    while True:
      history = await self.get_funding_rate_history(instrument_name, start=start, end=end, validate=validate, unsafe=True)
      history = [h for h in history if h['timestamp'] != last]
      if not history:
        break
      yield history
      last = history[0]['timestamp']
      end = ts.parse(last)