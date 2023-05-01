from app.models import User, Company

def update_info(user_id, city, cologn, cp, email, firstName, password, lastName, municipality, state, street, telephone, type, company):
    user = User.objects.get(id=user_id)
    if(type != 'ADMIN'):
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
    elif(type == "ADMIN" and company != None):
        comp = Company.objects.get(id=company["id"])
        comp.name = company["name"]
        comp.website = company["website"]
        comp.phone = company["phone"]
        comp.email = company["email"]
        user.email = company["email"]
        user.username = company["email"]
        comp.street = company["street"]
        comp.city = company["city"]
        comp.municipality = company["municipality"]
        comp.state = company["state"]
        comp.cologn = company["cologn"]
        comp.cp = company["cp"]
        if(password != ''):
            user.set_password(password)
        comp.save()
        user.save()