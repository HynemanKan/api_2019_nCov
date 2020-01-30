import time
from flask import Flask,render_template
from scrapy_dingxiang import get_data as dingxiang_data
from scrapy_tx_news import  get_data as tx_news_data
app = Flask(__name__)
dx_p_bind = "上海市"
dx_c_bind = None
tx_n_bind = "中国"
tx_p_bind = "上海"
tx_c_bind = None

@app.route('/dingxiang')
def dingxiang():
    n_data,p_data =dingxiang_data()
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    if dx_c_bind is None:
        local_data = p_data[dx_p_bind]
        nowPlace = dx_p_bind
    else:
        nowPlace = f"{p_bind}&nbsp; {c_bind}"
        local_data=p_data[dx_p_bind]["citys"][dx_c_bind]
    return render_template("dingxiang_show.html",reflashTime=now,nation=n_data,local=local_data,nowPlace=nowPlace)


@app.route('/tx_news')
def tx_news():
    n_data,a_data = tx_news_data()
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    if tx_p_bind is None:
        local_data = a_data[tx_n_bind]
        nowPlace = dx_c_bind
    else:
        if tx_c_bind is None:
            local_data = a_data[tx_n_bind]["children"][tx_p_bind]
            nowPlace = f"{tx_n_bind}&nbsp; {tx_p_bind}"
        else:
            local_data = a_data[tx_n_bind]["children"][tx_p_bind]["children"][tx_c_bind]
            nowPlace = f"{tx_n_bind}&nbsp; {tx_p_bind}&nbsp; {tx_c_bind}"
    return render_template("tx_new_show.html",reflashTime=now,nation=n_data,local=local_data,nowPlace=nowPlace)


if __name__ == '__main__':
    app.run("127.0.0.1",8880)