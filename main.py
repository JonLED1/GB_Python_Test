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
            nb = my_nb.load()
            view.print_notes(nb, text.nb_empty)
        case 4:
            note = view.input_value(text.input_new_note)
            id = my_nb.add(note)
            view.print_message(text.new_note_successful(id))
        case 5:
            id = view.input_value(text.change_index)
            nb = my_nb.load()
            for n in range(len(nb)):
                if nb[n].get('id')==id:
                    new_text = view.input_value( nb[n].get('text'))
                    my_nb.change(n, new_text)
                    view.print_message(text.change_successful(id))
                    break
            else:
                view.print_message(text.change_error(id))
        case 6:
            id = view.input_value(text.del_index)
            nb = my_nb.load()
            for n in range(len(nb)):
                if nb[n].get('id')==id:
                    my_nb.delete(n)
                    view.print_message(text.del_successful(id))
                    break
            else:
                view.print_message(text.del_error(id))            
        case 7:
            
            break