// pages/search/search.js
var URL_API = "https://douban.uieee.com/v2/movie/search";

Page({
  data: {
    movies: []
  },
  onLoad: function (options) {
    // 页面初始化 options为页面跳转所带来的参数
  },

  
  search: function (e) {
    console.log(e.detail.value);
    wx.showToast({
      title: '加载中',
      icon: 'loading',
      duration: 10000
    });

    var that = this;

    wx.request({
      url: URL_API + "?q=" + e.detail.value,
      data: {},
      header: {
        "Content-Type": "json"
      }, // 设置请求的 header
      success: function (res) {
        wx.hideToast();
        console.log(res.data);
        that.setData({
          movies: res.data.subjects
        })
      }
    });

  }
})