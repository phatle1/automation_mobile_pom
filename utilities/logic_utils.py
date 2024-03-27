from datetime import datetime
import string
import random


class Logic_Util:
    @staticmethod
    def id_generator(size=6, chars=string.ascii_lowercase + string.digits) -> str:
        return ''.join(random.choice(chars) for _ in range(size))

    @staticmethod
    def readable_time_generator():
        current_time = datetime.now()
        time_with_format = current_time.strftime('%b %d, %Y')
        return time_with_format


# print(str(Logic_Util.id_generator()))
# print(Logic_Util.readable_time_generator())


abc = 'aklfhasfhashflashdflkjh'
id = Logic_Util.id_generator()
# print(abc)
# print(id)
print(f'{''.join((id, abc))}')
