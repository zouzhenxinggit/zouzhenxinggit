//logs.js
const util = require('../../utils/util.js')

Page({
  data: {
    logs: []
  },
  onLoad: function () {
    this.setData({
      logs: (wx.getStorageSync('logs') || []).map(log => {
        return util.formatTime(new Date(log))
      })
    })

    wx.showToast({
      title: '加载中',
      icon: 'loading',
      duration: 10000
    })

    wx.request({
      url: "https://douban.uieee.com/v2/movie/top250",  //真实的接口地址 此处用的是大佬的代理
      //https://api.douban.com/v2/movie/top250
      data: {},
      header: {
        'content-type': 'json' // 默认值
      },
      header: {
        "content-type": "json"
      },
      success: function (res) {
        console.log(res.data)
        wx.hideToast()
      }
    })
  }
})
