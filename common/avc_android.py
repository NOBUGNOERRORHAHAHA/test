from airtest.core.api import *
from airtest import aircv
from airtest.core.cv import Predictor
from PIL import Image
from .avc_common import Common_AVC
from common import avc_constance as ac
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd=r'/usr/local/bin/tesseract'
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
# poco=AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
device_2 = connect_device('Android:///SGTOO7NFQKY9I7CU?cap_method=javacap&touch_method=adb')
poco_2 = AndroidUiautomationPoco(device_2, use_airtest_input=True, screenshot_each_action=False)
auto_setup(__file__)

class Android_AVC(Common_AVC):
    def __init__(self):
        self.interval = 2

    def setCurrentDevice(self,device):
        set_current(device)

    def startAVC(self,packageName):
        start_app(packageName)
        # wait(Template(r"resource/images/tpl1568208771836.png", record_pos=(-0.002, -0.009), resolution=(1080, 1920)))
        sleep(self.interval)

    def goMine(self):
        poco_2("io.agora.vcall:id/btSettings").click()

    def inputChannelName(self,channelname):
        poco_2("io.agora.vcall:id/editRoomName").click()
        poco_2("io.agora.vcall:id/editRoomName").set_text("")
        text(channelname)
        sleep(self.interval)

    def inputPassword(self,password):
        poco_2("io.agora.vcall:id/editRoomPwd").click()
        poco_2("io.agora.vcall:id/editRoomPwd").set_text("")
        text(password)
        sleep(self.interval)

    def joinChannel(self,channelname,password):
        self.inputChannelName(channelname)
        self.inputPassword(password)
        poco_2("io.agora.vcall:id/btJoin").click()
        # sleep(self.interval)

    def leaveChannel(self):
        print(">>>>>>>>>>Leave Channel Success>>>>>>>>")
        self.downIcon()
        poco_2("io.agora.vcall:id/hangUp").click()
        # print(">>>>>>>>>>Leave Channel Success>>>>>>>>")


    #会议中关闭自己的视频
    def muteVideoInchannel(self):
        # 关闭音频
        # def Click_audio(self):
        #     poco_1("io.agora.vcall:id/audioActionText").click()
        #
        # # 关闭视频
        # def Click_Vido(self):
        #     poco_1("io.agora.vcall:id/videoActionText").click()
        # btn_MuteVideo = poco_2("io.agora.vcall:id/videoActionText").click()
        # btn_UnMuteVideo
         poco_2("android.widget.LinearLayout").offspring("io.agora.vcall:id/localVideo").child(
            "io.agora.vcall:id/mediaImage").click()

    # 会议中关闭自己的音频
    def muteAudioInchannel(self):
        poco_2("android.widget.LinearLayout").offspring("io.agora.vcall:id/localAudio").child(
            "io.agora.vcall:id/mediaImage").click()

    #mute房间的视频
    def muteChannelVideo(self):
        poco_2("android.widget.LinearLayout").offspring("android:id/content").offspring(
            "io.agora.vcall:id/scrollView").offspring("io.agora.vcall:id/itemCamera").offspring(
            "io.agora.vcall:id/btSwitch").click()

    #mute房间的视频
    def muteChannelAudio(self):
        poco_2("android.widget.LinearLayout").offspring("android:id/content").offspring(
            "io.agora.vcall:id/scrollView").offspring("io.agora.vcall:id/itemMicrophone").offspring(
            "io.agora.vcall:id/btSwitch").click()



    def goSettingInChannel(self):
        poco_2("io.agora.vcall:id/btSettings").click()

    def applyToHost(self):
        poco_2("android.widget.LinearLayout").offspring("android:id/content").offspring(
            "io.agora.vcall:id/scrollView").offspring("io.agora.vcall:id/roomHost").offspring(
            "io.agora.vcall:id/actionContainer").click()
    
    def disApplyToHost(self):
        poco_2("android.widget.LinearLayout").offspring("android:id/content").offspring(
            "io.agora.vcall:id/scrollView").offspring("io.agora.vcall:id/roomHost").offspring(
            "io.agora.vcall:id/actionContainer").click()

    def back(self):
        poco_2("io.agora.vcall:id/btBack").click()


    # 进入频道前，关闭摄像头
    def preMuteVideo(self):

        btn_MuteVideo = poco_2("android.widget.LinearLayout").offspring("android:id/content").offspring(
            "io.agora.vcall:id/itemCamera").offspring("io.agora.vcall:id/btSwitch")
        btn_UnMuteVideo = poco_2("android.widget.LinearLayout").offspring("android:id/content").offspring(
            "io.agora.vcall:id/itemCamera").offspring("io.agora.vcall:id/btSwitch")

        if btn_MuteVideo.exists():
            print("video already mute")
        else:
            btn_UnMuteVideo.click()

     # 进入频道前，打开摄像头
    def preUnmuteVideo(self):

        btn_MuteVideo = poco_2("android.widget.LinearLayout").offspring("android:id/content").offspring(
            "io.agora.vcall:id/itemCamera").offspring("io.agora.vcall:id/btSwitch")
        btn_UnMuteVideo = poco_2("android.widget.LinearLayout").offspring("android:id/content").offspring(
            "io.agora.vcall:id/itemCamera").offspring("io.agora.vcall:id/btSwitch")

        if btn_UnMuteVideo.exists():
            print("video already unmute")
        else:
            btn_MuteVideo.click()

   # 进入频道前，关闭麦克风
    def preMuteAudio(self):
        btn_MuteAudio = poco_2("android.widget.LinearLayout").offspring("android:id/content").offspring(
            "io.agora.vcall:id/itemMicrophone").offspring("io.agora.vcall:id/btSwitch")
        btn_UnMuteAudio = poco_2("android.widget.LinearLayout").offspring("android:id/content").offspring(
            "io.agora.vcall:id/itemMicrophone").offspring("io.agora.vcall:id/btSwitch")
        if btn_MuteAudio.exists():
            print("audio already muted")
        else:
            btn_UnMuteAudio.click()


     # 进入频道前，打开麦克风
    def preUnmuteAudio(self):
        btn_MuteAudio = poco_2("android.widget.LinearLayout").offspring("android:id/content").offspring(
            "io.agora.vcall:id/itemMicrophone").offspring("io.agora.vcall:id/btSwitch")
        btn_UnMuteAudio = poco_2("android.widget.LinearLayout").offspring("android:id/content").offspring(
            "io.agora.vcall:id/itemMicrophone").offspring("io.agora.vcall:id/btSwitch")
        if btn_UnMuteAudio.exists():
            print("audio already unmute")
        else:
            btn_MuteAudio.click()

    # 进入与会者列表
    def goToParticipantList(self):
        poco_2("io.agora.vcall:id/icon").click()

    # 发送消息
    def readMessage(self):
        poco_2("io.agora.vcall:id/chatImage").click()

    def sendMessage(self,msg):  
        poco_2("io.agora.vcall:id/chatImage").click()
        poco_2("io.agora.vcall:id/input").click()
        poco_2("io.agora.vcall:id/input").set_text("")
        text(msg)
        poco_2("io.agora.vcall:id/sendInclude").click()
        
    def operate(self):
        poco_2("android.widget.LinearLayout").offspring("io.agora.vcall:id/part_recy").child("android.view.ViewGroup")[
            1].child("io.agora.vcall:id/more").click()

    def unMutuOthersAudio(self):
        poco_2("android.widget.LinearLayout").offspring("io.agora.vcall:id/part_recy").child("android.view.ViewGroup")[
            1].child("io.agora.vcall:id/more").click()
        poco_2("android.widget.LinearLayout").offspring("io.agora.vcall:id/mediaImage").click()
        poco_2("android:id/button1").click()

    def unMutuOthersVideo(self):
        poco_2("android.widget.LinearLayout").offspring("io.agora.vcall:id/part_recy").child("android.view.ViewGroup")[
            1].child("io.agora.vcall:id/more").click()
        poco_2("android.widget.LinearLayout").offspring("io.agora.vcall:id/mediaImage").click()
        poco_2("android:id/button1").click()

    def downIcon(self):
        poco_2("android.view.View").click()
        
    # 远端的音频mute存在
    def muteAudioIconExist(self):
        poco_2("android.widget.LinearLayout").offspring("io.agora.vcall:id/mediaImage").exists()

    def nameExists(self):
        poco_2("io.agora.vcall:id/userName").exists()
        
    def remoteTime(self):
        poco_2("io.agora.vcall:id/duration").get_text()

#
    # def leaveChannel(self):
    #     poco_2("io.agora.vcall:id/hangUp").click()
    #     sleep(self.interval)
    #
    # def checkversion(self):
    #     poco_2("io.agora.vcall:id/version").click()
    #     sleep(self.interval)
    #
    # def nick_comfirm(self,nickname):
    #     poco_2("io.agora.vcall:id/btSettings").click()
    #     poco_2("io.agora.vcall:id/editNickName").click()
    #     poco_2("io.agora.vcall:id/editNickName").set_text("")
    #     text(nickname)
    #     sleep(self.interval)
    #
    # def settings_back(self):
    #     poco("io.agora.vcall:id/btBack").click()
    #     sleep(self.interval)
    #
    #
    # def mutelocalvideo_channelout(self):
    #     poco("io.agora.vcall:id/btSettings").click()
    #     poco("android.widget.LinearLayout").offspring("android:id/content").offspring(
    #         "io.agora.vcall:id/itemCamera").offspring("io.agora.vcall:id/btSwitch").click()
    #     sleep(self.interval)
    #
    #
    # def getWordsInImage(self,image_path):
    #     image = Image.open(image_path)
    #     text = pytesseract.image_to_string(image,lang='chi_sim')
    #     return text
    #
    # def getImageSize(self, img_path):
    #     img = Image.open(img_path)
    #     width = img.size[0]
    #     height = img.size[1]
    #     print("width:%s,height:%s" % (width, height))
    #     return width, height
    #
    # def getCustomizeImage(self, origin_image_path, new_image_path, left, upper, right, lower):
    #     """
    #     :param origin_image_path: 原始图片的路径
    #     :param new_image_path: 图片裁剪后的路径
    #     :param left: 左 坐标
    #     :param upper: 上 坐标
    #     :param right: 右 坐标
    #     :param lower: 下 坐标
    #     :return:
    #     """
    #     img = Image.open(origin_image_path)
    #     cropped = img.crop((left, upper, right, lower))
    #     cropped.save(new_image_path)
    #
    # def key_back(self):
    #     keyevent("BACK")
    #     sleep(self.interval)
    #
    #
    # def clearRoomName(self):
    #     poco("io.agora.vcall:id/editRoomName").click()
    #     poco("io.agora.vcall:id/editRoomName").set_text("")
    #     sleep(self.interval)
    #
    # def clearRoomPwd(self):
    #     poco("io.agora.vcall:id/editRoomPwd").click()
    #     poco("io.agora.vcall:id/editRoomPwd").set_text("")
    #     sleep(self.interval)
    #
    #
    # def clearNickName(self):
    #     poco("io.agora.vcall:id/editNickName").click()
    #     poco("io.agora.vcall:id/editNickName").set_text("")
    #     sleep(self.interval)
    #
    #     # 点击查看版本号
    #
    # def checkversion(self):
    #     poco_1("io.agora.vcall:id/version").click()
    #     sleep(self.interval)

    # 点击设置输入昵称
    # def nick_comfirm(self, nickname):
    #     poco_1("io.agora.vcall:id/btSettings").click()
    #     poco_1("io.agora.vcall:id/editNickName").click()
    #     poco_1("io.agora.vcall:id/editNickName").set_text("")
    #     text(nickname)
    #     sleep(self.interval)
    #
    # # 点击返回
    # def settings_back(self):
    #     poco_1("io.agora.vcall:id/btBack").click()
    #     sleep(self.interval)
    #
    # # 点击设置打开摄像头
    # def mutelocalvideo_channelout(self):
    #     poco_1("io.agora.vcall:id/btSettings").click()
    #     poco_1("android.widget.LinearLayout").offspring("android:id/content").offspring(
    #         "io.agora.vcall:id/itemCamera").offspring("io.agora.vcall:id/btSwitch").click()
    #     sleep(self.interval)
    #
    #     # 得到文字图片
    #
    # def getWordsInImage(self, image_path):
    #     image = Image.open(image_path)
    #     text = pytesseract.image_to_string(image, lang='chi_sim')
    #     return text
    #
    #     # 得到图片大小
    #
    # def getImageSize(self, img_path):
    #     img = Image.open(img_path)
    #     width = img.size[0]
    #     height = img.size[1]
    #     print("width:%s,height:%s" % (width, height))
    #     return width, height
    #
    #     # 获取截图的大小
    #
    # def getCustomizeImage(self, origin_image_path, new_image_path, left, upper, right, lower):
    #     """
    #     :param origin_image_path: 原始图片的路径
    #     :param new_image_path: 图片裁剪后的路径
    #     :param left: 左 坐标
    #     :param upper: 上 坐标
    #     :param right: 右 坐标
    #     :param lower: 下 坐标
    #     :return:
    #     """
    #     img = Image.open(origin_image_path)
    #     cropped = img.crop((left, upper, right, lower))
    #     cropped.save(new_image_path)
    #
    # def key_back(self):
    #     keyevent("BACK")
    #     sleep(self.interval)
    #
    # def home(self):
    #     keyevent("HOME")
    #     sleep(self.interval)
    #
    # # 清除房间名
    #
    # def clearRoomName(self):
    #     poco_1("io.agora.vcall:id/editRoomName").click()
    #     poco_1("io.agora.vcall:id/editRoomName").set_text("")
    #     sleep(self.interval)
    #
    #     # 清除房间密码
    #
    # def clearRoomPwd(self):
    #     poco_1("io.agora.vcall:id/editRoomPwd").click()
    #     poco_1("io.agora.vcall:id/editRoomPwd").set_text("")
    #     sleep(self.interval)
    #
    #     # 清除昵称
    #
    # def clearNickName(self):
    #     poco_1("io.agora.vcall:id/editNickName").click()
    #     poco_1("io.agora.vcall:id/editNickName").set_text("")
    #     sleep(self.interval)
    #
    # """
    # 关于设置中的所有功能选项
    # """
    #
    # # 点击设置
    # def bt_settings(self):
    #     poco_1("io.agora.vcall:id/btSettings").click()
    #     sleep(self.interval)
    #
    # # 关闭摄像头
    # def Turn_off_the_camera(self):
    #     poco_1("android.widget.LinearLayout").offspring("android:id/content").offspring(
    #         "io.agora.vcall:id/itemCamera").child("android.view.ViewGroup").click()
    #     sleep(self.interval)
    #
    # # 关闭麦克风
    # def Turn_off_the_maicrophone(self):
    #     poco_1("android.widget.LinearLayout").offspring("android:id/content").offspring(
    #         "io.agora.vcall:id/itemMicrophone").child("android.view.ViewGroup").click()
    #
    # # 夜间模式
    # def Night_mode(self):
    #     poco_1("android.widget.LinearLayout").offspring("android:id/content").offspring(
    #         "io.agora.vcall:id/darkTheme").child("android.view.ViewGroup").click()
    #     sleep(self.interval)
    #
    # """
    # 屏幕分辨率设置
    # """
    #
    # def Resolution_360p(self):
    #     poco_1("io.agora.vcall:id/resolutionIcon").click()
    #     sleep(self.interval)
    #
    # def Resolution_480p(self):
    #     poco_1("io.agora.vcall:id/resolutionIcon").click()
    #     sleep(self.interval)
    #
    # def Resolution_720p(self):
    #     poco_1("io.agora.vcall:id/resolutionIcon").click()
    #     sleep(self.interval)
    #
    # # 日志上传
    # def log_upload(self):
    #     poco_1("android.widget.LinearLayout").offspring("android:id/content").offspring(
    #         "io.agora.vcall:id/uploadLog").child("android.view.ViewGroup").click()
    #
    # """
    # 头像上传
    # """
    #
    # def Avatar_upload(self):
    #     poco_1("io.agora.vcall:id/changeAvatar").click()
    #     poco_1("io.agora.vcall:id/choose1").click()
    #     poco_1("com.oppo.camera:id/shutter_button").click()
    #     poco_1("com.oppo.camera:id/btn_done").click()
    #     sleep(self.interval)
    #
    # def compare_images(self, path_one, path_two):  # 文件1的路径，文件2的路径，生成比较后不同的图片文件路径
    #     image_one = Image.open(path_one)
    #     image_two = Image.open(path_two)
    #
    #     try:
    #         diff = ImageChops.difference(image_one, image_two)
    #         if diff.getbbox() is None:
    #             # 图片间没有任何不同则直接退出
    #             print("We are the same!")
    #         else:
    #             print("图片不同")
    #
    #     except ValueError as e:
    #         text = ("表示图片大小和box对应的宽度不一致，参考API说明：Pastes another image into this image."
    #                 "The box argument is either a 2-tuple giving the upper left corner, a 4-tuple defining the left, upper, "
    #                 "right, and lower pixel coordinate, or None (same as (0, 0)). If a 4-tuple is given, the size of the pasted "
    #                 "image must match the size of the region.使用2纬的box避免上述问题")
    #         print("【{0}】{1}".format(e, text))
    #
    # """
    # 房间内的状态栏设置
    # """
    #
    # # 房间内点击恢复状态栏
    # def Recovery_status_bar(self):
    #     poco_1("io.agora.vcall:id/mediaImage").click()
    #
    # # 关闭音频
    # def Turn_off_audio(self):
    #     poco_1("android.widget.LinearLayout").offspring("io.agora.vcall:id/localAudio").child(
    #         "io.agora.vcall:id/mediaImage").click()
    #
    # # 关闭视频
    # def Close_vido(self):
    #     poco_1("android.widget.LinearLayout").offspring("io.agora.vcall:id/localVideo").child(
    #         "io.agora.vcall:id/mediaImage").click()
    #
    # # 窗口切换
    # def Window_switching(self):
    #     poco_1("io.agora.vcall:id/small_bg").click()
    #
    #
    #
    # """
    # 人员列表相关操作
    # """
    #
    # def list_of_pepole(self):
    #     poco_1("io.agora.vcall:id/icon").click()
    #     sleep(self.interval)
    #
    # # 选择确定
    # def Choose_OK(self):
    #     poco_1("android:id/button1").click()
    #
    # # 选择拒绝
    # def Choose_NO(self):
    #     poco_1("android:id/button2").click()
    #
    # # 选择属性(更具人数元素去获取)
    # def Select_attribute_0(self):
    #     poco_1("io.agora.vcall:id/more").click()
    #     sleep(self.interval)
    #
    # def Select_attribute_1(self):
    #     poco_1("android.widget.LinearLayout").offspring("io.agora.vcall:id/part_recy").child("android.view.ViewGroup")[
    #         1].child("io.agora.vcall:id/more").click()
    #
    # # 关闭音频
    # def Click_audio(self):
    #     poco_1("io.agora.vcall:id/audioActionText").click()
    #
    # # 关闭视频
    # def Click_Vido(self):
    #     poco_1("io.agora.vcall:id/videoActionText").click()
    #
    # # 踢人
    # def Kicking_people(self):
    #     poco_1("io.agora.vcall:id/hangUpText").click()
    #     poco_1("android:id/button1").click()
    #
    # """
    # 聊天
    # """
    #
    # # 点击消息列表
    # def Message_list(self):
    #     poco_1("io.agora.vcall:id/chatImage").click()
    #
    # # 点击链接
    # def link(self):
    #     poco_1("io.agora.vcall:id/chatContent").click()
    #     sleep(self.interval)
    #
    # # 聊天输入信息
    # def To_chat_with(self, information):
    #     poco_1("io.agora.vcall:id/input").click()
    #     poco_1("io.agora.vcall:id/input").set_text("")
    #     text(information)
    #     sleep(self.interval)
    #
    # # 聊天-发送
    # def Send(self):
    #     poco_1("io.agora.vcall:id/sendInclude").click()
    #     sleep(self.interval)
    #
    # """
    # 挂断电话，退出频道
    # """
    #
    # # 离开频道
    # def leaveChannel(self):
    #     poco_1("io.agora.vcall:id/hangUp").click()
    #     sleep(self.interval)
    #
    # """
    # 房间设置
    # """
    #
    # # 申请/放弃主持人
    # def Application_host(self):
    #     poco_1("android.widget.LinearLayout").offspring("android:id/content").offspring(
    #         "io.agora.vcall:id/scrollView").offspring("io.agora.vcall:id/roomHost").child(
    #         "android.view.ViewGroup").click()
    #     sleep(self.interval)
    #
    # # 日志上传
    # def Log_upload(self):
    #     poco_1("android.widget.LinearLayout").offspring("android:id/content").offspring(
    #         "io.agora.vcall:id/scrollView").offspring("io.agora.vcall:id/uploadLog").child(
    #         "android.view.ViewGroup").click()
    #     sleep(self.interval)
    #
    # # 关闭/打开音频
    # def Audio(self):
    #     poco_1("android.widget.LinearLayout").offspring("android:id/content").offspring(
    #         "io.agora.vcall:id/scrollView").offspring("io.agora.vcall:id/itemMicrophone").child(
    #         "android.view.ViewGroup").click()
    #     sleep(self.interval)
    #
    # # 关闭/打开视频
    # def Video(self):
    #     poco_1("android.widget.LinearLayout").offspring("android:id/content").offspring(
    #         "io.agora.vcall:id/scrollView").offspring("io.agora.vcall:id/itemCamera").child(
    #         "android.view.ViewGroup").click()
    #     sleep(self.interval)
    #
    # # 本机点击设置
    # def settings(self):
    #     poco_2("设置").click()
    #
    # # 关网/开网
    # def Network_settings(self):
    #     poco_2("android.widget.FrameLayout").offspring("com.android.settings:id/dashboard_container").child(
    #         "com.android.settings:id/category")[0].child("com.android.settings:id/category_content").child(
    #         "android.widget.FrameLayout")[1].offspring("com.android.settings:id/icon").click()
    #     poco_2("com.android.settings.wifi:id/switchButton").click()











