"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

# pylint: disable=C0302
import graphene
import secrets
import math
from graphene import ObjectType
from graphene_django import DjangoListField
from graphene_django.types import DjangoObjectType
from app.models import Cart as CartModel
from app.models import Category as CategoryModel
from app.models import Company as CompanyModel
from app.models import Message as MessageModel
from app.models import Opinion as OpinionModel
from app.models import Payment as PaymentModel
from app.models import Product as ProductModel
from app.models import Purchase as PurchaseModel
from app.models import Sale as SaleModel
from app.models import Shipping as ShippingModel
from app.models import User as UserModel
from app.models import Variant as VariantModel
from app.models import Variantoption as VariantoptionModel
from app.models import File as FileModel
from seed.util.query_util import sql_alike_q

class Cart(DjangoObjectType):
    id = graphene.Int(description="Cart primary key")
    class Meta:
        model = CartModel
        
    def resolve_id(self, info):
        return self.pk

class CartPagination(ObjectType):
    id = graphene.Int()
    pageNum = graphene.Int()
    pageSize = graphene.Int()
    totalPages = graphene.Int()
    totalCount = graphene.Int()
    carts = DjangoListField(Cart)

class CartCount(ObjectType):
    id = graphene.Int()
    count = graphene.Int()

class Category(DjangoObjectType):
    id = graphene.Int(description="Category primary key")
    class Meta:
        model = CategoryModel
        
    def resolve_id(self, info):
        return self.pk

class CategoryPagination(ObjectType):
    id = graphene.Int()
    pageNum = graphene.Int()
    pageSize = graphene.Int()
    totalPages = graphene.Int()
    totalCount = graphene.Int()
    categories = DjangoListField(Category)

class CategoryCount(ObjectType):
    id = graphene.Int()
    count = graphene.Int()

class Company(DjangoObjectType):
    id = graphene.Int(description="Company primary key")
    class Meta:
        model = CompanyModel
        
    def resolve_id(self, info):
        return self.pk

class CompanyPagination(ObjectType):
    id = graphene.Int()
    pageNum = graphene.Int()
    pageSize = graphene.Int()
    totalPages = graphene.Int()
    totalCount = graphene.Int()
    companies = DjangoListField(Company)

class CompanyCount(ObjectType):
    id = graphene.Int()
    count = graphene.Int()

class Message(DjangoObjectType):
    id = graphene.Int(description="Message primary key")
    class Meta:
        model = MessageModel
        
    def resolve_id(self, info):
        return self.pk

class MessagePagination(ObjectType):
    id = graphene.Int()
    pageNum = graphene.Int()
    pageSize = graphene.Int()
    totalPages = graphene.Int()
    totalCount = graphene.Int()
    messages = DjangoListField(Message)

class MessageCount(ObjectType):
    id = graphene.Int()
    count = graphene.Int()

class Opinion(DjangoObjectType):
    id = graphene.Int(description="Opinion primary key")
    class Meta:
        model = OpinionModel
        
    def resolve_id(self, info):
        return self.pk

class OpinionPagination(ObjectType):
    id = graphene.Int()
    pageNum = graphene.Int()
    pageSize = graphene.Int()
    totalPages = graphene.Int()
    totalCount = graphene.Int()
    opinions = DjangoListField(Opinion)

class OpinionCount(ObjectType):
    id = graphene.Int()
    count = graphene.Int()

class Payment(DjangoObjectType):
    id = graphene.Int(description="Payment primary key")
    class Meta:
        model = PaymentModel
        
    def resolve_id(self, info):
        return self.pk

class PaymentPagination(ObjectType):
    id = graphene.Int()
    pageNum = graphene.Int()
    pageSize = graphene.Int()
    totalPages = graphene.Int()
    totalCount = graphene.Int()
    payments = DjangoListField(Payment)

class PaymentCount(ObjectType):
    id = graphene.Int()
    count = graphene.Int()

class Product(DjangoObjectType):
    id = graphene.Int(description="Product primary key")
    class Meta:
        model = ProductModel
        
    def resolve_id(self, info):
        return self.pk

class ProductPagination(ObjectType):
    id = graphene.Int()
    pageNum = graphene.Int()
    pageSize = graphene.Int()
    totalPages = graphene.Int()
    totalCount = graphene.Int()
    products = DjangoListField(Product)

class ProductCount(ObjectType):
    id = graphene.Int()
    count = graphene.Int()

class Purchase(DjangoObjectType):
    id = graphene.Int(description="Purchase primary key")
    class Meta:
        model = PurchaseModel
        
    def resolve_id(self, info):
        return self.pk

class PurchasePagination(ObjectType):
    id = graphene.Int()
    pageNum = graphene.Int()
    pageSize = graphene.Int()
    totalPages = graphene.Int()
    totalCount = graphene.Int()
    purchases = DjangoListField(Purchase)

class PurchaseCount(ObjectType):
    id = graphene.Int()
    count = graphene.Int()

class Sale(DjangoObjectType):
    id = graphene.Int(description="Sale primary key")
    class Meta:
        model = SaleModel
        
    def resolve_id(self, info):
        return self.pk

class SalePagination(ObjectType):
    id = graphene.Int()
    pageNum = graphene.Int()
    pageSize = graphene.Int()
    totalPages = graphene.Int()
    totalCount = graphene.Int()
    sales = DjangoListField(Sale)

class SaleCount(ObjectType):
    id = graphene.Int()
    count = graphene.Int()

class Shipping(DjangoObjectType):
    id = graphene.Int(description="Shipping primary key")
    class Meta:
        model = ShippingModel
        
    def resolve_id(self, info):
        return self.pk

class ShippingPagination(ObjectType):
    id = graphene.Int()
    pageNum = graphene.Int()
    pageSize = graphene.Int()
    totalPages = graphene.Int()
    totalCount = graphene.Int()
    shippings = DjangoListField(Shipping)

class ShippingCount(ObjectType):
    id = graphene.Int()
    count = graphene.Int()

class User(DjangoObjectType):
    id = graphene.Int(description="User primary key")
    class Meta:
        model = UserModel
        exclude = ('password',)
        
    def resolve_id(self, info):
        return self.pk

class UserPagination(ObjectType):
    id = graphene.Int()
    pageNum = graphene.Int()
    pageSize = graphene.Int()
    totalPages = graphene.Int()
    totalCount = graphene.Int()
    users = DjangoListField(User)

class UserCount(ObjectType):
    id = graphene.Int()
    count = graphene.Int()

class Variant(DjangoObjectType):
    id = graphene.Int(description="Variant primary key")
    class Meta:
        model = VariantModel
        
    def resolve_id(self, info):
        return self.pk

class VariantPagination(ObjectType):
    id = graphene.Int()
    pageNum = graphene.Int()
    pageSize = graphene.Int()
    totalPages = graphene.Int()
    totalCount = graphene.Int()
    variants = DjangoListField(Variant)

class VariantCount(ObjectType):
    id = graphene.Int()
    count = graphene.Int()

class Variantoption(DjangoObjectType):
    id = graphene.Int(description="Variantoption primary key")
    class Meta:
        model = VariantoptionModel
        
    def resolve_id(self, info):
        return self.pk

class VariantoptionPagination(ObjectType):
    id = graphene.Int()
    pageNum = graphene.Int()
    pageSize = graphene.Int()
    totalPages = graphene.Int()
    totalCount = graphene.Int()
    variantoptions = DjangoListField(Variantoption)

class VariantoptionCount(ObjectType):
    id = graphene.Int()
    count = graphene.Int()

class File(DjangoObjectType):
    class Meta:
        model = FileModel
        description = 'Represents a File object'

class FilePagination(ObjectType):
    pageNum = graphene.Int()
    pageSize = graphene.Int()
    totalPages = graphene.Int()
    totalCount = graphene.Int()
    files = DjangoListField(File)

class FileCount(ObjectType):
    id = graphene.Int()
    count = graphene.Int()

def resolve_list(model, info, **kwargs):
    user = info.context.user
    if "query" in kwargs:
        res = model.objects.filter(sql_alike_q(kwargs["query"])).distinct()
    else:
        res = model.objects.all()
    if "orderBy" in kwargs:
        orders = kwargs["orderBy"].split(",")
        for order in orders:
            res = res.order_by(order)
    if "start" in kwargs and "end" not in kwargs:
        res = res[kwargs["start"]:]
    if "end" in kwargs and "start" not in kwargs:
        res = res[:kwargs["end"]]
    if "start" in kwargs and "end" in kwargs:
        res = res[kwargs["start"]:kwargs["end"]]
    res = model.filter_permissions(res, model.permission_filters(user))
    return res

def resolve_pagination(model, model_name, pagination_type, info, **kwargs):
    total_count = len(resolve_list(model, info, **kwargs))
    total_pages = math.ceil(total_count / kwargs["pageSize"])
    kwargs["start"] = (kwargs["pageNum"] - 1) * kwargs["pageSize"]
    kwargs["end"] = (kwargs["pageNum"]) * kwargs["pageSize"]
    page = resolve_list(model, info, **kwargs)

    return pagination_type(**{
       "id": int(''.join(secrets.choice("0123456789") for i in range(9))),
       "pageNum": kwargs["pageNum"],
       "pageSize": kwargs["pageSize"],
       "totalPages": total_pages,
       "totalCount": total_count,
       model_name: page
    })

def resolve_count(model, count_type, info, **kwargs):
    user = info.context.user
    if "query" in kwargs:
        query = model.objects.filter(sql_alike_q(kwargs["query"])).distinct()
    else:
        query = model.objects.all()
    query = model.filter_permissions(query, model.permission_filters(user))

    return count_type(
        id=int(''.join(secrets.choice("0123456789") for i in range(9))),
        count=len(query))

# pylint: disable=R0904
class Query(object):
    
    carts = graphene.List(
        Cart, query=graphene.String(),
        orderBy=graphene.String(), limit=graphene.Int())
    cartPagination = graphene.Field(
        CartPagination,
        pageNum=graphene.Int(required=True), pageSize=graphene.Int(required=True),
        query=graphene.String(), orderBy=graphene.String())
    cartCount = graphene.Field(
        CartCount, query=graphene.String())
    cart = graphene.Field(
        Cart, id=graphene.Int(required=True))
    categories = graphene.List(
        Category, query=graphene.String(),
        orderBy=graphene.String(), limit=graphene.Int())
    categoryPagination = graphene.Field(
        CategoryPagination,
        pageNum=graphene.Int(required=True), pageSize=graphene.Int(required=True),
        query=graphene.String(), orderBy=graphene.String())
    categoryCount = graphene.Field(
        CategoryCount, query=graphene.String())
    category = graphene.Field(
        Category, id=graphene.Int(required=True))
    companies = graphene.List(
        Company, query=graphene.String(),
        orderBy=graphene.String(), limit=graphene.Int())
    companyPagination = graphene.Field(
        CompanyPagination,
        pageNum=graphene.Int(required=True), pageSize=graphene.Int(required=True),
        query=graphene.String(), orderBy=graphene.String())
    companyCount = graphene.Field(
        CompanyCount, query=graphene.String())
    company = graphene.Field(
        Company, id=graphene.Int(required=True))
    messages = graphene.List(
        Message, query=graphene.String(),
        orderBy=graphene.String(), limit=graphene.Int())
    messagePagination = graphene.Field(
        MessagePagination,
        pageNum=graphene.Int(required=True), pageSize=graphene.Int(required=True),
        query=graphene.String(), orderBy=graphene.String())
    messageCount = graphene.Field(
        MessageCount, query=graphene.String())
    message = graphene.Field(
        Message, id=graphene.Int(required=True))
    opinions = graphene.List(
        Opinion, query=graphene.String(),
        orderBy=graphene.String(), limit=graphene.Int())
    opinionPagination = graphene.Field(
        OpinionPagination,
        pageNum=graphene.Int(required=True), pageSize=graphene.Int(required=True),
        query=graphene.String(), orderBy=graphene.String())
    opinionCount = graphene.Field(
        OpinionCount, query=graphene.String())
    opinion = graphene.Field(
        Opinion, id=graphene.Int(required=True))
    payments = graphene.List(
        Payment, query=graphene.String(),
        orderBy=graphene.String(), limit=graphene.Int())
    paymentPagination = graphene.Field(
        PaymentPagination,
        pageNum=graphene.Int(required=True), pageSize=graphene.Int(required=True),
        query=graphene.String(), orderBy=graphene.String())
    paymentCount = graphene.Field(
        PaymentCount, query=graphene.String())
    payment = graphene.Field(
        Payment, id=graphene.Int(required=True))
    products = graphene.List(
        Product, query=graphene.String(),
        orderBy=graphene.String(), limit=graphene.Int())
    productPagination = graphene.Field(
        ProductPagination,
        pageNum=graphene.Int(required=True), pageSize=graphene.Int(required=True),
        query=graphene.String(), orderBy=graphene.String())
    productCount = graphene.Field(
        ProductCount, query=graphene.String())
    product = graphene.Field(
        Product, id=graphene.Int(required=True))
    purchases = graphene.List(
        Purchase, query=graphene.String(),
        orderBy=graphene.String(), limit=graphene.Int())
    purchasePagination = graphene.Field(
        PurchasePagination,
        pageNum=graphene.Int(required=True), pageSize=graphene.Int(required=True),
        query=graphene.String(), orderBy=graphene.String())
    purchaseCount = graphene.Field(
        PurchaseCount, query=graphene.String())
    purchase = graphene.Field(
        Purchase, id=graphene.Int(required=True))
    sales = graphene.List(
        Sale, query=graphene.String(),
        orderBy=graphene.String(), limit=graphene.Int())
    salePagination = graphene.Field(
        SalePagination,
        pageNum=graphene.Int(required=True), pageSize=graphene.Int(required=True),
        query=graphene.String(), orderBy=graphene.String())
    saleCount = graphene.Field(
        SaleCount, query=graphene.String())
    sale = graphene.Field(
        Sale, id=graphene.Int(required=True))
    shippings = graphene.List(
        Shipping, query=graphene.String(),
        orderBy=graphene.String(), limit=graphene.Int())
    shippingPagination = graphene.Field(
        ShippingPagination,
        pageNum=graphene.Int(required=True), pageSize=graphene.Int(required=True),
        query=graphene.String(), orderBy=graphene.String())
    shippingCount = graphene.Field(
        ShippingCount, query=graphene.String())
    shipping = graphene.Field(
        Shipping, id=graphene.Int(required=True))
    users = graphene.List(
        User, query=graphene.String(),
        orderBy=graphene.String(), limit=graphene.Int())
    userPagination = graphene.Field(
        UserPagination,
        pageNum=graphene.Int(required=True), pageSize=graphene.Int(required=True),
        query=graphene.String(), orderBy=graphene.String())
    userCount = graphene.Field(
        UserCount, query=graphene.String())
    user = graphene.Field(
        User, id=graphene.Int(required=True))
    variants = graphene.List(
        Variant, query=graphene.String(),
        orderBy=graphene.String(), limit=graphene.Int())
    variantPagination = graphene.Field(
        VariantPagination,
        pageNum=graphene.Int(required=True), pageSize=graphene.Int(required=True),
        query=graphene.String(), orderBy=graphene.String())
    variantCount = graphene.Field(
        VariantCount, query=graphene.String())
    variant = graphene.Field(
        Variant, id=graphene.Int(required=True))
    variantoptions = graphene.List(
        Variantoption, query=graphene.String(),
        orderBy=graphene.String(), limit=graphene.Int())
    variantoptionPagination = graphene.Field(
        VariantoptionPagination,
        pageNum=graphene.Int(required=True), pageSize=graphene.Int(required=True),
        query=graphene.String(), orderBy=graphene.String())
    variantoptionCount = graphene.Field(
        VariantoptionCount, query=graphene.String())
    variantoption = graphene.Field(
        Variantoption, id=graphene.Int(required=True))
    files = graphene.List(
        File, query=graphene.String(), orderBy=graphene.String(), limit=graphene.Int())
    filePagination = graphene.Field(
        FilePagination,
        pageNum=graphene.Int(required=True), pageSize=graphene.Int(required=True),
        query=graphene.String(), orderBy=graphene.String())
    file = graphene.Field(File, id=graphene.Int(required=True))
    fileCount = graphene.Field(FileCount, query=graphene.String())

    # pylint: disable=C0103
    def resolve_carts(self, info, **kwargs):
        if "limit" in kwargs:
            kwargs["end"] = kwargs["limit"]
        return resolve_list(CartModel, info, **kwargs)

    # pylint: disable=C0103
    def resolve_cartPagination(self, info, **kwargs):
        return resolve_pagination(
            CartModel, 'carts',
            CartPagination, info, **kwargs)

    # pylint: disable=C0103
    def resolve_cartCount(self, info, **kwargs):
        return resolve_count(
          CartModel, CartCount, info, **kwargs)

    # pylint: disable=C0103,W0622
    def resolve_cart(self, info, id):
        user = info.context.user
        return CartModel.filter_permissions(
            CartModel.objects,
            CartModel.permission_filters(user)).get(pk=id)
    
    # pylint: disable=C0103
    def resolve_categories(self, info, **kwargs):
        if "limit" in kwargs:
            kwargs["end"] = kwargs["limit"]
        return resolve_list(CategoryModel, info, **kwargs)

    # pylint: disable=C0103
    def resolve_categoryPagination(self, info, **kwargs):
        return resolve_pagination(
            CategoryModel, 'categories',
            CategoryPagination, info, **kwargs)

    # pylint: disable=C0103
    def resolve_categoryCount(self, info, **kwargs):
        return resolve_count(
          CategoryModel, CategoryCount, info, **kwargs)

    # pylint: disable=C0103,W0622
    def resolve_category(self, info, id):
        user = info.context.user
        return CategoryModel.filter_permissions(
            CategoryModel.objects,
            CategoryModel.permission_filters(user)).get(pk=id)
    
    # pylint: disable=C0103
    def resolve_companies(self, info, **kwargs):
        if "limit" in kwargs:
            kwargs["end"] = kwargs["limit"]
        return resolve_list(CompanyModel, info, **kwargs)

    # pylint: disable=C0103
    def resolve_companyPagination(self, info, **kwargs):
        return resolve_pagination(
            CompanyModel, 'companies',
            CompanyPagination, info, **kwargs)

    # pylint: disable=C0103
    def resolve_companyCount(self, info, **kwargs):
        return resolve_count(
          CompanyModel, CompanyCount, info, **kwargs)

    # pylint: disable=C0103,W0622
    def resolve_company(self, info, id):
        user = info.context.user
        return CompanyModel.filter_permissions(
            CompanyModel.objects,
            CompanyModel.permission_filters(user)).get(pk=id)
    
    # pylint: disable=C0103
    def resolve_messages(self, info, **kwargs):
        if "limit" in kwargs:
            kwargs["end"] = kwargs["limit"]
        return resolve_list(MessageModel, info, **kwargs)

    # pylint: disable=C0103
    def resolve_messagePagination(self, info, **kwargs):
        return resolve_pagination(
            MessageModel, 'messages',
            MessagePagination, info, **kwargs)

    # pylint: disable=C0103
    def resolve_messageCount(self, info, **kwargs):
        return resolve_count(
          MessageModel, MessageCount, info, **kwargs)

    # pylint: disable=C0103,W0622
    def resolve_message(self, info, id):
        user = info.context.user
        return MessageModel.filter_permissions(
            MessageModel.objects,
            MessageModel.permission_filters(user)).get(pk=id)
    
    # pylint: disable=C0103
    def resolve_opinions(self, info, **kwargs):
        if "limit" in kwargs:
            kwargs["end"] = kwargs["limit"]
        return resolve_list(OpinionModel, info, **kwargs)

    # pylint: disable=C0103
    def resolve_opinionPagination(self, info, **kwargs):
        return resolve_pagination(
            OpinionModel, 'opinions',
            OpinionPagination, info, **kwargs)

    # pylint: disable=C0103
    def resolve_opinionCount(self, info, **kwargs):
        return resolve_count(
          OpinionModel, OpinionCount, info, **kwargs)

    # pylint: disable=C0103,W0622
    def resolve_opinion(self, info, id):
        user = info.context.user
        return OpinionModel.filter_permissions(
            OpinionModel.objects,
            OpinionModel.permission_filters(user)).get(pk=id)
    
    # pylint: disable=C0103
    def resolve_payments(self, info, **kwargs):
        if "limit" in kwargs:
            kwargs["end"] = kwargs["limit"]
        return resolve_list(PaymentModel, info, **kwargs)

    # pylint: disable=C0103
    def resolve_paymentPagination(self, info, **kwargs):
        return resolve_pagination(
            PaymentModel, 'payments',
            PaymentPagination, info, **kwargs)

    # pylint: disable=C0103
    def resolve_paymentCount(self, info, **kwargs):
        return resolve_count(
          PaymentModel, PaymentCount, info, **kwargs)

    # pylint: disable=C0103,W0622
    def resolve_payment(self, info, id):
        user = info.context.user
        return PaymentModel.filter_permissions(
            PaymentModel.objects,
            PaymentModel.permission_filters(user)).get(pk=id)
    
    # pylint: disable=C0103
    def resolve_products(self, info, **kwargs):
        if "limit" in kwargs:
            kwargs["end"] = kwargs["limit"]
        return resolve_list(ProductModel, info, **kwargs)

    # pylint: disable=C0103
    def resolve_productPagination(self, info, **kwargs):
        return resolve_pagination(
            ProductModel, 'products',
            ProductPagination, info, **kwargs)

    # pylint: disable=C0103
    def resolve_productCount(self, info, **kwargs):
        return resolve_count(
          ProductModel, ProductCount, info, **kwargs)

    # pylint: disable=C0103,W0622
    def resolve_product(self, info, id):
        user = info.context.user
        return ProductModel.filter_permissions(
            ProductModel.objects,
            ProductModel.permission_filters(user)).get(pk=id)
    
    # pylint: disable=C0103
    def resolve_purchases(self, info, **kwargs):
        if "limit" in kwargs:
            kwargs["end"] = kwargs["limit"]
        return resolve_list(PurchaseModel, info, **kwargs)

    # pylint: disable=C0103
    def resolve_purchasePagination(self, info, **kwargs):
        return resolve_pagination(
            PurchaseModel, 'purchases',
            PurchasePagination, info, **kwargs)

    # pylint: disable=C0103
    def resolve_purchaseCount(self, info, **kwargs):
        return resolve_count(
          PurchaseModel, PurchaseCount, info, **kwargs)

    # pylint: disable=C0103,W0622
    def resolve_purchase(self, info, id):
        user = info.context.user
        return PurchaseModel.filter_permissions(
            PurchaseModel.objects,
            PurchaseModel.permission_filters(user)).get(pk=id)
    
    # pylint: disable=C0103
    def resolve_sales(self, info, **kwargs):
        if "limit" in kwargs:
            kwargs["end"] = kwargs["limit"]
        return resolve_list(SaleModel, info, **kwargs)

    # pylint: disable=C0103
    def resolve_salePagination(self, info, **kwargs):
        return resolve_pagination(
            SaleModel, 'sales',
            SalePagination, info, **kwargs)

    # pylint: disable=C0103
    def resolve_saleCount(self, info, **kwargs):
        return resolve_count(
          SaleModel, SaleCount, info, **kwargs)

    # pylint: disable=C0103,W0622
    def resolve_sale(self, info, id):
        user = info.context.user
        return SaleModel.filter_permissions(
            SaleModel.objects,
            SaleModel.permission_filters(user)).get(pk=id)
    
    # pylint: disable=C0103
    def resolve_shippings(self, info, **kwargs):
        if "limit" in kwargs:
            kwargs["end"] = kwargs["limit"]
        return resolve_list(ShippingModel, info, **kwargs)

    # pylint: disable=C0103
    def resolve_shippingPagination(self, info, **kwargs):
        return resolve_pagination(
            ShippingModel, 'shippings',
            ShippingPagination, info, **kwargs)

    # pylint: disable=C0103
    def resolve_shippingCount(self, info, **kwargs):
        return resolve_count(
          ShippingModel, ShippingCount, info, **kwargs)

    # pylint: disable=C0103,W0622
    def resolve_shipping(self, info, id):
        user = info.context.user
        return ShippingModel.filter_permissions(
            ShippingModel.objects,
            ShippingModel.permission_filters(user)).get(pk=id)
    
    # pylint: disable=C0103
    def resolve_users(self, info, **kwargs):
        if "limit" in kwargs:
            kwargs["end"] = kwargs["limit"]
        return resolve_list(UserModel, info, **kwargs)

    # pylint: disable=C0103
    def resolve_userPagination(self, info, **kwargs):
        return resolve_pagination(
            UserModel, 'users',
            UserPagination, info, **kwargs)

    # pylint: disable=C0103
    def resolve_userCount(self, info, **kwargs):
        return resolve_count(
          UserModel, UserCount, info, **kwargs)

    # pylint: disable=C0103,W0622
    def resolve_user(self, info, id):
        user = info.context.user
        return UserModel.filter_permissions(
            UserModel.objects,
            UserModel.permission_filters(user)).get(pk=id)
    
    # pylint: disable=C0103
    def resolve_variants(self, info, **kwargs):
        if "limit" in kwargs:
            kwargs["end"] = kwargs["limit"]
        return resolve_list(VariantModel, info, **kwargs)

    # pylint: disable=C0103
    def resolve_variantPagination(self, info, **kwargs):
        return resolve_pagination(
            VariantModel, 'variants',
            VariantPagination, info, **kwargs)

    # pylint: disable=C0103
    def resolve_variantCount(self, info, **kwargs):
        return resolve_count(
          VariantModel, VariantCount, info, **kwargs)

    # pylint: disable=C0103,W0622
    def resolve_variant(self, info, id):
        user = info.context.user
        return VariantModel.filter_permissions(
            VariantModel.objects,
            VariantModel.permission_filters(user)).get(pk=id)
    
    # pylint: disable=C0103
    def resolve_variantoptions(self, info, **kwargs):
        if "limit" in kwargs:
            kwargs["end"] = kwargs["limit"]
        return resolve_list(VariantoptionModel, info, **kwargs)

    # pylint: disable=C0103
    def resolve_variantoptionPagination(self, info, **kwargs):
        return resolve_pagination(
            VariantoptionModel, 'variantoptions',
            VariantoptionPagination, info, **kwargs)

    # pylint: disable=C0103
    def resolve_variantoptionCount(self, info, **kwargs):
        return resolve_count(
          VariantoptionModel, VariantoptionCount, info, **kwargs)

    # pylint: disable=C0103,W0622
    def resolve_variantoption(self, info, id):
        user = info.context.user
        return VariantoptionModel.filter_permissions(
            VariantoptionModel.objects,
            VariantoptionModel.permission_filters(user)).get(pk=id)
    
    def resolve_files(self, info, **kwargs):
        if "limit" in kwargs:
            kwargs["end"] = kwargs["limit"]
        return resolve_list(FileModel, info, **kwargs)

    # pylint: disable=C0103
    def resolve_filePagination(self, info, **kwargs):
        return resolve_pagination(FileModel, 'files', FilePagination, info, **kwargs)

    # pylint: disable=C0103
    def resolve_fileCount(self, info, **kwargs):
        return resolve_count(FileModel, FileCount, info, **kwargs)

    # pylint: disable=C0103,W0622
    def resolve_file(self, info, id):
        user = info.context.user
        return FileModel.filter_permissions(
            FileModel.objects, FileModel.permission_filters(user)).get(pk=id)
    pass