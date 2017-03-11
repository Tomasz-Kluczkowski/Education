"""
6.Create a new class, SMS_store. The class will instantiate SMS_store objects, similar to an inbox or outbox on a cellphone:
"""
import datetime
from unit_testing import test

class SMS_store:
    """ sms holding class """
    msg_list = []
    msg_count = 0


    def __init__(self):
        pass


    def add_new_arrival(self, from_number, time_arrived, text_of_SMS):
        """ Adds a new message to the msg_list """
        SMS_store.msg_list.append((False, from_number, time_arrived, text_of_SMS))
        SMS_store.msg_count += 1


    def message_count(self):
        """ Returns numer of messages in my_inbox """
        return SMS_store.msg_count

    def get_unread_indexes(self):
        """ Returns a list of indexes of all not yet viewed SMS messages """
        index_list = []
        for (ix, item) in enumerate(SMS_store.msg_list):
            if item[0] == False:
                index_list.append(ix)
        return index_list

    def get_message(self, index):
        """ Return (from number, time_arrived, text_of_SMS) for message[index]
        also change state to has been viewed.
        If there is no message at postition index return None."""
        SMS_store.msg_list[index] = (True, ) + SMS_store.msg_list[index][1:]

        return SMS_store.msg_list[index][1:]

    def delete(self, index):
        """ Deletes the message at index """
        del(SMS_store.msg_list[index])
        SMS_store.msg_count -= 1

    def clear(self):
        """ Deletes all messages from the inbox """
        SMS_store.msg_list = []
        SMS_store.msg_count = 0



my_inbox = SMS_store()
time = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
my_inbox.add_new_arrival("00447403344912", time, "test sms message")
test(my_inbox.message_count(), 1)
my_inbox.add_new_arrival("00481234567865", time, "message from Poland")
test(my_inbox.message_count(), 2)
my_inbox.add_new_arrival("+4434563342344", time, "wiadomosc dnia")
test(my_inbox.message_count(), 3)

test(my_inbox.get_unread_indexes(), [0,1,2])
test(my_inbox.get_message(0), ("00447403344912", time, "test sms message"))
test(my_inbox.get_unread_indexes(), [1,2])
test(my_inbox.delete(0), )

