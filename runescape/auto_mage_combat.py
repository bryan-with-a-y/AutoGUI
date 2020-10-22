import pyautogui
import PIL
from time import sleep

start_x, start_y = (1737, 56)
end_x, end_y = (1888, 207)
enemy_pixel_value = (247, 247, 0) 
TOLERANCE = 3

x_factor = 10.5
y_factor = 10.5 
map_self = (1812, 131)
screen_self = (962, 538)

def pixel_distance(a,b):
    r1,g1,b1 = a
    r2,g2,b2 = b
    difference = (r1-r2)**2 + (g1-g2)**2 + (b1-b2)**2
    distance = difference**0.5
    return distance

def screenshot():
    screenshot = PIL.ImageGrab.grab()
    return screenshot

def get_enemy_map_positions():
    im = screenshot()
    im = im.convert("RGB")
    pix = im.load()
    xsize, ysize = im.size
    total = 0

    enemy_map_positions = list()
    for yi in range(start_y, end_y):
        for xi in range(start_x, end_x):
            #if pixel_distance(pix[xi,yi],enemy_pixel_value) < TOLERANCE:
            if pix[xi,yi] == enemy_pixel_value:
                enemy_map_positions.append((xi,yi))
    return enemy_map_positions

def map_to_screen(loc):
    map_x, map_y = loc
    click_x = screen_self[0] + (map_x - map_self[0])*x_factor
    click_y = screen_self[1] + (map_y - map_self[1])*y_factor
    return click_x, click_y

def map_positions_to_screen_positions(positions):
    screen_positions = list()
    for loc in positions:
        screen_positions.append(map_to_screen(loc))
    return screen_positions

def get_closest_enemy(positions):
    if len(positions) == 0:
        return map_self
    closest_distance = 100000000
    positions = map_positions_to_screen_positions(positions)
    for i in range(len(positions)):
        pos_x, pos_y = positions[i]
        self_x, self_y = screen_self
        distance = ((self_x-pos_x)**2 + (self_y-pos_y)**2)**0.5
        if distance < closest_distance:
            closest_distance = distance
            closest_enemy = i
    return positions[closest_enemy]

def main():
    print("Starting in 5 seconds")
    sleep(5)
    print("Starting")
    while True:
        enemy_map_positions = get_enemy_map_positions()
        for i in range(len(enemy_map_positions)):
            enemy_map_positions = get_enemy_map_positions()
            closest_loc = get_closest_enemy(enemy_map_positions)
            screen_loc = map_to_screen(closest_loc)
            x, y = closest_loc
            print("Clicking at {}, Length: {}".format((x,y), len(enemy_map_positions)))
            print("Number of enemies: {}".format(len(enemy_map_positions)))
            pyautogui.click(x=x, y=y)
            sleep(5)

main()



