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

app_name = tk.Label(app, text=" Welcome To My Translator ", font="arial 20 bold")
app_name.place(x= 170, y=10)

# app_name2 = tk.Label(app, text="Enter Your Text Here ", font="arial 15 bold")
# app_name2.place(x=35, y=345)

input_text = tk.Text(app, font="arial 10", height=15, width=40)
input_text.place(x=15, y=100)
input_quote = " Enter your text here "
input_text.insert(tk.END, input_quote)

input_lang = ttk.Combobox(app, width=40, values=Language_names)
input_lang.place(x=15, y=75)
input_lang.set(Language_names[0])
#---------------------------------------------------------------------
# out_name2 = tk.Label(app, text=" Translated Text Here ", font="arial 15 bold")
# out_name2.place(x=440, y=345)

output_text = tk.Text(app, font="arial 10", height=15, width=40)
output_text.place(x=400, y=100)
output_quote = " Translated text here "
output_text.insert(tk.END, output_quote)

out_lang = ttk.Combobox(app, width=40, values=Language_names)
out_lang.place(x=400, y=75)
out_lang.set(Language_names[1])
#-------------------------------------------------------------------
def translate():
  translated_text = lt.translate(input_text.get("1.0", tk.END), Language_codes[input_lang.get()], Language_codes[out_lang.get()])
  output_text.delete("1.0",tk.END)
  output_text.insert("1.0", translated_text)  

trans_btn = tk.Button(app, text="Translate", font="arial 10 bold", padx=5, width=9, command=translate)
trans_btn.place(x=307, y=180)

def clear():
    input_text.delete("1.0",tk.END)
    output_text.delete("1.0",tk.END)
  
clear_btn = tk.Button(app, text="Clear", font="arial 10 bold", padx=5, width=9, command=clear)
clear_btn.place(x=307, y=220)

app.mainloop()