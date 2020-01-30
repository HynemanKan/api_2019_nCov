import requests
import json

def get_data():
    url="https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5"
    raw_data = requests.get(url).content
    json_data = json.loads(raw_data)
    data = json.loads(json_data["data"])
    n_data = data["chinaTotal"]
    n_data["lastUpdateTime"]=data["lastUpdateTime"]
    a_data = {}
    for n in data["areaTree"]:
        nation = {"name":n["name"],
                  "total":n["total"],
                  "today":n["today"]}
        if "children" in n.keys():
            ps = {}
            for p in n["children"]:
                prv = {"name":p["name"],
                       "total":p["total"],
                       "today":p["today"]}
                if "children" in p.keys():
                    cs = {}
                    for c in p["children"]:
                        city = c
                        cs[c["name"]] = city
                    prv["children"] = cs
                ps[p["name"]] = prv
            nation["children"] = ps
        a_data[n["name"]] = nation
    return n_data, a_data



if __name__ == '__main__':
    n_data,a_data = get_data()
    print(n_data)
    print(a_data["中国"]["children"]["上海"]["children"]["杨浦"])
