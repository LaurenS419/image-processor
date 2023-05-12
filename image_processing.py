# Lauren Spee
# 261008497

import doctest

### Helper Functions ###

def check_img_length(pgm_list):
    '''(list<list><int>) -> bool
    Takes an input of a list of lists containing integers,
    returns if those nested lists are all the same length.
    >>> check_img_length([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    True
    >>> check_img_length([[8, 8, 90, 7, 5, 6], [200, 8, 90, 5, 5, -2], [0, 8, 55, 2, 4, 6], [40, 8, -11, 7, 5, 1000]])
    True
    >>> check_img_length([[2, 2], [3, 3, 1], [2, 7, 0]])
    False
    '''
    
    verdict = True
    length = len(pgm_list[0])
    
    for elmt in pgm_list:
        if len(elmt) != length:
            verdict = False
            break
        
    return verdict

def find_length_compressed_image(comp_pgm_list, row_num):
    '''(list<list><str>) -> int
    Takes a list of lists of strings and row number and returns the
    length of that row, taking the multiplier within each string into account.
    >>> find_length_compressed_image([["0x5", "200x2"], ["111x7"]], 0)
    7
    >>> find_length_compressed_image([["0x2", "10x10", "200x2"], ["1x7", "1x7"]], 1)
    14
    >>> find_length_compressed_image([["40x20"], ["10x20"], ["20x20"], ["30x20"]], 3)
    20
    '''
    
    length = 0
    
    row = comp_pgm_list[row_num]
    
    for index in row:
        x_loc = index.find('x')
        b = index[x_loc + 1:]
        
        length += int(b)
    
    return length

def check_compressed_img_length(comp_pgm_list):
    '''(list<list><str>) -> bool
    Takes a list of lists of strings and returns if all the rows are
    the same length, taking the multiplier within each string into account.
    >>> check_compressed_img_length([["0x5", "200x2"], ["111x7"]])
    True
    >>> check_compressed_img_length([["0x1", "10x10", "200x2"], ["1x7", "1x7"]])
    False
    >>> check_compressed_img_length([["4x20"], ["1x20"], ["2x20"]])
    True
    '''
    
    verdict = True
    index = 0
    
    length_standard = find_length_compressed_image(comp_pgm_list, 0)
    
    while index < len(comp_pgm_list):        
        length = find_length_compressed_image(comp_pgm_list, index)
            
        if length != length_standard:
            verdict = False
            break
        
        index += 1
            
    return verdict

def line_counter(filename):
    ''' (str) -> NoneType
    Takes a file and returns the number
    of lines it contains.
    >>> fobj = open('test.txt','w')
    >>> fobj.write('abc3x10')
    >>> fobj.close()
    >>> line_counter('test.txt')
    1
    >>> line_counter('comp.pgm')
    10
    >>> line_counter('comp.pgm.compressed')
    10
    '''
    
    pgm_obj = open(filename, 'r')
    line_counter = 0
        
    for line in pgm_obj:
        line_counter += 1
    
    pgm_obj.close()
    
    return line_counter


### Assignment Functions ###




def is_valid_image(pgm_list):
    '''(list<list><int>) -> bool
    Takes an input of a list of lists of integers and returns
    whether of not its a valid pgm image.
    >>> is_valid_image([[200, 0, 3], [255, 30, 1], [50, 50, 50], [0, 90, 80]])
    True
    >>> is_valid_image([[1, -1, 3], [4, 55, 7], [0, 0, 1]])
    False
    >>> is_valid_image([[100, 20], [256, 5], [9, 9]])
    False
    '''
    
    verdict = check_img_length(pgm_list)
    
    if not verdict:
        return verdict
    
    for elmt in pgm_list:
        
        for index in elmt:            
            if type(index) != int:
                verdict = False
                break
            
            if index > 255 or index < 0:
                verdict = False
                break
        
    
    return verdict

def is_valid_compressed_image(comp_pgm_list):
    ''' (list<list><str>) -> bool
    Takes a list of lists of strings and returns if that
    list is a valid compressed pgm image.
    >>> is_valid_compressed_image([[1, -1, 3], [4, 55, 7], [0, 0, 1]])
    False
    >>> is_valid_compressed_image([["4x20"], ["1x20"], ["2x20"]])
    True
    >>> is_valid_compressed_image([["0x1", "10x10", "200x2"], ["1x7", "1x7"]])
    False
    '''
    
    verdict = not is_valid_image(comp_pgm_list)
     
    if not verdict:
        return verdict
        
    for elmt in comp_pgm_list:
        for index in elmt:
            
            if type(index) != str:
                verdict = False
                break
            
            if index.find('x') < 0:
                verdict = False
                break
            
            x_loc = index.find('x')
            a = (index[:x_loc])
            b = (index[x_loc + 1:])
            
            if not a.isdecimal() or not b.isdecimal():
                verdict = False
                break
            
            a = int(a)
            b = int(b)
            
            if a > 255 or a < 0:
                verdict = False
                break
            
            if b < 1:
                verdict = False
                break
            
    if verdict:
        verdict = check_compressed_img_length(comp_pgm_list)
    
    return verdict


def load_regular_image(filename):
    ''' (str) -> list<list>
    Takes a name of a file and if it's a proper pgm image
    file, returns the contents of the file in a matrix.
    >>> load_regular_image("comp.pgm")
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 51, 51, 51, 51, 51, 0, 119, 119, 119, 119, 119, 0, 187, 187, 187, 187, 187, 0, 255, 255, 255, 255, 0], [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 255, 0], [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 255, 255, 255, 0], [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 0, 0], [0, 51, 51, 51, 51, 51, 0, 119, 119, 119, 119, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    >>> fobj = open('test.txt','w')
    >>> fobj.write('abc3x10')
    >>> fobj.close()
    >>> load_regular_image('test.txt')
    Traceback (most recent call last):
    AssertionError: File does not contain a valid image matrix.
    >>> fobj = open('regular_test.txt','w')
    >>> fobj.write('P2\\n5 3\\n255\\n0 0 0 0 100\\n100 100 200 200 100\\n50 50 40 30 60')
    >>> fobj.close()
    >>> load_regular_image('regular_test.txt')
    [[0, 0, 0, 0, 100], [100, 100, 200, 200, 100], [50, 50, 40, 30, 60]]
    '''
    
    img_matrix = []
    pgm_obj = open(filename, 'r')
    counter = 0
    line_amt = line_counter(filename)
    
    if line_amt <= 3:
        raise AssertionError("File does not contain a valid image matrix.")
    
    for line in pgm_obj:

        if counter < 3:
            counter += 1
            continue
        
        
        temp_list = []
        temp_list = line.split()
        
        for index in range(len(temp_list)):
                        
            if temp_list[index].isdecimal():
                temp_list[index] = int(temp_list[index])
                
        img_matrix.append(temp_list)
                 
        
    pgm_obj.close()
                
    if not is_valid_image(img_matrix):
        raise AssertionError("File does not contain a valid image matrix.")
    
    return img_matrix


def load_compressed_image(filename):
    ''' (str) -> list<list><str>
    Takes a name of a file and if it's a proper compressed pgm image
    file, returns the contents of the file in a matrix.
    >>> load_compressed_image("comp.pgm.compressed")
    [['0x24'], ['0x1', '51x5', '0x1', '119x5', '0x1', '187x5', '0x1', '255x4', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x2', '255x1', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x4', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x4'], ['0x1', '51x5', '0x1', '119x5', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x4'], ['0x24']]
    >>> fobj = open('test.txt','w')
    >>> fobj.write('abc3x10')
    >>> fobj.close()
    >>> load_compressed_image('test.txt')
    Traceback (most recent call last):
    AssertionError: File does not contain a valid image matrix.
    >>> fobj = open('another_test.txt','w')
    >>> fobj.write('P2C\\n10 3\\n255\\n0x1 20x3 4x6\\n50x10\\n200x5 250x5')
    >>> fobj.close()
    >>> load_compressed_image('another_test.txt')
    [['0x1', '20x3', '4x6'], ['50x10'], ['200x5', '250x5']]
    '''
    
    comp_img_matrix = []
    cpgm_obj = open(filename, 'r')
    counter = 0
    line_amt = line_counter(filename)
    
    if line_amt <= 3:
        print("lines")
        raise AssertionError("File does not contain a valid image matrix.")
    
    
        
    for line in cpgm_obj:

        if counter < 3:
            counter += 1
            continue
                         
        comp_img_matrix.append(line.split())
        
    cpgm_obj.close()
            
    if not is_valid_compressed_image(comp_img_matrix):
        raise AssertionError("File does not contain a valid compressed image matrix.")
    
    return comp_img_matrix

def load_image(filename):
    ''' (str) -> list<list>
    Takes the name of the file and returns the image matrix
    that it contains (either compressed or not compressed).
    Raises an error if it does not contain a valid image matrix.
    >>> load_image("comp.pgm.compressed")
    [['0x24'], ['0x1', '51x5', '0x1', '119x5', '0x1', '187x5', '0x1', '255x4', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x2', '255x1', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x4', '0x1'], ['0x1', '51x1', '0x5', '119x1', '0x3', '119x1', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x4'], ['0x1', '51x5', '0x1', '119x5', '0x1', '187x1', '0x1', '187x1', '0x1', '187x1', '0x1', '255x1', '0x4'], ['0x24']]
    >>> load_image("comp.pgm")
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 51, 51, 51, 51, 51, 0, 119, 119, 119, 119, 119, 0, 187, 187, 187, 187, 187, 0, 255, 255, 255, 255, 0], [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 255, 0], [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 255, 255, 255, 0], [0, 51, 0, 0, 0, 0, 0, 119, 0, 0, 0, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 0, 0], [0, 51, 51, 51, 51, 51, 0, 119, 119, 119, 119, 119, 0, 187, 0, 187, 0, 187, 0, 255, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    >>> fobj = open('test.txt','w')
    >>> fobj.write('abc3x10')
    >>> fobj.close()
    >>> load_image('test.txt')
    Traceback (most recent call last):
    AssertionError: File does not contain a valid image matrix.
    '''
    
    img_obj = open(filename, 'r')
    
    for line in img_obj:
        
        if line.strip() == "P2":
            img_matrix = load_regular_image(filename)
        
        
        elif line.strip() == "P2C":
            img_matrix = load_compressed_image(filename)
        
        else:
            raise AssertionError("File does not contain a valid image matrix.")
        
        break
    
    img_obj.close()
    
    return img_matrix


def save_regular_image(pgm_list, filename):
    ''' (list<list><int>, str) -> NoneType
    Takes an image matrix and a filename, and writes the
    image matrix to the file.
    >>> save_regular_image([[0]*10, [255]*10, [0]*10], "test.pgm")
    >>> fobj = open("test.pgm","r")
    >>> fobj.read()
    'P2\\n10 3\\n255\\n0 0 0 0 0 0 0 0 0 0\\n255 255 255 255 255 255 255 255 255 255\\n0 0 0 0 0 0 0 0 0 0\\n'
    >>> save_regular_image([[0]*3, [200]*4], "another_test.pgm")
    Traceback (most recent call last):
    AssertionError: List does not contain a valid image matrix.
    >>> save_regular_image([[0]*4, [250, 250, 20, 20], [0]*4], "test.pgm")
    >>> fobj = open("test.pgm","r")
    >>> fobj.read()
    'P2\\n4 3\\n255\\n0 0 0 0\\n250 250 20 20\\n0 0 0 0\\n'
    '''
    
    if not is_valid_image(pgm_list):
        raise AssertionError("List does not contain a valid image matrix.")
    
    fobj = open(filename,"w")
    str_list = []
    temp_list = []
    
    width = str(len(pgm_list[0]))
    height = str(len(pgm_list))
    
    fobj.write("P2\n" + width + " " + height +"\n255\n")
     
    for elmt in pgm_list:
        
        for index in elmt:
            
            temp = str(index)
            temp_list.append(temp)
            
        str_list.append(temp_list)
        temp_list = []
            
    for elmt in str_list:
                
        s = ' '.join(elmt)        
        fobj.write(s + "\n")
        
    
    fobj.close()
    
def save_compressed_image(comp_pgm_list, filename):
    ''' (list<list><int>, str) -> NoneType
    Takes a compressed image matrix and a filename, and writes the
    image matrix to the file.
    >>> save_compressed_image([["0x5", "200x2"], ["111x7"]], "test.pgm.compressed")
    >>> fobj = open("test.pgm.compressed", 'r')
    >>> fobj.read()
    'P2C\\n7 2\\n255\\n0x5 200x2\\n111x7\\n'
    >>> save_compressed_image([['0x3'], ['200x4']], "test.pgm.compressed")
    Traceback (most recent call last):
    AssertionError: List does not contain a valid image matrix.
    >>> save_compressed_image([['0x3'], ['200x3'], ['0x3']], "test.pgm.compressed")
    >>> fobj = open("test.pgm.compressed","r")
    >>> fobj.read()
    'P2C\\n3 3\\n255\\n0x3\\n200x3\\n0x3\\n'
    '''
    
    if not is_valid_compressed_image(comp_pgm_list):
        raise AssertionError("List does not contain a valid image matrix.")
    
    fobj = open(filename,"w")
    width = str(find_length_compressed_image(comp_pgm_list, 0))
    height = str(len(comp_pgm_list))
    
    fobj.write("P2C\n" + width + " " + height +"\n255\n")
     
            
    for elmt in comp_pgm_list:
                
        s = ' '.join(elmt)        
        fobj.write(s + "\n")
        
    
    fobj.close()
    
    
def save_image(img_list, filename):
    ''' (list<list>, str) -> NoneType
    Takes an image matrix and a filename, and writes the
    image matrix to the file.
    >>> save_image([["0x5", "200x2"], ["111x7"]], "test.pgm.compressed")
    >>> fobj = open("test.pgm.compressed", 'r')
    >>> fobj.read()
    'P2C\\n7 2\\n255\\n0x5 200x2\\n111x7\\n'
    >>> save_image([['0x3'], ['200x3'], ['0x3']], "test.pgm.compressed")
    >>> fobj = open("test.pgm.compressed", 'r')
    >>> fobj.read()
    'P2C\\n3 3\\n255\\n0x3\\n200x3\\n0x3\\n'
    >>> save_image([[0]*4, [250, 250, 20, 20], [0]*4], "test.pgm")
    >>> fobj = open("test.pgm","r")
    >>> fobj.read()
    'P2\\n4 3\\n255\\n0 0 0 0\\n250 250 20 20\\n0 0 0 0\\n'
    >>> save_image([['0x3'], ['200x4']], "test.pgm.compressed")
    Traceback (most recent call last):
    AssertionError: List does not contain a valid image matrix.
    '''  
    
    first_index = img_list[0]
    
    if type(first_index[0]) == int:
        save_regular_image(img_list, filename)
    
    elif type(first_index[0]) == str:
        save_compressed_image(img_list, filename)
    
    else:
        raise AssertionError("List does not contain a valid image matrix.")
    
def invert(pgm_list):
    ''' (list<list><int>) -> list<list><int>
    Takes an image matrix and returns the list of the 255 minus
    each individual integer.
    >>> invert([[0, 100, 150], [200, 200, 200], [255, 255, 255]])
    [[255, 155, 105], [55, 55, 55], [0, 0, 0]]
    >>> invert([[1, 254], [100, 255], [20, 2]])
    [[254, 1], [155, 0], [235, 253]]
    >>> invert([[255, 0]])
    [[0, 255]]
    '''
    
    if not is_valid_image(pgm_list):
        raise AssertionError("List does not contain a valid image matrix.")
    
    inverted_img = []
    
    for elmt in pgm_list:
        temp = []
        
        for index in elmt:            
            temp.append(255 - index)
            
        inverted_img.append(temp)
    
    return inverted_img
  
  
def flip_horizontal(pgm_list):
    ''' (list<list><int>) -> list<list><int>
    Takes a list of lists of ints, and returns the flipped
    order of the integers inside each nested list.
    >>> flip_horizontal([[0, 100, 150], [200, 200, 200], [255, 255, 255]])
    [[150, 100, 0], [200, 200, 200], [255, 255, 255]]
    >>> flip_horizontal([[0, 1, 5, 6], [2, 3, 5, 9], [8, 9, 0, 1]])
    [[6, 5, 1, 0], [9, 5, 3, 2], [1, 0, 9, 8]]
    >>> flip_horizontal([[0, 1]])
    [[1, 0]]
    '''
    
    if not is_valid_image(pgm_list):
        raise AssertionError("List does not contain a valid image matrix.")
    
    hflipped_img = []
    
    for elmt in pgm_list:
        temp = []
        temp = elmt[::-1]
        
        hflipped_img.append(temp)
    
    return hflipped_img

def flip_vertical(pgm_list):
    ''' (list<list><int>) -> list<list><int>
    Takes a list of lists of ints, and returns the flipped
    order of the nested lists.
    >>> flip_vertical([[1, 2, 3, 4, 5], [0, 0, 5, 10, 10], [5, 5, 5, 5, 5]])
    [[5, 5, 5, 5, 5], [0, 0, 5, 10, 10], [1, 2, 3, 4, 5]]
    >>> flip_vertical([[0, 1, 5, 6], [2, 3, 5, 9], [8, 9, 0, 1]])
    [[8, 9, 0, 1], [2, 3, 5, 9], [0, 1, 5, 6]]
    >>> flip_vertical([[0, 1], [254, 255]])
    [[254, 255], [0, 1]]
    '''
    
    if not is_valid_image(pgm_list):
        raise AssertionError("List does not contain a valid image matrix.")
        
    vflipped_img = pgm_list[::-1]
            
    return vflipped_img
    
def crop(pgm_list, y1, x1, height, width):
    ''' (list<list><int>) -> list<list><int>
    Takes a list of lists of ints, and returns the "cropped"
    version of the list of lists of ints, with the y1 and x1 being
    the starting row and column, and the height and width
    being the new height and width of the image matrix.
    >>> crop([[5, 5, 5], [5, 6, 6], [6, 6, 7]], 1, 1, 2, 2)
    [[6, 6], [6, 7]]
    >>> crop([[1, 2, 10], [1, 8, 6], [8, 7, 6]], 0, 1, 3, 1)
    [[2], [8], [7]]
    >>> crop([[4, 1], [3, 2], [5, 3]], 0, 0, 2, 2)
    [[4, 1], [3, 2]]
    '''
    
    if not is_valid_image(pgm_list):
        raise AssertionError("List does not contain a valid image matrix.")
    
    cropped_img = []
    h_count = 1
    y_coord = y1
        
    for elmt in pgm_list:
        
        if h_count > height:
            break
        
        cropped_img.append(pgm_list[y_coord][x1:x1+width])
        
        y_coord += 1
        h_count += 1
                
    return cropped_img
    
    
def find_end_of_repetition(num_list, start, target):
    ''' (list<int>) -> int
    Takes a lists of integers and a starting point,
    and returns the last occurance of a consecutive amount
    of target integers.
    >>> find_end_of_repetition([1, 2, 3, 4, 5, 6, 7], 6, 7)
    6
    >>> find_end_of_repetition([1, 1, 1, 1, 1, 4], 0, 1)
    4
    >>> find_end_of_repetition([0, 1, 1, 3, 5, 5], 4, 5)
    5
    '''
    
    i = start
    
    while i < len(num_list):
        
        if num_list[i] != target:
            break
        
        index = i
        i += 1
        
    return index

def compress(pgm_list):
    ''' (list<list><int>) -> list<list><str>
    Takes a list of lists of integers and turns that
    image matrix into a compressed image matrix, consisting
    of a list of lists of strings, returning that.
    >>> compress([[11, 11, 11, 11, 11], [1, 5, 5, 5, 7], [255, 255, 255, 0, 255]])
    [['11x5'], ['1x1', '5x3', '7x1'], ['255x3', '0x1', '255x1']]
    >>> compress([[1, 1, 2, 2, 2, 3], [0, 0, 0, 0, 0, 7], [30, 40, 50, 60, 70, 80]])
    [['1x2', '2x3', '3x1'], ['0x5', '7x1'], ['30x1', '40x1', '50x1', '60x1', '70x1', '80x1']]
    >>> compress([[1, 3], [4, 4], [2, 2], [3, 0]])
    [['1x1', '3x1'], ['4x2'], ['2x2'], ['3x1', '0x1']]
    '''
    
    if not is_valid_image(pgm_list):
        raise AssertionError("List does not contain a valid image matrix.")
    
    comp_pgm_list = []
    
    for elmt in pgm_list:
        temp_list = []
        i = 0
        
        while i < len(elmt):
            found = find_end_of_repetition(elmt, i, elmt[i])
            
            temp_list.append(str(elmt[i]) + "x" + str(found-i+1))
            
            i += (found-i+1)
        
        comp_pgm_list.append(temp_list)
            
    return comp_pgm_list
        
        
def decompress(comp_pgm_list):
    ''' (list<list><str>) -> list<list><int>
    Takes a list of lists of strings and turns that
    compressed image matrix into a decompressed image matrix,
    consisting of a list of lists of integers, and returns that.
    >>> decompress([['11x5'], ['1x1', '5x3', '7x1'], ['255x3', '0x1', '255x1']])
    [[11, 11, 11, 11, 11], [1, 5, 5, 5, 7], [255, 255, 255, 0, 255]]
    >>> decompress([['1x1', '2x1', '5x2'], ['1x3', '5x1'], ['4x4']])
    [[1, 2, 5, 5], [1, 1, 1, 5], [4, 4, 4, 4]]
    >>> decompress([['255x20'], ['100x10', '5x7', '4x2', '0x1'], ['0x5', '5x5', '100x5', '200x5']])
    [[255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255], [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 5, 5, 5, 5, 5, 5, 5, 4, 4, 0], [0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 100, 100, 100, 100, 100, 200, 200, 200, 200, 200]]
    '''
    
    if not is_valid_compressed_image(comp_pgm_list):
        raise AssertionError("List does not contain a valid compressed image matrix.")
    
    pgm_list = []
    length = find_length_compressed_image(comp_pgm_list, 0)
    counter = 0
    
    for elmt in comp_pgm_list:
        temp_list = []
        i = 0
        
        
        while i < len(elmt):
            counter = 0
            
            x_loc = elmt[i].find('x')
            a = int(elmt[i][:x_loc])
            b = int(elmt[i][x_loc + 1:])
                        
            while counter < b:
                temp_list.append(a)
                counter += 1
                
            i += 1
        
        pgm_list.append(temp_list)
            
    return pgm_list

def process_command(commands):
    ''' (str) -> NoneType
    Takes a string of command shortcuts and
    performs those functions.
    >>> process_command("LOAD<comp.pgm> CP DC INV SAVE<comp2.pgm>")
    >>> load_image("comp2.pgm")
    [[255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255], [255, 204, 204, 204, 204, 204, 255, 136, 136, 136, 136, 136, 255, 68, 68, 68, 68, 68, 255, 0, 0, 0, 0, 255], [255, 204, 255, 255, 255, 255, 255, 136, 255, 255, 255, 136, 255, 68, 255, 68, 255, 68, 255, 0, 255, 255, 0, 255], [255, 204, 255, 255, 255, 255, 255, 136, 255, 255, 255, 136, 255, 68, 255, 68, 255, 68, 255, 0, 0, 0, 0, 255], [255, 204, 255, 255, 255, 255, 255, 136, 255, 255, 255, 136, 255, 68, 255, 68, 255, 68, 255, 0, 255, 255, 255, 255], [255, 204, 204, 204, 204, 204, 255, 136, 136, 136, 136, 136, 255, 68, 255, 68, 255, 68, 255, 0, 255, 255, 255, 255], [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255]]
    >>> process_command("LOAD<comp.pgm> INV FH FV CR<2,2,4,10> SAVE<comp2.1.pgm>")
    >>> load_image("comp2.1.pgm")
    [[255], [0], [255], [0]]
    >>> process_command("LOD<comp.pgm> FH SAVE<comp_test.pgm>")
    Traceback (most recent call last):
    AssertionError: Invalid starting command entered
    '''
        
    cmd_list = commands.split()
    last_index = len(cmd_list) - 1
    
    if cmd_list[0].find("LOAD<") < 0:
        raise AssertionError("Invalid starting command entered")
    
    if cmd_list[last_index].find("SAVE<") < 0:
        raise AssertionError("Invalid ending command entered")
    
    ## Loading ##
    
    lt_loc = cmd_list[0].find("<")
    gt_loc = cmd_list[0].find(">")
    filename = (cmd_list[0][lt_loc+1:gt_loc])
    
    img_matrix = load_image(filename)
    
    ## Middle Commands ##
    
    for elmt in cmd_list:
        
        if elmt.find("LOAD") > -1:
            continue
                        
        elif elmt.find("SAVE") > -1:
            continue
            
        elif elmt.find("INV") > -1:
            img_matrix = invert(img_matrix)
            
        elif elmt.find("FH") > -1:
            img_matrix = flip_horizontal(img_matrix)
    
        elif elmt.find("FV") > -1:
            img_matrix = flip_vertical(img_matrix)
            
        elif elmt.find("CR<") > -1:
            
            lt_loc = elmt.find("<")
            gt_loc = elmt.find(">")
            
            dimensions = elmt.split(',')
            dimensions[0] = dimensions[0][3]
            dimensions[3] = dimensions[3][0]
                        
            y = int(dimensions[0])
            x = int(dimensions[1])
            height = int(dimensions[2])
            width = int(dimensions[3])
                        
            img_matrix = crop(img_matrix, y, x, height, width)
            
        elif elmt.find("CP") > -1:
            img_matrix = compress(img_matrix)
            
        elif elmt.find("DC") > -1:
            img_matrix = decompress(img_matrix)
            
        else:
           raise AssertionError("Invalid command entered:" + elmt) 
     
     
    ## Saving ##
    lt_loc = cmd_list[last_index].find("<")
    gt_loc = cmd_list[last_index].find(">")
    new_filename = (cmd_list[last_index][lt_loc+1:gt_loc])
                    
    save_image(img_matrix, new_filename)    


if __name__ == "__main__":
    doctest.testmod()
    
    
    
    
    
    