liste = open('stillnotcal.txt', 'r')

register = 1
current_cycle = 1
result_sum = 0
pixels = ''
current_ctr_location = 1

def check_cycle():
    global result_sum
    global pixels
    cycle_strengths = [20, 60, 100, 140, 180, 220]
    if current_cycle in cycle_strengths:
        result_sum += register * current_cycle
        #print(current_cycle, register, current_cycle*register)

def draw_pixels():
    global pixels
    global current_ctr_location
    line_splits = [40, 80, 120, 160, 200, 240]
    if current_ctr_location - register < 3 and current_ctr_location - register >= 0:
        pixels += '#'
        current_ctr_location += 1

    else:
        pixels += ' '
        current_ctr_location += 1
    if current_cycle in line_splits:
        print(pixels)
        pixels = ''
        current_ctr_location = 1


for item in liste.readlines():
    if item.startswith("addx"):
        for i in item.split(' '):
            draw_pixels()
            check_cycle()
            current_cycle += 1
        register += int(item.replace('\n', '').split(' ')[1])

    else:
        draw_pixels()
        check_cycle()
        current_cycle += 1

print(result_sum)
