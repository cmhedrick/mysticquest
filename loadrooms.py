from mysticquest import Room, House, Hero

def make_house(raw):
    house = House()
    for raw_room in raw:
        room = raw_room.split('***')
        house.add_room(Room(room[0].strip(),
                          room[1].strip(),
                          room[2].strip(),
                          eval(room[3].strip())))
    return house


f = open('StoryBoard.txt', 'r')
raw_data = f.read()
f.close()

def begin():
    raw_rooms = raw_data.split('+++')
    the_mansion = make_house(raw_rooms)
    our_hero = Hero("Hero", the_mansion, 0)
    return our_hero

if __name__ == "__main__":
    our_hero = begin()
    print(our_hero)

    while True:
        direction = input('> ')
        direction = direction[0].upper()   
        if direction == 'N':
            our_hero.go_north()
            print(our_hero)
        elif direction == 'S':
            our_hero.go_south()
            print(our_hero)
        elif direction == 'E':
            our_hero.go_east()
            print(our_hero)
        elif direction == 'W':
            our_hero.go_west()
            print(our_hero)
        else:     
            print('Choice not valid, Try again')

def destiny(our_hero, direction):
    if direction == 'N':
        our_hero.go_north()
        return our_hero
    elif direction == 'S':
        our_hero.go_south()
        return our_hero
    elif direction == 'E':
        our_hero.go_east()
        return our_hero
    elif direction == 'W':
        our_hero.go_west()
        return our_hero
    else:
        msg = 'Choice not valid, Try again'
        return msg

