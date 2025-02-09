import pytest
from ..models.user_model import User
from datetime import datetime
from freezegun import freeze_time

@pytest.fixture
def test_user():
    with freeze_time("2022-01-01"):
        email = 'test@test.com'
        user_id = '123456789'
        first_name = 'Test'
        middle_name = 'FC'
        last_name = 'User'
        second_last_name = 'Test'
        password = 'Sapp123456789'
        address = 'Test Avenue'
        contact_number = '+1234567890'
        rol = 'cliente'
        date_register = '2022-01-01'
        is_active = True
        is_staff = False
        is_superuser = False
        profile_picture = 'test.jpg'
        
        if not User.objects.filter(email=email).exists():
            user = User.objects.create(
                email=email, user_id=user_id, first_name=first_name, middle_name=middle_name,
                last_name=last_name, second_last_name=second_last_name, address=address, contact_number=contact_number,
                rol=rol, date_register=date_register, is_active=is_active, is_staff=is_staff, is_superuser=is_superuser,
                profile_picture=profile_picture
            )
            user.set_password(password)
            user.save()
            
        yield User.objects.get(email=email)

        User.objects.all().delete()