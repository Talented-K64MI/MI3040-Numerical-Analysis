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
        dynamic py;
        public FormP1()
        {
            InitializeComponent();
            //build python calculator
            var engine = Python.CreateEngine();
            py = engine.ExecuteFile(calculatorPath);
            //calculator = py.Function();
        }

        private void repeat_Click(object sender, EventArgs e)
        {
            //calculate new value
            var function = py.Function(functionBox.Text);

            double x = Convert.ToDouble(Xn.Text);
            Xn1.Text = Xn.Text;
            //Xn.Text = ""+ calculator.cal(function.Text, x);
            Xn.Text = "" + function.value(x);

            Delta.Text = ""+ ( Convert.ToDouble(Xn.Text) - Convert.ToDouble(Xn1.Text) );
            //
            double offset = 1;
            Epsilon.Text = "" + Convert.ToDouble(Delta.Text) * offset;
        }

        private void label8_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {

        }
    }
}
