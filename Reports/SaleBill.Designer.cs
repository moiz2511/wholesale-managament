namespace Accounting_Project.Reports
{
    partial class SaleBill
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
            this.View_bt = new MetroFramework.Controls.MetroButton();
            this.Export_bt = new MetroFramework.Controls.MetroButton();
            this.metroLabel2 = new MetroFramework.Controls.MetroLabel();
            this.Print_bt = new MetroFramework.Controls.MetroButton();
            this.Bill_cb = new System.Windows.Forms.ComboBox();
            this.Name_cb = new System.Windows.Forms.ComboBox();
            this.metroLabel1 = new MetroFramework.Controls.MetroLabel();
            this.crystalReportViewer1 = new CrystalDecisions.Windows.Forms.CrystalReportViewer();
            this.SuspendLayout();
            // 
            // View_bt
            // 
            this.View_bt.FontSize = MetroFramework.MetroButtonSize.Tall;
            this.View_bt.FontWeight = MetroFramework.MetroButtonWeight.Regular;
            this.View_bt.Location = new System.Drawing.Point(509, 63);
            this.View_bt.Name = "View_bt";
            this.View_bt.Size = new System.Drawing.Size(110, 48);
            this.View_bt.TabIndex = 15;
            this.View_bt.Text = "&View";
            this.View_bt.UseSelectable = true;
            this.View_bt.Click += new System.EventHandler(this.View_bt_Click);
            // 
            // Export_bt
            // 
            this.Export_bt.FontSize = MetroFramework.MetroButtonSize.Tall;
            this.Export_bt.FontWeight = MetroFramework.MetroButtonWeight.Regular;
            this.Export_bt.Location = new System.Drawing.Point(741, 63);
            this.Export_bt.Name = "Export_bt";
            this.Export_bt.Size = new System.Drawing.Size(110, 48);
            this.Export_bt.TabIndex = 14;
            this.Export_bt.Text = "&Export";
            this.Export_bt.UseSelectable = true;
            this.Export_bt.Click += new System.EventHandler(this.Export_bt_Click);
            // 
            // metroLabel2
            // 
            this.metroLabel2.AutoSize = true;
            this.metroLabel2.Location = new System.Drawing.Point(270, 63);
            this.metroLabel2.Name = "metroLabel2";
            this.metroLabel2.Size = new System.Drawing.Size(91, 19);
            this.metroLabel2.TabIndex = 13;
            this.metroLabel2.Text = "Search Bill No";
            // 
            // Print_bt
            // 
            this.Print_bt.FontSize = MetroFramework.MetroButtonSize.Tall;
            this.Print_bt.FontWeight = MetroFramework.MetroButtonWeight.Regular;
            this.Print_bt.Location = new System.Drawing.Point(625, 63);
            this.Print_bt.Name = "Print_bt";
            this.Print_bt.Size = new System.Drawing.Size(110, 48);
            this.Print_bt.TabIndex = 12;
            this.Print_bt.Text = "&Print";
            this.Print_bt.UseSelectable = true;
            this.Print_bt.Click += new System.EventHandler(this.Print_bt_Click);
            // 
            // Bill_cb
            // 
            this.Bill_cb.FormattingEnabled = true;
            this.Bill_cb.Location = new System.Drawing.Point(270, 86);
            this.Bill_cb.Name = "Bill_cb";
            this.Bill_cb.Size = new System.Drawing.Size(121, 21);
            this.Bill_cb.TabIndex = 11;
            this.Bill_cb.Enter += new System.EventHandler(this.Bill_cb_Enter);
            // 
            // Name_cb
            // 
            this.Name_cb.FormattingEnabled = true;
            this.Name_cb.Location = new System.Drawing.Point(23, 86);
            this.Name_cb.Name = "Name_cb";
            this.Name_cb.Size = new System.Drawing.Size(229, 21);
            this.Name_cb.TabIndex = 10;
            this.Name_cb.Enter += new System.EventHandler(this.Name_cb_Enter);
            // 
            // metroLabel1
            // 
            this.metroLabel1.AutoSize = true;
            this.metroLabel1.Location = new System.Drawing.Point(23, 63);
            this.metroLabel1.Name = "metroLabel1";
            this.metroLabel1.Size = new System.Drawing.Size(92, 19);
            this.metroLabel1.TabIndex = 9;
            this.metroLabel1.Text = "Search  Name";
            // 
            // crystalReportViewer1
            // 
            this.crystalReportViewer1.ActiveViewIndex = -1;
            this.crystalReportViewer1.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.crystalReportViewer1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.crystalReportViewer1.Cursor = System.Windows.Forms.Cursors.Default;
            this.crystalReportViewer1.Location = new System.Drawing.Point(20, 151);
            this.crystalReportViewer1.Name = "crystalReportViewer1";
            this.crystalReportViewer1.Size = new System.Drawing.Size(840, 326);
            this.crystalReportViewer1.TabIndex = 8;
            this.crystalReportViewer1.ToolPanelView = CrystalDecisions.Windows.Forms.ToolPanelViewType.None;
            // 
            // SaleBill
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(883, 500);
            this.Controls.Add(this.View_bt);
            this.Controls.Add(this.Export_bt);
            this.Controls.Add(this.metroLabel2);
            this.Controls.Add(this.Print_bt);
            this.Controls.Add(this.Bill_cb);
            this.Controls.Add(this.Name_cb);
            this.Controls.Add(this.metroLabel1);
            this.Controls.Add(this.crystalReportViewer1);
            this.Name = "SaleBill";
            this.Text = "SaleBill";
            this.TopMost = true;
            this.Load += new System.EventHandler(this.SaleBill_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private MetroFramework.Controls.MetroButton View_bt;
        private MetroFramework.Controls.MetroButton Export_bt;
        private MetroFramework.Controls.MetroLabel metroLabel2;
        private MetroFramework.Controls.MetroButton Print_bt;
        private System.Windows.Forms.ComboBox Bill_cb;
        private System.Windows.Forms.ComboBox Name_cb;
        private MetroFramework.Controls.MetroLabel metroLabel1;
        private CrystalDecisions.Windows.Forms.CrystalReportViewer crystalReportViewer1;
    }
}