using System;
using Dapper;
using MySql.Data.MySqlClient;

namespace ado_mysql
{
    class Program
    {
        static void Main(string[] args)
        {
            // Data Source：ip地址，Initial Catalog：数据库名，User ID：用户名，Password：密码，port：端口
            string connStr = "Data Source=192.168.36.144;Initial Catalog=worktemp;User ID=root;Password=dntdnt;CharSet=utf8;port=3306";
            using (var conn = new MySqlConnection(connStr))
            {
                conn.Open(); //打开连接
                var result = conn.QueryFirst("select count(*) from userinfo;");
                System.Console.WriteLine(result);
            }
            Console.WriteLine("done...");
        }
    }
}
