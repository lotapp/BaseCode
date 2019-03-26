Page({
  // 页面的初始数据
  data: {
    title: "定位案例",
    demo1: "点我获取位置信息",
    demo2: "点我进行地图定位",
    demo3: "点我使用百度地图",
    bottom_info: "微信小程序推荐使用腾讯地图",
    lon: 0, // 经度
    lat: 0 // 纬度
  },
  // 页面加载执行
  onLoad: function(options) {
    wx.setNavigationBarTitle({
      title: this.data.title,
    });
  },
  // 弹框提醒
  show_text: function(msg) {
    //自定义方法
    wx.showToast({
      title: msg,
      icon: 'none', // 不显示图标，此时 title 文本最多可显示两行
      duration: 3000 // 提醒时间3s
    })
  },
  get_location: function() {
    console.debug("into get_location");
    var that = this;
    // 获取经纬度
    wx.getLocation({
      // type: "wsg84",
      success: res => {
        // let speed = res.speed; // 移动速度
        // let accuracy = res.accuracy; // 精确程度（低于50就没有意义）
        // 设置data的值
        that.setData({
          lon: res.longitude, // 经度
          lat: res.latitude // 纬度
        });
        that.show_text(`经纬度：(${res.longitude},${res.latitude})`);
      },
      fail: ex => {
        console.warn(ex);
        that.show_text("获取失败~ 你可以删除小程序后再打开")
      }
    });
    console.debug("outside get_location");
  },
  // 验证经纬度是否已经获取
  verify_value: function() {
    var that = this;
    // 如果还没获取位置就先获取一下
    if (that.data.lon == 0 && that.data.lat == 0) {
      that.show_text("请先获取位置信息")
      return false;
    } else {
      return true;
    }
  },
  open_location: function() {
    var that = this;
    if (that.verify_value()) {
      // 打开地图位置
      wx.openLocation({
        longitude: that.data.lon, // 经度
        latitude: that.data.lat // 纬度
      });
    }
  },
  // 跳转
  goto_page: function(e) {
    var that = this;
    if (that.verify_value()) {
      let new_url = `${e.target.dataset.url}?lon=${this.data.lon}&lat=${this.data.lat}`;
      // console.log(new_url);
      // 页面跳转
      wx.navigateTo({
        url: new_url // 获取data-url的值
      });
    }
  }
})