using System;
using System.Net;
using System.Text;
using System.Net.Sockets;
using System.Threading.Tasks;

namespace _2_TCP
{
    class Program
    {
        static void Main(string[] args)
        {
            using (var tcp_socket = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp))
            {
                var ip_addr = IPAddress.Parse("192.168.36.235");
                // 服务器端绑定Port
                tcp_socket.Bind(new IPEndPoint(ip_addr, 8080));
                // 服务器监听
                tcp_socket.Listen(5);
                while (true)
                {
                    // 等待客户端连接
                    var client_socket = tcp_socket.Accept();
                    // 远程端口
                    var client_point = client_socket.RemoteEndPoint;
                    Task.Run(() =>
                    {
                        while (true)
                        {
                            byte[] buffer = new byte[1024];
                            int count = client_socket.Receive(buffer);
                            Console.WriteLine($"来自{client_socket.RemoteEndPoint.ToString()}的消息:\n{Encoding.UTF8.GetString(buffer, 0, count)}");
                            client_socket.Send(Encoding.UTF8.GetBytes("知道了～"));
                        }
                    });
                }
            }
        }
    }
}