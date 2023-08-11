import text
import view
import model

my_nb = model.NoteBook()

while True:
    choice = view.main_menu()

    match choice:
        case 1:
            my_nb.open()
            view.print_message(text.load_successful)
        case 2:
            my_nb.save()
            view.print_message(text.save_successful)
        case 3:
            pb = my_nb.load()
            view.print_notes(pb, text.nb_empty)
        case 4:
            note = view.input_note(text.input_new_note)
            id = my_nb.add(note)
            view.print_message(text.new_note_successful(id))
        case 5:
            pass
        case 6:
            pass
        case 7:
            break