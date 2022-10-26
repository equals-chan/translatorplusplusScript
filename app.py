import random
import time
from flask import Flask,request,jsonify
from flask_cors import CORS
from tencentAPI import tencentTranAPI
from baiduTransAPI import baiduTranslate



####
#baidu
appid = '百度id'
appkey = '百度key'
#tencent
SecretId = "腾讯id"
SecretKey = "腾讯key"


#语言
from_lang = 'jp'
to_lang =  'zh'
#`https://api.fanyi.baidu.com/doc/21`
#日语 jp 英语 en 中文 zh

#选择翻译引擎
useEngine = "tencent"
#               tencent     /    baidu

####


app = Flask(__name__)
cors = CORS(app)


@app.route('/',methods=['GET','POST'])
def index():
    if request.method == "GET":
        quest = request.args
    
    if request.method == "POST":
        quest = request.form
    
    dev = quest['q']
    if(dev != ""):
        print("----------\n")
        print("×"+dev +"\n")
        if useEngine == "tencent": #腾讯翻译
            time.sleep(1*random.random())
            dst = tencentTranAPI(from_lang,to_lang,str(dev),SecretId,SecretKey)
        elif useEngine == "baidu": #百度翻译
            dst = baiduTranslate(from_lang,to_lang,str(dev),appid,appkey)
        
        #去掉最末尾多余的一个 \n
        if(dst[-1] == "\n" ):
            dst = dst[0:-1]
        data = {
            'det' : dst,
        }
        print("√"+dst+"\n")
        return jsonify(data)
    else: return ""



if __name__ == '__main__':
    app.run(port=9999,debug = True)