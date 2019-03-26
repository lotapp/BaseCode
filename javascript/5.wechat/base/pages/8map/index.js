Page({
  data: {
    demo: '完整案例',
    demo1: '获取经纬',
    demo2: '显示标记',
    demo3: '地图案例',
    lon: 120.674297,
    lat: 31.324571
  },
  onLoad: function(options) {},
  // 需要使用this的时候，最外面方法老老实实写function()
  get_location: function() {
    var that = this;
    // 获取经纬度
    wx.getLocation({
      // 成功的时候
      success: res => {
        // res.longitude：经度、res.latitude：纬度
        // res.speed：移动速度（实时定位的时候用的多）
        // res.accuracy：精确度（一般低于50，经纬数据就偏差太多）
        console.log(res.latitude, res.longitude, res.speed, res.accuracy);
        // 更新页面数据
        that.setData({
          lon: res.longitude,
          lat: res.latitude
        });
        // 弹框提醒
        wx.showToast({
          title: `(${res.longitude}，${res.latitude})`, // ES6语法
          icon: 'none'
        });
      },
      // 失败的时候
      fail: ex => {
        // 弹框提醒
        wx.showToast({
          title: '定位未授权，请重新授权：\r\n删除小程序后再打开',
          icon: 'none'
        });
      }
    });
  },
  // 打开位置
  open_location: function() {
    var that = this;
    // 打开位置
    wx.openLocation({
      latitude: that.data.lat,
      longitude: that.data.lon,
      // scale: 10, // 缩放级别（5~18）默认是18
      address: '江苏省苏州市工业园区都市花园' // 这个信息可以通过地图api逆向解析
    });
  },
  // 页面跳转
  // 用不到this的时候，箭头函数任意用（ES6语法）
  goto_demo: function(e) {
    wx.navigateTo({
      url: e.currentTarget.dataset.url
    })
  }
})