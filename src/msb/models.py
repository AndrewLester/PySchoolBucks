from enum import Enum
from typing import List, Literal, TypedDict


class APIServer(Enum):
    LAB = 'https://schoolbucks.msb-lab.com/msbpay/v2'
    QA = 'https://test.www.myschoolbucks.com/msbpay/v2'
    STAGING = 'https://staging.www.myschoolbucks.com/msbpay/v2'
    PRODUCTION = 'https://www.myschoolbucks.com/msbpay/v2'
    

MsbPayResult = Literal['unknown','success','error',]
CartStatus = Literal['pending','canceled','authorized','closed',]
PaymentTxnType = Literal['sale','credit','refund','reversal','preauth','postauth',]
PaymentType = Literal['sale','credit',]
OrderStatus = Literal['active','canceled','closed','declined','pending','review','void',]
PayApiEventType = Literal['ping','cart.authorized','cart.processed','cart.canceled','payment.settled','payment.authorized','payment.failed','payment.refunded',]

class MsbPayResponse(TypedDict):
    result: 'MsbPayResult'
    errors: List[str]
    
class MsbPayUser(TypedDict):
    defaultClientId: str
    developerAccountId: str
    firstName: str
    lastName: str
    email: str
    clients: List['MsbPayUserClient']
    
class MsbPayUserClient(TypedDict):
    isEnabled: bool
    clientId: str
    departmentId: str
    storeId: str
    paymentMethodId: str
    
class Cart(TypedDict):
    id: str
    status: 'CartStatus'
    createdDate: str
    lastUpdated: str
    redirectUrl: str
    returnToSiteUrl: str
    checkoutUrl: str
    allowDuplicatePayments: str
    loginPolicy: str
    checkoutStyle: str
    cartItems: List['CartItem']
    paymentPreauthPolicy: str
    webhookSubscriptions: List['WebhookSubscription']
    
class WebhookSubscription(TypedDict):
    notifyUrl: str
    type: 'PayApiEventType'
    isEnabled: bool
    subscriptionId: str
    
class CartItem(TypedDict):
    clientId: str
    departmentId: str
    storeId: str
    itemId: str
    itemName: str
    paymentMethodId: str
    quantity: str
    unitPrice: str
    displaySalesTaxRate: float
    salesTaxAmount: float
    studentName: str
    reference: str
    properties: List['ItemProperty']
    glAccountId: str
    
class CartOrder(TypedDict):
    clientId: str
    orderId: str
    date: str
    status: 'OrderStatus'
    recipientName: str
    recipientEmail: str
    billingAcctDesc: str
    tag: object
    storeId: str
    paymentMethodId: str
    cartOrderItems: List['CartOrderItem']
    
class CartOrderItem(TypedDict):
    orderItemId: str
    itemName: str
    itemId: str
    unitPrice: float
    quantity: int
    price: float
    userTxnFee: float
    clientTxnFee: float
    salesTax: float
    reference: str
    properties: List['ItemProperty']
    studentName: str
    
class CartPayment(TypedDict):
    id: str
    clientId: str
    cartId: str
    orderId: str
    payerName: str
    date: str
    txnType: 'PaymentTxnType'
    storeId: str
    paymentMethodId: str
    billingAcctDesc: str
    amount: float
    salesTax: float
    userTxnFee: float
    clientTxnFee: float
    confirmation: str
    batchDate: str
    batchNumber: str
    depositAmount: float
    settled: bool
    cartPaymentItems: List['CartPaymentItem']
    remainingRefundableAmount: float
    
class CartPaymentItem(TypedDict):
    paymentItemId: str
    itemName: str
    itemId: str
    unitPrice: float
    quantity: int
    price: float
    userTxnFee: float
    clientTxnFee: float
    salesTax: float
    reference: str
    glAccountId: str
    studentName: str
    properties: List['ItemProperty']
    
class CartRefundItem(TypedDict):
    departmentId: str
    itemId: str
    itemName: str
    quantity: str
    unitPrice: str
    salesTax: str
    studentName: str
    glAccountId: str
    reference: str
    properties: List['ItemProperty']
    
class ItemProperty(TypedDict):
    name: str
    value: str
    displayResponse: str
    
class ClientProperty(TypedDict):
    id: str
    name: str
    
class ListPaging(TypedDict):
    page: int
    prev: str
    self: str
    next: str
    total: int
    
class GetMsbPayUserResponse(MsbPayResponse):
    user: 'MsbPayUser'
    
class GetCartsResponse(MsbPayResponse):
    carts: List['Cart']
    meta: 'ListPaging'
    
class GetCartResponse(MsbPayResponse):
    cart: 'Cart'
    
class CreateUpdateCartResponse(MsbPayResponse):
    cartId: str
    
class ProcessCartResponse(MsbPayResponse):
    resultCodes: List[str]
    cartId: str
    paymentIds: List[str]
    
class BooleanResponse(MsbPayResponse):
    responseBoolean: bool
    
class GetCartOrdersResponse(MsbPayResponse):
    cartOrders: List['CartOrder']
    
class CartPaymentRefundResponse(MsbPayResponse):
    paymentId: str
    cartId: str
    
class SearchPaymentsResponse(MsbPayResponse):
    cartPayments: List['CartPayment']
    meta: 'ListPaging'
    
class SearchPaymentMethodsResponse(MsbPayResponse):
    paymentMethods: List['ClientProperty']
    meta: 'ListPaging'
    
class SearchStoresResponse(MsbPayResponse):
    stores: List['ClientProperty']
    meta: 'ListPaging'
    
class SearchDepartmentsResponse(MsbPayResponse):
    departments: List['ClientProperty']
    meta: 'ListPaging'
    
class SearchGLAccountsResponse(MsbPayResponse):
    glaccounts: List['ClientProperty']
    meta: 'ListPaging'
    
class CreateUpdateCartRequest(TypedDict, total=False):
    """
    Item ID must be fewer than or equal to 60 characters, and may contain only letters, numbers, underscores, dashes, periods, or at signs.
    Item name must be fewer than or equal to 80 characters.
    Unit price must be a positive number.
    Quantity must be greater than 0.
   
    OPTIONAL FIELDS
    Student name must fewer than or equal to 60 characters.
    Reference must be fewer than or equal to 80 characters.
    Property names must not be empty or null.
    Property Display Response must be "visible", "hidden", or null/empty.
    Redirect URL and Return to Site URL must be fewer than or equal to 1900 characters.
   
    """
    cartItems: List['CartItem']
    redirectUrl: str
    allowDuplicatePayments: str
    returnToSiteUrl: str
    loginPolicy: str
    checkoutStyle: str
    paymentPreauthPolicy: str
    webhookSubscriptions: List['WebhookSubscription']
    
class CartPaymentRefundRequest(TypedDict, total=False):
    """
    Item ID must be fewer than or equal to 60 characters, and may contain only letters, numbers, underscores, dashes, periods, or at signs.
    Item name must be fewer than or equal to 80 characters.
    Unit price must be a positive number.
    Quantity must be greater than 0.
   
    OPTIONAL FIELDS
    Student name must fewer than or equal to 60 characters.
    Reference must be fewer than or equal to 80 characters.
    Property names must not be empty or null.
    Property Display Response must be "visible", "hidden", or null/empty.
    Redirect URL and Return to Site URL must be fewer than or equal to 1900 characters.
   
    """
    refundItems: List['CartRefundItem']
    refundFullAmount: bool
    refundReason: str

class PageParam(TypedDict, total=False):
    page: int
    
class RowCountParam(TypedDict, total=False):
    rowCount: int
    
class SearchTextParam(TypedDict, total=False):
    searchText: str
