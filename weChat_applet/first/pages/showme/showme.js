// pages/showme/showme.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    name:"",
    age:"",
    id: 0,
    array:[1, 2, 3, 4, 5, 6, 7, 8, 9],
    flag: 'other',
    obj: {
      "myname":"zouzhenxing",
      "myage":100
    }
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    console.log("页面加载")
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {
    console.log("页面显示")
  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {
    console.log("页面隐藏")
  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  },

  onclikme: function () {
    console.log("我被点击")
    this.setData({
      name: "zouzhenxing",
      age: "23"
    })
  },
  viewtap: function () {
    console.log("viewtap")
  },
  
  jumpone: function () {
    wx.switchTab({
      url: '/pages/index/index'
    })
  }
})