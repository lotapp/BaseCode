Page({
  data: {},
  onLoad: function(pms) {
    console.log(pms);

    var that = this;
    // 设置data值
    this.setData({
      name: pms.name,
      age: pms.age
    });
  }
})