import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("Current time is ",now)

while True:
    user_action = input("Type add, edit, show, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + "\n")

        functions.write_todos(todos)

    elif user_action.startswith("show"):

        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print (row)
    
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)

            number = number-1

            todos = functions.get_todos()

            new_todo = input("Please enter new TODO: ")
            todos[number] = new_todo + "\n"

            functions.write_todos(todos)
        except ValueError:
            print("Your Command is not Valid. ")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            number = number-1

            todos = functions.get_todos()

            todo_to_remove = todos[number].strip('\n')
            todos.pop(number)

            functions.write_todos(todos)

        except ValueError:
            print("Your Command is not Valid. ")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("You have the wrong command, please try again")
        continue
        

