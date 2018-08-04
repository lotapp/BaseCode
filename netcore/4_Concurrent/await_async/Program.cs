using System;
using System.Net.Http;
using System.Threading.Tasks;

namespace await_async
{
    class Program
    {
        static void Main(string[] args)
        {
          str =  GetHtmlString("https://github.com/kasecato/vscode-intellij-idea-keybindings");
          System.Console.WriteLine(str);
        }

        /// <summary>
        /// 模拟一个网络操作（别忘了重试机制）
        /// </summary>
        /// <param name="url">url</param>
        /// <returns></returns>
        private async Task<string> DownloadString(string url)
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
            }
        }
    }
}
