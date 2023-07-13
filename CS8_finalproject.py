

# Zoe Zhou, CSW 8 (M21)



def vampirize(coordinate, city ):
    """
    Vampires transform humans.
    :param coordinate:
    :param city:a 2D list of integers
    :return:None
    """
    rows = len(city)
    columns = len(city[0])

    current_row = coordinate[0]
    current_colum = coordinate[1]
    left = (current_row, current_colum - 1)
    right = (current_row, current_colum + 1)
    up = (current_row - 1, current_colum)
    down = (current_row + 1, current_colum)

    current_row = left[0]
    current_colum = left[1]
    if current_row >= 0 and current_row < rows:
        if current_colum >= 0 and current_colum < columns:
            left = left
        else:
            left = ''
    else:
        left = ''
    current_row = down[0]
    current_colum = down[1]
    if current_row >= 0 and current_row < rows:
        if current_colum >= 0 and current_colum < columns:
            down = down
        else:
            down = ''
    else:
        down = ''

    current_row = right[0]
    current_colum = right[1]
    if current_row >= 0 and current_row < rows:
        if current_colum >= 0 and current_colum < columns:
            right = right
        else:
            right = ''
    else:
        right = ''

    current_row = up[0]
    current_colum = up[1]
    if current_row >= 0 and current_row < rows:
        if current_colum >= 0 and current_colum < columns:
            up = up
        else:
            up = ''
    else:
        up = ''

    neighbors=[left, right, up, down]

    for neighbor in neighbors:
        if neighbor!='':
            if city[neighbor[0]][neighbor[1]]==0:
                city[neighbor[0]][neighbor[1]]=1
def next_day(city):
    """
    Update the state of the city overnight.
    :param city:
    :return: new city
    """
    City_copy=[[item for item in line] for line in city]#deep copy

    Vampires_loc=[]
    for i in range(len(City_copy)):
        for j in range(len(City_copy[i])):
            if City_copy[i][j]==1:
                Vampires_loc.append((i,j))
    for Location in Vampires_loc:
        vampirize(Location,City_copy)

    Cure_loc=[]
    for i in range(len(City_copy)):
        for j in range(len(City_copy[i])):
            if City_copy[i][j]==3:
                if not potion_surrounded((i,j),City_copy):
                    Cure_loc.append((i,j))
                else:
                    City_copy[i][j]=1
    for CL in Cure_loc:
        cure(CL,City_copy)
    return City_copy
def get_city_from_file(filename):
    """
    Build a two-dimensional list from the contents read from the file.
    :param filename:filename (string)
    :return:a city (2D list of integers)
    """
    city=[]
    with open(filename) as f:
        for line in f:
            line=line.strip()
            int_list = list(map(int, line.split()))
            city.append(int_list)
    return city
def show_city(city):
    """
    Print city status.
    :param city: (2D list of integers)
    :return: None
    """
    new_state = []
    for line in city:
        temp = []
        for item in line:
            if item == 0:
                temp.append('H')
            elif item == 1:
                temp.append('V')
            elif item==3:
                temp.append('P')
            else:
                temp.append('W')
        if len(temp)!=0:
            new_state.append(' '.join(temp))
    strt=''
    for state in new_state:
        strt+=state+' \n'
    print(strt.strip()+' ')
def cure(coordinate,city):
    """
    Turn vampires into humans.
    :param coordinate:
    :param city:
    :return:
    """
    rows = len(city)
    columns = len(city[0])

    current_row = coordinate[0]
    current_colum = coordinate[1]
    left = (current_row, current_colum - 1)
    right = (current_row, current_colum + 1)
    up = (current_row - 1, current_colum)
    down = (current_row + 1, current_colum)
    up_left = (current_row - 1, current_colum - 1)
    up_right = (current_row - 1, current_colum + 1)
    down_left = (current_row + 1, current_colum - 1)
    down_right = (current_row + 1, current_colum + 1)

    current_row = left[0]
    current_colum = left[1]
    if current_row >= 0 and current_row < rows:
        if current_colum >= 0 and current_colum < columns:
            left = left
        else:
            left = ''
    else:
        left = ''

    current_row = down[0]
    current_colum = down[1]
    if current_row >= 0 and current_row < rows:
        if current_colum >= 0 and current_colum < columns:
            down = down
        else:
            down = ''
    else:
        down = ''

    current_row = right[0]
    current_colum = right[1]
    if current_row >= 0 and current_row < rows:
        if current_colum >= 0 and current_colum < columns:
            right = right
        else:
            right = ''
    else:
        right = ''

    current_row = up[0]
    current_colum = up[1]
    if current_row >= 0 and current_row < rows:
        if current_colum >= 0 and current_colum < columns:
            up = up
        else:
            up = ''
    else:
        up = ''

    current_row = up_left[0]
    current_colum = up_left[1]
    if current_row >= 0 and current_row < rows:
        if current_colum >= 0 and current_colum < columns:
            up_left = up_left
        else:
            up_left = ''
    else:
        up_left = ''

    current_row = up_right[0]
    current_colum = up_right[1]
    if current_row >= 0 and current_row < rows:
        if current_colum >= 0 and current_colum < columns:
            up_right = up_right
        else:
            up_right = ''
    else:
        up_right = ''

    current_row = down_left[0]
    current_colum = down_left[1]
    if current_row >= 0 and current_row < rows:
        if current_colum >= 0 and current_colum < columns:
            down_left = down_left
        else:
            down_left = ''
    else:
        down_left = ''

    current_row = down_right[0]
    current_colum = down_right[1]
    if current_row >= 0 and current_row < rows:
        if current_colum >= 0 and current_colum < columns:
            down_right = down_right
        else:
            down_right = ''
    else:
        down_right = ''

    neighbors_eight =[left, right, up, down, up_left, up_right, down_left, down_right]

    for neighbor in neighbors_eight:
        if neighbor != '':
            if city[neighbor[0]][neighbor[1]] == 1:
                city[neighbor[0]][neighbor[1]] = 0
def potion_surrounded(coordinate,city):
    """
    Judging whether the medicament is blocked or not.
    :param coordinate:
    :param city:
    :return:
    """
    rows = len(city)
    columns = len(city[0])

    current_row = coordinate[0]
    current_colum = coordinate[1]
    left = (current_row, current_colum - 1)
    right = (current_row, current_colum + 1)
    up = (current_row - 1, current_colum)
    down = (current_row + 1, current_colum)

    current_row = left[0]
    current_colum = left[1]
    if current_row >= 0 and current_row < rows:
        if current_colum >= 0 and current_colum < columns:
            left = left
        else:
            left = ''
    else:
        left = ''
    current_row = down[0]
    current_colum = down[1]
    if current_row >= 0 and current_row < rows:
        if current_colum >= 0 and current_colum < columns:
            down = down
        else:
            down = ''
    else:
        down = ''

    current_row = right[0]
    current_colum = right[1]
    if current_row >= 0 and current_row < rows:
        if current_colum >= 0 and current_colum < columns:
            right = right
        else:
            right = ''
    else:
        right = ''

    current_row = up[0]
    current_colum = up[1]
    if current_row >= 0 and current_row < rows:
        if current_colum >= 0 and current_colum < columns:
            up = up
        else:
            up = ''
    else:
        up = ''

    neighbors = [left, right, up, down]

    ret=[]
    for neighbor in neighbors:
        if neighbor != '':
            ret.append(str(city[neighbor[0]][neighbor[1]]))
        else:
            ret.append('e')
    if ''.join(ret)=='1111':
        return True
    else:
        return False
def days_remaining(city,verbose=True):
    """
    Print the daily status of the city and the time taken for all transformations.
    :param city:
    :param verbose:If verbose is true, then days_remaining() should act as normal from parts 1,2,3.
    If verbose is false, it should not print anything, and only return an integer.
    :return: the shortest number of days until there are no more infections to be made (integer)

    """
    if verbose:
        flag=True
        for item in city:
            if type(item)!=type([1,2]):
                flag=False
        if flag:
            day=0
            city_copy=[[item for item in line] for line in city]#deep copy
            while 1:
                print('Day: {}'.format(day))
                show_city(city_copy)
                print()
                city_new=next_day(city_copy)
                if city_new==city_copy:
                    break
                else:
                    city_copy=city_new
                day+=1
            return day
        else:
            return None
    else:
        flag = True
        for item in city:
            if type(item) != type([1, 2]):
                flag = False
        if flag:
            day = 0
            city_copy = [[item for item in line] for line in city]  # deep copy
            while 1:
                city_new = next_day(city_copy)
                if city_new == city_copy:
                    break
                else:
                    city_copy = city_new
                day += 1
            return count_humans(city_copy)
        else:
            return None
def count_humans(city):
    """
    Calculate the number of remaining humans in the city
    :param city:
    :return:
    """
    Human_number=0
    for line in city:
        for item in line:
            if item==1:
                Human_number+=1
    return Human_number
def get_best_potion_location(city):
    """
    Given a city (2D list of integers), return a coordinate (integer tuple with length 2: (row, column)) of the location
     where an added potion will result in the greatest number of remaining humans after the virus has finished spreading
    :param city:
    :return: (row,colum)
    """
    rows = len(city)
    colums = len(city[0])

    Human_number=[count_humans(city)]
    ret=[(None,None)]
    for row in range(rows):
        for colum in range(colums):
            city_copy = [[item for item in line] for line in city]
            city_copy[row][colum]=3
            ret.append((row,colum))
            Human_number.append(days_remaining(city_copy,False))

    MaxNumber=max(Human_number)
    if ret[Human_number.index(MaxNumber)]==(None,None):
        return None
    else:
        return ret[Human_number.index(MaxNumber)]













