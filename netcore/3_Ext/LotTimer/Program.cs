using System;
using System.Threading;
using System.Diagnostics;
using System.Runtime.InteropServices;

//Old: https://github.com/dunitian/DNTLive/blob/master/Software/LoTTimer/Program.cs
namespace timer
{
    class Program
    {
        static void Main(string[] args)
        {
            while (true)
            {
                try
                {
                    Console.WriteLine(DateTime.Now.ToString());
                    Thread.Sleep(new TimeSpan(0, 10, 0));
                    MyBeep();
                }
                catch
                {
                    //异常还不结束？
                    break;
                }
            }
        }
        private static void MyBeep()
        {
            if (RuntimeInformation.IsOSPlatform(OSPlatform.Linux))
            {
                Console.WriteLine("当前系统为Linux");
                Process.Start("notify-send", "友情提醒 10分钟过去了");
                //用shell启动指定程序+命令
                //Process.Start(new ProcessStartInfo("notify-send", "友情提醒 10分钟过去了") { RedirectStandardOutput = true });
            }
            else if (RuntimeInformation.IsOSPlatform(OSPlatform.Windows))
            {
                Console.WriteLine("当前系统为Windows");
                // frequency:提示音的频率，介于 37 到 32767 赫兹之间。// duration:提示音的持续时间，以毫秒为单位。
                Console.Beep(500, 1500);
            }
            else
            {
                Console.WriteLine("精力有限，暂不支持");
            }
        }
    }
}
