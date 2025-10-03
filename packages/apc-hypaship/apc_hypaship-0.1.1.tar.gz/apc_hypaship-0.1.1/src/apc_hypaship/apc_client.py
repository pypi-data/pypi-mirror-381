from typing import Literal

import httpx

from apc_hypaship.config import APCSettings, apc_settings
from apc_hypaship.models.response.label_track import Tracks
from apc_hypaship.models.response.resp import BookingResponse, ServiceAvailabilityResponse
from apc_hypaship.models.response.shipment import Label
from apc_hypaship.models.request.shipment import Shipment

ResponseMode = Literal['raw'] | Literal['json'] | type


def make_post(
    url: str,
    data: dict | None = None,
    settings: APCSettings = apc_settings(),
) -> httpx.Response:
    headers = settings.headers
    res = httpx.post(url, headers=headers, json=data, timeout=30)
    res.raise_for_status()
    return res


def make_get(
    url: str,
    params: dict | None = None,
    settings: APCSettings = apc_settings(),
) -> httpx.Response:
    headers = settings.headers
    res = httpx.get(url, headers=headers, params=params, timeout=30)
    res.raise_for_status()
    return res


def service_available(
    shipment: Shipment,
    settings: APCSettings = apc_settings(),
) -> ServiceAvailabilityResponse:
    shipment_dict = shipment.model_dump(by_alias=True, mode='json')
    res = make_post(settings.services_endpoint, shipment_dict)
    return ServiceAvailabilityResponse(**res.json())


def book_shipment(
    shipment: Shipment,
    settings=apc_settings(),
) -> BookingResponse:
    shipment_dict = shipment.model_dump(by_alias=True, mode='json')
    res = make_post(url=settings.orders_endpoint, data=shipment_dict, settings=settings)
    return BookingResponse(**res.json())


def get_label(
    shipment_num: str,
    settings: APCSettings = apc_settings(),
) -> Label:
    params = {'labelformat': 'PDF'}
    label = make_get(
        url=settings.one_order_endpoint(shipment_num),
        params=params,
        settings=settings,
    )
    label = BookingResponse(**label.json())
    return label.orders.order.label


def get_tracks(
    shipment_num: str,
    settings: APCSettings = apc_settings(),
) -> Tracks:
    res = make_get(url=settings.track_endpoint(shipment_num), settings=settings)
    res = res.json()
    t = res.get('Tracks')
    return Tracks(**t)


