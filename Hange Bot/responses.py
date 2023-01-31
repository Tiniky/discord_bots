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

    messages_decisions = p_message.split()
    if messages_decisions[0] == "decisionadd" or messages_decisions[0] == "da":
        options = " ".join(messages_decisions[2:]).split(" or ")
        if len(messages_decisions) >= 3:
            if username not in usernames:
                decisions = []
                decisions.append(messages_decisions[1])

                alloptions = []
                alloptions.append(options)

                users.append({
                    "username": username,
                        "decisions": decisions,
                        "options": alloptions
                })
            else:
                for i in range(len(users)):
                    if users[i]["username"] == username:
                        if messages_decisions[1] in users[i]["decisions"]:
                           return "You already have a decision saved with that name. You can either edit it or give this another name."
                        else:
                            users[i]["decisions"].append(messages_decisions[1])
                            users[i]["options"].append(options)
            
            with open('hange_users.json', 'w') as ff:
                json.dump(users, ff, indent=4, separators=(',', ': '))
            return "I'm gonna remember this one."
        else:
            return "Not enough parameters! Use '?decisions' to learn more about them."

    if messages_decisions[0] == "decisionview" or messages_decisions[0] == "dv":
        if username not in usernames:
            return "You have 0 saved decisions. Use '?decision' to learn more about those commands."
        elif username in usernames:
            for i in range(len(users)):
                if users[i]["username"] == username:
                    if len(users[i]["decisions"]) == 0:
                        return "You have 0 saved decisions. Use '?decision' to learn more about those commands."
                    elif len(messages_decisions) == 1:
                        return "Your saved decision(s): " + ' '.join(users[i]["decisions"])
                    else:
                        if messages_decisions[1] in users[i]["decisions"]:
                            for j in range(len(users[i]["decisions"])):
                                if users[i]["decisions"][j] == messages_decisions[1]:
                                    return "The options for the decision are: " + " or ".join(users[i]["options"][j])
                        else:
                            return "You don't have saved decision with that name. Use 'decisionview' or 'dv' to look at all your saved decisions."

    if messages_decisions[0] == "decisionrename" or messages_decisions[0] == "dre":
        if len(messages_decisions) == 3:
            old_name = messages_decisions[1]
            new_name = messages_decisions[2]
            if username not in usernames:
                return "You don't have any saved decisions. Use '?decision' to learn more about those commands."
            elif username in usernames:
                for i in range(len(users)):
                    if users[i]["username"] == username:
                        if old_name not in users[i]["decisions"]:
                            return "You don't have a saved decision with that name. Use 'decisionview' or 'dv' to look at your saved decisions."
                        else:
                            for j in range(len(users[i]["decisions"])):
                                if users[i]["decisions"][j] == old_name:
                                    users[i]["decisions"][j] = new_name
                            
                            with open('hange_users.json', 'w') as ff:
                                json.dump(users, ff, indent=4, separators=(',', ': '))
            return "Change noted."
        else:
            return "Wrong parameters! Use '?decisions' to learn more about them."

    if messages_decisions[0] == "decisionremove" or messages_decisions[0] == "dr":
        if len(messages_decisions) == 2:
            if username not in usernames:
                return "You don't have any saved decisions. Use '?decision' to learn more about those commands."
            elif username in usernames:
                for i in range(len(users)):
                    if users[i]["username"] == username:
                        if messages_decisions[1] not in users[i]["decisions"]:
                            return "You don't have a saved decision with that name. Use 'decisionview' or 'dv' to look at your saved decisions."
                        else:
                            decisions_new = []
                            options_new = []
                            for j in range(len(users[i]["decisions"])):
                                if users[i]["decisions"][j] != messages_decisions[1]:
                                    decisions_new.append(users[i]["decisions"][j])
                                    options_new.append(users[i]["options"][j])
                            
                            users[i]["decisions"] = decisions_new
                            users[i]["options"] = options_new
                            with open('hange_users.json', 'w') as ff:
                                json.dump(users, ff, indent=4, separators=(',', ': '))
                            return "Okay, let's forget it."
        else:
            return "Wrong parameters! Use '?decisions' to learn more about them."
        
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
