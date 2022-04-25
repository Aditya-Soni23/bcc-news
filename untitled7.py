from tkinter import *
import requests
import json

root=Tk()
root.overrideredirect(True)
root.title("Country City App")
root.geometry("700x1000")

root.configure(background="white")
#Setting labels
city_name_label=Label(root, text="BCC NEWS UPDATE",font=("Helvetica", 18,'bold'),bg="yellow")
city_name_label.place(relx=0.40,rely=0.03,anchor=CENTER)

weather_info_label = Label(root,text="Title 1: ", bg="cyan", font=("bold", 10))
weather_info_label.place(relx=0.22,rely=0.2,anchor=CENTER) 

humidity_info_label = Label(root,text="Description 1: ", bg="cyan", font=( "bold",10)) 
humidity_info_label.place(relx=0.22,rely=0.19,anchor=CENTER) 

language_info_label = Label(root,text="Title 2: ", bg="cyan", font=( "bold",10)) 
language_info_label.place(relx=0.22,rely=0.3,anchor=CENTER) 

population_info_label = Label(root,text="Description 2: ", bg="cyan", font=( "bold",10)) 
population_info_label.place(relx=0.22,rely=0.29,anchor=CENTER) 

area_info_label = Label(root,text="Title 3: ", bg="cyan", font=( "bold",10)) 
area_info_label.place(relx=0.22,rely=0.4,anchor=CENTER) 

title_info_label = Label(root,text="Description 3: ", bg="cyan", font=( "bold",10)) 
title_info_label.place(relx=0.22,rely=0.39,anchor=CENTER) 

title44_info_label = Label(root,text="Title 4: ", bg="cyan", font=( "bold",10)) 
title44_info_label.place(relx=0.22,rely=0.5,anchor=CENTER) 

title4_info_label = Label(root,text="Description 4: ", bg="cyan", font=( "bold",10)) 
title4_info_label.place(relx=0.22,rely=0.49,anchor=CENTER) 

title55_info_label = Label(root,text="Title 5: ", bg="cyan", font=( "bold",10)) 
title55_info_label.place(relx=0.22,rely=0.6,anchor=CENTER) 

title5_info_label = Label(root,text="Description 5: ", bg="cyan", font=( "bold",10)) 
title5_info_label.place(relx=0.22,rely=0.59,anchor=CENTER) 




api_request = requests.get("https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=1aa41e74fabf466b862c3b5398f1adb7")
    
api_output_json = json.loads(api_request.content)
    
weather_info = api_output_json["title1"]
print(weather_info)
    
humidity = api_output_json["desc1"]
print(str(humidity))
    
language = api_output_json["title2"]
print(str(language))
    
population = api_output_json["desc2"]
print(str(population))
    
area = api_output_json["title3"]
print(str(area))
    
des3_info = api_output_json["desc3"]
print(des3)
    
title4 = api_output_json["title4"]
print(str(title4))

des4 = api_output_json["desc4"]
print(str(des4))
    
title5 = api_output_json["title5"]
print(str(title5))
    
des5 = api_output_json["desc5"]
print(str(des4))
    
    
    
weather_info_label["text"] = "Title 1 : " + str(weather_info)
humidity_info_label["text"] = "Description 1 : " + str(humidity)
language_info_label["text"] = "Title 2 : " + str(language)
population_info_label["text"] = "Description 2 : " + str(population)
area_info_label["text"] = "Title 3 : " + str(area)
des3_info_label["text"] = "Description 3 : " + str(des3_info)
title4_info_label["text"] = "Title 4 : " + str(title4)
des4_info_label["text"] = "Description 4 : " + str(des4)
title5_info_label["text"] = "Title 5 : " + str(title5)
des5_info_label["text"] = "Description 5 : " + str(title5)
    
    
    
    
root.mainloop()
