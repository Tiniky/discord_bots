import random

def handle_response(msg) -> str:
    p_message = msg.lower()
    users = []

    with open('hange_users.json') as f:
        users = json.load(f)
        
    usernames = []
    for i in range(len(users)):
        usernames.append(users[i]["username"])

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

    #decisions in progress

    if p_message[0] == '!' and p_message != "!help":
        return "Uhm.. I might not be the best person to ask for that. But if you need a quick decision hit me up!"

    if p_message == '!help':
        return "Use '?roll'/'?rollxy'/'?decide'/'?decision' if you want to know more about them."

    if p_message == "?roll":
        return "Use 'roll' or 'r' and I'm gonna give you a random number."
    elif p_message == "?rollxy":
        return "Use 'roll x y' or 'r x y' and I'm gonna give you a number between x and y."
    elif p_message == "?decide":
        return "Use 'decide x or y or ...' or 'd x or y or ...' and I'm gonna pick one of your given options. If you added a frequent decision you can also use 'decide decision_name'."
    elif p_message == "?decision":
        return "I can remember frequent decisions. You can access them by 'decide decision_name'. Use '?decisionadd'/'?decisionedit'/'?decisionremove'/'?decisionview' if you want to know more about them."
    elif p_message == "?decisionadd":
        return "Use 'decisionadd(/da) name x or y or ...' and I'm gonna remember this decision."
    elif p_message == "?decisionrename":
        return "Use 'decisionrename(/dre) old_name new_name' to rename a decision."
    elif p_message == "?decisionedit":
        return "Use 'decisioneditadd(/dea) name x or ...' to add more options.  Use 'decisioneditchange(/dec) name option_before option_after' to change a saved option. Use 'decisioneditdelete(/ded) name option' to delete a saved option."
    elif p_message == "?decisionremove":
        return "Use 'decisionremove(/dr) name' to delete a saved decision."
    elif p_message == "?decisionview":
        return "Use 'decisionview' or 'dv' to view your saved decision. Use 'decisionview(/dv) name' to view the options of a saved decision."
