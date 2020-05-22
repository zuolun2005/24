from aip import AipOcr
import configparser

class BaiDuAPI:
    '''调用百度API实现图片数字的识别
    filepPath:
    ---------
    是工单信息的ini配置文件全路径
    '''

    def __init__(self,filePath):
        # 实例化
        target = configparser.ConfigParser()
        target.read(filePath)
        app_id = target.get('工单密码', 'APP_ID')
        api_key = target.get('工单密码','API_KEY')
        secret_key = target.get('工单密码','SECRET_KEY')
        '''你的APPID密码账号等'''
        APP_ID = app_id
        API_KEY = api_key
        SECRET_KEY = secret_key

        self.client = AipOcr(APP_ID,API_KEY,SECRET_KEY)

    def picture2Number(self,filePath):
        image = self.getFileContent(filePath)
        numbers = self.client.basicAccurate(image)

        try:
            numberLists = list(map(lambda x:int(x), list(numbers['words_result'][0]['words'])))
            print('识别结果为：',numberLists)
            return numberLists
        except:
            print('识别结果不符合要求')
       # 装饰器 静态方法
    @staticmethod
    def getFileContent(filePath):
        with open(filePath,'rb') as fp:
            return fp.read()

        # 类方法
    # @classmethod
    # def getFileContent(cls,filePath):
    #     with open(filePath,'rb') as fp:
    #         return fp.read()



if __name__ == '__main__':



    baiduapi = BaiDuAPI(r'C:\Users\Administrator\PycharmProjects\24\password.ini')
    baiduapi.picture2Number(r'C:\Users\Administrator\PycharmProjects\24\大众.png')
