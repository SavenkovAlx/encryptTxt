#!/usr/bin/python3
import tkinter
import tkinter.filedialog as tkFileDialog
import tkinter.messagebox as tkMessageBox

# the key to encrypt/decrypt symetrical with
key = b'\xb12N\xf4y\x07m\xa7\xae\xe1\xfc8Tv\xa3r?\xbb=0\xf3&\x8e\x94\xeb\xe9x\xf5\xaa\xa7%\x9b'


# encrypt the string
def encrypt(plain_text, key):
    # returns plain text by repeatedly xoring it with key
    pt = plain_text
    len_key = len(key)
    encoded = []

    for i in range(0, len(pt)):
        encoded.append(pt[i] ^ key[i % len_key])
    return bytes(encoded)


# encrypt a file
def encrypt_txt(file_name, key):
    with open(file_name, 'rb') as f:  # open the file, reading it as binary
        plaintext = f.read()  # store the text from the file
    enc = encrypt(plaintext, key)  # encrypt the text
    # create a new file with .enc extension, and write as binary
    with open(file_name[:-4] + "_encrypt.txt", 'wb') as f:
        f.write(enc)  # write or place, the enc ciphertext in the new file


# get the text file from the user
def load_txt():
    global key, filename  # global variable
    txtfile = tkFileDialog.askopenfile(
        filetypes=[('Text Files', '*.txt')])  # get the file address
    if txtfile.name != None:  # if a file was selected
        filename = txtfile.name  # set the global variable, filename, to the selected file's name


filename = None


# encrypt file function for the GUI button
def encrypt_the_file():
    global key, filename
    if filename != None:  # encrypt the file
        encrypt_txt(filename, key)
        tkinter.messagebox.showinfo(title='Успіх', message='Ваш файл успішно зашифровано')
    else:  # show error
        tkMessageBox.showerror(
            title="Помилка", message="Не був завантажений файл для шифрування")


# create the GUI window
root = tkinter.Tk()
# set the window title to "CryptoFile"
root.title("Шифрування файлу")
root.minsize(width=200, height=200)
root.maxsize(width=200, height=200)

# create the buttons for the application
loadTxtBtn = tkinter.Button(root, text="Загрузити текстовий файл", command=load_txt)
encryptBtn = tkinter.Button(root, text="Зашифрувати файл",
                            command=encrypt_the_file)

loadTxtBtn.pack()
encryptBtn.pack()

# start the mainloop of the applications
root.mainloop()
