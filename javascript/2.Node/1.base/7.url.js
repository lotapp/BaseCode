const url = require("url");

let jd_url = "https://search.jd.com/Search?keyword=空气净化器&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&psort=3&stock=1&wtype=1&cod=1&click=2";

let str = url.parse(jd_url);
// port=null说明是默认端口（http：80，https：443）
console.log(str);
// Url {
//     protocol: 'https:',
//     slashes: true,
//     auth: null,
//     host: 'search.jd.com',
//     port: null,
//     hostname: 'search.jd.com',
//     hash: null,
//     search:'?keyword=空气净化器&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&psort=3&stock=1&wtype=1&cod=1&click=2',
//     query:'keyword=空气净化器&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&psort=3&stock=1&wtype=1&cod=1&click=2',
//     pathname: '/Search',
//     path:'/Search?keyword=空气净化器&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&psort=3&stock=1&wtype=1&cod=1&click=2',
//     href:'https://search.jd.com/Search?keyword=空气净化器&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&psort=3&stock=1&wtype=1&cod=1&click=2'
// }

// 想要解析`query`，可以多传一个参数
str = url.parse(jd_url, true);
console.log(str);
// Url {
//     protocol: 'https:',
//     slashes: true,
//     auth: null,
//     host: 'search.jd.com',
//     port: null,
//     hostname: 'search.jd.com',
//     hash: null,
//     search: '?keyword=空气净化器&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&psort=3&stock=1&wtype=1&cod=1&click=2',
//     query: { //已经被解析了，内部使用了`querystring`模块
//        keyword: '空气净化器',
//        enc: 'utf-8',
//        qrst: '1',
//        rt: '1',
//        stop: '1',
//        vt: '2',
//        psort: '3',
//        stock: '1',
//        wtype: '1',
//        cod: '1',
//        click: '2' 
//     },
//     pathname: '/Search',
//     path: '/Search?keyword=空气净化器&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&psort=3&stock=1&wtype=1&cod=1&click=2',
//     href: 'https://search.jd.com/Search?keyword=空气净化器&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&psort=3&stock=1&wtype=1&cod=1&click=2'
// }