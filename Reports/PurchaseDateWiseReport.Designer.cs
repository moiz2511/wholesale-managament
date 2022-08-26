namespace Accounting_Project.Reports
{
    partial class PurchaseDateWiseReport
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
            this.View_Bt = new System.Windows.Forms.Button();
            this.Print_Bt = new System.Windows.Forms.Button();
            this.Export_Bt = new System.Windows.Forms.Button();
            this.crystalReportViewer1 = new CrystalDecisions.Windows.Forms.CrystalReportViewer();
            this.metroLabel1 = new MetroFramework.Controls.MetroLabel();
            this.metroLabel2 = new MetroFramework.Controls.MetroLabel();
            this.dateTimePicker1 = new System.Windows.Forms.DateTimePicker();
            this.dateTimePicker2 = new System.Windows.Forms.DateTimePicker();
            this.NextPage_Bt = new System.Windows.Forms.Button();
            this.LastPage_bt = new System.Windows.Forms.Button();
            this.PreviousPage_Bt = new System.Windows.Forms.Button();
            this.button1 = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // View_Bt
            // 
            this.View_Bt.Location = new System.Drawing.Point(410, 60);
            this.View_Bt.Name = "View_Bt";
            this.View_Bt.Size = new System.Drawing.Size(95, 56);
            this.View_Bt.TabIndex = 0;
            this.View_Bt.Text = "&View";
            this.View_Bt.UseVisualStyleBackColor = true;
            this.View_Bt.Click += new System.EventHandler(this.View_Bt_Click);
            // 
            // Print_Bt
            // 
            this.Print_Bt.Location = new System.Drawing.Point(511, 60);
            this.Print_Bt.Name = "Print_Bt";
            this.Print_Bt.Size = new System.Drawing.Size(95, 56);
            this.Print_Bt.TabIndex = 1;
            this.Print_Bt.Text = "&Print";
            this.Print_Bt.UseVisualStyleBackColor = true;
            this.Print_Bt.Click += new System.EventHandler(this.Print_Bt_Click);
            // 
            // Export_Bt
            // 
            this.Export_Bt.Location = new System.Drawing.Point(612, 60);
            this.Export_Bt.Name = "Export_Bt";
            this.Export_Bt.Size = new System.Drawing.Size(95, 56);
            this.Export_Bt.TabIndex = 2;
            this.Export_Bt.Text = "&Export";
            this.Export_Bt.UseVisualStyleBackColor = true;
            this.Export_Bt.Click += new System.EventHandler(this.Export_Bt_Click);
            // 
            // crystalReportViewer1
            // 
            this.crystalReportViewer1.ActiveViewIndex = -1;
            this.crystalReportViewer1.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.crystalReportViewer1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.crystalReportViewer1.Cursor = System.Windows.Forms.Cursors.Default;
            this.crystalReportViewer1.Location = new System.Drawing.Point(2, 163);
            this.crystalReportViewer1.Name = "crystalReportViewer1";
            this.crystalReportViewer1.Size = new System.Drawing.Size(732, 293);
            this.crystalReportViewer1.TabIndex = 3;
            this.crystalReportViewer1.ToolPanelView = CrystalDecisions.Windows.Forms.ToolPanelViewType.None;
            // 
            // metroLabel1
            // 
            this.metroLabel1.AutoSize = true;
            this.metroLabel1.Location = new System.Drawing.Point(45, 65);
            this.metroLabel1.Name = "metroLabel1";
            this.metroLabel1.Size = new System.Drawing.Size(76, 19);
            this.metroLabel1.TabIndex = 4;
            this.metroLabel1.Text = "From Date ";
            // 
            // metroLabel2
            // 
            this.metroLabel2.AutoSize = true;
            this.metroLabel2.Location = new System.Drawing.Point(45, 94);
            this.metroLabel2.Name = "metroLabel2";
            this.metroLabel2.Size = new System.Drawing.Size(57, 19);
            this.metroLabel2.TabIndex = 5;
            this.metroLabel2.Text = "To Date ";
            // 
            // dateTimePicker1
            // 
            this.dateTimePicker1.Format = System.Windows.Forms.DateTimePickerFormat.Short;
            this.dateTimePicker1.Location = new System.Drawing.Point(142, 64);
            this.dateTimePicker1.Name = "dateTimePicker1";
            this.dateTimePicker1.Size = new System.Drawing.Size(130, 20);
            this.dateTimePicker1.TabIndex = 6;
            // 
            // dateTimePicker2
            // 
            this.dateTimePicker2.Format = System.Windows.Forms.DateTimePickerFormat.Short;
            this.dateTimePicker2.Location = new System.Drawing.Point(142, 95);
            this.dateTimePicker2.Name = "dateTimePicker2";
            this.dateTimePicker2.Size = new System.Drawing.Size(130, 20);
            this.dateTimePicker2.TabIndex = 7;
            // 
            // NextPage_Bt
            // 
            this.NextPage_Bt.Location = new System.Drawing.Point(154, 134);
            this.NextPage_Bt.Name = "NextPage_Bt";
            this.NextPage_Bt.Size = new System.Drawing.Size(40, 23);
            this.NextPage_Bt.TabIndex = 8;
            this.NextPage_Bt.Text = ">";
            this.NextPage_Bt.UseVisualStyleBackColor = true;
            this.NextPage_Bt.Click += new System.EventHandler(this.NextPage_Bt_Click);
            // 
            // LastPage_bt
            // 
            this.LastPage_bt.Location = new System.Drawing.Point(200, 134);
            this.LastPage_bt.Name = "LastPage_bt";
            this.LastPage_bt.Size = new System.Drawing.Size(40, 23);
            this.LastPage_bt.TabIndex = 9;
            this.LastPage_bt.Text = ">>";
            this.LastPage_bt.UseVisualStyleBackColor = true;
            this.LastPage_bt.Click += new System.EventHandler(this.LastPage_bt_Click);
            // 
            // PreviousPage_Bt
            // 
            this.PreviousPage_Bt.Location = new System.Drawing.Point(108, 134);
            this.PreviousPage_Bt.Name = "PreviousPage_Bt";
            this.PreviousPage_Bt.Size = new System.Drawing.Size(40, 23);
            this.PreviousPage_Bt.TabIndex = 10;
            this.PreviousPage_Bt.Text = "<";
            this.PreviousPage_Bt.UseVisualStyleBackColor = true;
            this.PreviousPage_Bt.Click += new System.EventHandler(this.PreviousPage_Bt_Click);
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(62, 134);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(40, 23);
            this.button1.TabIndex = 11;
            this.button1.Text = "<<";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // PurchaseDateWiseReport
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(735, 456);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.PreviousPage_Bt);
            this.Controls.Add(this.LastPage_bt);
            this.Controls.Add(this.NextPage_Bt);
            this.Controls.Add(this.dateTimePicker2);
            this.Controls.Add(this.dateTimePicker1);
            this.Controls.Add(this.metroLabel2);
            this.Controls.Add(this.metroLabel1);
            this.Controls.Add(this.crystalReportViewer1);
            this.Controls.Add(this.Export_Bt);
            this.Controls.Add(this.Print_Bt);
            this.Controls.Add(this.View_Bt);
            this.Name = "PurchaseDateWiseReport";
            this.ShadowType = MetroFramework.Forms.MetroFormShadowType.AeroShadow;
            this.Text = "Purchase Date Wise Report";
            this.Load += new System.EventHandler(this.PurchaseDateWiseReport_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button View_Bt;
        private System.Windows.Forms.Button Print_Bt;
        private System.Windows.Forms.Button Export_Bt;
        private CrystalDecisions.Windows.Forms.CrystalReportViewer crystalReportViewer1;
        private MetroFramework.Controls.MetroLabel metroLabel1;
        private MetroFramework.Controls.MetroLabel metroLabel2;
        private System.Windows.Forms.DateTimePicker dateTimePicker1;
        private System.Windows.Forms.DateTimePicker dateTimePicker2;
        private System.Windows.Forms.Button NextPage_Bt;
        private System.Windows.Forms.Button LastPage_bt;
        private System.Windows.Forms.Button PreviousPage_Bt;
        private System.Windows.Forms.Button button1;
    }
}