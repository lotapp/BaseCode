// 引用百度地图微信小程序JSAPI模块 
var bmap = require('../../libs/bmap-wx.min.js');

Page({
  data: {
    lat: 0,
    lon: 0,
    markers: []
  },
  // 页面加载的时候接受传递过来的参数
  onLoad: function(pms) {
    var that = this;
    console.log(pms);
    // 为经纬度赋值
    this.setData({
      lat: pms.lat,
      lon: pms.lon
    });
    // 新建百度地图对象 
    var BMap = new bmap.BMapWX({
      ak: 'vMDMZckGqYkFEHv28psnhS6KjGpPvbqu'
    });
    // 根据经纬度获得对应的地理描述信息
    BMap.regeocoding({
      iconPath: '../../images/marker_red.png',
      iconTapPath: '../../images/marker_red.png',
      success: ret => {
        console.info(ret.wxMarkerData)
        // 自定义marker上的气泡callout
        for (var i = 0; i < ret.wxMarkerData.length; i++) {
          ret.wxMarkerData[i]['callout'] = {
            'content': ret.wxMarkerData[i].address,
            'bgColor': "#fff",
            'color': "#f00",
            'padding': 15,
            'display': "ALWAYS", // BYCLICK：点击显示
            'borderRadius': 5
          };
        }
        // 数据存储
        that.setData({
          markers: ret.wxMarkerData
        });
      },
      fail: (ex) => {
        console.log(ex);
      }
    });
  },
  // 点击图标后执行的事件
  makertap: function(e) {
    var that = this;
    // 去列表中获取对应的信息
    let info = that.data.markers[e.markerId];
    // 弹框提醒
    wx.showToast({
      title: '执行了点击事件',
      icon: 'none',
      duration: 3000 // 提醒时间3s
    });
  }
})