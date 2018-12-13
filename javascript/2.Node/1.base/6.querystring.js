const querystring = require("querystring");

let jd_url = "https://search.jd.com/Search?keyword=空气净化器&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&psort=3&stock=1&wtype=1&cod=1&click=2";

let jd_qs = "keyword=空气净化器&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&psort=3&stock=1&wtype=1&cod=1&click=2";


let str = querystring.parse(jd_qs);
console.log(str)
// {
//     keyword: '空气净化器',
//     enc: 'utf-8',
//     qrst: '1',
//     rt: '1',
//     stop: '1',
//     vt: '2',
//     psort: '3',
//     stock: '1',
//     wtype: '1',
//     cod: '1',
//     click: '2' 
// }

// querystring.parse 只是对?后面(不包括`?`)的参数进行解析（以`=`和`&`分隔）
str = querystring.parse(jd_url);
console.log(str);
// {
//     https://search.jd.com/Search?keyword: '空气净化器',
//     enc: 'utf-8',
//     qrst: '1',
//     rt: '1',
//     stop: '1',
//     vt: '2',
//     psort: '3',
//     stock: '1',
//     wtype: '1',
//     cod: '1',
//     click: '2' 
// }