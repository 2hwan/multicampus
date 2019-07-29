class Contact:
    def __init__(self, name, phone_number, e_mail, addr):
        self.name = name
        self.phone_number = phone_number
        self.e_mail = e_mail
        self.addr = addr

    def print_info(self):
        print('Name: ', self.name)
        print('Phone Number: ', self.phone_number)
        print('E-mail: ', self.e_mail)
        print('Address: ', self.addr)

def print_menu():
    print('1. 연락처 입력')
    print('2. 연락처 출력')
    print('3. 연락처 삭제')
    print('4. 종료')
    menu = input('메뉴선택: ')
    return int(menu)

def input_item(title):
    while 1:
        try:
            val = input(title)
            if len(val) < 2:
                raise ValueError
            else: break
        except ValueError:
            print('%s is too short' % title)
    return val

def set_contact(contact_list):
    while 1:
        name = input_item('Name: ')

        for i in contact_list:
            if i.name == name :
                print('같은이름 중복 불가!')
                break
        else : break
    phone_number = input_item('Phone Number: ')
    e_mail = input_item('E-mail: ')
    address = input_item('Address: ')

    contact = Contact(name, phone_number, e_mail, address)
    contact_list.append(contact)

def print_contact(contact_list):
    for contact in contact_list:
        contact.print_info()
        print('-' * 50)

def delete_contact(contact_list):
    name = input('삭제 할 사람 : ')
    for i, contact in enumerate(contact_list):
        if contact.name == name :
            del contact_list[i]

def store_contact(contact_list):
    with open('contact_db.txt','wt') as f:
        for contact in contact_list :
            f.write(contact.name + '\n')
            f.write(contact.phone_number + '\n')
            f.write(contact.e_mail + '\n')
            f.write(contact.addr + '\n')

def load_contact(contact_list):
    with open('contact_db.txt','rt') as f:
        lines = f.readlines()
        num = int(len(lines)/4)

        for i in range(num):
            name = lines[i*4].rstrip('\n')
            phone_number = lines[i*4 +1].rstrip('\n')
            e_mail = lines[i *4 +2].rstrip('\n')
            addr = lines[i*4 +3].rstrip('\n')

            contact = Contact(name,phone_number,e_mail,addr)
            contact_list.append(contact)

def run():
    contact_list = []
    load_contact(contact_list)
    while 1:
        menu = print_menu()
        if menu == 1:
            set_contact(contact_list)
        elif menu == 2:
            print_contact(contact_list)
        elif menu == 3:
            delete_contact(contact_list)
        elif menu == 4:
            store_contact(contact_list)
            break



if __name__ == "__main__" :
    run()