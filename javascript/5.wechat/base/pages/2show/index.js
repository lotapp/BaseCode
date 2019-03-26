Page({
  data: {
    title1: '你知道吗？这是可以显示多行的弹框提醒~\r\n你知道吗？这是可以显示多行的弹框提醒~\r\n你知道吗？这是可以显示多行的弹框提醒~',
    title2: '一二三四五六七八'
  },
  onLoad: function () {
    console.log("页面加载完成");
  },
  // 弹框提醒
  show_msg1: function () {
    wx.showToast({
      title: this.data.title1,
      icon: 'none', // 可以显示2行
      duration: 2000 // 默认1500
    })
  },
  // 弹框提醒
  show_msg2: function () {
    // 默认只能显示7个中文字
    wx.showToast({
      title: this.data.title2
    })
  }
})