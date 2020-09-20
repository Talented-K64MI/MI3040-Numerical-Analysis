namespace WindowsFormsApp1
{
    partial class Form1
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
            this.button1 = new System.Windows.Forms.Button();
            this.button2 = new System.Windows.Forms.Button();
            this.button3 = new System.Windows.Forms.Button();
            this.button4 = new System.Windows.Forms.Button();
            this.button5 = new System.Windows.Forms.Button();
            this.label = new System.Windows.Forms.Label();
            this.function = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.result = new System.Windows.Forms.TextBox();
            this.SuspendLayout();
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(12, 43);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(200, 124);
            this.button1.TabIndex = 0;
            this.button1.Text = "Bài toán 1:";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.open1);
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(297, 43);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(200, 124);
            this.button2.TabIndex = 1;
            this.button2.Text = "Bài toán 2:";
            this.button2.UseVisualStyleBackColor = true;
            // 
            // button3
            // 
            this.button3.Location = new System.Drawing.Point(569, 43);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(200, 124);
            this.button3.TabIndex = 2;
            this.button3.Text = "Bài toán 3:";
            this.button3.UseVisualStyleBackColor = true;
            // 
            // button4
            // 
            this.button4.Location = new System.Drawing.Point(135, 218);
            this.button4.Name = "button4";
            this.button4.Size = new System.Drawing.Size(200, 124);
            this.button4.TabIndex = 3;
            this.button4.Text = "Bài toán 4:";
            this.button4.UseVisualStyleBackColor = true;
            // 
            // button5
            // 
            this.button5.Location = new System.Drawing.Point(472, 218);
            this.button5.Name = "button5";
            this.button5.Size = new System.Drawing.Size(200, 124);
            this.button5.TabIndex = 4;
            this.button5.Text = "Bài toán 5:";
            this.button5.UseVisualStyleBackColor = true;
            // 
            // label
            // 
            this.label.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
            this.label.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F);
            this.label.ForeColor = System.Drawing.SystemColors.ControlText;
            this.label.ImageAlign = System.Drawing.ContentAlignment.BottomRight;
            this.label.Location = new System.Drawing.Point(669, 408);
            this.label.Name = "label";
            this.label.Size = new System.Drawing.Size(100, 22);
            this.label.TabIndex = 5;
            this.label.Text = "Giải tích số";
            this.label.TextAlign = System.Drawing.ContentAlignment.BottomRight;
            this.label.Click += new System.EventHandler(this.label_Click);
            // 
            // function
            // 
            this.function.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
            this.function.Location = new System.Drawing.Point(70, 367);
            this.function.Multiline = true;
            this.function.Name = "function";
            this.function.Size = new System.Drawing.Size(497, 50);
            this.function.TabIndex = 7;

            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Microsoft Sans Serif", 11F);
            this.label1.Location = new System.Drawing.Point(67, 346);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(69, 18);
            this.label1.TabIndex = 8;
            this.label1.Text = "Function:";
            // 
            // result
            // 
            this.result.Location = new System.Drawing.Point(70, 418);
            this.result.Name = "result";
            this.result.Size = new System.Drawing.Size(265, 20);
            this.result.TabIndex = 9;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.result);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.function);
            this.Controls.Add(this.label);
            this.Controls.Add(this.button5);
            this.Controls.Add(this.button4);
            this.Controls.Add(this.button3);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.button1);
            this.Name = "Form1";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.Button button3;
        private System.Windows.Forms.Button button4;
        private System.Windows.Forms.Button button5;
        private System.Windows.Forms.Label label;
        private System.Windows.Forms.TextBox function;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox result;
    }
}

