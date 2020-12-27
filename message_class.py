class Messaging:
    def __init__(self, phone_number):
        self.message_log = []
        self.call_log = []

    def make_message(self, phone_number):
        self.call_log.append(phone_number)

    def show_message_log(self):
        print(self.call_log)

    def clear_message_log(self):
        print(self.call_log.clear())


#Creating instance and sending messages 

message = Messaging("This is a test")
message.make_message(356-364-949)
message.make_message(3455)
message.show_message_log()
message.show_message_log()

