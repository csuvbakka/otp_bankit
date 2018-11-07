matrix_string = '''
1234 
5678 
9012'''

big_matrix_string = '''
37107287533902102798797998220837590246510135740250
46376937677490009712648124896970078050417018260538
74324986199524741059474233309513058123726617309629
91942213363574161572522430563301811072406154908250
23067588207539346171171980310421047513778063246676
89261670696623633820136378418383684178734361726757
28112879812849979408065481931592621691275889832738
44274228917432520321923589422876796487670272189318
47451445736001306439091167216856844588711603153276
70386486105843025439939619828917593665686757934951
62176457141856560629502157223196586755079324193331
64906352462741904929101432445813822663347944758178
92575867718337217661963751590579239728245598838407
58203565325359399008402633568948830189458628227828
80181199384826282014278194139940567587151170094390
18336384825330154686196124348767681297534375946515
80386287592878490201521685554828717201219257766954
78182833757993103614740356856449095527097864797581
16726320100436897842553539920931837441497806860984
48403098129077791799088218795327364475675590848030
87086987551392711854517078544161852424320693150332
59959406895756536782107074926966537676326235447210
69793950679652694742597709739166693763042633987085
41052684708299085211399427365734116182760315001271
65378607361501080857009149939512557028198746004375
35829035317434717326932123578154982629742552737307
94953759765105305946966067683156574377167401875275
88902802571733229619176668713819931811048770190271
25267680276078003013678680992525463401061632866526
36270218540497705585629946580636237993140746255962
24074486908231174977792365466257246923322810917141
91430288197103288597806669760892938638285025333403
34413065578016127815921815005561868836468420090470
23053081172816430487623791969842487255036638784583
11487696932154902810424020138335124462181441773470
63783299490636259666498587618221225225512486764533
67720186971698544312419572409913959008952310058822
95548255300263520781532296796249481641953868218774
76085327132285723110424803456124867697064507995236
37774242535411291684276865538926205024910326572967
23701913275725675285653248258265463092207058596522
29798860272258331913126375147341994889534765745501
18495701454879288984856827726077713721403798879715
41698116222072977186158236678424689157993532961922
62467957194401269043877107275048102390895523597457
22918802058777319719839450180888072429661980811197
77158542502016545090413245809786882778948721859617
72107838435069186155435662884062257473692284509516
20849603980134001723930671666823555245252804609722
53503534226472524250874054075591789781264330331690
'''


class StartIterator(object):
    def __init__(self):
        self.end_index = -1
        self.column_index = -1


class RightIterator(object):
    def __init__(self, up_iterator, distance):
        self.row_index = up_iterator.end_index + 1
        self.start_index = up_iterator.column_index + 1
        self.end_index = self.start_index + distance if distance > 0 else self.start_index
        self.distance = distance

    def loop(self):
        for column_index in range(self.start_index, self.end_index):
            yield self.row_index, column_index


class DownIterator(object):
    def __init__(self, right_iterator, distance):
        self.column_index = right_iterator.end_index - 1
        self.start_index = right_iterator.row_index + 1
        self.end_index = self.start_index + distance if distance > 0 else self.start_index
        self.distance = distance

    def loop(self):
        for row_index in range(self.start_index, self.end_index):
            yield row_index, self.column_index


class LeftIterator(object):
    def __init__(self, down_iterator, distance):
        self.row_index = down_iterator.end_index - 1
        self.start_index = down_iterator.column_index - 1
        self.end_index = self.start_index - distance if distance > 0 else self.start_index
        self.distance = distance

    def loop(self):
        for column_index in range(self.start_index, self.end_index, -1):
            yield self.row_index, column_index


class UpIterator(object):
    def __init__(self, left_iterator, distance):
        self.column_index = left_iterator.end_index + 1
        self.start_index = left_iterator.row_index - 1
        self.end_index = self.start_index - distance if distance > 0 else self.start_index
        self.distance = distance

    def loop(self):
        for row_index in range(self.start_index, self.end_index, -1):
            yield row_index, self.column_index


def traverse(matrix):
    traversed_numbers = []
    vertical_distance = len(matrix)
    horizontal_distance = len(matrix[0])
    iterator = StartIterator()

    while True:

        iterator = RightIterator(iterator, horizontal_distance)
        for row_index, column_index in iterator.loop():
            traversed_numbers.append(matrix[row_index][column_index])
        vertical_distance -= 1
        if vertical_distance <= 0:
            break

        iterator = DownIterator(iterator, vertical_distance)
        for row_index, column_index in iterator.loop():
            traversed_numbers.append(matrix[row_index][column_index])
        horizontal_distance -= 1
        if horizontal_distance <= 0:
            break

        iterator = LeftIterator(iterator, horizontal_distance)
        for row_index, column_index in iterator.loop():
            traversed_numbers.append(matrix[row_index][column_index])
        vertical_distance -= 1
        if vertical_distance <= 0:
            break

        iterator = UpIterator(iterator, vertical_distance)
        for row_index, column_index in iterator.loop():
            traversed_numbers.append(matrix[row_index][column_index])
        horizontal_distance -= 1
        if horizontal_distance <= 0:
            break

    return traversed_numbers


def string_to_matrix(matrix_str):
    lines = matrix_str.split('\n')
    lines = [line.strip() for line in lines if line]
    matrix = []
    for line in lines:
        row = []
        for char in line:
            row.append(int(char))
        matrix.append(row)
    return matrix


def generate_account_number(random_number):
    start_index = 79
    step = 103
    account_number = ''
    for num in range(start_index - 1, len(random_number), step):
        account_number += str(num)

    return account_number


if __name__ == '__main__':
    print(generate_account_number(traverse(string_to_matrix(big_matrix_string))))