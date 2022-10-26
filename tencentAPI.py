import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.tmt.v20180321 import tmt_client, models

def tententTrans(from_lang,to_lang,SourceTextLists,SecretId,SecretKey):
    try:
        # 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey,此处还需注意密钥对的保密
        # 密钥可前往https://console.cloud.tencent.com/cam/capi网站进行获取
        

        cred = credential.Credential(SecretId, SecretKey)
        # 实例化一个http选项，可选的，没有特殊需求可以跳过
        httpProfile = HttpProfile()
        httpProfile.endpoint = "tmt.tencentcloudapi.com"

        # 实例化一个client选项，可选的，没有特殊需求可以跳过
        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        # 实例化要请求产品的client对象,clientProfile是可选的
        client = tmt_client.TmtClient(cred, "ap-hongkong", clientProfile)

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.TextTranslateBatchRequest()
        params = {
            "Source": from_lang,
            "Target": to_lang,
            "ProjectId": 0,
            "SourceTextList": SourceTextLists,
        }
        req.from_json_string(json.dumps(params))

        # 返回的resp是一个TextTranslateBatchResponse的实例，与请求对象对应
        resp = client.TextTranslateBatch(req)
        # 输出json格式的字符串回包
        #print(resp.to_json_string())
        return fix(resp.__getattribute__("TargetTextList"))
    except TencentCloudSDKException as err:
        print(err)
        return "ERROR_CATCH_ERROR"


def fix(TargetTextList):
    str1 = ""
    for i in TargetTextList:
        str1 += i + "\n"
    return str1


def divideSentence(str1):
    return str1.split("\n")


def tencentTranAPI(from_lang,to_lang,str1,SecretId,SecretKey):
    return tententTrans(from_lang,to_lang,divideSentence(str1),SecretId,SecretKey)



if __name__ == '__main__':
    print()