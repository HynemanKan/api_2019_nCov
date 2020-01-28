import requests
import re,json,time
from bs4 import BeautifulSoup

url="https://3g.dxy.cn/newh5/view/pneumonia"
def get_data():
    data = requests.get(url).content
    soup = BeautifulSoup(data,"lxml")
    all_city_script=soup.find("script",{"id":"getAreaStat"}).text
    all_city = re.search("\[.*]",all_city_script).group()
    all_city = json.loads(all_city)
    nation_data_script=soup.find("script",{"id":"getStatisticsService"}).text
    nation_data = re.search("{\".*\"}",nation_data_script).group()
    nation_data = json.loads(nation_data)
    p_data={}
    for p in all_city:
        p_name = p["provinceName"]
        c_dict={}
        for c in p["cities"]:
            c_dict[c["cityName"]]=c
        p_data[p_name]={"citys":c_dict,
                       "provinceName":p_name,
                       "confirmedCount":p["confirmedCount"],
                       "curedCount":p["curedCount"],
                       "deadCount":p["deadCount"]}
    n_data={
        "confirmedCount":nation_data["confirmedCount"],
        "suspectedCount":nation_data["suspectedCount"],
        "curedCount":nation_data["curedCount"],
        "deadCount":nation_data["deadCount"],
        "modifyTime":time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(nation_data["modifyTime"]/1000)),
        "mapShowUrl":nation_data["imgUrl"],
        "chartShowUrl":nation_data["dailyPic"]
    }
    return n_data,p_data
if __name__ == '__main__':
    print(get_data())