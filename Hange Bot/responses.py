import random
import json

def handle_response(msg, username, permission) -> str:
    p_message = msg.lower()
    users = []
    message_split = p_message.lower().split()

    with open('hange_users.json') as f:
        users = json.load(f)
        
    usernames = []
    for i in range(len(users)):
        usernames.append(users[i]["username"])

    if p_message == 'helloo':
        return 'Oh hello there!'
    
    if p_message == "roll" or p_message == "r":
        return str(random.randint(1,1000))

    if len(message_split) == 3 and message_split[0] == "roll" or message_split[0] == "r":
        if message_split[1].isnumeric() and message_split[2].isnumeric():
            return str(random.randint(int(message_split[1]),int(message_split[2])))
        else:
            return 'Gimme two numbers next time!'
    
    command = message_split[0].split("!")
    if command[0] == "decide" or command[0] == "d":
        options = " ".join(message_split[1:]).split(" or ")
        if len(command) == 2:
            if not command[1].isnumeric():
                return "If you want me to make multiple disicions give me a number next time!"
            else:
                rep = int(command[1])
                index = 0
                decisions = []
                
                if options[0] == '':
                    return 'Very funny.. you want me to decide or not?!'
                elif len(options) == 1 and options[0] != '':
                    if username in usernames:
                        for i in range(len(usernames)):
                            if users[i]["username"] == username:
                                if options[0] in users[i]["decisions"]:
                                    for j in range(len(users[i]["decisions"])):
                                        if users[i]["decisions"][j] == options[0]:
                                            while index < rep:
                                                decisions.append(random.choice(users[i]["options"][j]))
                                                index += 1
                                else:
                                    return "You ain't giving me a choice here. Let's go with: " + options[0] + " x " + str(rep) + " times"
                    else:
                        return "You ain't giving me a choice here. Let's go with: " + options[0] + " x " + str(rep) + " times"
                else:
                    while index < rep:
                        decisions.append(random.choice(options))
                        index += 1
                return "My final decision is: " + ', '.join(decisions)
        else:
            if options[0] == '':
                return 'Very funny.. you want me to decide or not?!'
            elif len(options) == 1 and options[0] != '':
                if username in usernames:
                    for i in range(len(usernames)):
                        if users[i]["username"] == username:
                            if options[0] in users[i]["decisions"]:
                                for j in range(len(users[i]["decisions"])):
                                    if users[i]["decisions"][j] == options[0]:
                                        return "My final decision is: " + random.choice(users[i]["options"][j])
                            else:
                                return "You ain't giving me a choice here. Let's go with: " + options[0]
                else:
                    return "You ain't giving me a choice here. Let's go with: " + options[0]
            else:
                return "My final decision is: " + random.choice(options)

    if message_split[0] == "decisionadd" or message_split[0] == "da":
        if permission == "YES":
            options = " ".join(message_split[2:]).split(" or ")
            if len(message_split) >= 3:
                if username not in usernames:
                    decisions = []
                    decisions.append(message_split[1])

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
                            if message_split[1] in users[i]["decisions"]:
                                return "You already have a decision saved with that name. You can either edit it or give this another name."
                            else:
                                users[i]["decisions"].append(message_split[1])
                                users[i]["options"].append(options)
                
                with open('hange_users.json', 'w') as ff:
                    json.dump(users, ff, indent=4, separators=(',', ': '))
                return "I'm gonna remember this one."
            else:
                return "Not enough parameters! Use '?decisions' to learn more about them."
        else:
            return "You have no permission to do that!"

    if message_split[0] == "decisionview" or message_split[0] == "dv":
        if username not in usernames:
            return "You have 0 saved decisions. Use '?decision' to learn more about those commands."
        elif username in usernames:
            for i in range(len(users)):
                if users[i]["username"] == username:
                    if len(users[i]["decisions"]) == 0:
                        return "You have 0 saved decisions. Use '?decision' to learn more about those commands."
                    elif len(message_split) == 1:
                        return "Your saved decision(s): " + ' '.join(users[i]["decisions"])
                    else:
                        if message_split[1] in users[i]["decisions"]:
                            for j in range(len(users[i]["decisions"])):
                                if users[i]["decisions"][j] == message_split[1]:
                                    return "The options for the decision are: " + " or ".join(users[i]["options"][j])
                        else:
                            return "You don't have saved decision with that name. Use 'decisionview' or 'dv' to look at all your saved decisions."

    if message_split[0] == "decisionrename" or message_split[0] == "dre":
        if permission == "YES":
            if len(message_split) == 3:
                old_name = message_split[1]
                new_name = message_split[2]
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
        else:
            return "You have no permission to do that!"

    if message_split[0] == "decisionremove" or message_split[0] == "dr":
        if permission == "YES":
            if len(message_split) == 2:
                if username not in usernames:
                    return "You don't have any saved decisions. Use '?decision' to learn more about those commands."
                elif username in usernames:
                    for i in range(len(users)):
                        if users[i]["username"] == username:
                            if message_split[1] not in users[i]["decisions"]:
                                return "You don't have a saved decision with that name. Use 'decisionview' or 'dv' to look at your saved decisions."
                            else:
                                decisions_new = []
                                options_new = []
                                for j in range(len(users[i]["decisions"])):
                                    if users[i]["decisions"][j] != message_split[1]:
                                        decisions_new.append(users[i]["decisions"][j])
                                        options_new.append(users[i]["options"][j])
                                
                                users[i]["decisions"] = decisions_new
                                users[i]["options"] = options_new
                                with open('hange_users.json', 'w') as ff:
                                    json.dump(users, ff, indent=4, separators=(',', ': '))
                                return "Okay, let's forget it."
            else:
                return "Wrong parameters! Use '?decisions' to learn more about them."
        else:
            return "You have no permission to do that!"
    
    if message_split[0] == "decisioneditadd" or message_split[0] == "dea":
        if permission == "YES":
            if len(message_split) >= 3:
                options = " ".join(message_split[2:]).split(" or ")
                if username not in usernames:
                    return "You don't have any saved decisions. Use '?decision' to learn more about those commands."
                else:
                    for i in range(len(users)):
                        if users[i]["username"] == username:
                            if message_split[1] not in users[i]["decisions"]:
                                return "You don't have a saved decision with that name. Use 'decisionview' or 'dv' to look at your saved decisions."
                            else:
                                for j in range(len(users[i]["decisions"])):
                                    if users[i]["decisions"][j] == message_split[1]:
                                        for k in range(len(options)):
                                            users[i]["options"][j].append(options[k])

                                with open('hange_users.json', 'w') as ff:
                                    json.dump(users, ff, indent=4, separators=(',', ': '))
                                return "Okay, changes noted."
            else:
                return "Not enough parameters! Use '?decisions' to learn more about them."
        else:
            return "You have no permission to do that!"

    if message_split[0] == "decisioneditchange" or message_split[0] == "dec":
        if permission == "YES":
            options = " ".join(message_split[2:]).split(" to ")
            if len(message_split) >= 5 and len(options) == 2:
                if username not in usernames:
                    return "You don't have any saved decisions. Use '?decision' to learn more about those commands."
                else:
                    for i in range(len(users)):
                        if users[i]["username"] == username:
                            if message_split[1] not in users[i]["decisions"]:
                                return "You don't have a saved decision with that name. Use 'decisionview' or 'dv' to look at your saved decisions."
                            else:
                                for j in range(len(users[i]["decisions"])):
                                    if users[i]["decisions"][j] == message_split[1]:
                                        if options[0] not in users[i]["options"][j]:
                                            return "You don't have a saved option like that. Use 'decisionview' or 'dv' to look at your saved decisions."
                                        else:
                                            for k in range(len(users[i]["options"][j])):
                                                if users[i]["options"][j][k] == options[0]:
                                                    users[i]["options"][j][k] = options[1]

                                with open('hange_users.json', 'w') as ff:
                                    json.dump(users, ff, indent=4, separators=(',', ': '))
                                return "Okay, changes noted."
            else:
                return "Not enough parameters! Use '?decisions' to learn more about them."
        else:
            return "You have no permission to do that!"

    if message_split[0] == "decisioneditdelete" or message_split[0] == "ded":
        if permission == "YES":
            option = message_split[2:]
            if len(message_split) >= 3:
                if username not in usernames:
                    return "You don't have any saved decisions. Use '?decision' to learn more about those commands."
                else:
                    for i in range(len(users)):
                        if users[i]["username"] == username:
                            if message_split[1] not in users[i]["decisions"]:
                                return "You don't have a saved decision with that name. Use 'decisionview' or 'dv' to look at your saved decisions."
                            else:
                                for j in range(len(users[i]["decisions"])):
                                    if users[i]["decisions"][j] == message_split[1]:
                                        if option[0] not in users[i]["options"][j]:
                                            return "You don't have a saved option like that. Use 'decisionview' or 'dv' to look at your saved decisions."
                                        else:
                                            options_new = []
                                            for k in range(len(users[i]["options"][j])):
                                                if users[i]["options"][j][k] != option[0]:
                                                    options_new.append(users[i]["options"][j][k])
                                        users[i]["options"][j] = options_new

                                with open('hange_users.json', 'w') as ff:
                                    json.dump(users, ff, indent=4, separators=(',', ': '))
                                return "Okay, changes noted."
            else:
                return "Not enough parameters! Use '?decisions' to learn more about them."
        else:
            return "You have no permission to do that!"
    
    if p_message[0] == '!' and p_message != "!help":
        return "Uhm.. I might not be the best person to ask for that. But if you need a quick decision hit me up!"

    if p_message == '!help':
        return "Use '?roll'/'?rollxy'/'?decide'/'?decision' if you want to know more about them."

    if p_message == "?roll":
        return "Use 'roll' or 'r' and I'm gonna give you a random number."
    elif p_message == "?rollxy":
        return "Use 'roll x y' or 'r x y' and I'm gonna give you a number between x and y."
    elif p_message == "?decide":
        return "Use 'decide x or y or ...' or 'd x or y or ...' or 'decide saved_decision' and I'm gonna pick one of your given options. If you added a frequent decision you can also use 'decide decision_name'. If you want me to decide it multiple times use 'decide!x'/'d!x' instead."
    elif p_message == "?decision":
        return "I can remember frequent decisions. You can access them by 'decide decision_name'. Use '?decisionadd'/'?decisionrename'/'?decisionedit'/'?decisionremove'/'?decisionview' if you want to know more about them."
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
