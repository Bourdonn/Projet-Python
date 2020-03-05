import numpy as np

# n is a string which values vary from 0 to 9 and from A to F
def HexaToBin(n):
    bin_number = list(format(int(n,16),'b'))
    k = len(bin_number)
    zeros = ['0' for i in range(4-k)]
    return(zeros + bin_number)


class Robot:
    """
    The Robot class contains the position and the color of the robot. 
    Methods:
        get_position
        set_position
        get_color
        directions
        distances
        move
    
    You can find a small description for each one just after its definitions.
    """
    __position = []
    __color = ''

    def __init__(self, data):
        self.__position = [data[1], data[2]]
        self.__color = data[0]

    def get_position(self):
        return self.__position

    def set_position(self, new_position):
        self.__position = new_position
        return new_position

    def get_color(self):
        return self.__color

    def directions(self, obstacles, Robots):
        """ directions makes a list of possible directions for the
        current position """
        direct = ['W', 'S', 'E', 'N']
        res = []
        i, j = self.__position[0], self.__position[1]
        for k in range(len(direct)):
            if HexaToBin(obstacles[i][j])[k] == '0':
                res += direct[k]
        for Robot in Robots:
            iR, jR = Robot.get_position()[0], Robot.get_position()[1]
            if jR == j-1 and 'W' in direct:
                res.remove('W')
            if iR == i+1 and 'S' in direct:
                res.remove('S')
            if jR == j+1 and 'E' in direct:
                res.remove('E')
            if iR == i-1 and 'N' in direct:
                res.remove('N')
        return res

    def distances(self, directions, obstacles, Robots):
        """ distances calculates the distances of each direction
        and return the result in a map where direction is a key and
        distance is a value """
        i, j = self.__position[0], self.__position[1]
        C = self.__color
        distR = {}
        for Robot in Robots:
            iR, jR = Robot.get_position()[0], Robot.get_position()[1]
            if [i,j] != [iR, jR]:
                if i == iR:
                    if j - jR > 0:
                        distR['W'] = j-jR-1
                    if j - jR < 0:
                        distR['E'] = jR-j-1
                if j == jR:
                    if i - iR > 0:
                        distR['N'] = i-iR-1
                    if i - iR < 0:
                        distR['S'] = iR-i-1
        dist = {}
        for direction in directions:
            d = 1
            if direction == 'W':
                while HexaToBin(obstacles[i][j-d])[0]  == '0':
                    d += 1
                dist[C+direction] = d
            elif direction == 'S':
                while HexaToBin(obstacles[i+d][j])[1] == '0':
                    d += 1
                dist[C+direction] = d
            elif direction == 'E':
                while HexaToBin(obstacles[i][j+d])[2] == '0':
                    d += 1
                dist[C+direction] = d
            elif direction == 'N':
                while HexaToBin(obstacles[i-d][j])[3] == '0':
                    d += 1
                dist[C+direction] = d
        res = {}
        for direction in directions:
            if direction in distR and direction in dist:
                res[C+direction] = min(distR[C+direction], dist[C+direction])
            else:
                res[C+direction] = dist[C+direction]
        return res

    def compute_move(self,direction,dist,room,path,por):
        """
        move gets a robot to move. It changes it's position, cleans the
        room wherever it goes, and saves it's movement in the vector path.
        Argument por means "progress or retreat", it's value must be 1 or -1
        """
        [i,j] = self.__position
        if direction == 'W':
            self.__position[1] -= dist
            room[i][self.__position[1]:j] += [por for k in range(self.__position[1],j)]
            path.append(self.__color + direction)
        elif direction == 'S':
            self.__position[0] += dist
            room[i+1:self.__position[0]+1][j] += [por for k in range(j,self.__position[0])]
            path.append(self.__color + direction)
        elif direction == 'E':
            self.__position[1] += dist
            room[i][j+1:self.__position[1]+1] += [por for k in range(j,self.__position[1])]
            path.append(self.__color + direction)
        else:            # N 
            self.__position[1] -= dist
            room[self.__position[0]:i][j] += [por for k in range(self.__position[0],j)]
            path.append(self.__color + direction)
        return self.__position

