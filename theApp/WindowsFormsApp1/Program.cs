using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using System.Windows.Forms;
using IronPython.Hosting;
namespace WindowsFormsApp1
{
    public class Program
    {
        Microsoft.Scripting.Hosting.ScriptEngine engine;
        /// <summary>
        /// The main entry point for the application.
        /// </summary>
        [STAThread]
        static void Main()
        {
            new Program();
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            Application.Run(new Form1());
            
        }
        Program()
        {
            engine = Python.CreateEngine();
        }
    }
}
