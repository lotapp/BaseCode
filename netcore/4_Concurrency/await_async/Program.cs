using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Http;
using System.Threading;
using System.Threading.Tasks;

namespace await_async
{
    class Program
    {
        static void Main(string[] args)
        {
            // var task = DownloadStringAsync("https://github.com/kasecato/vscode-intellij-idea-keybindings").Result;

            // var urlList =new List<string>(){
            //     "https://www.baidu.com",
            //     "https://www.cnblogs.com"
            // };
            // var strs = DownloadStringAsync(urlList).Result;

            // var apiList = new List<string>(){
            //     "https://api.ipify.org",
            //     "http://int.dpool.sina.com.cn/iplookup/iplookup.php"
            // };
            // var str = GetIPAsync(apiList).Result;

            var tempStr = CancellMethod().Result;
        }

        /// <summary>
        /// 3.超时取消
        /// </summary>
        /// <returns></returns>
        private static async Task<string> CancellMethod()
        {
            //实例化取消任务
            var cts = new CancellationTokenSource();
            cts.CancelAfter(TimeSpan.FromSeconds(3)); // 设置失效时间为3s
            try
            {
                return await DoSomethingAsync(cts.Token);
            }
            // 任务已经取消会引发TaskCanceledException
            catch (TaskCanceledException ex)
            {

                return "false";
            }
        }

        /// <summary>
        /// 模仿一个耗时操作
        /// </summary>
        /// <returns></returns>
        private static async Task<string> DoSomethingAsync(CancellationToken token)
        {
            await Task.Delay(TimeSpan.FromSeconds(5), token);
            return "ok";
        }

        /// <summary>
        /// 2.返回首先完成的Task
        /// </summary>
        /// <param name="list"></param>
        /// <returns></returns>
        private static async Task<string> GetIPAsync(IEnumerable<string> list)
        {
            using (var client = new HttpClient())
            {
                var tasks = list.Select(url => client.GetStringAsync(url)).ToArray();
                var task = await Task.WhenAny(tasks); // 返回第一个完成的Task
                return await task.ConfigureAwait(false);
            }
        }


        /// <summary>
        /// 批量任务
        /// </summary>
        /// <param name="list"></param>
        /// <returns></returns>
        private async static Task<string[]> DownloadStringAsync(IEnumerable<string> list)
        {
            using (var client = new HttpClient())
            {
                var tasks = list.Select(url => client.GetStringAsync(url)).ToArray();
                return await Task.WhenAll(tasks);
            }
        }
        // private async static Task/
        /// <summary>
        /// 1.模拟一个网络操作（别忘了重试机制）
        /// </summary>
        /// <param name="url">url</param>
        /// <returns></returns>
        private async static Task<string> DownloadStringAsync(string url)
        {
            using (var client = new HttpClient())
            {
                // 设置第一次重试时间
                var nextDelay = TimeSpan.FromSeconds(1);
                for (int i = 0; i < 3; i++)
                {
                    try
                    {
                        return await client.GetStringAsync(url);
                    }
                    catch { }
                    await Task.Delay(nextDelay);
                    nextDelay *= 2; // 3次重试机会，第一次1s，第二次2s，第三次4s
                }
                // 最后一次尝试，错误就抛出
                return await client.GetStringAsync(url);
            }
        }
    }
}
