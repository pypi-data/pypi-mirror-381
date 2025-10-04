import pytest


def test_import_ap2():
    import ap2  # noqa: F401


def test_payment_types_roundtrip():
    from ap2.types.payment_request import (
        PaymentCurrencyAmount,
        PaymentItem,
        PaymentDetailsInit,
        PaymentMethodData,
        PaymentRequest,
    )

    amount = PaymentCurrencyAmount(currency="USD", value=10.0)
    total = PaymentItem(label="Total", amount=amount)
    details = PaymentDetailsInit(
        id="order-1",
        display_items=[total],
        total=total,
    )
    pr = PaymentRequest(
        method_data=[PaymentMethodData(supported_methods="basic-card")],
        details=details,
    )

    # Model serialization roundtrip
    payload = pr.model_dump()
    pr2 = PaymentRequest.model_validate(payload)
    assert pr2.details.total.amount.currency == "USD"
    assert pr2.details.total.amount.value == 10.0
