
# n is a string which values vary from 0 to 9 and from A to F
def Hexa2Bin(n):
    bin_number = list(format(int(n,16),'b'))
    k = len(bin_number)
    zeros = ['0' for i in range(4-k)]
    return(zeros + bin_number)


class Room:
	"""
	Contains the wall's room informations
	"""
	__obstacles = []
	__n = 0
	__m = 0

    def __init__(self,n_m, obstacles):
        self.__obstacles = obstacles
        self.__n = n_m[0]
        self.__m = n_m[1]

    def __init__(self, n_x, n_y, file_in):
    	"""
    	Constructor used in Test class
    	""" 
        self.__n = n_x
        self.__m = n_y
        for i in range(n_x):
	        line = file_in.readline().strip()
    	    for j in list(line):
        	    self.__obstacles.append(j)

	def has_wall(self,index,direction):
		"""
		Returns True if there is a wall in direction at position index, False if not. 
		"""
		if direction == 'W':
			return Hexa2Bin(self.__obstacles(index))[0] == '1'
		if direction == 'S':
			return Hexa2Bin(self.__obstacles(index))[1] == '1'
		if direction == 'E':
			return Hexa2Bin(self.__obstacles(index))[2] == '1'
		if direction == 'N':
			return Hexa2Bin(self.__obstacles(index))[3] == '1'
		else: 
			print("ERROR: Direction Not Recognised")
			return True

    def get_walls(self,index):
        return Hexa2bin(self.__obstacles(index))
        
        
        
