import random
class CSVFile:
    csv_file = None
    def __init__(self, file_name):
        self.csv_file = open(file_name, 'w+')
    def write_line(self, line):
        self.csv_file.write(line + '\n')
    def close_file(self):
        self.csv_file.close()
# Function reserve the list
def reverse_list(my_list):
    my_list.reverse()
    return my_list
# Function sort the list
def sort_list(my_list):
    my_list.sort()
    return my_list
# Function to add an element at the end of the list
def add_end(my_list):
    my_list.append(44)
    return my_list
#Function to delete that last element of the list
def delete_end(my_list):
    my_list.pop()
    return my_list
#Function to add num to middle
def add_middle(my_list):
    user_num = 44
    my_list.insert(len(my_list)//2, user_num)
    return my_list
#Function to delete the middle num
def delete_middle(my_list):
    del my_list[len(my_list)//2]
    return my_list
# add to beginning of the list
def add_beginning(my_list):
    user_num = 1
    my_list.insert(0, user_num)
    return my_list
# delete from beginning for the list
def delete_beginning(my_list):
    del my_list[0]
    return my_list
# Function to check if element is in the list
def in_list(my_list):
    user_num = 4890
    if (user_num in my_list):
        return 1
    else:
        return 0
import time
def bench(f,inp):
    t1 = time.time()
    ans = f(inp)
    t2 = time.time()
    t = "{:.14f}".format(t2-t1)
    return t

def list_main():
    add_to_end = CSVFile("add_to_end-List")
    delete_at_end = CSVFile("delete_end-List")
    add_to_middle = CSVFile("add_to_middle-List")
    delete_the_middle = CSVFile("delete_middle-List")
    add_to_beginning = CSVFile("add_to_beginning-List")
    delete_the_beginning = CSVFile("delete_beginning-List")
    in_the_list = CSVFile("In_List")
    reverse_the_list = CSVFile("reverse_List")
    sort_the_list = CSVFile("sort_List")
    # Creating random elements in the list
    for i in range(1,21):
        userRange = i * 100000
        #make list
        my_list = [random.randrange(0, 10**6) for j in range(userRange)]
        #check run time ----------------------
        time = bench(add_end, my_list)
        string = str(userRange) + ", " + str(time)
        #write to file
        add_to_end.write_line(string)
        #check run time ----------------------
        time = bench(delete_end, my_list)
        string = str(userRange) + ", " + str(time)
        #write to file
        delete_at_end.write_line(string)
        #check run time ----------------------
        time = bench(add_middle, my_list)
        string = str(userRange) + ", " + str(time)
        #write to file
        add_to_middle.write_line(string)
        #check run time ----------------------
        time = bench(delete_middle, my_list)
        string = str(userRange) + ", " + str(time)
        #write to file
        delete_the_middle.write_line(string)
        #check run time ----------------------
        time = bench(add_beginning, my_list)
        string = str(userRange) + ", " + str(time)
        #write to file
        add_to_beginning.write_line(string)
        #check run time ----------------------
        time = bench(delete_beginning, my_list)
        string = str(userRange) + ", " + str(time)
        #write to file
        delete_the_beginning.write_line(string)
        #check run time ----------------------
        time = bench(in_list, my_list)
        string = str(userRange) + ", " + str(time)
        #write to file
        in_the_list.write_line(string)
	#check run time ----------------------
        time = bench(reverse_list, my_list)
        string = str(userRange) + ", " + str(time)
        #write to file
        reverse_the_list.write_line(string)
	#check run time ----------------------
	time = bench(sort_list, my_list)
        string = str(userRange) + ", " + str(time)
        #write to file
        sort_the_list.write_line(string)

list_main()