import text


def main_menu() -> int:
    print(text.main_menu)
    while True:
        choice = input(text.input_choice)
        if choice.isdigit() and 0 < int(choice) < 9:
            return int(choice)


def print_message(message: str):
    print('\n' + '=' * len(message))
    print(message)
    print('=' * len(message) + '\n')


def print_notes(book: list[dict[str, str]], error: str):
    if book:
        print('\n' + '=' * 71)
        for notes in book:
            print(f'Записка №{notes.get("id")} от {notes.get("data")}')
            text_note = str(notes.get("text"))
            count = 0
            for n in (text_note):
                print (n, end='')
                if count == 70:
                    print ('\n', end='')
                    count = -1
                count = count + 1
            print('\n'+'=' * 71 )
    else:
        print_message(error)
        
def input_note(message):
    value = input(message)
    return value



