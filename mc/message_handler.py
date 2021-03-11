# /mc_add <USER>
# /mc_del <USER>
from mc.whitelist_handler import UserAlreadyExistsException


class IllegalMessageContentException(Exception):
    pass


def handle_message(message, whitelist_handler):
    if message.startswith('/mc_add'):
        try:
            username = _extract_username(message)
            whitelist_handler.add_user(username)
            return 'Great! You are now able to play minecraft on the server!'
        except IllegalMessageContentException:
            return 'Use me like /mc_add <YOUR_MINECRAFT_USERNAME>'
        except UserAlreadyExistsException:
            return 'Oh I just detected that you are already whitelisted! You\'re good to go'
    elif message.startswith('/mc_del'):
        try:
            username = _extract_username(message)
            whitelist_handler.del_user(username)
            return 'Oh no! That\'s very very sad! Hope to see you again some time!'
        except IllegalMessageContentException:
            return 'Use me like /mc_del <YOUR_MINECRAFT_USERNAME>'


def _extract_username(content):
    msg_parts = content.split(' ')
    if len(msg_parts) != 2:
        raise IllegalMessageContentException()
    return msg_parts[1]
