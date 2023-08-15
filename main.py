from tkinter import filedialog,StringVar,Toplevel
import tkinter as tk
import pytesseract
from PIL import ImageTk,Image,ImageFilter
from googletrans import Translator
from langdetect import detect
from textblob import TextBlob


image_list=[]
text=[]
lang_list=[]
t_text_list=[]
detected_lang=[]

LANGUAGES={'afrikaans':'af','albanian':'sq',
'amharic':'am','arabic':'ar',
'armenian':'hy','azerbajani':'az',
'basque':'eu','belarusian':'be',
'bengali':'bn','bosnian':'bn','bulgarian':'bg',
'catalan':'ca','cebuano':'ceb',
'chichewa':'ny','chinese (simplified)':'zh-cn',
'chinese (traditional)':'zh-tw','corsican':'co','croatian':'hr',
'czech':'cs','danish':'da','dutch':'nl','english':'en','esparanto':'eo',
'estonian':'et','filipino':'tl','finnish':'fi','french':'fr',
'frisian':'fy','galican':'gl',
'georgian':'ka','german':'de','greek':'el','gujurati':'gu',
'haitian creole':'ht','hausa':'ha',
'hawaiian':'haw','hebrew':'he','hindi':'hi','hmong':'hmn','hungarian':'hu',
'icelandic':'is','igbo':'ig',
'indonesian':'id','irish':'ga','italian':'it','japanese':'ja','jawanese':'jw',
'kannada':'kn','kazakh':'kk','khmer':'km',
'korean':'ko','kurdish (kurmanji)':'ku','kyrgyz':'ky','lao':'lo','latvian':'lv',
'lithuanian':'lt','luxemborgish':'lb','macedonian':'mk','malagasy':'mg',
'malay':'ms','malayalam':'ml','maltese':'mt','maori':'mi','marathi':'mr',
'mongolian':'mn','myanmar (burmese)':'my',
'nepali':'ne','norwegian':'no','odia':'or','pashto':'ps','persian':'fa',
'polish':'pl','portugese':'pt','punjabi':'pa','romanian':'ro',
'russian':'ru','samoan':'sm','scots gaelic':'gd','sebian':'sr','sesotho':'st',
'sindhi':'sd','sinhala':'si','slovak':'sk','slovenian':'sl',
'somali':'so','spanish':'es','sundanese':'su','swahali':'sw','swedish':'sv',
'tajik':'tg','tamil':'ta','telugu':'te','thai':'th','turkish':'tr',
'ukranian':'uk','urdu':'ur','uyghur':'ug','uzbek':'uz','viatnamese':'vi',
'welsh':'cy','xhosa':'xh','yiddish':'yi','yoruba':'yo','zulu':'zu'}

new_window=tk.Tk()
window=Toplevel(new_window)
window.title("LENS")
window.geometry('500x500')
new_window.title("Result Window")
new_window.geometry('1000x1000')

def open_image():
    global i
    file_path =filedialog.askopenfilename()
    image_name=file_path.split('/')[-1]
    imag=Image.open(file_path)
    image_w,image_h=imag.size
    image_list.clear()
    image_list.append(imag)
    label=tk.Label(new_window,text=image_name+" has been uploaded")
    label.pack(side='top')
    i=ImageTk.PhotoImage(file=file_path)
    i_label=tk.Label(new_window,width=int(image_w), height=int(image_h),anchor=tk.CENTER)
    i_label.image = i
    i_label.configure(image=i_label.image)
    i_label.place(x=300,y=300)

def extract_text(img):
    if img:
        im = img.filter(ImageFilter.BLUR)
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        t=pytesseract.image_to_string(im)
        if t=="":
            text_label=tk.Label(new_window,text="There is no text in the above image")
            text_label.pack(pady=20)
        else:
            lan=detect(t)
            detected_lang.append(lan)
            text.clear()
            text.append(t)
            for name,code in LANGUAGES.items():
                if code==lan:
                    text_label=tk.Label(new_window,text="The Extracted Text in "+name+"\n "+t)
                    text_label.pack(pady=20)
    else:
        label=tk.Label(new_window,text="Please Upload an Image first")
        label.pack(side="top")

def correct_text(text):
    spell = TextBlob(text)
    corrected_text=spell.correct()
    label=tk.Label(new_window,text="Corrected Text"+"\n"+str(corrected_text))
    label.pack(side="bottom")

def translate_text(text,lang,detected_lang):
        translator=Translator(service_urls=['translate.googleapis.com'])
        t_text=translator.translate(text,src=detected_lang,dest=lang)
        t_text_list.clear()
        t_text_list.append(t_text.text)
        for name,code in LANGUAGES.items():
            if code==lang:
                label=tk.Label(new_window,text="Extracted Text in "+name+"\n"+t_text.text)
                label.pack(pady=20)

def save(text,translated_text):
    file_path=filedialog.asksaveasfile(filetypes = [('text files','*.txt')])
    file_name=file_path.name
    f= open(file_name,'w')
    f.write(fr"{text}")
    f.writelines(fr"{translated_text}")
    f.close()
    f_label=tk.Label(new_window,text="Your file has been saved as "+file_path.name)
    f_label.pack()


open_button=tk.Button(window,text="Open Image",command=open_image)
open_button.pack(pady=10)
extract_button=tk.Button(window,text="Extract Text From Image",command=lambda :extract_text(image_list[0]))
extract_button.pack(pady=10)
correct_button=tk.Button(window,text="Correct the Text",command=lambda :correct_text(text[0]))
correct_button.pack(pady=10)


menu=StringVar(window)
menu.set('english')
list_option=tk.OptionMenu(window,menu,*['afrikaans','albanian','amharic','arabic','armenian',
        'azerbajani','basque','belarusian','bengali','bosnian','bulgarian','catalan',
        'cebuano','chichewa','chinese (simplified)','chinese (traditional)','corsican',
        'croatian','czech','danish','dutch','english','esparanto','estonian','filipino',
        'finnish','french','frisian','galican','georgian','german','greek','gujurati',
        'haitian creole','hausa','hawaiian','hebrew','hindi','hmong','hungarian',
        'icelandic','igbo','indonesian','irish','italian','japanese','jawanese',
        'kannada','kazakh','khmer','korean','kurdish (kurmanji)','kyrgyz','lao','latvian',
        'lithuanian','luxemborgish','macedonian','malagasy','malay','malayalam','maltese',
        'maori','marathi','mongolian','myanmar (burmese)','nepali','norwegian','odia',
        'pashto','persian','polish','portugese','punjabi','romanian','russian','samoan',
        'scots gaelic','sebian','sesotho','sindhi','sinhala','slovak','slovenian','somali',
        'spanish','sundanese','swahali','swedish','tajik','tamil','telugu','thai','turkish',
        'ukranian','urdu','uyghur','uzbek','viatnamese','welsh','xhosa','yiddish','yoruba','zulu'])
list_option.pack(pady=10)

def submit():
  lang_list.append(LANGUAGES[menu.get()])

submit_lab=tk.Button(window,text="Submit",command=submit,)
submit_lab.pack(pady=10)
Translate_button=tk.Button(window,text="Translate Text From Image",command=lambda :translate_text(text[0],lang_list[0],detected_lang[0]))
Translate_button.pack(pady=10)
Save_button=tk.Button(new_window,text="Save",command=lambda: save(text[0],t_text_list[0]))
Save_button.pack(side='top')
new_window.mainloop()