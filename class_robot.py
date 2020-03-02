class Robot:
    __position = []
    __colour = ''

    def __init__(self, position, colour):
        self.__position = position
        self.__colour = colour


    def get_position(self):
        return self.__position

    def set_position(self, new_position):
        self.__position = new_position
        return new_position

    def get_colour(self):
        return self.__colour

    def directions(self, obstacles):
        direct = []
        x, y = self.__position[0], self.__position[1]
        if obstacles[x-1][y] == 0:
            direct += 'W'
        if obstacles[x][y-1] == 0:
            direct += 'S'
        if obstacles[x+1][y] == 0:
            direct += 'E'
        if obstacles[x][y+1] == 0:
            direct += 'N'
        return direct
    
    def distances(self, position, directions, obstacles):
        x, y = self.__position[0], self.__position[1]
        dist = {}
        for direction in directions:
            d = 1
            if direction == 'W':
                while obstacles[x-d][y] == 0:
                    d += 1
                dist[direction] = d
            if direction == 'S':
                while obstacles[x][y-d] == 0:
                    d += 1
                dist[direction] = d
            if direction == 'E':
                while obstacles[x+d][y] == 0:
                    d += 1
                dist[direction] = d
            if direction == 'N':
                while obstacles[x][y+d] == 0:
                    d += 1
                dist[direction] = d
    return dist 















