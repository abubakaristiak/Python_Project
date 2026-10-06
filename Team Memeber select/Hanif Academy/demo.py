import random

def create_groups(leader_names, members):
    members = members[:]        
    random.shuffle(members)

    groups = {leader: [] for leader in leader_names}

    for i, member in enumerate(members):
        leader = leader_names[i % len(leader_names)]
        groups[leader].append(member)

    return groups


leader_names = ["Bedna Akter Bristy", 
                "Jannatul Ferdous Ananna", 
                "Renad Khan", 
                "Kaium Al Rafiu", 
                "Abir Khan"] # Leader's name


member_names = ["Md. Ashikul Islam", "Md Ashadujjaman Asad", "sohan Mia", "Md Jakaria", "Apon das", "Ashiqur Rahman", "Rashedul Islam", "Altaf Hossain", "Sakib sarker", "Shawn", "Prottoy Mojumder", "Mahmuda akter shanta", "Shajahan Ali", "Arjina Ashrafi Obonti", "Md. Babul Hossain", "Istiak", "Rakibul Hasan", "Md. Shakibul Hasan Saikat", "Ashik Ahmed", "Abdullah Al Noman", "Md. Yeamin Hossain", "Mahbuba Akter", "Sadekul Islam", "Moniruzzaman Joni", "Muslima Khatun", "Jibon Ali", "Raihan Islam", "K.M. Mehbubul Hasan Emon", "Md. Iffat Salehin", "Md. Rafinozzaman", "Atiqur Rahman", "Anas", "Pronob Chandra Barman", "Sinha tabasum", "Sumi Sarker", "Mobashsira Akter Sumaiya"]  # Member's name

groups = create_groups(leader_names, member_names)








YELLOW = "\033[93m"
RESET = "\033[0m"

print("\nMember selection for Hanif English Academy, Batch: SW-114\n")
for i, (leader, members) in enumerate(groups.items(), 1):
    print(f"Group {i} ({len(members)} members):")
    print(f"  Leader: {YELLOW}{leader}{RESET}")
    print(f"  Members: {', '.join(members)}")
    print()