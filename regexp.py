from pprint import pprint
import re
import csv

with open("./data_files/phonebook_raw.csv") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

def format_name(contacts_list):
    format_name_list = []
    pattern = re.compile(r'^([А-Яа-я]+)[\s|,]([А-Яа-я]+)[\s|,]([А-Яа-я]+|)')
    replacer = r'\1, \2, \3'
    for people in contacts_list:
        people = ','.join(people)
        result = [pattern.sub(replacer, people)]
        format_name_list.append(result)
    return format_name_list

def format_telephone(contacts_list):
    format_telephone_list = []
    pattern = re.compile(r'(\+7|8)(\s*)((\()\d+(\))|\d{3})(\s*|-)(\d{3})(-|\s*)(\d{2})(-|\s*)(\d{2})(\s*)(\(|)|(\w+.)(\s)(\d+)')
    replacer = r'+7(\3)\7-\9-\11 \14\16'
    for people in contacts_list:
        people = ','.join(people)
        result = [pattern.sub(replacer, people)]
        format_telephone_list.append(result)
    return format_telephone_list

format_name_telephone_list = format_telephone(format_name(contacts_list))

def delete_duplicates(contacts_list):
    new_list_contact = []
    for contact in contacts_list:
        contact = ' '.join(contact)
        contact = contact.split(',')
        new_list_contact.append(contact)

    for contact in new_list_contact:
        while contact[3] == '':
            del(contact[3])

    name_list = []
    set_list_contact = []
    for contact in new_list_contact:
        if contact[0] not in name_list:
            name_list.append(contact[0])
            set_list_contact.append(contact)
    return set_list_contact

contacts_list = delete_duplicates(format_name_telephone_list)

with open("./data_files/phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contacts_list)
pprint(contacts_list)