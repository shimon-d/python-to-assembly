from tkinter import *
from subprocess import PIPE, Popen

root = Tk()
root.title("Python to Assembly Editor")

python_text = Text(root)
python_text.pack(side=LEFT)

asm_text = Text(root)
asm_text.pack(side=RIGHT)


def compile_code():
    python_code = python_text.get("1.0", END)
    proc = Popen(["python", "-m", "dis"], stdin=PIPE, stdout=PIPE)
    asm_code = proc.communicate(input=python_code.encode())[0].decode()
    asm_text.delete("1.0", END)
    asm_text.insert(END, asm_code)


compile_button = Button(root, text="Compile", command=compile_code)
compile_button.pack()

root.mainloop()
