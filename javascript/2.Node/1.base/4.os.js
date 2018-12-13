const os = require("os");

// cup核数
console.log(os.cpus().length);

console.log(os.cpus());
// eg:
// [{
//     model: 'Intel(R) Core(TM) i5-3470 CPU @ 3.20GHz',
//     speed: 3193,
//     times:
//     {
//         user: 1660812,
//         nice: 0,
//         sys: 2001875,
//         idle: 43247140,
//         irq: 430812
//     }
// },
// {
//     model: 'Intel(R) Core(TM) i5-3470 CPU @ 3.20GHz',
//     speed: 3193,
//     times:
//     {
//         user: 1765718,
//         nice: 0,
//         sys: 1371296,
//         idle: 43772437,
//         irq: 14531
//     }
// },
// {
//     model: 'Intel(R) Core(TM) i5-3470 CPU @ 3.20GHz',
//     speed: 3193,
//     times:
//     {
//         user: 1957578,
//         nice: 0,
//         sys: 1427359,
//         idle: 43524515,
//         irq: 10250
//     }
// },
// {
//     model: 'Intel(R) Core(TM) i5-3470 CPU @ 3.20GHz',
//     speed: 3193,
//     times:
//         { user: 2366937, nice: 0, sys: 1504171, idle: 43038343, irq: 8000 }
// }]