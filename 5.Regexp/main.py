import re
# читаем адресную книгу в формате CSV в список contacts_list
import csv

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

# TODO 1: выполните пункты 1-3 ДЗ
# Поместить Фамилию, Имя и Отчество человека в поля lastname, firstname и surname.
for contact in contacts_list[1:]:
    name = contact[0], contact[1], contact[2]
    full_name = " ".join(name).split()
    contact_id = 0
    for update in full_name:
        contact[contact_id] = update
        contact_id += 1

# Привести все телефоны в формат +7(999)999-99-99. С добавочным номером, формат будет такой: +7(999)999-99-99 доб.9999.
pattern = re.compile(
    r'(\+7|8)?\s*\(?(\d{3})\)?[-\s]?(\d{3})-?(\d{2})-?(\d{2})((\s)?\(?(доб.)?\s?(\d+)\)?)?')
substitution = r'+7(\2)\3-\4-\5\7\8\9'
for contact in contacts_list:
    contact[5] = pattern.sub(substitution, contact[5])

# Объединить все дублирующиеся записи о человеке в одну.
new_contacts_list = [i for i in contacts_list[:1]]
for contact in contacts_list[1:]:
    name = contact[0], contact[1]
    for check in contacts_list[1:]:
        check_name = check[0], check[1]
        if name == check_name:
            contact_id = 2
            while contact_id < 7:
                if contact[contact_id] == '':
                    contact[contact_id] = check[contact_id]
                contact_id += 1

    if contact not in new_contacts_list:
        new_contacts_list.append(contact)


# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(new_contacts_list)
