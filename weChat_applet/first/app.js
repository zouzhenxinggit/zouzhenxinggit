//app.js
App({
  
  onLaunch: function () {
    //小程序初始化完成时触发，全局只触发一次。参数也可以使用 wx.getLaunchOptionsSync 获取。
    // 展示本地存储能力
    var logs = wx.getStorageSync('logs') || []
    logs.unshift(Date.now())
    wx.setStorageSync('logs', logs)

    // 登录
    wx.login({
      success: res => {
        // 发送 res.code 到后台换取 openId, sessionKey, unionId
      }
    })
    // 获取用户信息
    wx.getSetting({
      success: res => {
        if (res.authSetting['scope.userInfo']) {
          // 已经授权，可以直接调用 getUserInfo 获取头像昵称，不会弹框
          wx.getUserInfo({
            success: res => {
              // 可以将 res 发送给后台解码出 unionId
              this.globalData.userInfo = res.userInfo

              // 由于 getUserInfo 是网络请求，可能会在 Page.onLoad 之后才返回
              // 所以此处加入 callback 以防止这种情况
              if (this.userInfoReadyCallback) {
                this.userInfoReadyCallback(res)
              }
            }
          })
        }
      }
    })
  },
  onShow(options) {
    // Do something when show.
    //小程序启动，或从后台进入前台显示时触发。也可以使用 wx.onAppShow 绑定监听。
    console.log("onShow xxyyzz")
  },
  onHide() {
    // Do something when hide.
    //小程序从前台进入后台时触发。也可以使用 wx.onAppHide 绑定监听。
    console.log("onHide xxyyzz")
  },
  onError(msg) {
    console.log("onError xxyyzz")
  },
  globalData: {
    userInfo: null
  }
})