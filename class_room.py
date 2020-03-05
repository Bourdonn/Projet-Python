
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
	__room = []

    def __init__(self, data):
        self.__room = data

	def has_wall(self,index,direction):
		"""
		Returns True if there is a wall in direction at position index, False if not. 
		"""
		if direction == 'W':
			return Hexa2Bin(self.__room(index))[0] == '1'
		if direction == 'S':
			return Hexa2Bin(self.__room(index))[1] == '1'
		if direction == 'E':
			return Hexa2Bin(self.__room(index))[2] == '1'
		if direction == 'N':
			return Hexa2Bin(self.__room(index))[3] == '1'
		else: 
			print("ERROR: Direction Not Recognised")
			return True

    def get_walls(self,index):
        return Hexa2bin(self.__room(index))
        
        
        
