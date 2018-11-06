using System;
using System.Net;
using System.Text;
using System.Net.Sockets;

namespace client
{
    class Program
    {
        static void Main(string[] args)
        {
            using (var tcp_socket = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp))
            {
                // 连接服务器
                tcp_socket.Connect(new IPEndPoint(IPAddress.Parse("192.168.36.235"), 8080));

                while (true)
                {
                    // 发送消息
                    tcp_socket.Send(Encoding.UTF8.GetBytes("服务器你好"));
                    // 接收服务器消息
                    byte[] buffer = new byte[1024];
                    int count = tcp_socket.Receive(buffer);
                    Console.WriteLine($"来自服务器的消息：{Encoding.UTF8.GetString(buffer, 0, count)}");
                }
            }
        }
    }
}
