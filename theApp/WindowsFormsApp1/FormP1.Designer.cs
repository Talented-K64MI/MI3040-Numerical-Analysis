namespace WindowsFormsApp1
{
    partial class FormP1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.functionBox = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.repeat = new System.Windows.Forms.Button();
            this.label2 = new System.Windows.Forms.Label();
            this.Xn = new System.Windows.Forms.TextBox();
            this.label3 = new System.Windows.Forms.Label();
            this.Xn1 = new System.Windows.Forms.TextBox();
            this.Delta = new System.Windows.Forms.TextBox();
            this.label4 = new System.Windows.Forms.Label();
            this.label5 = new System.Windows.Forms.Label();
            this.label6 = new System.Windows.Forms.Label();
            this.Epsilon = new System.Windows.Forms.TextBox();
            this.lowerBound = new System.Windows.Forms.TextBox();
            this.label7 = new System.Windows.Forms.Label();
            this.label8 = new System.Windows.Forms.Label();
            this.label9 = new System.Windows.Forms.Label();
            this.upperBound = new System.Windows.Forms.TextBox();
            this.button1 = new System.Windows.Forms.Button();
            this.textBox1 = new System.Windows.Forms.TextBox();
            this.SuspendLayout();
            // 
            // functionBox
            // 
            this.functionBox.BackColor = System.Drawing.SystemColors.Window;
            this.functionBox.Font = new System.Drawing.Font("Microsoft Sans Serif", 16F);
            this.functionBox.Location = new System.Drawing.Point(12, 44);
            this.functionBox.Name = "functionBox";
            this.functionBox.Size = new System.Drawing.Size(526, 32);
            this.functionBox.TabIndex = 0;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Microsoft Sans Serif", 14F);
            this.label1.Location = new System.Drawing.Point(12, 17);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(82, 24);
            this.label1.TabIndex = 1;
            this.label1.Text = "hàm lặp:";
            // 
            // repeat
            // 
            this.repeat.Font = new System.Drawing.Font("Microsoft Sans Serif", 20F);
            this.repeat.ForeColor = System.Drawing.SystemColors.ControlText;
            this.repeat.Location = new System.Drawing.Point(619, 17);
            this.repeat.Name = "repeat";
            this.repeat.Size = new System.Drawing.Size(256, 100);
            this.repeat.TabIndex = 2;
            this.repeat.Text = "Lặp";
            this.repeat.UseVisualStyleBackColor = true;
            this.repeat.Click += new System.EventHandler(this.repeat_Click);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("Microsoft Sans Serif", 14F);
            this.label2.ForeColor = System.Drawing.SystemColors.ControlText;
            this.label2.Location = new System.Drawing.Point(8, 106);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(46, 24);
            this.label2.TabIndex = 3;
            this.label2.Text = "Xn=";
            // 
            // Xn
            // 
            this.Xn.Font = new System.Drawing.Font("Microsoft Sans Serif", 14F);
            this.Xn.Location = new System.Drawing.Point(86, 103);
            this.Xn.Name = "Xn";
            this.Xn.Size = new System.Drawing.Size(146, 29);
            this.Xn.TabIndex = 4;
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Font = new System.Drawing.Font("Microsoft Sans Serif", 14F);
            this.label3.ForeColor = System.Drawing.SystemColors.ControlText;
            this.label3.Location = new System.Drawing.Point(238, 106);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(79, 24);
            this.label3.TabIndex = 5;
            this.label3.Text = "X(n+1)=";
            // 
            // Xn1
            // 
            this.Xn1.Font = new System.Drawing.Font("Microsoft Sans Serif", 14F);
            this.Xn1.Location = new System.Drawing.Point(338, 103);
            this.Xn1.Name = "Xn1";
            this.Xn1.Size = new System.Drawing.Size(163, 29);
            this.Xn1.TabIndex = 6;
            // 
            // Delta
            // 
            this.Delta.Font = new System.Drawing.Font("Microsoft Sans Serif", 14F);
            this.Delta.Location = new System.Drawing.Point(86, 195);
            this.Delta.Name = "Delta";
            this.Delta.Size = new System.Drawing.Size(146, 29);
            this.Delta.TabIndex = 8;
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Font = new System.Drawing.Font("Microsoft Sans Serif", 14F);
            this.label4.ForeColor = System.Drawing.SystemColors.ControlText;
            this.label4.Location = new System.Drawing.Point(8, 198);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(0, 24);
            this.label4.TabIndex = 7;
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Font = new System.Drawing.Font("Microsoft Sans Serif", 14F);
            this.label5.ForeColor = System.Drawing.SystemColors.ControlText;
            this.label5.Location = new System.Drawing.Point(8, 198);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(63, 24);
            this.label5.TabIndex = 9;
            this.label5.Text = "Delta=";
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Font = new System.Drawing.Font("Microsoft Sans Serif", 14F);
            this.label6.ForeColor = System.Drawing.SystemColors.ControlText;
            this.label6.Location = new System.Drawing.Point(238, 198);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(84, 24);
            this.label6.TabIndex = 10;
            this.label6.Text = "Epsilon=";
            // 
            // Epsilon
            // 
            this.Epsilon.Font = new System.Drawing.Font("Microsoft Sans Serif", 14F);
            this.Epsilon.Location = new System.Drawing.Point(338, 193);
            this.Epsilon.Name = "Epsilon";
            this.Epsilon.Size = new System.Drawing.Size(163, 29);
            this.Epsilon.TabIndex = 11;
            // 
            // lowerBound
            // 
            this.lowerBound.Font = new System.Drawing.Font("Microsoft Sans Serif", 14F);
            this.lowerBound.Location = new System.Drawing.Point(86, 349);
            this.lowerBound.Name = "lowerBound";
            this.lowerBound.Size = new System.Drawing.Size(146, 29);
            this.lowerBound.TabIndex = 12;
            // 
            // label7
            // 
            this.label7.AutoSize = true;
            this.label7.Font = new System.Drawing.Font("Microsoft Sans Serif", 14F);
            this.label7.ForeColor = System.Drawing.SystemColors.ControlText;
            this.label7.Location = new System.Drawing.Point(12, 354);
            this.label7.Name = "label7";
            this.label7.Size = new System.Drawing.Size(36, 24);
            this.label7.TabIndex = 13;
            this.label7.Text = "a =";
            // 
            // label8
            // 
            this.label8.AutoSize = true;
            this.label8.Font = new System.Drawing.Font("Microsoft Sans Serif", 14F);
            this.label8.ForeColor = System.Drawing.SystemColors.ControlText;
            this.label8.Location = new System.Drawing.Point(12, 309);
            this.label8.Name = "label8";
            this.label8.Size = new System.Drawing.Size(96, 24);
            this.label8.TabIndex = 14;
            this.label8.Text = "Bisection: ";
            this.label8.Click += new System.EventHandler(this.label8_Click);
            // 
            // label9
            // 
            this.label9.AutoSize = true;
            this.label9.Font = new System.Drawing.Font("Microsoft Sans Serif", 14F);
            this.label9.ForeColor = System.Drawing.SystemColors.ControlText;
            this.label9.Location = new System.Drawing.Point(384, 352);
            this.label9.Name = "label9";
            this.label9.Size = new System.Drawing.Size(37, 24);
            this.label9.TabIndex = 15;
            this.label9.Text = "b =";
            // 
            // upperBound
            // 
            this.upperBound.Font = new System.Drawing.Font("Microsoft Sans Serif", 14F);
            this.upperBound.Location = new System.Drawing.Point(453, 349);
            this.upperBound.Name = "upperBound";
            this.upperBound.Size = new System.Drawing.Size(146, 29);
            this.upperBound.TabIndex = 16;
            // 
            // button1
            // 
            this.button1.Font = new System.Drawing.Font("Microsoft Sans Serif", 20F);
            this.button1.ForeColor = System.Drawing.SystemColors.ControlText;
            this.button1.Location = new System.Drawing.Point(657, 309);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(256, 100);
            this.button1.TabIndex = 17;
            this.button1.Text = "Lặp";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // textBox1
            // 
            this.textBox1.Location = new System.Drawing.Point(77, 500);
            this.textBox1.Name = "textBox1";
            this.textBox1.Size = new System.Drawing.Size(100, 20);
            this.textBox1.TabIndex = 18;
            // 
            // FormP1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(984, 561);
            this.Controls.Add(this.textBox1);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.upperBound);
            this.Controls.Add(this.label9);
            this.Controls.Add(this.label8);
            this.Controls.Add(this.label7);
            this.Controls.Add(this.lowerBound);
            this.Controls.Add(this.Epsilon);
            this.Controls.Add(this.label6);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.Delta);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.Xn1);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.Xn);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.repeat);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.functionBox);
            this.Name = "FormP1";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "FormP1";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        public System.Windows.Forms.TextBox functionBox;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Button repeat;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TextBox Xn;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.TextBox Xn1;
        private System.Windows.Forms.TextBox Delta;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.TextBox Epsilon;
        private System.Windows.Forms.TextBox lowerBound;
        private System.Windows.Forms.Label label7;
        private System.Windows.Forms.Label label8;
        private System.Windows.Forms.Label label9;
        private System.Windows.Forms.TextBox upperBound;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.TextBox textBox1;
    }
}