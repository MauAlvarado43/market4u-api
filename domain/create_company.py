from app.models import Company, User, File


def create_company(company_data, user_data, validation):
    
    name = company_data["name"]
    common_name = company_data["commonName"]
    rfc = company_data["rfc"]
    email_company = company_data["email"]

    first_name = user_data["firstname"]
    last_name = user_data["lastname"]
    email = user_data["email"]
    password = user_data["password"]
    photo = File.objects.get(pk=10001)

    if Company.objects.filter(rfc=rfc).exists():
        return 440

    if User.objects.filter(email=email).exists():
        return 441

    # TODO check for validation of the fiel
    if not validate_fiel(validation):
        return 442

    company = Company.objects.create(
        name=name,
        common_name=common_name,
        rfc=rfc,
        email=email_company,
        photo=photo
    )
    
    user = User.objects.create_user(
        type="ADMIN",
        token_verified=True,
        company=company,
        first_name=first_name,
        last_name=last_name,
        email=email,
        username=email,
        photo=photo,
        state="NS"
    )

    user.set_password(password)
    user.save()

    return 200

def validate_fiel(validation):

    return True