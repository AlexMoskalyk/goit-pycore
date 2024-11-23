import re

def normalize_phone(phone_number):
    phone_number = re.sub(r'[^\d+]', '', phone_number)
    
    if phone_number.startswith('380'):
        phone_number = '+' + phone_number
    elif not phone_number.startswith('+'):
        phone_number = '+38' + phone_number
    
    return phone_number


print(normalize_phone("+38(050)123-32-34"))  # +380501233234
print(normalize_phone(" 0503451234"))  # +380503451234
print(normalize_phone("(050)8889900"))  # +380508889900
print(normalize_phone("38050-111-22-22"))  # +380501112222
print(normalize_phone("38050 111 22 11 "))  # +380501112211