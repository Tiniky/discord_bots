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

    if p_message[:9] == "decision" or p_message[:3] == "da" or p_message[:3] == "dr" or p_message[:3] == "dv" or p_message[:4] == "dea" or p_message[:4] == "dec" or p_message[:4] == "ded":
        messages_decision = p_message.split("")
        if messages_decision[0] == "decisionview" or messages_decision[0] == "dv":
            if username not in usernames:
                return "You have 0 saved decisions. Use '?decision'to learn more about those commands."
            elif username in usernames:
                for i in range(len(users)):
                    if users[i]["username"] == username and len(users[i]["decisions"] == 0):
                        return "You have 0 saved decisions. Use '?decision'to learn more about those commands."
                    elif users[i]["username"] == username and len(users[i]["decisions"] == 1):
                        return "Your saved decision: " + ' '.join(map(str, users[i]["decisions"]))
                    else:
                        if messages_decision[1] in users[i]["decisions"]:
                            for j in range(len(users[i]["decisions"])):
                                if users[i]["decisions"][j] == messages_decision[1]:
                                    return "The options for the decision are: " + users[i]["options"][j][1].join(" or " + e for e in users[i]["options"][j][1:])

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
    elif p_message == "?decisionedit":
        return "Use 'decisioneditadd(/dea) name x or ...' to add more options.  Use 'decisioneditchange(/dec) name option_before option_after' to change a saved option. Use 'decisioneditdelete(/ded) name option' to delete a saved option."
    elif p_message == "?decisionremove":
        return "Use 'decisionremove(/dr) name' to delete a saved decision."
    elif p_message == "?decisionview":
        return "Use 'decisionview' or 'dv' to view your saved decision. Use 'decisionview(/dv) name' to view the options of a saved decision."
