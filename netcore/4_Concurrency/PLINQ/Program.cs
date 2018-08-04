using System;
using System.Threading.Tasks;
using System.Collections.Generic;
using System.Linq;
using System.Threading;

namespace PLINQ
{
    class Program
    {
        static void Main(string[] args)
        {
            // foreach (var item in ParallelMethod1(new List<int>() { 1, 2, 3, 4, 5, 7, 8, 9 }))
            // {
            //     Console.WriteLine(item);
            // }

            // var list = new List<long>();
            // for (long i = 0; i < 1000000; i++)
            // {
            //     list.Add(i);
            // }
            // System.Console.WriteLine(GetSumParallel(list));

            // WorkingAsync().Wait();
        }

        private static void WorkingParallel(CancellationToken token, params Action[] actions)
        {
            Parallel.Invoke(new ParallelOptions() { CancellationToken = token }, actions);

        }
        private static async Task WorkingParallelAsync()
        {
            await Task.Run(() =>
                Parallel.Invoke(
                    () => Task.Delay(TimeSpan.FromSeconds(3)),
                    () => Task.Delay(TimeSpan.FromSeconds(2))
                ));
        }

        /// <summary>
        /// 举个例子3
        /// </summary>
        /// <param name="list"></param>
        /// <returns></returns>
        private static long GetSumParallel(IEnumerable<long> list, CancellationToken token)
        {
            return list.AsParallel().WithCancellation(token).Sum();
        }

        /// <summary>
        /// 举个例子2
        /// </summary>
        /// <param name="list"></param>
        /// <returns></returns>
        private static long GetSumParallel(IEnumerable<long> list)
        {
            return list.AsParallel().Sum();
        }

        /// <summary>
        /// 举个例子1
        /// </summary>
        private static IEnumerable<int> ParallelMethod1(IEnumerable<int> list)
        {
            return list.AsParallel().AsOrdered().Select(x => x * x);
        }

        /// <summary>
        /// 举个例子
        /// </summary>
        private static IEnumerable<int> ParallelMethod(IEnumerable<int> list)
        {
            return list.AsParallel().Select(x => x * x);
        }
    }
}
