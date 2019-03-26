Page({
  data: {
    lon: 120.674297,
    lat: 31.324571,
    markers: []
  },
  // 页面加载
  onLoad: function() {
    var that = this;
    // eg：可以通过baidu Map获取到markers信息
    // BMap.regeocoding({success: ret => {ret.wxMarkerData}});
    // 假设通过API获取到了数据
    that.setData({
      markers: [{
        id: 0,
        latitude: that.data.lat,
        longitude: that.data.lon,
        address: '江苏省苏州市工业园区都市花园',
        iconPath: '/images/marker_red.png',
        callout: {
          'content': '江苏省苏州市工业园区都市花园',
          'bgColor': '#fff',
          'color': '#f00',
          'padding': 15,
          'display': 'ALWAYS', // BYCLICK：点击显示
          'borderRadius': 5
        }
      }]
    });
  },
  // 标记点击事件
  makertap: function(e) {
    var that = this;
    // 提示
    wx.showToast({
      title: `点击了标记点${e.markerId}`,
      icon: 'none'
    });
    // 可以根据e.markerId获取marker信息
    console.log(that.data.markers[e.markerId]);
  }
})