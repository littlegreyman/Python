import re


'''
define the global variables
'''
content = ""
cursor_position = 0  ## to make the intial postion at 0 after append
## save the memory for the undo and repeat command
cursor_position_stack = []
memory_stack = []
command_stack = []
##using to adjust globle visible 
cursor_visible = True

def check_input(command):
    '''
    checking the legal input
    '''
    available_commands = ["?", ".", "h", "l", "^", "$", "w",
                          "b", "x", "dw", "u", "r", "s", "q"]
    if command in available_commands:
        return command
    elif command.startswith("a") or command.startswith("i"):
        return command[0]
    else:
        return False

def display_info():
    print("? – display this help info")
    print(". – toggle row cursor on and off")
    print("h - move cursor left")
    print("l - move cursor right")
    print("^ - move cursor to beginning of the line")
    print("$ - move cursor to end of the line")
    print("w - move cursor to beginning of next word")
    print("b - move cursor to beginning of previous word")
    print("i - insert <text> before cursor")
    print("a - append <text> after cursor")
    print("x - delete character at cursor")
    print("dw - delete word and trailing spaces at cursor")
    print("u - undo previous command")
    print("r - repeat last command")
    print("s - show content")
    print("q - quit program")

def toggle_cursor():
    global cursor_visible
    cursor_visible = not cursor_visible

def move_cursor(direction):
    global cursor_position
    if direction == 'h' and cursor_position > 0:
        cursor_position -= 1
    elif direction == 'l' and cursor_position < len(content):
        cursor_position += 1
    elif direction == '^':
        cursor_position = 0
    elif direction == '$':
        cursor_position = max(0, len(content) - 1)  
    elif direction == "w":
        new_position = content.find(" ", cursor_position)
        if new_position != -1:
            cursor_position = new_position
    elif direction == "b":
        new_position = content.rfind(" ", 0, cursor_position)
        new_position = content.rfind(" ", 0, new_position)
        if new_position != -1:
            cursor_position = new_position + 1
        else:
            cursor_position = 0
    memory_update()

def insert_text(command):
    global content, cursor_position
    insert_text = command[1:]
    content = content[:cursor_position] + insert_text + content[cursor_position:]
 
    memory_update()

def append_text(command):
    global content, cursor_position
    insert_text = command[1:]
    content = content[:cursor_position + 1] + insert_text + content[cursor_position + 1:]
    cursor_position += len(insert_text)
    memory_update()

def delete_character():
    global content, cursor_position
    if cursor_position < len(content):
        content = content[:cursor_position] + content[cursor_position + 1:]
    memory_update()

def delete_word():
    global content, cursor_position
    end_of_word = content.find(" ", cursor_position)
    if end_of_word != -1:
        content = content[:cursor_position] + content[end_of_word+1:]
    else:
        content = content[:cursor_position]
    memory_update()

def undo():
    global content, memory_stack, cursor_position
    try:
        if len(memory_stack)>1:
            content = memory_stack[-2]
            memory_stack.pop()
            cursor_position = cursor_position_stack[-2]
            cursor_position_stack.pop()
            return True
    except:
        pass
    return False
def repeat():
    if command_stack:
        return convert_command(command_stack[-1])
    return False

def show():
    if cursor_visible:
        cursor_marker = "\033[42m" + (" " if cursor_position >=\
                                       len(content) else content[cursor_position]) + "\033[0m"
        print_content = content[:cursor_position] + cursor_marker + content[cursor_position + 1:]
    else:
        print_content = content
    print(print_content)

def quit():
    exit()

def memory_update():
    cursor_position_stack.append(cursor_position)
    memory_stack.append(content)

def convert_command(command):
    global command_stack
    simple_command = check_input(command)
    if not simple_command:
        return False  

    need_show = False  

    if simple_command == "?":
        display_info()
    elif simple_command == ".":
        toggle_cursor()
        need_show = True
    elif simple_command in ["h", "l", "^", "$", "w", "b"]:
        move_cursor(simple_command)
        need_show = True
    elif simple_command == "i":
        insert_text(command)
        need_show = True
    elif simple_command == "a":
        append_text(command)
        need_show = True
    elif simple_command == "x":
        delete_character()
        need_show = True
    elif simple_command == "dw":
        delete_word()
        need_show = True
    elif simple_command == "u":
        if undo():
            need_show = True
    elif simple_command == "r":
        need_show = repeat()
    elif simple_command == "s":
        show()
    elif simple_command == "q":
        quit()

    # 更新命令堆栈（u和r不重复记录）
    if simple_command not in ["u", "r"]:
        command_stack.append(command)

    return need_show

def main():
    while True:
        input_command = input(">")
        need_show = convert_command(input_command)
        if need_show:
            show()

if __name__ == "__main__":
    main()