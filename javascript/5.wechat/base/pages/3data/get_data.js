Page({
  data: {
    title: '获取Data属性的值'
  },
  onLoad: function (options) {
    // 设置标题
    wx.setNavigationBarTitle({
      title: this.data.title,
    });
  },
  get_datas: function (e) {
    console.log(e);
    let infos = e.currentTarget.dataset;
    // 显示弹框
    wx.showToast({
      title: `Name：${infos.name}，Age：${infos.age}`,
      icon: 'none'
    })
  }
})