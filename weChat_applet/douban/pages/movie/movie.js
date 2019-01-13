// pages/movie/movie.js
var URL_API = "https://douban.uieee.com/v2/movie/subject/"

Page({

  /**
   * 页面的初始数据
   */
  data: {

  },
  onLoad: function (parms) {
    var that = this;
    wx.request({
      url: URL_API + parms.id,
      data: {},

      header: {
        "content-type": "json"
      },
      success: function (res) {
        console.log(res.data)
        that.setData({
          movie: res.data
        })
      }
    })
  }
})