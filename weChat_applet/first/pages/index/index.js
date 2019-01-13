//index.js
//获取应用实例
const app = getApp()

Page({
  onReady(e) {
    // 使用 wx.createAudioContext 获取 audio 上下文 context
    this.audioCtx = wx.createAudioContext('myAudio')
    this.audioCtx.setSrc('http://m10.music.126.net/20190110135046/ef3b8cd89f11de9cfc8786686a7a5c31/ymusic/baf1/eef0/b8bb/3eea7d951dcf4edd1bb03a15235fe6c5.mp3')
    //神经病爱的供养
    //http://m10.music.126.net/20190110135046/ef3b8cd89f11de9cfc8786686a7a5c31/ymusic/baf1/eef0/b8bb/3eea7d951dcf4edd1bb03a15235fe6c5.mp3
    //玩儿个痛快
    //http://m10.music.126.net/20190110132457/b8abe72f6138d802a7c48557c7b61580/ymusic/49ad/415b/015a/96cfcdc9564ac75b8f7729e424a24216.mp3
    //你的微笑
    //http://m10.music.126.net/20190110134834/ca5afd3b2fc9065920b568007b38ae18/ymusic/10cc/02b1/0643/6e52e8c865eaf93c83b8a4609d8f07f3.mp3
    //this.audioCtx.play()
  },
  data: {
    motto: '请向下滑动',
    src: '',
    userInfo: {},
    hasUserInfo: false,
    canIUse: wx.canIUse('button.open-type.getUserInfo')
  },
  //事件处理函数
  bindViewTap: function() {
    wx.navigateTo({
      url: '../logs/logs'
    })
  },
  onLoad: function () {
    if (app.globalData.userInfo) {
      this.setData({
        userInfo: app.globalData.userInfo,
        hasUserInfo: true
      })
    } else if (this.data.canIUse){
      // 由于 getUserInfo 是网络请求，可能会在 Page.onLoad 之后才返回
      // 所以此处加入 callback 以防止这种情况
      app.userInfoReadyCallback = res => {
        this.setData({
          userInfo: res.userInfo,
          hasUserInfo: true
        })
      }
    } else {
      // 在没有 open-type=getUserInfo 版本的兼容处理
      wx.getUserInfo({
        success: res => {
          app.globalData.userInfo = res.userInfo
          this.setData({
            userInfo: res.userInfo,
            hasUserInfo: true
          })
        }
      })
    }

    wx.showToast({
      title: '加载成功',
      icon: 'succeed',
      duration: 2000
    })
  },
  getUserInfo: function(e) {
    console.log(e)
    app.globalData.userInfo = e.detail.userInfo
    this.setData({
      userInfo: e.detail.userInfo,
      hasUserInfo: true
    })
  },
  audioPlay() {
    this.audioCtx.play()
  },
  audioPause() {
    this.audioCtx.pause()
  },
  audio14() {
    this.audioCtx.seek(57)
  },
  audioStart() {
    this.audioCtx.seek(0)
  }
})
