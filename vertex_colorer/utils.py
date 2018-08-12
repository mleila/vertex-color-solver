''' A collection of utility functions '''

def varname_to_vertexID(varname):
    return int(varname.split('_')[0][6:])

def varname_to_colorID(varname):
    return int(varname.split('_')[1][5:])

def normalize_ints(lst):
    '''map items in list to ordered list of ints '''
    unique = list(set(lst))
    dic = {}
    for idx, item in enumerate(unique):
        dic[item] = idx
    return dic

if __name__ == '__main__':
    varname = 'Vertex12_color2'
    print(varname_to_vertexID(varname))
    print(varname_to_colorID(varname))
