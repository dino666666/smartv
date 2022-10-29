# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
import time

from Common.Globe_Lib.Adbevent import ADB
from Common.Globe_Lib.maneger_devices_info import ManageDevices

class App_Playcontrol():

    def __init__(self,adb,dict):
        '''1:YouTube  2:primevideo  3:ZEE5  4:Netflix'''
        self.dict = dict
        # self.adb = ADB(device)
        self.adb = adb
        list_app = [{1:'com.google.android.youtube.tv'},
                    # {2:'com.amazon.amazonvideo.livingroom/com.amazon.ignition.IgniteActivity'},
                    {2: ' com.amazon.amazonvideo.livingroom -c android.intent.category.LEANBACK_LAUNCHER '},
                    {3:'com.graymatrix.did'},
                    {4: 'com.netflix.ninja'},
                    {5: 'com.heytap.tv.filebrowser'},
                    {6: 'com.sonyliv  -c android.intent.category.LEANBACK_LAUNCHER'},
                    ]
        for i in list_app:
            try:
                if i[dict]:
                    self.app = i[dict]
                    break
            except Exception as e:
                print("搜索app资源库：{}".format(e))

    def start(self):
        # self.stop()
        self.adb.order("monkey -p "+self.app + " 1 ")
        # self.adb.app_start(self.app)
        time.sleep(15)

    def into_play(self,Sleep=20):
        if self.dict==1:
            print("播放YouTube片源")
            self.adb.ok(1, 1)
        elif self.dict==2:
            print("播放PrimeVideo片源")
            self.adb.ok(1, 1)
        elif self.dict==3:
            pass
        elif self.dict==4:
            self.adb.ok(2, 10)
            self.adb.down(1, 2)
            self.adb.right(1, 2)
            print("播放Netflix片源")
            self.adb.ok(1, 1)
        elif self.dict==5:
            self.adb.right(2, 2)
            self.adb.down(1, 2)
            print("播放本地片源")
            self.adb.ok(1, 1)

        time.sleep(Sleep)

    def into_play_4K(self,Sleep=20):
        if self.dict==1:
            print("播放YouTube片源")
            self.adb.left(1, 2)
            self.adb.down(6, 2)
            self.adb.right(2, 2)
            self.adb.ok(1, 2)
        elif self.dict==2:
            self.adb.ok(1, 5)
            self.adb.down(2, 3)
            self.adb.right(1, 3)
            self.adb.ok(1, 4)
        elif self.dict==3:
            pass
        elif self.dict==4:
            self.adb.ok(2, 10)
            self.adb.down(1, 2)
            self.adb.right(1, 2)
            print("播放Netflix片源")
            self.adb.ok(1, 1)
        elif self.dict==5:
            self.adb.right(2, 2)
            self.adb.down(1, 2)
            print("播放本地片源")
            self.adb.ok(1, 1)
        elif self.dict==6:
            time.sleep(3)
            self.adb.left(2, 2)
            self.adb.down(3, 2)
            self.adb.ok(3, 3)
            print("播放SonyLIV片源")
        time.sleep(Sleep)

    def play_control(self,control):
        '''1:快进   2：快退   3：暂停'''
        if control==1:
            self.adb.right(2,1)
            self.adb.ok(1, 2)
        elif control==2:
            self.adb.left(2,1)
            self.adb.ok(1, 2)
        elif control==3:
            self.adb.ok(1,2)

    def stop(self):
        if self.dict==2:
            self.adb.app_stop("com.amazon.amazonvideo.livingroom")
        elif self.dict!=2 and self.dict!=6:
            self.adb.app_stop(self.app)
        elif self.dict==6:
            self.adb.app_stop("com.sonyliv")

    def test_play(self):
        self.start()
        self.into_play()




if __name__ == '__main__':
    device = ManageDevices().get_devices()[0]
    adb = ADB(device)
    while True:
        time.sleep(1)
        result,win = adb.windows("ninja")
        if not result:
            print("播放异常，重新播放")
            adb.order("monkey -p com.google.android.tvlauncher 1")
            d = App_Playcontrol(adb, 4)
            d.start()
            d.into_play()
        print("播放正常")



