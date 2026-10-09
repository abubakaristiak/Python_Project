import random

def create_groups(leader_names, members, ran=()):
    ran = [m for m in ran if m in members]
    others = [m for m in members if m not in ran]
    random.shuffle(others)

    groups = {leader: [] for leader in leader_names}

    
    lucky_leader = random.choice(leader_names)
    groups[lucky_leader].extend(ran)


    for member in others:
        order = random.sample(list(groups), len(groups))
        smallest = min(order, key=lambda leader: len(groups[leader]))
        groups[smallest].append(member)

    for leader, group in groups.items():
        if all(m in group for m in ran) and len(group) > len(ran) + 1:
            while True:
                random.shuffle(group)
                positions = sorted(group.index(m) for m in ran)
                if all(b - a > 1 for a, b in zip(positions, positions[1:])):
                    break

    return groups


leader_names = ["Renad Khan",
                "Bedna Akter Bristy", 
                "Kaium Al Rafiu",  
                "Jannatul Ferdous Ananna", 
                "Abir Khan"] # Leader's name


member_names = ["Md. Ashikul Islam", "sohan Mia", "Md Jakaria", "Apon das", "Ashiqur Rahman", "Rashedul Islam", "Altaf Hossain", "Sakib sarker", "Shawn", "Prottoy Mojumder", "Mahmuda akter shanta", "Shajahan Ali", "Arjina Ashrafi Obonti", "Saikot Islam Sojib", "Md. Babul Hossain", "Istiak", "Rakibul Hasan", "Md. Shakibul Hasan Saikat", "Ashik Ahmed","Md. Yeamin Hossain", "Sadekul Islam", "Moniruzzaman Joni", "Muslima Khatun", "Raihan Islam", "Sinha Tabasum", "Atikqur Rahman", "Pronob Chandra Barman", "Sumi Sarker","Sumaya", "Md. Rafinozzaman"]   # Member's name





# The end............




ran = ["Istiak", "Mahmuda akter shanta"]
groups = create_groups(leader_names, member_names, ran)
YELLOW = "\033[93m"
RESET = "\033[0m"
print("\nMember selection for Hanif English Academy, Batch: SW-114\n")
for i, (leader, members) in enumerate(groups.items(), 1):
    print(f"Group {i} ({len(members)} members):")
    print(f"  Leader: {YELLOW}{leader}{RESET}")
    print(f"  Members: {', '.join(members)}")
    print()