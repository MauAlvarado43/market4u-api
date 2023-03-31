"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import graphene

import seed.schema.types
import seed.mutations.cart
import seed.mutations.category
import seed.mutations.company
import seed.mutations.message
import seed.mutations.opinion
import seed.mutations.payment
import seed.mutations.product
import seed.mutations.purchase
import seed.mutations.sale
import seed.mutations.user

class Query(seed.schema.types.Query, graphene.ObjectType):
    pass

class Mutation(graphene.ObjectType):
    saveCart = seed.mutations.cart \
        .SaveCartMutation.Field()
    setCart = seed.mutations.cart \
        .SetCartMutation.Field()
    deleteCart = seed.mutations.cart \
        .DeleteCartMutation.Field()
    saveCategory = seed.mutations.category \
        .SaveCategoryMutation.Field()
    setCategory = seed.mutations.category \
        .SetCategoryMutation.Field()
    deleteCategory = seed.mutations.category \
        .DeleteCategoryMutation.Field()
    saveCompany = seed.mutations.company \
        .SaveCompanyMutation.Field()
    setCompany = seed.mutations.company \
        .SetCompanyMutation.Field()
    deleteCompany = seed.mutations.company \
        .DeleteCompanyMutation.Field()
    saveMessage = seed.mutations.message \
        .SaveMessageMutation.Field()
    setMessage = seed.mutations.message \
        .SetMessageMutation.Field()
    deleteMessage = seed.mutations.message \
        .DeleteMessageMutation.Field()
    saveOpinion = seed.mutations.opinion \
        .SaveOpinionMutation.Field()
    setOpinion = seed.mutations.opinion \
        .SetOpinionMutation.Field()
    deleteOpinion = seed.mutations.opinion \
        .DeleteOpinionMutation.Field()
    savePayment = seed.mutations.payment \
        .SavePaymentMutation.Field()
    setPayment = seed.mutations.payment \
        .SetPaymentMutation.Field()
    deletePayment = seed.mutations.payment \
        .DeletePaymentMutation.Field()
    saveProduct = seed.mutations.product \
        .SaveProductMutation.Field()
    setProduct = seed.mutations.product \
        .SetProductMutation.Field()
    deleteProduct = seed.mutations.product \
        .DeleteProductMutation.Field()
    savePurchase = seed.mutations.purchase \
        .SavePurchaseMutation.Field()
    setPurchase = seed.mutations.purchase \
        .SetPurchaseMutation.Field()
    deletePurchase = seed.mutations.purchase \
        .DeletePurchaseMutation.Field()
    saveSale = seed.mutations.sale \
        .SaveSaleMutation.Field()
    setSale = seed.mutations.sale \
        .SetSaleMutation.Field()
    deleteSale = seed.mutations.sale \
        .DeleteSaleMutation.Field()
    saveUser = seed.mutations.user \
        .SaveUserMutation.Field()
    setUser = seed.mutations.user \
        .SetUserMutation.Field()
    deleteUser = seed.mutations.user \
        .DeleteUserMutation.Field()
    pass
schema = graphene.Schema(query=Query, mutation=Mutation)