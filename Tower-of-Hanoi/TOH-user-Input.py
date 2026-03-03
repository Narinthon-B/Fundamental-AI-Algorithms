move_count = 0
def tower_of_hanoi(num, source, aux, target, show_details):
    global move_count
    if num == 1:
        move_count += 1
        if show_details:
            print(f"Move disk 1 from {source} to {target}")
        return

    tower_of_hanoi(num-1, source, target, aux, show_details)
    move_count += 1
    if show_details:
        print(f"Move disk {num} from {source} to {target}")
    tower_of_hanoi(num-1, aux, source, target, show_details)

user_input = input("Enter number of disks (Press Enter for default 5): ")
if user_input.strip() == "":
    n = 5
else:
    n = int(user_input)

show_details = True
if n > 5:
    show_details = False
    print(f"N = {n}")

tower_of_hanoi(n, 'A', 'B', 'C', show_details)
print("-" * 30)
print(f"Total moves: {move_count} times")
print("-" * 30)