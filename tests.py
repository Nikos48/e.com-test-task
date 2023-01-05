from get import find_data_by_query

print(1, find_data_by_query("login=nikos&password=12345"))
print(2, find_data_by_query(
    "user_phone=+7 961 228 77 93&user_email=episkoposyan2044@gmail.com"))
print(3, find_data_by_query("host=+7 928 234 85 27&destination=+7 961 446 23 87"))
print(4, find_data_by_query(
    "host=vovochka2015@mail.ru&destination=lenochkadevochka@yahoo.com"))
print(5, find_data_by_query("host=vovochka2015@mail.ru&destination=+7 961 446 23 87"))
