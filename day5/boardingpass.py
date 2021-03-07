import math 

def part1(boardingpasses): 
    max_seat_id = -1
    for boardingpass in boardingpasses:
        seat_id = get_seat_id(boardingpass)
        if seat_id > max_seat_id: 
            max_seat_id = seat_id

    print(max_seat_id)

def part2(boardingpasses): 
    seat_ids = [get_seat_id(boardingpass) for boardingpass in boardingpasses]
    print(seat_ids)
    for seat_id in range(max(seat_ids)):
        low = seat_id - 1
        high = seat_id + 1
        if seat_id not in seat_ids and low in seat_ids and high in seat_ids:
            print(seat_id)

def get_seat_id(boardingpass):
    binary_seat_id = "".join(['1' if char == "B" or char == "R" else '0' for char in boardingpass])
    seat_id = int(binary_seat_id, 2)
    return seat_id

with open("../data/day5.txt") as f:
    bps = f.read().splitlines() 
    part1(bps)
    part2(bps)
   

