using System;

namespace _4TryCatch
{
    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                throw new Exception("出错了啊");
                //Convert.ToInt32("mmd");
            }
            catch (Exception ex)
            {
                // Input string was not in a correct format
                Console.WriteLine(ex.Message);
            }
            finally
            {
                Console.WriteLine("finally");
            }
        }
    }
}
