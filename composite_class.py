class CellPhone:

    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.account_balance = 0
        self.pin = "pin"
        self.contact_list = {}
        self.call_log = []

    def make_call(self, phone_number):
        self.call_log.append(phone_number)

    def show_call_log(self):
        print(self.call_log)

    def clear_call_log(self):
        print(self.call_log.clear())

    def add_contact(self, name, phone_number):
        self.contact_list.setdefault(name, phone_number)

    def get_contact(self, name):
        print(self.contact_list[name])

    def change_contact(self, name, number, new_pin):
        self.contact_list.update({name: number})
        self.pin = new_pin

    def del_contact(self, name):
        if name in self.contact_list.keys():
            del self.contact_list[name]


# Creating instance and making calls


phone = CellPhone(571398938)
phone.make_call(5444)
phone.make_call(3444)
phone.show_call_log()
phone.clear_call_log()
phone.show_call_log()
phone.add_contact("kay", 7503)
phone.add_contact("Nicole", 2433)
phone.del_contact("Nicole")
phone.change_contact("rick", 7565, 234)
phone.get_contact("kay")


class Messaging:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.message_log = []

    def make_message(self, phone_number):
        self.message_log.append(phone_number)

    def show_message_log(self):
        print(self.message_log)

    def clear_message_log(self):
        print(self.message_log.clear())


# Creating instance and sending messages

message = Messaging(23445)
message.make_message('thia is a message')
message.make_message('this is the second message')
message.show_message_log()
message.clear_message_log()


class CompositeCellPhone(CellPhone, Messaging):
    def __init__(self):
        self.email = "Kings"
        self.combined_log = (self.message_log + self.call_log)

    def email_contact(self):
        print(self)

    def combined_logs(self):
        print(self.combined_log)

    def erase_all_logs(self):
        pass


joined = CompositeCellPhone
joined.combined_logs()
joined.email_contact()