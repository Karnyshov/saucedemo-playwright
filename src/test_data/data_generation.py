from faker import Faker

fake = Faker()

def random_username() -> str:
    return fake.user_name()

def random_password() -> str:
    return fake.password()