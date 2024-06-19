import random
print("Create group")
def create_groups(leader_names, members, group_size):
    # Shuffle the members list
    random.shuffle(members)
    
    # Create empty groups
    groups = []
    
    # Assign leaders to their own groups
    for leader in leader_names:
        groups.append([(leader, [])])
    
    # Distribute members into groups
    group_index = 0
    for member in members:
        # Check if the current group is full
        if len(groups[group_index % len(groups)][0][1]) == group_size:
            # Move to the next group
            group_index += 1
        # Append member to the current group
        groups[group_index % len(groups)][0][1].append(member)
        group_index += 1
    
    return groups

# Example usage
leader_names = ["Sayam", "Ajmire", "Jaynab"]  # Example group leader names
member_names = ["Tuhid", "Istiak", "Israt", "Isnan", "Dider", "Swarup", "Shojib", "Shaluk", "Isnan1", "Dider1", "Swarup1" ]  # Example member names
group_size = 5  # Example group size

groups = create_groups(leader_names, member_names, group_size)

# Print groups
print("Project Member selection for Batch-09")
for i, group in enumerate(groups, 1):
    print(f"Group {i}:")
    leader, members = group[0]  # Extract leader and members from the group tuple
    print(f"  Leader: {leader}")
    print(f"  Members: {', '.join(members)}")
    print()