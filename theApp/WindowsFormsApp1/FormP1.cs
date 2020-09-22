using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using IronPython.Hosting;
namespace WindowsFormsApp1
{
    public partial class FormP1 : Form
    {
        string calculatorPath = @"..\\..\\Calculator.py";
        dynamic calculator;
        public FormP1()
        {
            InitializeComponent();
            //build python calculator
            var engine = Python.CreateEngine();
            dynamic py = engine.ExecuteFile(calculatorPath);
            calculator = py.Calculator();
        }

        private void repeat_Click(object sender, EventArgs e)
        {
            //calculate new value
            double x = Convert.ToDouble(Xn.Text);
            Xn1.Text = Xn.Text;
            Xn.Text = ""+ calculator.cal(function.Text, x);
            Delta.Text = ""+ ( Convert.ToDouble(Xn.Text) - Convert.ToDouble(Xn1.Text) );
            //
            double offset = 1;
            Epsilon.Text = "" + Convert.ToDouble(Delta.Text) * offset;
        }
    }
}
