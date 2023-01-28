import random

def handle_response(msg) -> str:
    p_message = msg.lower()

    if p_message == 'helloo':
        return 'Oh hello there!'
    
    if p_message == 'roll':
        return str(random.randint(1,1000))

    messages_roll = p_message.split()
    if len(messages_roll) == 3 and messages_roll[0] == "roll":
        if messages_roll[1].isnumeric() and messages_roll[2].isnumeric():
            return str(random.randint(int(messages_roll[1]),int(messages_roll[2])))
        else:
            return 'Gimme two numbers next time!'
    
    if p_message[:6] == "decide":
        messages_decide = p_message[6:].split(" or ")
        if len(messages_decide[0]) == 0:
            return 'Very funny.. you want me to decide or not?!'
        if len(messages_decide) == 1:
            return "You ain't giving me a choice here. Let's go with: " + messages_decide[0]
        else:
            return "My final decision is: " + random.choice(messages_decide)

    if p_message[0] == '!' and p_message[:5] != "!help":
        return "Uhm.. I might not be the best person to ask for that. But if you need a quick decision hit me up!"

    if p_message == '!help':
        return "Use !help roll/rollxy/decide if you want to know more about them."

    if p_message[:5] == "!help" and len(p_message) > 5:
        messages_help = p_message.split()
        if messages_help[1] == "roll":
            return "Use 'roll' and I'm gonna give you a random number."
        elif messages_help[1] == "rollxy":
            return "Use 'roll x y' and I'm gonna give you a number between x and y."
        elif messages_help[1] == "decide":
            return "Use 'decide x or y or ...' and I'm gonna pick one of your given options."