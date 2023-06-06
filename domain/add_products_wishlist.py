from app.models import User

def add_products_wishlist(user_id, product_id):
    user = User.objects.get(id=user_id)
    #Validate if product_id is in wishlist, if it is, delete the product_id from wishlist
    if user.wishlist.filter(id=product_id).exists():
        user.wishlist.remove(product_id)
        return True
    else:
        user.wishlist.add(product_id)
        user.save()
        return False