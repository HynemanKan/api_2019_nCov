import time
from flask import Flask,render_template
from scrapy import get_data
app = Flask(__name__)
p_bind = "上海市"
c_bind = None
@app.route('/977bc4c1-1f58-437e-b312-a1c5642de5f3')
def hello_world():
    n_data,p_data =get_data()
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    if c_bind is None:
        local_data = p_data[p_bind]
        nowPlace = p_bind
    else:
        nowPlace = f"{p_bind}&nbsp; {c_bind}"
        local_data=p_data[p_bind]["citys"][c_bind]
    return render_template("main_show.html",reflashTime=now,nation=n_data,local=local_data,nowPlace=nowPlace)


if __name__ == '__main__':
    app.run("127.0.0.1",8880)