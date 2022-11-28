FILEPATH = 'todos.txt'

def show_l(list):
    for index, item in enumerate(list):
        item = item.replace("\n","")
        print(f"{index+1}. {item}")

def read_file(filename=FILEPATH):
    new_list = []
    with open(filename, 'r') as file:
        new_list = file.readlines()
        return(new_list)

def update_file(list, filename=FILEPATH):
    """
        Take a list and saved it in a file. Default file is todos.txt
    """
    with open(filename,'w') as file: 
            file.writelines(list)

print(__name__)

# if __name__=="__main__":
#     print("Hello from functions") 