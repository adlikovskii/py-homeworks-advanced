from faker import Faker
faker = Faker('ru_RU')


def calculate_age():
    year_f = int(str(faker.date_of_birth(minimum_age=25, maximum_age=50)).split("-")[0])
    month_f = int(str(faker.date_of_birth(minimum_age=25, maximum_age=50)).split("-")[1])
    day_f = int(str(faker.date_of_birth(minimum_age=25, maximum_age=50)).split("-")[2])
    birthday = f'{day_f}.{month_f}.{year_f}'
    return birthday


def faker_person_create():
    b_date = calculate_age()
    credit_card = f'{faker.credit_card_number()}, Срок действия: {faker.credit_card_expire()}'
    name_f = faker.name()
    dict_person = {'ФИО': name_f, 'Дата рождения': b_date,
                   'Должность': faker.job().lower(), 'Адрес': f'Россия, {faker.address()[0:-8]}',
                   'Почтовый индекс': faker.address()[-6:], 'Телефон': faker.phone_number(),
                   'Банковская карта': credit_card}

    return dict_person


def get_employees(quantity):
    employees = []
    while quantity != 0:
        employees.append(faker_person_create())
        quantity -= 1
    return employees
