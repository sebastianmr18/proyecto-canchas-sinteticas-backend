from .shared_user_test import *
from datetime import date
from freezegun import freeze_time

def test_user_get_email(test_user):
    assert test_user.get_email() == 'test@test.com'

def test_user_get_user_id(test_user):
    assert test_user.get_user_id() == '123456789'

def test_user_get_first_name(test_user):
    assert test_user.get_first_name() == 'Test'

def test_user_get_middle_name(test_user):
    assert test_user.get_middle_name() == 'FC'

def test_user_get_last_name(test_user):
    assert test_user.get_last_name() == 'User'

def test_user_get_second_last_name(test_user):
    assert test_user.get_second_last_name() == 'Test'

def test_user_get_address(test_user):
    assert test_user.get_address() == 'Test Avenue'

def test_user_get_contact_number(test_user):
    assert test_user.get_contact_number() == '+1234567890'

def test_user_get_rol(test_user):
    assert test_user.get_rol() == 'cliente'

@freeze_time("2022-01-01")
def test_user_get_date_register(test_user):
    assert test_user.get_date_register().date() == date(2022, 1, 1)

def test_user_get_is_active(test_user):
    assert test_user.get_is_active() == True

def test_user_get_is_staff(test_user):
    assert test_user.get_is_staff() == False

def test_user_get_is_superuser(test_user):
    assert test_user.get_is_superuser() == False

def test_user_get_profile_picture(test_user):
    assert test_user.get_profile_picture() == 'test.jpg'