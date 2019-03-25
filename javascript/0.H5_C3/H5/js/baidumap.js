var map;
//创建地图
function createMap(id_str, lng, lat) {
    map = new BMap.Map(id_str);
    map.centerAndZoom(new BMap.Point(lng, lat), 15);
}
//设置地图事件
function setMapEvent() {
    map.enableScrollWheelZoom();
    map.enableKeyboard();
    map.enableDragging();
    map.enableDoubleClickZoom()
}
// 图标单击事件
function addClickHandler(target, window) {
    target.addEventListener("click", function () {
        target.openInfoWindow(window);
    });
}
//向地图添加覆盖物
function addMapOverlay(lng, lat, content) {
    var markers = [{
        content: content, // 一般写详细地址
        title: "",
        imageOffset: {
            width: -46,
            height: -21
        },
        position: {
            lng: lng,
            lat: lat
        }
    }, ];
    for (var index = 0; index < markers.length; index++) {
        var point = new BMap.Point(markers[index].position.lng, markers[index].position.lat);
        var marker = new BMap.Marker(point, {
            icon: new BMap.Icon("http://api.map.baidu.com/lbsapi/createmap/images/icon.png", new BMap.Size(20, 25), {
                imageOffset: new BMap.Size(markers[index].imageOffset.width, markers[index].imageOffset.height)
            })
        });
        var label = new BMap.Label(markers[index].title, {
            offset: new BMap.Size(25, 5)
        });
        var opts = {
            width: 200,
            title: markers[index].title,
            enableMessage: false
        };
        var infoWindow = new BMap.InfoWindow(markers[index].content, opts);
        marker.setLabel(label);
        addClickHandler(marker, infoWindow);
        map.addOverlay(marker);
    };
    var labels = [];
    for (var index = 0; index < labels.length; index++) {
        var opt = {
            position: new BMap.Point(labels[index].position.lng, labels[index].position.lat)
        };
        var label = new BMap.Label(labels[index].content, opt);
        map.addOverlay(label);
    };
    var plOpts = [];
    var plPath = [];
    for (var index = 0; index < plOpts.length; index++) {
        var polyline = new BMap.Polyline(plPath[index], plOpts[index]);
        map.addOverlay(polyline);
    }
}
//向地图添加控件
function addMapControl() {
    var scaleControl = new BMap.ScaleControl({
        anchor: BMAP_ANCHOR_BOTTOM_LEFT
    });
    scaleControl.setUnit(BMAP_UNIT_IMPERIAL);
    map.addControl(scaleControl);
    var navControl = new BMap.NavigationControl({
        anchor: BMAP_ANCHOR_TOP_LEFT,
        type: 0
    });
    map.addControl(navControl);
    var overviewControl = new BMap.OverviewMapControl({
        anchor: BMAP_ANCHOR_BOTTOM_RIGHT,
        isOpen: true
    });
    map.addControl(overviewControl);
}
//创建和初始化地图函数：id字符串，经度，纬度，详细信息
function initMap(id_str, lng, lat, content) {
    console.info(id_str, lng, lat, content);
    if (content == undefined) {
        content = "I am here"; //`lng:${lng},lat:${lat}`; // ES6语法（默认参数也是ES6语法）
        console.info("没有详细描述");
    }
    createMap(id_str, lng, lat); //创建地图
    setMapEvent(); //设置地图事件
    addMapControl(); //向地图添加控件
    addMapOverlay(lng, lat, content); //向地图添加覆盖物
}