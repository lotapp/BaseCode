Page({
  data: {
    title: '欢迎光临'
  },
  onLoad: function (options) {
    // 设置标题
    wx.setNavigationBarTitle({
      title: this.data.title,
    });
  }
})