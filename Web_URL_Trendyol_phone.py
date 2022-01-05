#pip3 install requests
#pip3 install bs4
#pip3 install smtplib
import requests
from bs4 import BeautifulSoup
from smtplib import SMTP


#min_price = 0
#max_price = 150000
#The price range is determined
user_price1 = 0
user_price2 = 0
def prices_range():
    global user_price1
    global user_price2
    print("please enter the price range! The value range is from 249 to 150000.")
    try:
        user_price1 = int(input("Give the min prices: "))

        if 248 >= user_price1 or user_price1 >= 150000:
            print("You entered an incorrect value.. Please enter a value between 249 and 150000. ")
            prices_range()

            
        user_price2 = int(input("Give the max prices: "))

        if 248 >= user_price2 or user_price2 >= 150000 or (user_price1 + 100) > user_price2  :
            print("You entered an incorrect value.. Please enter a value between 249 and 150000.. and The user_prices2 must be at least 100 TL greater than user_prices1.")
            prices_range()

    except ValueError:
        print("You entered an incorrect value.. Please enter a value between 0 and 150000..")
        prices_range()
    
prices_range()


#Trendyol url link.
base_url = "https://www.trendyol.com/sr/cep-telefonu-x-c103498?sst=PRICE_BY_ASC&prc="

#The phone links have in this list.
all_phone_links = []

#The page counter.
cntr = 1

while True:

    #it helps us to set the Url we want.
    requests_url = (base_url + str(user_price1) + "-" + str(user_price2) + "&pi=" + str(cntr)) 

    #The request library handles data scraping from the website.
    r = requests.get(requests_url)
    
    #Checks if requests have as much data as requested
    if r.status_code == 200:
        
        #It helps us to change the captured URL as we want.
        soup = BeautifulSoup(r.content, "html.parser")
        try:
            all_phone_informations = soup.find("div", attrs={"class":"prdct-cntnr-wrppr"}).find_all("div", attrs={"class":"p-card-wrppr"})
        except AttributeError:
            break
        phone_links = list(map(lambda phone: "https://www.trendyol.com" + phone.find("a").get("href"), all_phone_informations))
        all_phone_links.append(phone_links)


    #breaks the loop
    else:
        break
    
    cntr += 1







#Where links will be collected in one list.
new_all_phone_links = []

#This loop cleans the lists inside the list.
for links in all_phone_links:
    for one_link in links:
        new_all_phone_links.append(one_link)


#This list stores the 4 cheapest priced items, the 4 mid-priced items, and the 4 most expensive items.
mail_phone_links = []

#From the list of all available products here, select the 4 cheapest items, 4 mid-priced items, and 4 most expensive items and append them to the new list.
x = (len(new_all_phone_links)) // 2
mail_phone_links.append(new_all_phone_links[0:4])
mail_phone_links.append(new_all_phone_links[(x-2):(x+2)])
mail_phone_links.append(new_all_phone_links[(len(new_all_phone_links)-4):(len(new_all_phone_links))])

#Where links will be collected in one list
new_mail_phone_links = []

#This loop cleans the lists inside the list
for links in mail_phone_links:
    for one_link in links:
        new_mail_phone_links.append(one_link)



try:
    #e-mail message information
    subject = "Give the prices get the device"
    message1 = "Hi Berat"
    message2 = "The 4 cheapest products, 4 moderately priced products and 4 most expensive products in the price range you specified are listed below."
    message3 = "Thank you for using our program."
    content = "Subject:  {0}\n\n{1}\n{2}\n\n{3}\n{4}\n{5}\n{6}\n{7}\n\n{8}\n{9}\n{10}\n{11}\n{12}\n\n{13}\n{14}\n{15}\n{16}\n{17}\n\n{18}".format(subject, message1,  message2, "-> The 4 products with the cheapest price", "- " + new_mail_phone_links[0], "- " + new_mail_phone_links[1], "- " + new_mail_phone_links[2], "- " + new_mail_phone_links[3], "-> The 4 products with medium price", "- " + new_mail_phone_links[4], "- " + new_mail_phone_links[5], "- " + new_mail_phone_links[6], "- " + new_mail_phone_links[7],  "-> The 4 most expensive products", "- " + new_mail_phone_links[8], "- " + new_mail_phone_links[9], "- " + new_mail_phone_links[10], "- " + new_mail_phone_links[11], message3)
except IndexError:
    print("No device was found within the entered value range.")
    prices_range()

#account information
my_mail_adress = "bmtrying123@gmail.com"
password = "bm552689"

#e-mail address to be sent
send_email = "bmtrying123@gmail.com"

mail = SMTP("smtp.gmail.com", 587)
mail.ehlo()
mail.starttls()
mail.login(my_mail_adress, password)
mail.sendmail(my_mail_adress, send_email, content)
