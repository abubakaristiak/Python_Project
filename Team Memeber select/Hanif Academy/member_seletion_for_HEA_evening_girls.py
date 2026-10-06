import random

def create_groups(leader_names, members):
    members = members[:]        
    random.shuffle(members)

    groups = {leader: [] for leader in leader_names}

    for i, member in enumerate(members):
        leader = leader_names[i % len(leader_names)]
        groups[leader].append(member)

    return groups


leader_names = ["Shanjida Islam", 
                "Chiiti Rani"
                ] # Leader's name


member_names = ["Sweet", "Borsha", "Mst. Asia Akter","Nishu Rani", "Masuma Akter Shormi",  "Shirajun Monira"];  # Member's name

groups = create_groups(leader_names, member_names)












YELLOW = "\033[93m"
RESET = "\033[0m"

print("\nMember selection for Hanif English Academy, Batch: SW-120\n")
for i, (leader, members) in enumerate(groups.items(), 1):
    print(f"Group {i} ({len(members)} members):")
    print(f"  Leader: {YELLOW}{leader}{RESET}")
    print(f"  Members: {', '.join(members)}")
    print()