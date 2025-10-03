import os
from functools import wraps

from fastapi import APIRouter, Body
from fastapi.params import Depends, Query
from starlette.requests import Request
from starlette.responses import HTMLResponse

from shipaw.config import shipaw_settings
from shipaw.fapi.responses import ShipawTemplateResponse
from shipaw.fapi.form_data import shipment_request_form, shipment_request_form_json
from shipaw.fapi.requests import ShipmentRequest
from shipaw.models.shipment import Shipment, sample_shipment
from shipaw.fapi.routes_api import (
    order_results as order_confirm_json,
    order_summary as order_review_json,
    ship_form as ship_form_json,
)

router = APIRouter()


@router.get('/open-file', response_class=HTMLResponse)
async def open_file(filepath: str = Query(...)):
    os.startfile(filepath)
    return HTMLResponse(content=f'<span>Re</span>')


@router.post('/print-file', response_class=HTMLResponse)
async def print_file(filepath: str = Query(...)):
    os.startfile(filepath, 'print')
    return HTMLResponse(content=f'<span>Re</span>')


def render_template_response(request: Request, resp: ShipawTemplateResponse) -> HTMLResponse:
    return shipaw_settings().templates.TemplateResponse(
        request=request,
        name=resp.template.template_path,
        context=resp.template.context,
    )


def html_from_json(json_endpoint):
    @wraps(json_endpoint)
    async def wrapper(request: Request, *args, **kwargs):
        resp = await json_endpoint(request, *args, **kwargs)

        return shipaw_settings().templates.TemplateResponse(
            request=request, name=resp.template_path, context=resp.context
        )

    return wrapper


@router.post('/shipping_form', response_class=HTMLResponse)
async def shipping_form(request: Request, shipment: Shipment = Body(...)) -> HTMLResponse:
    res = await ship_form_json(request, shipment)
    return render_template_response(request, res)


@router.post('/order_summary', response_class=HTMLResponse)
async def order_summary(
    request: Request,
    shipment_request: ShipmentRequest = Depends(shipment_request_form),
) -> HTMLResponse:
    res = await order_review_json(request, shipment_request)
    return render_template_response(request, res)


@router.post('/order_results', response_class=HTMLResponse)
async def order_results(
    request: Request,
    shipment_request: ShipmentRequest = Depends(shipment_request_form_json),
) -> HTMLResponse:
    template_response = await order_confirm_json(request, shipment_request)
    return render_template_response(request, template_response)


@router.get('/test', response_class=HTMLResponse)
async def ship(request: Request) -> HTMLResponse:
    shipment = sample_shipment()
    res = await ship_form_json(request, shipment)
    return render_template_response(request, res)


@router.get('/home_mobile_phone', response_class=HTMLResponse)
async def home_mobile_phone():
    mobile_phone = shipaw_settings().mobile_phone
    return f"""
    <input type="tel" id="mobile_phone" name="mobile_phone" value="{mobile_phone}" required>
    """

