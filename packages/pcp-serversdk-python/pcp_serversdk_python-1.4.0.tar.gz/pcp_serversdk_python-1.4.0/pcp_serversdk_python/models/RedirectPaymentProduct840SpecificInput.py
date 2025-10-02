from dataclasses import dataclass
from typing import Optional


@dataclass(kw_only=True)
class RedirectPaymentProduct840SpecificInput:
    """
    Object containing specific input required for PayPal payments
    (Payment product ID 840)
    """

    addressSelectionAtPayPal: Optional[bool] = False
    fraudNetId: Optional[str] = (
        None  # A unique ID determined by the merchant, to link a Paypal transaction
        # to a FraudNet PayPal risk session. Only applicable to customer-initiated
        # transactions, when the FraudNet SDK is used, and to be passed in the API
        # request the same tracking ID value (FraudNet Session Identifier).
    )
    javaScriptSdkFlow: bool = (
        True  # Required parameter which defines how PayPal is being integrated
        # inside the checkout page. True = the current integration uses PayPal SDK,
        # False = classic usage with PayPal Redirect flow
    )
    action: Optional[str] = (
        None  # Required parameter for a COMPLETE CALL (not only an ORDER CALL)
        # which one value "CONFIRM_ORDER_STATUS" signals process is finished
        # on merchant side
    )
