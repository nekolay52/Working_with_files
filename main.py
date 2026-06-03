import os


class File:
    """
    Description or some text    
    """
    def __init__(self, file_name: str, create_or_not: bool, writing_content: str):
        self.file_name = file_name
        self.create_or_not = create_or_not
        self.writing_content = writing_content
        try:
            self.read()
        except:
            if create_or_not == True:
                self.create()
                if writing_content != "":
                    self.write(text = writing_content)
                
    def create(self):
        with open(self.file_name, 'w') as my_file:
            my_file.write("")

    def delete(self):
        os.remove(self.file_name)

    def rename(self, new_name: str):
        content = self.read()
        self.delete()
        self.file_name = new_name
        self.write(content)

    def write(self, text: str):
        with open(self.file_name, 'w') as my_file:
            my_file.write(text)

    def read(self):
        with open(self.file_name, 'r') as my_file:
            content = my_file.read()
            return content

    def copy(self, new_name: str):
        content = self.read()
        finally_copy = File(file_name = new_name, create_or_not = True, writing_content = content)
        return finally_copy

    def append(self, text: str):
        with open(self.file_name, 'r') as my_file:
            content = my_file.read()
        with open(self.file_name, 'w') as my_file:
            my_file.write(content + text)

