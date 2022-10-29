# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy

class settings:
    Network=(MobileBy.XPATH,'//*[@text="Network & Internet"]')
    Sound = (MobileBy.XPATH, '//*[@text="Sound"]')
    Network_Connected=(MobileBy.XPATH,'//*[@text="Connected"]')

class USB_Play_Locator:
    video = (MobileBy.XPATH, '//*[@text="视频"]')

class Size_Window:
    aiqiyi = (MobileBy.XPATH, '//*[@text="推荐"]')
    window_full = (MobileBy.ID, 'com.gitvvideo.oppo:id/share_detail_btn_album_full')

class WIFI_Locator:
    net = (MobileBy.XPATH,
           '//*[@resource-id="com.android.tv.settings:id/list"]/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]')
    net_wifi = (MobileBy.XPATH,
                '//*[@resource-id="com.android.tv.settings:id/list"]/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]')
    net_wifi_status = (MobileBy.XPATH,  '//*[@text="已连接"]')

class APP_Locator:
    aiqiyi = (MobileBy.XPATH, '//*[@text="奇异果"]')
    gaoqing = (MobileBy.XPATH, '//*[@text="高清"]')
    qingxidu = (MobileBy.XPATH, '//*[@text="清晰度"]')
    chaoqing = (MobileBy.XPATH, '//*[@text="超清 720P"]')
    kaitong = (MobileBy.XPATH, '//*[@text="立即开通"]')

class HDMI_Locator:
    HDMI1 = (MobileBy.XPATH, '//*[@text="HDMI 1"]')
    HDMI2 = (MobileBy.XPATH, '//*[@text="HDMI 2"]')
    HDMI3 = (MobileBy.XPATH, '//*[@text="HDMI 3"]')
    mi = (MobileBy.XPATH, '//*[@text="MiBOX4"]')
    AV = (MobileBy.XPATH, '//*[@text="AV"]')
    DTMB = (MobileBy.XPATH, '//*[@text="DTMB"]')
    USB = (MobileBy.XPATH, '//*[@text="USB"]')

class vedioplayer:
    bendi = (MobileBy.XPATH, '//*[@text="本地文件"]')
    Pictures = (MobileBy.XPATH, '//*[@text="Pictures"]')
    dange = (MobileBy.XPATH, '//*[@text="单个循环"]')
    media_4K_30fps = (MobileBy.XPATH, '//*[@text="4K_30fps_Taipei.mp4"]')
    media_4K_60fps = (MobileBy.XPATH, '//*[@text="4K_60fps_india.mp4"]')
    media_4K_120fps = (MobileBy.XPATH, '//*[@text="4K_120fps_OPPO.mov"]')
    media_8K_60fps = (MobileBy.XPATH, '//*[@text="8K_60fps_IRSVsCBtgnk.ts"]')
    media_1080p = (MobileBy.XPATH, '//*[@text="1080P_Football.avi"]')
    media_1080i = (MobileBy.XPATH, '//*[@text="1080I_PC.ts"]')
    media_hdr = (MobileBy.XPATH, '//*[@text="HDR_Camp.mp4"]')
    media_hdr10 = (MobileBy.XPATH, '//*[@text="HDR10_World.mkv"]')
    media_Dolby_Atmos = (MobileBy.XPATH, '//*[@text="Dolby_Atmos_AmazeMobile.mp4"]')
    media_Dolby_Vision = (MobileBy.XPATH, '//*[@text="Dolby_Vision_Haleakala.mp4"]')