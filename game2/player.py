from items import *
from map import rooms

inventory = [item_id, item_laptop, item_money]

inv_mass_cur = 0.0
inv_mass_max = 3.0

# Start game at the reception
current_room = rooms["Reception"]
