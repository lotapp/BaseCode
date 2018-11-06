using System.Net;
using System.Text;
using System.Net.Sockets;

namespace netcore
{
    class Program
    {
        static void Main(string[] args)
        {
            // UDP通信
            using (var udp_socket = new Socket(AddressFamily.InterNetwork, SocketType.Dgram, ProtocolType.Udp))
            {
                var ip_addr = IPAddress.Parse("192.168.36.235");

                // 绑定本地端口
                udp_socket.Bind(new IPEndPoint(ip_addr, 5400));
                // UDP发送消息
                int i = udp_socket.SendTo(Encoding.UTF8.GetBytes("小明你好啊～"), new IPEndPoint(ip_addr, 8080));
                Console.WriteLine($"发送计数：{i}");
            }
            Console.WriteLine("over");
        }
    }
}