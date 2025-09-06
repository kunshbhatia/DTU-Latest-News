from bs4 import BeautifulSoup
import requests


def main_code(input):
    url = "https://dtu.ac.in/"

    with open("data.txt","wb") as f:
        f.writelines(requests.get(url))

    with open("data.txt","rb") as f:
        data = f.read()

    soup = BeautifulSoup(data,"html.parser")

    various_inputs = {  "Latest News" : 0,
                        "Notices" : 1,
                        "Jobs" : 2,
                        "Tenders" : 3,
                        "Forthcoming Events" : 4,
                        "1st Year Notices" : 5 
                    }

    for i in various_inputs.keys():
        if input == i:
            final_key = various_inputs[i]

    latest_tab_data = soup.find_all("div",class_="latest_tab")[final_key]


    headings = []
    links = []
    list_of_sentence = latest_tab_data.find_all("li")

    for i in list_of_sentence:
        try:
            headings.append(i.find("h6").find("a").get_text(strip=True))

            try:
                link = i.find("h6").find("a",class_="colr")['href']

                if link[0] == ".":
                    link = "https://dtu.ac.in"+link[1:]
                    links.append(link)
                else:
                    links.append(link)
            except:
                links.append("Not Applicable")
        except:
            pass


    return headings,links


