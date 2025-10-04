from dataclasses import dataclass
from decimal import Decimal

from deribit.core import TypedDict, ClientMixin, ApiResponse, validator

class Index(TypedDict):
  estimated_delivery_price: Decimal
  index_price: Decimal

validate_response = validator(Index)

@dataclass(frozen=True)
class GetIndexPrice(ClientMixin):
  async def get_index_price(
    self, index_name: str, *,
    validate: bool = True
  ) -> ApiResponse[Index]:
    """Get a given index price.
    
    - `instrument_name`: The name of the instrument to get the index price for. See available indices in the [docs](https://docs.deribit.com/#public-get_index_price).
    - `validate`: Whether to validate the response against the expected schema.
    
    > [Deribit API docs](https://docs.deribit.com/#public-get_index_price)
    """
    r = await self.get('/public/get_index_price', {
      'index_name': index_name,
    })
    if self.validate(validate) and 'result' in r:
      r['result'] = validate_response(r['result'])
    return r
    