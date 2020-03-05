#Reading problem file
def ReadFile(file_name):
    """ 
    Reads the file in problem format. 
    Returns:
        n, m:  size of the problem
        nb_rob: number of robots
        obstacles: contains the information of all walls in a vector
        robots: list of informations needed to construct Robot objects
        visited: vector which shape equals obstacle's shape. 
              Contains 0 if no robot went there, a positif number if not.
    """
    file = open(file_name, "r")
    line = file.readline().split()
    n = int(line[0])
    m = int(line[1])
    nb_rob = int(line[2])
    obstacles = []
    for i in range(n):
        line = file.readline().strip()
        for j in list(line):
            obstacles.append(j)
    robots = []
    room = [0 for i in range(n*m)]
    for i in range(nb_rob):
        line = file.readline().strip().split()
        index = m*int(line[1])+int(line[2])
        robots.append([line[0],index])
        room[index] = 1
    file.close()
    return(n,m,nb_rob,obstacles,robots,visited)

# pour l'affichage:    plt.imshow(a)
# Telecharger le package import matplotlib.pyplot as plt 

    
