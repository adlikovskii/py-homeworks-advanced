import json
from datetime import datetime
from application import salary
from application.db import people

quantity = 2  # Количество сотрудников в фирме


def salary_calculation():
    complete = []
    employees = people.get_employees(quantity)
    for e in employees:
        j = json.loads(json.dumps(e))
        complete.append([j['ФИО'], j['Банковская карта'], salary.calculate_salary()])
    return complete


if __name__ == '__main__':
    print(f'Сегодня: {datetime.now().strftime("%d.%m.%Y")} выдача зарплаты у следующих сотрудников:')
    for i in salary_calculation():
        print(f'ФИО: {i[0]}, Банковская карта: {i[1]}, К выплате: {i[2]} рублей.')
