//index.js

var API_URL = "https://douban.uieee.com/v2/movie/top250";
//https://api.douban.com/v2/movie/top250

//获取应用实例
const app = getApp()

Page({
  data: {
    movies: []
  },
  onLoad: function () {
    var that = this
    wx.showToast({
      title: "加载中...",
      icon: "loading",
      duration: 60000
    });

    wx.request({
      url: API_URL,  //真实的接口地址 此处用的是大佬的代理
      data: {},
      method: "GET",
      header: {
        'content-type': 'json' // 默认值
      },
      header: {
        "content-type": "json"
      },
      success: function (res) {
        wx.hideToast();
        console.log(res.data)
        that.setData({
          movies: res.data.subjects
        })  
      }
    })
  }


})
