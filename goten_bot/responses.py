#Exported to bot so responses can be said if correct words are passed in

import random

def handle_response(message) -> str: #message: str
    p_message = message.lower()

    if p_message == 'hello':
        return 'Sup?!'
    
    if p_message == 'hey':
        return "How's it going??"
    
    if p_message == 'roll':
        return str(random.randint(1,6))
    
    if p_message == '!help':
        return "`Can't help you bud, I'm just a bot...`"