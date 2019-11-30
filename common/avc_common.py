#-*- coding:utf-8 -*-
from airtest.core.api import *
from PIL import Image
import cv2 as cv
import pytesseract
import re
import requests
import pandas
import csv

pytesseract.pytesseract.tesseract_cmd=r'/usr/local/bin/tesseract'
# connect_device("ios:///http://127.0.0.1:8100")
from airtest.core.api import connect_device
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
connect_device("ios:///http://127.0.0.1:8100")
# device_2 = connect_device('Android:///SGTOO7NFQKY9I7CU?cap_method=javacap&touch_method=adb')
# poco_2 = AndroidUiautomationPoco(device_2, use_airtest_input=True, screenshot_each_action=False)
# connect_device("Android:///")
from poco.drivers.ios import iosPoco
poco = iosPoco()
auto_setup(__file__)

class Common_AVC:
    def __init__(self):
        self.interval = 2

    def setCurrentDevice(self,device):
        set_current(device)

    def startAVC(self,packageName):
        start_app(packageName)
        # wait(Template(r"resource/images/tpl1568100069708.png", record_pos=(0.003, -0.54), resolution=(750, 1334)),5)
        # sleep(self.interval)

    def stopAVC(self,packageName):
        stop_app(packageName)

    def getScreenSize(self):
        width,height = poco.get_screen_size()
        return width,height

    def getScreenshot(self,filename):
        snapshot(filename)

    def getImageSize(self,img_path):
        img = Image.open(img_path)
        width = img.size[0]
        height = img.size[1]
        print("width:%s,height:%s" % (width, height))
        return width,height

    def getCustomizeImage(self,origin_image_path, new_image_path, left, upper, right, lower):
        """
        :param origin_image_path: 原始图片的路径
        :param new_image_path: 图片裁剪后的路径
        :param left: 左 坐标
        :param upper: 上 坐标
        :param right: 右 坐标
        :param lower: 下 坐标
        :return:
        """
        img = Image.open(origin_image_path)
        cropped = img.crop((left, upper, right, lower))
        cropped.save(new_image_path)

    def getWordsInImage(self,image_path):
        '''
        :param image_path: 图片路径
        :return: 返回识别的文本内容
        '''
        '''
        部分内容会识别出错："^"->"*","Q"->"[","c"-"e"
        '''
        img = cv.imread(image_path)
        text = pytesseract.image_to_string(Image.fromarray(img))
        return text

    def getNumberOfParticipants(self,file_path):
        text = self.getWordsInImage(file_path).split()[1]
        number  = re.findall("\d+",text)[0]
        return int(number)

    #获取管理后台当前第一页的用户反馈
    def get_feedback_csv(self,post_url, data, get_url,feedbackfilepath):
        '''
        :param post_url: Beckon管理后台的登陆URL
        :param data: 用户名和密码 格式{"username":username,"password":password}
        :param get_url: 用户反馈页面的URL
        :param feedbackfilepath: 要保存的文件路径
        :return:
        '''
        s = requests.session()
        s.post(post_url, data)
        res1 = s.get(get_url)
        tb = pandas.read_html(res1.text)[0]
        tb.to_csv(feedbackfilepath, header=1, index=True)

    #获取第一条用户反馈
    def get_firtfeedback_info(self,feedbackfilepath):
        with open(feedbackfilepath, 'r') as csvfile:
            r = csv.reader(csvfile)
            next(r, None)
            rows = [row for row in r]
            info = rows[0]
            log_info = "upload time:%s"%info[1],"LogName:%s"%info[3]
            return log_info




