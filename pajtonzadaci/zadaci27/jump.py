jump_list = []
jump = 0

while True:
    jump = int(input("Input jump in meters: "))
    
    if jump == 0:
        break
    else:
        jump_list.append(jump)

farthest_jump = lambda jump_list : max(jump_list)
closest_jump = lambda jump_list : min(jump_list)

print("The farthest jump is", farthest_jump(jump_list), "m, while the closest is", closest_jump(jump_list), "m")
