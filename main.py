import tkinter as tk
from tkinter import ttk
from libretranslatepy import LibreTranslateAPI

lt = LibreTranslateAPI("https://translate.argosopentech.com/")
Language_data = lt.languages()
Language_names = [lang['name'] for lang in Language_data]
Language_codes = {lang['name']: lang['code'] for lang in Language_data}


app = tk.Tk()
app.geometry('700x400')
app.resizable(False, False)
app.title("Mo Translator V1.0")
app.config()

app_name = tk.Label(app, text=" Welcome To My Translator ", font="arial 15 bold")
app_name.place(x= 230, y=0)

app_name2 = tk.Label(app, text="Enter Your Text Here ", font="arial 15 bold")
app_name2.place(x=15, y=45)

input_text = tk.Text(app, font="arial 10", height=11, width=40)
input_text.place(x=15, y=100)

input_lang = ttk.Combobox(app, width=19, values=Language_names)
input_lang.place(x=55, y=75)
input_lang.set(Language_names[0])
#---------------------------------------------------------------------
out_name2 = tk.Label(app, text=" Translated Text Here ", font="arial 15 bold")
out_name2.place(x=440, y=45)

out_text = tk.Text(app, font="arial 10", height=11, width=40)
out_text.place(x=400, y=100)

out_lang = ttk.Combobox(app, width=19, values=Language_names)
out_lang.place(x=440, y=75)
out_lang.set(Language_names[1])
#-------------------------------------------------------------------
def translate():
  translated_text = lt.translate(input_text.get("1.0", tk.END), Language_codes[input_lang.get()], Language_codes[out_lang.get()])
  out_text.delete("1.0",tk.END)
  out_text.insert("1.0", translated_text)  


trans_btn = tk.Button(app, text="Translate", font="arial 10 bold", padx=5, width=9, command=translate)
trans_btn.place(x=307, y=180)

def clear():
    input_text.delete("1.0",tk.END)
    out_text.delete("1.0",tk.END)


  
clear_btn = tk.Button(app, text="Clear", font="arial 10 bold", padx=5, width=9, command=clear)
clear_btn.place(x=307, y=220)


app.mainloop()
