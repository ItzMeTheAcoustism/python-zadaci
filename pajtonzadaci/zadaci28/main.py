weight_list = []
weight = 0

while True:
    weight = int(input("Input weight: "))
    
    if weight == 0:
        break
    else:
        weight_list.append(weight)

weight_index = lambda weight_list : (sum(weight_list) / len(weight_list)) + (max(weight_list) - min(weight_list))

print(weight_index(weight_list))