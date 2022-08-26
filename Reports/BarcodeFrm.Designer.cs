namespace Accounting_Project.Reports
{
    partial class BarcodeFrm
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
            this.PreviousPage_Bt = new System.Windows.Forms.Button();
            this.LastPage_bt = new System.Windows.Forms.Button();
            this.NextPage_Bt = new System.Windows.Forms.Button();
            this.crystalReportViewer1 = new CrystalDecisions.Windows.Forms.CrystalReportViewer();
            this.Export_Bt = new System.Windows.Forms.Button();
            this.Print_Bt = new System.Windows.Forms.Button();
            this.View_Bt = new System.Windows.Forms.Button();
            this.metroLabel1 = new MetroFramework.Controls.MetroLabel();
            this.Pid_Tx = new MetroFramework.Controls.MetroTextBox();
            this.QTY_Tx = new MetroFramework.Controls.MetroTextBox();
            this.metroLabel2 = new MetroFramework.Controls.MetroLabel();
            this.button2 = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(44, 96);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(40, 23);
            this.button1.TabIndex = 23;
            this.button1.Text = "<<";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // PreviousPage_Bt
            // 
            this.PreviousPage_Bt.Location = new System.Drawing.Point(90, 96);
            this.PreviousPage_Bt.Name = "PreviousPage_Bt";
            this.PreviousPage_Bt.Size = new System.Drawing.Size(40, 23);
            this.PreviousPage_Bt.TabIndex = 22;
            this.PreviousPage_Bt.Text = "<";
            this.PreviousPage_Bt.UseVisualStyleBackColor = true;
            this.PreviousPage_Bt.Click += new System.EventHandler(this.PreviousPage_Bt_Click);
            // 
            // LastPage_bt
            // 
            this.LastPage_bt.Location = new System.Drawing.Point(182, 96);
            this.LastPage_bt.Name = "LastPage_bt";
            this.LastPage_bt.Size = new System.Drawing.Size(40, 23);
            this.LastPage_bt.TabIndex = 21;
            this.LastPage_bt.Text = ">>";
            this.LastPage_bt.UseVisualStyleBackColor = true;
            this.LastPage_bt.Click += new System.EventHandler(this.LastPage_bt_Click);
            // 
            // NextPage_Bt
            // 
            this.NextPage_Bt.Location = new System.Drawing.Point(136, 96);
            this.NextPage_Bt.Name = "NextPage_Bt";
            this.NextPage_Bt.Size = new System.Drawing.Size(40, 23);
            this.NextPage_Bt.TabIndex = 20;
            this.NextPage_Bt.Text = ">";
            this.NextPage_Bt.UseVisualStyleBackColor = true;
            this.NextPage_Bt.Click += new System.EventHandler(this.NextPage_Bt_Click);
            // 
            // crystalReportViewer1
            // 
            this.crystalReportViewer1.ActiveViewIndex = -1;
            this.crystalReportViewer1.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.crystalReportViewer1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.crystalReportViewer1.Cursor = System.Windows.Forms.Cursors.Default;
            this.crystalReportViewer1.Location = new System.Drawing.Point(12, 142);
            this.crystalReportViewer1.Name = "crystalReportViewer1";
            this.crystalReportViewer1.Size = new System.Drawing.Size(812, 297);
            this.crystalReportViewer1.TabIndex = 15;
            this.crystalReportViewer1.ToolPanelView = CrystalDecisions.Windows.Forms.ToolPanelViewType.None;
            // 
            // Export_Bt
            // 
            this.Export_Bt.Location = new System.Drawing.Point(704, 44);
            this.Export_Bt.Name = "Export_Bt";
            this.Export_Bt.Size = new System.Drawing.Size(95, 56);
            this.Export_Bt.TabIndex = 14;
            this.Export_Bt.Text = "&Export";
            this.Export_Bt.UseVisualStyleBackColor = true;
            this.Export_Bt.Click += new System.EventHandler(this.Export_Bt_Click);
            // 
            // Print_Bt
            // 
            this.Print_Bt.Location = new System.Drawing.Point(603, 44);
            this.Print_Bt.Name = "Print_Bt";
            this.Print_Bt.Size = new System.Drawing.Size(95, 56);
            this.Print_Bt.TabIndex = 13;
            this.Print_Bt.Text = "&Print";
            this.Print_Bt.UseVisualStyleBackColor = true;
            this.Print_Bt.Click += new System.EventHandler(this.Print_Bt_Click);
            // 
            // View_Bt
            // 
            this.View_Bt.Location = new System.Drawing.Point(372, 44);
            this.View_Bt.Name = "View_Bt";
            this.View_Bt.Size = new System.Drawing.Size(95, 56);
            this.View_Bt.TabIndex = 12;
            this.View_Bt.Text = "&View";
            this.View_Bt.UseVisualStyleBackColor = true;
            this.View_Bt.Click += new System.EventHandler(this.View_Bt_Click);
            // 
            // metroLabel1
            // 
            this.metroLabel1.AutoSize = true;
            this.metroLabel1.Location = new System.Drawing.Point(12, 63);
            this.metroLabel1.Name = "metroLabel1";
            this.metroLabel1.Size = new System.Drawing.Size(63, 19);
            this.metroLabel1.TabIndex = 24;
            this.metroLabel1.Text = "Enter PID";
            // 
            // Pid_Tx
            // 
            // 
            // 
            // 
            this.Pid_Tx.CustomButton.Image = null;
            this.Pid_Tx.CustomButton.Location = new System.Drawing.Point(72, 1);
            this.Pid_Tx.CustomButton.Name = "";
            this.Pid_Tx.CustomButton.Size = new System.Drawing.Size(21, 21);
            this.Pid_Tx.CustomButton.Style = MetroFramework.MetroColorStyle.Blue;
            this.Pid_Tx.CustomButton.TabIndex = 1;
            this.Pid_Tx.CustomButton.Theme = MetroFramework.MetroThemeStyle.Light;
            this.Pid_Tx.CustomButton.UseSelectable = true;
            this.Pid_Tx.CustomButton.Visible = false;
            this.Pid_Tx.Lines = new string[0];
            this.Pid_Tx.Location = new System.Drawing.Point(81, 61);
            this.Pid_Tx.MaxLength = 32767;
            this.Pid_Tx.Name = "Pid_Tx";
            this.Pid_Tx.PasswordChar = '\0';
            this.Pid_Tx.ScrollBars = System.Windows.Forms.ScrollBars.None;
            this.Pid_Tx.SelectedText = "";
            this.Pid_Tx.SelectionLength = 0;
            this.Pid_Tx.SelectionStart = 0;
            this.Pid_Tx.ShortcutsEnabled = true;
            this.Pid_Tx.Size = new System.Drawing.Size(94, 23);
            this.Pid_Tx.TabIndex = 25;
            this.Pid_Tx.UseSelectable = true;
            this.Pid_Tx.WaterMarkColor = System.Drawing.Color.FromArgb(((int)(((byte)(109)))), ((int)(((byte)(109)))), ((int)(((byte)(109)))));
            this.Pid_Tx.WaterMarkFont = new System.Drawing.Font("Segoe UI", 12F, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Pixel);
            // 
            // QTY_Tx
            // 
            // 
            // 
            // 
            this.QTY_Tx.CustomButton.Image = null;
            this.QTY_Tx.CustomButton.Location = new System.Drawing.Point(53, 1);
            this.QTY_Tx.CustomButton.Name = "";
            this.QTY_Tx.CustomButton.Size = new System.Drawing.Size(21, 21);
            this.QTY_Tx.CustomButton.Style = MetroFramework.MetroColorStyle.Blue;
            this.QTY_Tx.CustomButton.TabIndex = 1;
            this.QTY_Tx.CustomButton.Theme = MetroFramework.MetroThemeStyle.Light;
            this.QTY_Tx.CustomButton.UseSelectable = true;
            this.QTY_Tx.CustomButton.Visible = false;
            this.QTY_Tx.Lines = new string[0];
            this.QTY_Tx.Location = new System.Drawing.Point(250, 61);
            this.QTY_Tx.MaxLength = 32767;
            this.QTY_Tx.Name = "QTY_Tx";
            this.QTY_Tx.PasswordChar = '\0';
            this.QTY_Tx.ScrollBars = System.Windows.Forms.ScrollBars.None;
            this.QTY_Tx.SelectedText = "";
            this.QTY_Tx.SelectionLength = 0;
            this.QTY_Tx.SelectionStart = 0;
            this.QTY_Tx.ShortcutsEnabled = true;
            this.QTY_Tx.Size = new System.Drawing.Size(75, 23);
            this.QTY_Tx.TabIndex = 27;
            this.QTY_Tx.UseSelectable = true;
            this.QTY_Tx.WaterMarkColor = System.Drawing.Color.FromArgb(((int)(((byte)(109)))), ((int)(((byte)(109)))), ((int)(((byte)(109)))));
            this.QTY_Tx.WaterMarkFont = new System.Drawing.Font("Segoe UI", 12F, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Pixel);
            // 
            // metroLabel2
            // 
            this.metroLabel2.AutoSize = true;
            this.metroLabel2.Location = new System.Drawing.Point(214, 64);
            this.metroLabel2.Name = "metroLabel2";
            this.metroLabel2.Size = new System.Drawing.Size(30, 19);
            this.metroLabel2.TabIndex = 26;
            this.metroLabel2.Text = "Qty";
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(502, 44);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(95, 56);
            this.button2.TabIndex = 28;
            this.button2.Text = "View &All";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // BarcodeFrm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(836, 451);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.QTY_Tx);
            this.Controls.Add(this.metroLabel2);
            this.Controls.Add(this.Pid_Tx);
            this.Controls.Add(this.metroLabel1);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.PreviousPage_Bt);
            this.Controls.Add(this.LastPage_bt);
            this.Controls.Add(this.NextPage_Bt);
            this.Controls.Add(this.crystalReportViewer1);
            this.Controls.Add(this.Export_Bt);
            this.Controls.Add(this.Print_Bt);
            this.Controls.Add(this.View_Bt);
            this.Name = "BarcodeFrm";
            this.Text = "BarcodeFrm";
            this.Load += new System.EventHandler(this.BarcodeFrm_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Button PreviousPage_Bt;
        private System.Windows.Forms.Button LastPage_bt;
        private System.Windows.Forms.Button NextPage_Bt;
        private CrystalDecisions.Windows.Forms.CrystalReportViewer crystalReportViewer1;
        private System.Windows.Forms.Button Export_Bt;
        private System.Windows.Forms.Button Print_Bt;
        private System.Windows.Forms.Button View_Bt;
        private MetroFramework.Controls.MetroLabel metroLabel1;
        private MetroFramework.Controls.MetroTextBox Pid_Tx;
        private MetroFramework.Controls.MetroTextBox QTY_Tx;
        private MetroFramework.Controls.MetroLabel metroLabel2;
        private System.Windows.Forms.Button button2;
    }
}