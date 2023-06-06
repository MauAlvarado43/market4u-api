from app.models import User, Company

def update_info(user_id, city, cologn, cp, email, firstName, password, lastName, municipality, state, street, telephone, type, company):
    user = User.objects.get(id=user_id)
    if(type == 'NORMAL' or type == 'SUPERADMIN'):
        user.city = city
        user.cologn = cologn
        user.cp = cp
        user.email = email
        user.username = email
        user.first_name = firstName
        user.last_name = lastName
        user.municipality = municipality
        user.state = state
        user.street = street
        user.telephone = telephone
        if(password != ''):
            user.set_password(password)
        user.save()
    elif((type == "ADMIN" or type == "SELLER") and company != None):
        user.city = city
        user.cologn = cologn
        user.cp = cp
        user.email = email
        user.username = email
        user.first_name = firstName
        user.last_name = lastName
        user.municipality = municipality
        user.state = state
        user.street = street
        user.telephone = telephone
        if(password != ''):
            user.set_password(password)
        user.save()