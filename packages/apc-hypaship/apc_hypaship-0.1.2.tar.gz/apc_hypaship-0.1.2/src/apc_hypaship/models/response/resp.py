from apc_hypaship.config import APCBaseModel
from apc_hypaship.models.response.common import Messages
from apc_hypaship.models.response.service import Services
from apc_hypaship.models.response.shipment import Orders, Order


class Response(APCBaseModel): ...


class BookingResponse(Response):
    orders: Orders | None = None

    @property
    def order_num(self):
        return self.orders.order.order_number if self.orders and self.orders.order else None


class OrdersResponse(APCBaseModel):
    orders: Orders


class ServiceAvailability(APCBaseModel):
    account_number: str | None = None
    messages: Messages | None = None
    order: Order | None = None
    services: Services | None = None


class ServiceAvailabilityResponse(APCBaseModel):
    service_availability: ServiceAvailability

