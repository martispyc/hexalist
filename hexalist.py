class hexlist:
    def __init__(self, max_val=99, starting_val=0):

        # CHANGEABLE
        self.max_val = max_val
        self.starting_val = starting_val


        # MAIN DS INIT
        self.hex_dict = {key_p:{key:self.starting_val for key in [str(i) for i in range(1,11)]+["A", "B", "C", "D", "E", "F"]} 
            for key_p in [str(i)+"x" for i in [n for n in range(1,11)]+["A", "B", "C", "D", "E", "F"]]}
        self.key_list = [[s+"x", s] for s in ([str(i+1) for i in range(10)]+["A", "B", "C", "D", "E", "F"])]



    def __repr__(self):
        repr_string = ""
        spaces = 4

        for key1 in self.hex_dict:
            repr_string += f"{key1}{' '*(spaces+4)}"

        repr_string += '\n'

        for i in range(16):
            for key1 in self.hex_dict:
                test = self.key_list[key1[i]][1]
                test = self.hex_dict[key1][self.key_list[i][1]]
                repr_string += f" \\{self.key_list[key1[i]][1]}: {self.hex_dict[key1][self.key_list[i][1]]}{' '*spaces}"
            
            repr_string += '\n'

        return repr_string

        # for e in self.hex_dict: hexlist_string += f"{}"
        # # hexlist_string = ""
        # # for i in range(16):
        # #     pass
        # #     hexlist_string += f"\n{self.key_list[i][1]+' ' if self.key_list[i][1] != ' ' else self.key_list[i][1]}|".join(["0"+n+"|" if n<10 else n+"|" for n in ])

        # return hexlist_string


    def __mul__(self, x): #TODO -- make more efficient
        if type(x) is not int:
            raise Exception("Invalid arguments, mus be int")

        for key1 in self.hex_dict:
            self.hex_dict[key1].update((key, ele*x if ele*x<100 else ele-ele+self.max_val) for key, ele in self.hex_dict[key1].items())

    
    def __rmul__(self, x):
        self.__mul__(x)
        return self.__repr__()

    def __call__(self, string):
        if type(string) is not str:
            raise Exception("Invalid arguments, mus be str")

        if len(string) == 3: # Not using shortcut
            return self.hex_dict[string[0:1]][string[2]]
        elif len(string) == 1: # Using shortcut
            return self.hex_dict[string+"x"][string]
        else:
            raise Exception("Invalid index")


if __name__ == '__main__':
    '''
    * (*) multiplies every elemnet, till max_val. ex. {name} * n
    * index can be H1xH2 or H as HxH, return value. ex. {name}(index)
    * 
    '''

    my_hexlist = hexlist(starting_val=1)

    print(2*my_hexlist)

