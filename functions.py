FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_args, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todos_args)

if __name__ == "__main__":
    # Om de functies los te testen
    # __name__ is __main__ wanneer dit script los gedraaid wordt buiten de aanroepende script om
    print(get_todos())