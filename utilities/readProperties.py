import configparser
import os

config = configparser.RawConfigParser()
#config.read(os.path.abspath(os.curdir) + "\\configurations\\config.ini\\")

ini_file_path = r'C:\Users\apande\PycharmProjects\nopCommerce_V1\configurations\config.ini'
config.read(ini_file_path)


class ReadConfig:

    @staticmethod
    def getApplicationURL():
        url = config.get('commonInfo', 'baseURL')
        return url

    @staticmethod
    def getPassword():
        password = config.get('commonInfo', 'password')
        return password

    @staticmethod
    def getUserMail():
        user = config.get('commonInfo', 'user')
        return user
