#-*- coding:utf-8 -*-
from .avc_common import Common_AVC
from airtest.core.api import *
from PIL import Image
import cv2 as cv
from datetime import datetime
import pytesseract
pytesseract.pytesseract.tesseract_cmd=r'/usr/local/bin/tesseract'
connect_device("ios:///http://127.0.0.1:8100")
# connect_device("Android:///")
from common import avc_constance as ac
from poco.drivers.ios import iosPoco
poco = iosPoco()
auto_setup(__file__)

class IOS_AVC(Common_AVC):
    def __init__(self):
        self.interval =2

    def goMine(self):
        #poco("mine").click()
        poco("login setting").click()

    def back(self):
        poco("back").click()

    def home(self):
        keyevent("HOME")

    def updateNickname(self,nickname):
       # btn_nickName = poco("Window").child("Other").child("Other").child("Other").child("Other").child("Other")[1].child("Button")[1]
       # btn_nickName.click()
       #  btn_nickName = poco("TextField")
        poco("TextField").click()

        poco("TextField").click()

        poco("全选").click()
        poco("剪切").click()

        # poco("TextField").set_text("")
        text(nickname)

    #更新头像
    def updateAvatar(self):
        # btn_avatar = poco("Window").child("Other").child("Other").child("Other").child("Other").child("Other")[1].child("Button")[0]
        # btn_avatar.click()
        poco("Window").child("Other").child("Other").child("Other").child("Other").offspring("Button").click()
        #poco("相机").click()
        poco("Window").child("Other").child("Other")[0].child("Other").child("Other").child("Other").offspring(
            "Table").child("Cell")[2].click()
     #touch(Template(r"resource/images/tpl1568115823545.png", record_pos=(-0.005, 0.747), resolution=(750, 1334)))
        #touch(Template(r"tpl1573120267803.png", record_pos=(0.019, 0.78), resolution=(750, 1334)))
        poco("PhotoCapture").click()
        poco("使用照片").click()

    def setRoomName(self,roomName):
        poco("Window").child("Other").child("Other").child("Other").offspring("ScrollView").child("Other").child(
               "TextField")[0].click()
        text(roomName)

    def setPassword(self,password):
        #poco("Window").child("Other").child("Other").child("Other").child("Other").child("Other").child("TextField")[1].click()
        poco("Window").child("Other").child("Other").child("Other").offspring("ScrollView").child("Other").child(
            "TextField")[1].click()
        text(password)
        # touch(Template('resource/images/tpl1568100069708.png'))

    def joinChannel(self,roomName,password):
        self.setRoomName(roomName)
        self.setPassword(password)
        # poco("加入").click()
        # wait(Template(r"resource/images/tpl1568189862382.png", record_pos=(0.0, 0.811), resolution=(750, 1334)))
        # print(">>>>>>>>>>Join Channel Success>>>>>>>>")
        
    # def joinChannel(self):
    #     poco("加入").click()

    def joinChannelSecond(self):
        poco("加入").click()
        
    def joinChannelWithoutPassword(self,roomName):
        self.setRoomName(roomName)
        poco("加入").click()
        
    
    def leaveChannel(self):
        # poco("hang up").click()
        print(">>>>>>>>>>Leave Channel Success>>>>>>>>")
        poco("hangup noraml").click()
        # print(">>>>>>>>>>Leave Channel Success>>>>>>>>")



    def setVideoResolution(self,resolution):
        '''
        :param resotion: 0:360P, 1:480P(默认),  2:720P
        '''
        if resolution == ac.Video_Resolution.video_360P:
            # poco("240P").click()
            swipe(Template(r"resource/images/tpl1573195402974.png", record_pos=(0.219, 0.669), resolution=(750, 1334)),
                  Template(r"resource/images/tpl1573195594310.png", record_pos=(0.027, 0.653), resolution=(750, 1334)), duration=0.01)
        elif resolution == ac.Video_Resolution.video_480P:
            # poco("360P").click()
            swipe(Template(r"resource/images/tpl1573195979517.png", record_pos=(0.061, 0.472), resolution=(750, 1334)),
                  Template(r"resource/images/tpl1573195988773.png", record_pos=(0.227, 0.485), resolution=(750, 1334)), duration=0.01)
        elif resolution == ac.Video_Resolution.video_720p:
            # poco("480P").click()
            swipe(Template(r"resource/images/tpl1573195402974.png", record_pos=(0.219, 0.669), resolution=(750, 1334)),
                  Template(r"resource/images/tpl1573195449862.png", record_pos=(0.409, 0.663), resolution=(750, 1334)), duration=0.01)
        else:
            raise ValueError("[Fail] Resolution is not supported : %s" % resolution)

    #会议中视频关闭
    def videoMuteExistsInChannel(self):
        poco("camera disable").exists()

    # 会议中视频打开
    def videoUnmuteExistsInChannel(self):
        poco("camera normal").exists()

    # 会议音频中关闭
    def audioMuteExistsInChannel(self):
        poco("mic disable").exists()

    #会议中音频打开
    def audioUnmuteExistsInChannel(self):
        poco("mic normal").exists()

    #会议中关闭视频
    def muteVideoInchannel(self):
        if poco("camera disable").exists():
            print("video already mute")
        else:
            poco("camera normal").click()

    #会议中打开视频
    def unmuteVideoInchannel(self):
        if poco("camera normal").exists():
            print("video already unmute")
        else:
            poco("camera disable").click()

    #会议中关闭音频
    def muteAudioInchannel(self):
        if poco("mic disable").exists():
            print("audio already mute")
        else:
            poco("mic normal").click()

    #会议中打开音频
    def unmuteAudioInchannel(self):
        if poco("mic normal").exists():
            print("audio already unmute")
        else:
            poco("mic disable").click()


    #个人设置中，视频关闭状态
    def preVideoMuteExists(self):
        poco("摄像头, 默认关闭").exists()

    # 个人设置中，视频打开状态
    def preVideoUnMuteExists(self):
        poco("摄像头, 默认打开").exists()

    #个人设置中，麦克风是关闭状态
    def preAudioMuteExists(self):
        poco("麦克风, 默认关闭").exists()

    #个人设置中，麦克风是打开状态
    def preAudioUnMuteExists(self):
        poco("麦克风, 默认打开").exists()

    #进入频道前，关闭摄像头
    def preMuteVideo(self):
        if poco("摄像头, 默认关闭").exists():
           print("video already mute")
        else:
            poco("摄像头, 默认打开").click()

    #进入频道前，打开摄像头
    def preUnmuteVideo(self):
        if poco("摄像头, 默认打开").exists():
           print("video already unmute")
        else:
            poco("摄像头, 默认关闭").click()

    # 进入频道前，关闭麦克风
    def preMuteAudio(self):
        if poco("麦克风, 默认关闭").exists():
            print("audio already muted")
        else:
            poco("麦克风, 默认打开").click()

    # 进入频道前，打开麦克风
    def preUnmuteAudio(self):
        if poco("麦克风, 默认打开").exists():
            print("audio already unmute")
        else:
            poco("麦克风, 默认关闭").click()


    #发送消息
    def sendMessage(self,msg):
        poco("message tool").click()
        poco("TextField").click()
        text(msg)
    
    #读消息
    def readMessage(self):
        poco("message tool hasMsg").click()

    #复制并发送消息
    def copyHistroyMessageAndSend(self):
        touch([200,100])
        poco("TextView").long_click(duration=2)
        poco("复制").click()
        # for i in range(2):
        #     poco("TextField").click()
        poco("TextField").long_click(duration=2)
        poco("粘贴").click()
        poco("Send").click()

    def clickLink(self):
         poco("www.baidu.com").click()
        

    #进入与会者列表
    def goToParticipantList(self):
        # poco("participants").click()
        poco("members").click()


    #进入频道内设置
    def goSettingInChannel(self):
        # poco("Button").click()
        poco("login setting").click()
        sleep(self.interval)

    def applyToHost(self):
        if poco("放弃主持人权限").exists():
            print("You are already the host")
        else:
            poco("申请成为主持人").click()
            assert poco("放弃主持人权限").exists()

    def giveUpHost(self):
        if poco("申请成为主持人").exists():
            print("You are not the host")
        else:
            poco("放弃主持人权限").click()
            assert poco("无").exists()

    def changeRoomPassword(self,pwd):
        if poco("申请成为主持人").exists() or poco("放弃主持人权限").exists():
            poco("房间密码").click()
            poco("TextField").click()
            poco("全选").click()
            poco("剪切").click()
            text(pwd)
        else:
            raise TimeoutError("You are not the host!")

    #点击远端的小窗口切换
    def smallAndBigwindowChange(self):
        poco("Cell").click()

    #切换前后摄像头
    def frontAndRearCameras(self):
        poco("camera switch").click()


    def uploadLog(self):
        '''
            网络不好，上传时间会变长，可能会失败
        '''
        poco("上传 日志").click()
        time = str(datetime.utcnow())
        wait(Template(r"resource/images/tpl1568205469989.png", record_pos=(0.003, -0.489), resolution=(750, 1334)))
        print("日志上传时间:%s" % time)

    #与会者列表中unmute别人的音频
    def unMutuOthersAudio(self):
        # poco("header_icon").click()
        poco("Window").child("Other").child("Other").child("Other").child("Other").offspring("Table").child("Cell")[1]
        if (poco("mic active").exists()):
            print("others audio already unmute")
        else:
            poco("mic inactive").click()


    #与会者列表中mute别人的音频

    def mutuOthersAudio(self):
        # poco("header_icon").click()
        poco("Window").child("Other").child("Other").child("Other").child("Other").offspring("Table").child("Cell")[1]
        if (poco("mic inactive").exists()):
            print("others audio already mute")
        else:
            poco("mic active").click()

    # 与会者列表中unmute别人的视频
    def unMutuOthersVideo(self):
        # poco("header_icon").click()
        poco("Window").child("Other").child("Other").child("Other").child("Other").offspring("Table").child("Cell")[1]
        if (poco("video active").exists()):
            print("others video already unmute")
        else:
            poco("video inactive").click()

    # 与会者列表中mute别人的视频
    def mutuOthersVideo(self):
        # poco("header_icon").click()
        poco("Window").child("Other").child("Other").child("Other").child("Other").offspring("Table").child("Cell")[1]
        if (poco("video inactive").exists()):
            print("others video already mute")
        else:
            poco("video active").click()

    # 与会者列表中将别人移出房间
    def getOthersOut(self):
        poco("header_icon").click()
        poco("hangup noraml").click()

    #与会者列表中确定unmute
    def  sureClickUnmute(self):
        poco("确定").click()

   #与会者列表中取消unmute
    def cancelClickUnmute(self):
        poco("Window").offspring("Alert")[2].child("Other").child("Other").child("Other")[1].child("Other")[2].child(
            "Other").child("Other").offspring("取消")[0].click()

    def lessThree(self):
        poco("房间名必须不小于3位").exists()

    def hostIconExists(self):
        poco("call_host").exists()
    
    def OthersHostIconExist(self):
        poco("Window").child("Other").child("Other").child("Other").child("Other").offspring("Table").child("Cell")[
            1].offspring("call_host")[0].exists()
        
    #频道内存在对方的说话图标
    def audioExistInChannel(self):
        poco("mic_active").exists()

    #频道内存在对方mute音频的图标
    def disAudioExistInChannel(self):
        poco("mic_inactive").exists()

    def videoExistInChannel(self):
        poco("round").exists()

    #mute音视频后查看观众显示情况
    def nameExists(self):
         poco("ios").exists()


    def participantNameExists(self):
        poco("ios(你)").exists()

    #点击房间密码说明
    def passwordInfoClick(self):
        poco("Info").click()

    def errorPasswordInfo(self):
        poco("Room join failed, incorrect password, ").exists()

    def inviteExists(self):
        poco("邀请对方打开麦克风").exists()

    def getStart(self):
        poco("Get Started").click()

    def slide(self):
        screenWidth, screenHeigth = poco.get_screen_size()
        swipe((screenWidth * 0.5, screenHeigth * 0.9), vector=[0, -0.5])

    def agreeClick(self):
        poco("同意").click()
        
    def hasMessageExist(self):
        poco("message tool hasMsg").exists()

    # 存在主持人无法更改房间属性
    def hostNotApplyClick(self):
        poco("摄像头, 参会者进入房间时不自动关闭摄像头").click()

    # 
    def hostNotApplyExists(self):
        poco("摄像头, 参会者进入房间时不自动关闭摄像头").exists()
        
    # 点击主持人信息说明
    def hostInfoClick(self):
        poco("Info").click()

    # 主持人说明信息存在
    def hostInfoExists(self):
        poco("主持人可以对房间进行设置，房间里最多只有一位主持人。").exists()
    
    def versionExist(self):
        poco("Version 4.0.0").exists()

    def versionClick(self):
        poco("Version 4.0.0").click()

    def RTCExist(self):
        poco("RTC: 2.9.1").exists()

    def RTCClick(self):
        poco("RTC: 2.9.1").click()

    def RTMExist(self):
        poco("RTM: 1.1.0").exists()

    def RTMClick(self):
        poco("RTM: 1.1.0").click()

    def buildExist(self):
        poco("V4.0.0 Build 541").exists()






