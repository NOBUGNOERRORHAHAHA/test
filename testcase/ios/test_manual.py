# -*- coding:utf-8 -*-
from airtest.core.api import  *
from airtest.core.ios.ios import IOS
import pytest
from common import case_tag,verify_utils
from common.avc_ios import IOS_AVC
from common import avc_constance as ac
from common import pytest_utils
from poco.drivers.ios import iosPoco
poco = iosPoco()

class TestIOS:

    def setup(self):
        # self.avc = IOS_AVC()
        # self.channel_name = "AVCAUTO"
        # self.password = "avctest"
        # self.packageName = ac.Package_Name.ios_packageName
        # self.screeshot_path = "resource/screenshot/"
        # self.feedbackpath = "resource/feedback.csv"
        # self.postData = {"userName": "sdk", "password": "__sdk_8estv0ip!"}
        self.avc = IOS_AVC()
        # self.avcAndroid = Android_AVC()
        self.channel_name = "AVCAUTO"
        self.password = "avctest"
        self.packageName = ac.Package_Name.ios_packageName
        self.packageName_android = ac.Package_Name.android_packageName
        self.screeshot_path = "resource/screenshot/"

    def tearDown(self):
        pass

    '''3742 首次安装信息'''
    @pytest.mark.tags(case_tag.iOS, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_firstInstall(self):
        avc = self.avcIOS
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.getStart()
        avc.slide()
        avc.agreeClick()

    '''3772设置不同的分辨率进入房间'''
    @pytest.mark.parametrize("resolution", [ac.Video_Resolution.video_360P, ac.Video_Resolution.video_480P,
                                            ac.Video_Resolution.video_720p])
    @pytest.mark.tags(case_tag.iOS, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_joinChannelWithDifferentReslotion(self, resolution):
        avc = self.avcIOS
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.goMine()
        avc.setVideoResolution(resolution=resolution)
        avc.back()
        avc.joinChannel(self.channel_name, self.password)
        sleep(2)
        avc.leaveChannel()

    # 设置不同的网络检查网络质量回调是否符合预期
    @pytest.mark.tags(case_tag.iOS, case_tag.HIGH, case_tag.MANUAL, case_tag.FUNCTIONALITY)
    def test_checkNetworkQuality(self):
        avc = self.avc
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        pytest_utils.execute_manual_step("设置下行网络，丢包100%")
        assert verify_utils.network_quality() == "Unkown"
        pytest_utils.execute_manual_step("设置下行网络，丢包0")
        assert verify_utils.network_quality() == "Good"
        pytest_utils.execute_manual_step("设置下行网络，丢包60%")
        assert verify_utils.network_quality() == "Bad"

    '''日志上传'''
    @pytest.mark.tags(case_tag.iOS, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_log(self):
        avc = self.avcIOS
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.joinChannel(self.channel_name, self.password)
        avc.goSettingInChannel()
        avc.slide()
        avc.uploadLog()

    # '''日志上报'''
    # @pytest.mark.tags(case_tag.iOS, case_tag.HIGH, case_tag.MANUAL, case_tag.FUNCTIONALITY)
    # def test_uploadLog(self):
    #     avc = self.avc
    #     avc.setCurrentDevice(0)
    #     avc.startAVC(self.packageName)
    #     avc.goMine()
    #     avc.uploadLog()
    #     avc.get_feedback_csv(post_url=ac.URL.login,data=self.postData,get_url=ac.URL.feedback,feedbackfilepath=self.feedbackpath)
    #     info = avc.get_firtfeedback_info(feedbackfilepath=self.feedbackpath)
    #     print(info)
    #     pytest_utils.execute_manual_step('日志上传信息完整')
    
    # 断网过程中，被mute/unmute后重新联网
    def t(self):
        # 启动android
        avc_android = self.avcAndroid
        avc_android.setCurrentDevice(1)
        avc_android.startAVC(self.packageName_android)
        avc_android.joinChannel(self.channel_name, self.password)
        avc_android.muteAudioInchannel()
        avc_android.muteVideoInchannel()
        # 启动ios
        avc_ios = self.avcIOS
        avc_ios.setCurrentDevice(0)
        avc_ios.startAVC(self.packageName)
        avc_ios.joinChannel(self.channel_name, self.password)
        avc_ios.goToParticipantList()
        # unmute音频
        avc_ios.unMutuOthersAudio()
        assert avc_ios.inviteExists
        avc_ios.sureClickUnmute()
        # unmute视频
        avc_ios.unMutuOthersVideo()
        assert avc_ios.inviteExists
        avc_ios.sureClickUnmute()
        # 踢人
        avc_ios.getOthersOut()
        assert avc_ios.inviteExists
        avc_ios.sureClickUnmute()


