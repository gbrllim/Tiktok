import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_tiktok_metrics(tiktok_username):
    """Gets the performance metrics for a TikTok channel."""

    url = "https://www.tiktok.com/@{}".format(tiktok_username)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    img_elements = soup.find_all("img", mode="1")
    view_elements = soup.find_all("strong",class_=lambda value: value and value.startswith("video-count"))

    print(len(img_elements))
    print(len(view_elements))
    title_list = []
    views_list = []
    
    for img_element in img_elements:
        title = img_element.get("alt")       

        title_list.append(title)
    
    for view_element in view_elements:
        views = view_element.text

        views_list.append(views)
    
    metrics_list = [{"title": title, "views": views} for title, views in zip(title_list, views_list)]
    return metrics_list
    

if __name__ == "__main__":
    tiktok_username = "channelnewsasia"
    metrics = get_tiktok_metrics(tiktok_username)
    df = pd.DataFrame(metrics)
    df.to_csv("tiktok_metrics_@{}.csv".format(tiktok_username))
    
