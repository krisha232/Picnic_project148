from tkinter import*
import random

root=Tk()
root.title("Project_148")
root.geometry("500x400")
root.configure(background="lightgreen")

list=["food","juice", "mat","bottle", "ID card","chocolates", "mosquito spray"]
picnic_items=Label(root)
picnic_items["text"] = "Listed Items" + str(list)
item_number=Label(root)

def chooseItem() :
    random_number = random.randint(1,7)
    
    item_number["text"] = "Put Item no " + str(random_number) +" in the bag"
    
    
    
btn= Button(root, text="Which Item To Put In The Bag?", command=chooseItem)
btn.place(relx=0.5, rely=0.5,anchor = CENTER)


picnic_items.place(relx=0.5, rely=0.4,anchor = CENTER)
item_number.place(relx=0.5, rely=0.6,anchor = CENTER)

root.mainloop()