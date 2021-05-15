import random
class CSVFile:
    csv_file = None
    def __init__(self, file_name):
        self.csv_file = open(file_name, 'w+')
    def write_line(self, line):
        self.csv_file.write(line + '\n')
    def close_file(self):
        self.csv_file.close()

def add_dict(dict):
    dict["NewKey"] = "NewValue" 
    return dict
def update_dict(dict):
    update_item = {"Update":"First"}
    dict.update(update_item) 
    return dict
def contain_dict(dict):
    element = 'thisKey5'
    if element in dict:
        return 1
    else:
        return 0
def del_first_dict(dict): 
    del dict["thisKey0"]
    return dict
def del_last_dict(dict):
    after = dict.popitem()
    return after
import time
def bench(f,inp):
    t1 = time.time()
    ans = f(inp)
    t2 = time.time()
    t = "{:.14f}".format(t2-t1)
    return t
def MakeDict(size):
    dict = {}
    for i in range(0,size):
        dict['thisKey'+str(i)] = random.randint(0,size)
    return dict

def dict_main():
    add_dictionary = CSVFile("add_to_dictionary")
    update_the_dictionary = CSVFile("update_to_dictionary")
    contain_the_dictionary = CSVFile("contain_in_dictionary")
    delete_first_dictionary = CSVFile("delete_beginning_dictionary")
    delete_last_dictionary = CSVFile("delete__last_dictionary")
    for i in range(1,21):
        size = i * 10000
        dict = MakeDict(size)
        #check run time ----------------------
        time = bench(add_dict, dict)
        string = str(size) + ", " + str(time)
        # #write to file
        add_dictionary.write_line(string)
        #check run time ----------------------
        time = bench(contain_dict, dict)
        string = str(size) + ", " + str(time)
        #write to file
        contain_the_dictionary.write_line(string)
        #check run time ----------------------
        time = bench(del_first_dict, dict)
        string = str(size) + ", " + str(time)
        #write to file
        delete_first_dictionary.write_line(string)
        #check run time ----------------------
        time = bench(del_last_dict, dict)
        string = str(size) + ", " + str(time)
        #write to file
        delete_last_dictionary.write_line(string)
        #check run time ----------------------
        time = bench(update_dict, dict)
        string = str(size) + ", " + str(time)
        #write to file
        update_the_dictionary.write_line(string)
        
            
dict_main()
