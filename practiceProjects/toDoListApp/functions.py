FILEPATH = "todos_item.txt"


def get_todos(filepath=FILEPATH):
    """read a text file and return the list of todos"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_args, filepath=FILEPATH):
    """Write the list of todos into the text file"""

    with open(filepath, "w") as file:
        file.writelines(todos_args)



if __name__ == "__main__":
    print("Hello")
    print(get_todos())

