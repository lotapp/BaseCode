Page({
  data: {
    info: "客服电话：",
    tel: "95017"
  },
  onLoad: function (options) { },
  call_tel: function () {
    // 打电话
    wx.makePhoneCall({
      phoneNumber: this.data.tel
    });
  }
})