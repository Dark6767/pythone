class Editor:
    document = 'Даже у динрозавра не хватит мощи жизнь жёстче'
    license_key='555'
    def view_document(self):
        print(Editor.document)
    def edit_document(self):
        print('В данной версии программы редактирование невозможно')
        key = input('Введите лицензионный ключ >')
        if key==Editor.license_key:
            return True
        else:
            print('Лицензионный ключ неверный')
            return False
class ProEditor(Editor):
    def edit_document(self):
        text = input('НАпишите текст который следует добавить в документ')
        Editor.document+=' '+text
File = Editor()
File.view_document()
if File.edit_document()==True:
    File = ProEditor()
File.edit_document()
File.view_document()