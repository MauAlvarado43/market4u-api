from app.models import User, Company

def update_info(user_id, city, cologn, cp, firstName, password, lastName, municipality, state, street, telephone):
    user = User.objects.get(id=user_id)
    user.city = city
    user.cologn = cologn
    user.cp = cp
    user.first_name = firstName
    user.last_name = lastName
    user.municipality = municipality
    user.state = state
    user.street = street
    user.telephone = telephone
    if(password != ''):
        user.set_password(password)
    user.save()