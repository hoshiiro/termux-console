import wikipedia
import os

os.system("figlet Wikipedia")
nm = input("\tInput Page Name: ")
page = wikipedia.page(nm)
sum = wikipedia.summary(nm, sentences=3)

os.system("clear")
print("\nInfo: \n==========")
print("Page Name: "+ page.title)
print("Page Url: "+ page.url)

def put():
    p = input("\n\tWanna read full content or just summary? [fc/sum]: ")
    if p == "fc" or p == "Fc":
        print("\nFull Content\n==========\n"+ page.content +"\n")
    elif p == "sum" or p == "Sum":
        print("\nSummary\n==========\n"+ sum +"\n")
    else:
        print("\n\t\tOption not found, try to write fc or sum.")
        put()

put()