Page({
  data: {
    name: '小明',
    age: 22,
    url: '../1data/update_info',
    url2: './main'
  },
  onLoad: function(options) {

  },
  to_page: e => {
    // 页面跳转
    wx.navigateTo({
      url: e.currentTarget.dataset.url
    })
  },
  goto_page: function(e) {
    var that = this;
    // 页面跳转
    wx.navigateTo({
      url: `${e.currentTarget.dataset.url}?name=${that.data.name}&age=${that.data.age}`
    });
  }
})