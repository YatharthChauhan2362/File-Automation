# import os
# import shutil
# path = input("Enter Path: ")
# files = os.listdir(path)

# for file in files:
#     filename, extension = os.path.splitext(file)
#     extension = extension[1:]
#     if os.path.exists(path+'/'+extension):
#         shutil.move(path + '/' + file, path + '/'+extension + '/'+file)
#     else:
#         os.makedirs(path + '/' + extension)
#         shutil.move(path + '/' + file, path + '/' + extension + '/' + file)

# Organizing Files Using Python Automation (PYTHAKON)

# PYTHAKON TEAM:
# Yatharth Chauhan
# Sansriti Ishwar
# Reeya Thanki
# Mehul Patel

from tkinter import *
from tkinter import filedialog
import os
import shutil

class GUI(Tk):
    def _init_(self):
        super()._init_()
        self.geometry('400x300')

    def gettingPath(self):
        self.path = filedialog.askdirectory()
        return self.path

    def startButton(self, path_value):
        self.button_Frame = Frame(self)
        self.button_Frame.pack()
        self.start_Button = Button(self.button_Frame, text='Start', command=lambda: self.startOperation(
            path_value)).grid(row=0, column=0)

    def startOperation(self, path_value):
        count = 0
        os.chdir(path_value)
        self.file_list = os.listdir()
        no_of_files = len(self.file_list)

        if len(self.file_list) == 0:
            self.error_label = Label(text="Error empty folder").pack()
            exit()
        for file in self.file_list:
            if file.endswith(".doc"):
                self.dir_name = "DOC"
                self.new_path = os.path.join(path_value, self.dir_name)
                self.file_list = os.listdir()

            if file.endswith(".png"):
                self.dir_name = "PNG"
                self.new_path = os.path.join(path_value, self.dir_name)
                self.file_list = os.listdir()
                if self.dir_name not in self.file_list:
                    os.mkdir(self.new_path)
                shutil.move(file, self.new_path)

            elif file.endswith(".txt"):
                self.dir_name = "TextFiles"
                self.new_path = os.path.join(path_value, self.dir_name)
                self.file_list = os.listdir()
                if self.dir_name not in self.file_list:
                    os.mkdir(self.new_path)
                shutil.move(file, self.new_path)
            count = count+1

        if(count == no_of_files):
            success = Label(text="Operation Successful!").pack()
        else:
            error = Label(text="Failed").pack()


if _name_ == '_main_':
    object = GUI()
    path = object.gettingPath()
    object.startButton(path)
    object.mainloop()
    