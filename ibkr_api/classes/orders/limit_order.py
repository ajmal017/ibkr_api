from ibkr_api.classes.orders.order import Order

class LimitOrder(Order):
    def __init__(self, contract, total_quantity, limit_price, **kwargs):
        super().__init__(**kwargs)
        self.contract       =   contract
        self.order_type     =   "LMT"
        self.total_quantity =   total_quantity
        self.limit_price    =   limit_price


