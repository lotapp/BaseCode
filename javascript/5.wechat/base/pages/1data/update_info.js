Page({
  data: {
    name: "小明",
    age: 23,
    work: {
      "name": "微软",
      "location": "中国"
    },
    my_class: "red"
  },
  onLoad: function () {
    console.log("页面加载完成");
  },
  // 自定义方法
  update_info: function () {
    // this对象经常容易变，我一般都存一份
    var that = this;
    // 后台获取data里的值
    console.log(that.data.name, that.data.age)
    // 修改data(直接赋值没用)
    that.setData({
      age: 25,
      name: "小华",
      work: {
        "name": "苹果",
        "location": "美国"
      }
    });
  }
})