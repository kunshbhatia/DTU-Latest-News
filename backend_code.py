from bs4 import BeautifulSoup
import requests


def main_code():
    url = "https://dtu.ac.in/"

    with open("data.txt","wb") as f:
        f.writelines(requests.get(url))

    with open("data.txt","rb") as f:
        data = f.read()

    soup = BeautifulSoup(data,"html.parser")

    latest_tab_data = soup.find_all("div",class_="latest_tab")[0]

    headings = []
    links = []
    list_of_sentence = latest_tab_data.find_all("li")

    for i in list_of_sentence:
        try:
            headings.append(i.find("h6").find("a").get_text(strip=True))

            try:
                link = i.find("h6").find("a",class_="colr")['href']

                if link[0] == ".":
                    link = "https://dtu.ac.in/"+link[1:]
                    links.append(link)
                else:
                    links.append(link)
            except:
                links.append("Not Applicable")
        except:
            pass


    return headings,links


