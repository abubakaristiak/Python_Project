import random

def create_groups(leader_names, members):
    members = members[:]        
    random.shuffle(members)

    groups = {leader: [] for leader in leader_names}

    for i, member in enumerate(members):
        leader = leader_names[i % len(leader_names)]
        groups[leader].append(member)

    return groups


leader_names = ["Nasim Reja",
                "Md. Nahid Hassan",
                "Rakibul Hasan",
                "Angkan Das",
                "Sagor Sheikh"] # Leader's name


member_names = ["Al Mamun", "Forhad Hosen", "Shahariar", "Md. Forhadul Islam", "Jahid Hasan", "Zahidul Islam", "Majharul Islam Tuhin", "Mehedi", "Md. Rezwan Islam", "Rifat Jone", "Md. Parvaj Hasan Tuhin", "Joy Sarkar", "Md. Bipul Hossen", "Md. Maruf Hossain", "Md Maruf Hossain", "Tahsin Ahmed", "Md. Bijoy Hossen", "Md. Zisun Islam", "Md. Shahik Anom", "Raihan", "Md. Khademul Islam Rabbi", "Md. Rifat Ali", "Md. Tanvir Hasan", "Mukhlesur Rahman", "Sadhan Chandro Barman", "Emon Hossain", "Jihad Mahmud", "MD Ashadujjanman Atik"];  # Member's name

groups = create_groups(leader_names, member_names)












YELLOW = "\033[93m"
RESET = "\033[0m"

print("\nMember selection for Hanif English Academy, Batch: SW-120\n")
for i, (leader, members) in enumerate(groups.items(), 1):
    print(f"Group {i} ({len(members)} members):")
    print(f"  Leader: {YELLOW}{leader}{RESET}")
    print(f"  Members: {', '.join(members)}")
    print()