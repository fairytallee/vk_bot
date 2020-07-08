from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
from datetime import datetime

token, password = '592e0379fe0a29fdb4999c18e33780df7216a32d7220bd85e7e70c372c7b2ba7004e9e489b223e77e1bb2', 'ddr4redz'

vk_session = vk_api.VkApi(token=token)

session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print('сообщение пришло в:', str(datetime.strftime(datetime.now(), "%H:%M:%S")))
            print('Текст сообщения:', str(event.text))
            print('user id:', event.user_id)
            cur_user_id = event.user_id

            current_mes = event.text.lower()
            if event.from_user and not (event.from_me):
                if "приве" in current_mes or "ку" in current_mes:
                    vk_session.method('messages.send', {'user_id': cur_user_id, 'message': 'Приветик',
                                                        'random_id': 0})



