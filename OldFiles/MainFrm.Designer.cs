namespace Accounting_Project.Project
{
    partial class MainFrm
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
            this.components = new System.ComponentModel.Container();
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(MainFrm));
            this.Sale_Tl = new MetroFramework.Controls.MetroTile();
            this.Purchase_Tl = new MetroFramework.Controls.MetroTile();
            this.Income_tl = new MetroFramework.Controls.MetroTile();
            this.Expense_tl = new MetroFramework.Controls.MetroTile();
            this.SaleRpt_tl = new MetroFramework.Controls.MetroTile();
            this.PurchaseRpt_tl = new MetroFramework.Controls.MetroTile();
            this.Login_lb = new MetroFramework.Controls.MetroLabel();
            this.metroLabel2 = new MetroFramework.Controls.MetroLabel();
            this.Product_tl = new MetroFramework.Controls.MetroTile();
            this.metroTile1 = new MetroFramework.Controls.MetroTile();
            this.metroTile2 = new MetroFramework.Controls.MetroTile();
            this.MasterEntry_menu = new MetroFramework.Controls.MetroContextMenu(this.components);
            this.toolStripMenuItem1 = new System.Windows.Forms.ToolStripMenuItem();
            this.toolStripMenuItem2 = new System.Windows.Forms.ToolStripMenuItem();
            this.barcodePrintToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.Master_bt = new MetroFramework.Controls.MetroButton();
            this.Sale_bt = new MetroFramework.Controls.MetroButton();
            this.Sale_menu = new MetroFramework.Controls.MetroContextMenu(this.components);
            this.toolStripMenuItem3 = new System.Windows.Forms.ToolStripMenuItem();
            this.toolStripMenuItem4 = new System.Windows.Forms.ToolStripMenuItem();
            this.Purchase_bt = new MetroFramework.Controls.MetroButton();
            this.Purchase_Menu = new MetroFramework.Controls.MetroContextMenu(this.components);
            this.purchaseNewToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.purchaseReportToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.purchaseDateVendorWiseToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.purchaseDateItemWiseToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.purchaseBillToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.Setting_bt = new MetroFramework.Controls.MetroButton();
            this.Stock_bt = new MetroFramework.Controls.MetroTile();
            this.metroTile3 = new MetroFramework.Controls.MetroTile();
            this.MasterEntry_menu.SuspendLayout();
            this.Sale_menu.SuspendLayout();
            this.Purchase_Menu.SuspendLayout();
            this.SuspendLayout();
            // 
            // Sale_Tl
            // 
            this.Sale_Tl.ActiveControl = null;
            this.Sale_Tl.Location = new System.Drawing.Point(219, 285);
            this.Sale_Tl.Name = "Sale_Tl";
            this.Sale_Tl.Size = new System.Drawing.Size(133, 101);
            this.Sale_Tl.TabIndex = 0;
            this.Sale_Tl.Text = "Sale";
            this.Sale_Tl.TextAlign = System.Drawing.ContentAlignment.BottomCenter;
            this.Sale_Tl.TileImage = ((System.Drawing.Image)(resources.GetObject("Sale_Tl.TileImage")));
            this.Sale_Tl.TileImageAlign = System.Drawing.ContentAlignment.TopCenter;
            this.Sale_Tl.TileTextFontSize = MetroFramework.MetroTileTextSize.Tall;
            this.Sale_Tl.TileTextFontWeight = MetroFramework.MetroTileTextWeight.Regular;
            this.Sale_Tl.UseSelectable = true;
            this.Sale_Tl.UseTileImage = true;
            this.Sale_Tl.Click += new System.EventHandler(this.Sale_Tl_Click);
            // 
            // Purchase_Tl
            // 
            this.Purchase_Tl.ActiveControl = null;
            this.Purchase_Tl.Location = new System.Drawing.Point(370, 285);
            this.Purchase_Tl.Name = "Purchase_Tl";
            this.Purchase_Tl.Size = new System.Drawing.Size(149, 98);
            this.Purchase_Tl.TabIndex = 1;
            this.Purchase_Tl.Text = "Purchase";
            this.Purchase_Tl.TextAlign = System.Drawing.ContentAlignment.BottomCenter;
            this.Purchase_Tl.TileImage = ((System.Drawing.Image)(resources.GetObject("Purchase_Tl.TileImage")));
            this.Purchase_Tl.TileImageAlign = System.Drawing.ContentAlignment.TopCenter;
            this.Purchase_Tl.TileTextFontSize = MetroFramework.MetroTileTextSize.Tall;
            this.Purchase_Tl.TileTextFontWeight = MetroFramework.MetroTileTextWeight.Regular;
            this.Purchase_Tl.UseSelectable = true;
            this.Purchase_Tl.UseTileImage = true;
            this.Purchase_Tl.Click += new System.EventHandler(this.Purchase_Tl_Click);
            // 
            // Income_tl
            // 
            this.Income_tl.ActiveControl = null;
            this.Income_tl.Location = new System.Drawing.Point(535, 285);
            this.Income_tl.Name = "Income_tl";
            this.Income_tl.Size = new System.Drawing.Size(151, 98);
            this.Income_tl.TabIndex = 2;
            this.Income_tl.Text = "Income";
            this.Income_tl.TileTextFontSize = MetroFramework.MetroTileTextSize.Tall;
            this.Income_tl.TileTextFontWeight = MetroFramework.MetroTileTextWeight.Regular;
            this.Income_tl.UseSelectable = true;
            this.Income_tl.Click += new System.EventHandler(this.Income_tl_Click);
            // 
            // Expense_tl
            // 
            this.Expense_tl.ActiveControl = null;
            this.Expense_tl.Location = new System.Drawing.Point(535, 392);
            this.Expense_tl.Name = "Expense_tl";
            this.Expense_tl.Size = new System.Drawing.Size(151, 99);
            this.Expense_tl.TabIndex = 3;
            this.Expense_tl.Text = "Expense";
            this.Expense_tl.TileTextFontSize = MetroFramework.MetroTileTextSize.Tall;
            this.Expense_tl.TileTextFontWeight = MetroFramework.MetroTileTextWeight.Regular;
            this.Expense_tl.UseSelectable = true;
            this.Expense_tl.Click += new System.EventHandler(this.Expense_tl_Click);
            // 
            // SaleRpt_tl
            // 
            this.SaleRpt_tl.ActiveControl = null;
            this.SaleRpt_tl.Location = new System.Drawing.Point(219, 392);
            this.SaleRpt_tl.Name = "SaleRpt_tl";
            this.SaleRpt_tl.Size = new System.Drawing.Size(133, 99);
            this.SaleRpt_tl.TabIndex = 4;
            this.SaleRpt_tl.Text = "Sale Report";
            this.SaleRpt_tl.TextAlign = System.Drawing.ContentAlignment.BottomCenter;
            this.SaleRpt_tl.TileImage = ((System.Drawing.Image)(resources.GetObject("SaleRpt_tl.TileImage")));
            this.SaleRpt_tl.TileImageAlign = System.Drawing.ContentAlignment.TopCenter;
            this.SaleRpt_tl.TileTextFontSize = MetroFramework.MetroTileTextSize.Tall;
            this.SaleRpt_tl.TileTextFontWeight = MetroFramework.MetroTileTextWeight.Regular;
            this.SaleRpt_tl.UseSelectable = true;
            this.SaleRpt_tl.UseTileImage = true;
            this.SaleRpt_tl.Click += new System.EventHandler(this.SaleRpt_tl_Click);
            // 
            // PurchaseRpt_tl
            // 
            this.PurchaseRpt_tl.ActiveControl = null;
            this.PurchaseRpt_tl.Location = new System.Drawing.Point(370, 389);
            this.PurchaseRpt_tl.Name = "PurchaseRpt_tl";
            this.PurchaseRpt_tl.Size = new System.Drawing.Size(149, 102);
            this.PurchaseRpt_tl.TabIndex = 5;
            this.PurchaseRpt_tl.Text = "Purchase Report";
            this.PurchaseRpt_tl.TextAlign = System.Drawing.ContentAlignment.BottomCenter;
            this.PurchaseRpt_tl.TileImage = ((System.Drawing.Image)(resources.GetObject("PurchaseRpt_tl.TileImage")));
            this.PurchaseRpt_tl.TileImageAlign = System.Drawing.ContentAlignment.TopCenter;
            this.PurchaseRpt_tl.TileTextFontSize = MetroFramework.MetroTileTextSize.Tall;
            this.PurchaseRpt_tl.TileTextFontWeight = MetroFramework.MetroTileTextWeight.Regular;
            this.PurchaseRpt_tl.UseSelectable = true;
            this.PurchaseRpt_tl.UseTileImage = true;
            this.PurchaseRpt_tl.Click += new System.EventHandler(this.PurchaseRpt_tl_Click);
            // 
            // Login_lb
            // 
            this.Login_lb.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.Login_lb.AutoSize = true;
            this.Login_lb.FontSize = MetroFramework.MetroLabelSize.Tall;
            this.Login_lb.FontWeight = MetroFramework.MetroLabelWeight.Regular;
            this.Login_lb.Location = new System.Drawing.Point(1043, 23);
            this.Login_lb.Name = "Login_lb";
            this.Login_lb.Size = new System.Drawing.Size(48, 25);
            this.Login_lb.TabIndex = 6;
            this.Login_lb.Text = ".........";
            this.Login_lb.Theme = MetroFramework.MetroThemeStyle.Dark;
            // 
            // metroLabel2
            // 
            this.metroLabel2.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.metroLabel2.AutoSize = true;
            this.metroLabel2.FontSize = MetroFramework.MetroLabelSize.Tall;
            this.metroLabel2.FontWeight = MetroFramework.MetroLabelWeight.Regular;
            this.metroLabel2.Location = new System.Drawing.Point(966, 23);
            this.metroLabel2.Name = "metroLabel2";
            this.metroLabel2.Size = new System.Drawing.Size(71, 25);
            this.metroLabel2.TabIndex = 7;
            this.metroLabel2.Text = "Log In :";
            this.metroLabel2.Theme = MetroFramework.MetroThemeStyle.Dark;
            this.metroLabel2.Click += new System.EventHandler(this.metroLabel2_Click);
            // 
            // Product_tl
            // 
            this.Product_tl.ActiveControl = null;
            this.Product_tl.Location = new System.Drawing.Point(807, 198);
            this.Product_tl.Name = "Product_tl";
            this.Product_tl.Size = new System.Drawing.Size(175, 63);
            this.Product_tl.TabIndex = 8;
            this.Product_tl.Text = "Product Entry";
            this.Product_tl.Theme = MetroFramework.MetroThemeStyle.Dark;
            this.Product_tl.TileTextFontSize = MetroFramework.MetroTileTextSize.Tall;
            this.Product_tl.TileTextFontWeight = MetroFramework.MetroTileTextWeight.Regular;
            this.Product_tl.UseSelectable = true;
            this.Product_tl.Click += new System.EventHandler(this.Product_tl_Click);
            // 
            // metroTile1
            // 
            this.metroTile1.ActiveControl = null;
            this.metroTile1.Location = new System.Drawing.Point(807, 287);
            this.metroTile1.Name = "metroTile1";
            this.metroTile1.Size = new System.Drawing.Size(175, 68);
            this.metroTile1.TabIndex = 9;
            this.metroTile1.Text = "Backup Recovery";
            this.metroTile1.TileTextFontSize = MetroFramework.MetroTileTextSize.Tall;
            this.metroTile1.TileTextFontWeight = MetroFramework.MetroTileTextWeight.Regular;
            this.metroTile1.UseSelectable = true;
            this.metroTile1.Click += new System.EventHandler(this.metroTile1_Click);
            // 
            // metroTile2
            // 
            this.metroTile2.ActiveControl = null;
            this.metroTile2.Location = new System.Drawing.Point(39, 287);
            this.metroTile2.Name = "metroTile2";
            this.metroTile2.Size = new System.Drawing.Size(159, 204);
            this.metroTile2.TabIndex = 10;
            this.metroTile2.Text = "Person Detail";
            this.metroTile2.TileImage = ((System.Drawing.Image)(resources.GetObject("metroTile2.TileImage")));
            this.metroTile2.TileImageAlign = System.Drawing.ContentAlignment.MiddleCenter;
            this.metroTile2.TileTextFontSize = MetroFramework.MetroTileTextSize.Tall;
            this.metroTile2.TileTextFontWeight = MetroFramework.MetroTileTextWeight.Regular;
            this.metroTile2.UseSelectable = true;
            this.metroTile2.UseTileImage = true;
            this.metroTile2.Click += new System.EventHandler(this.metroTile2_Click);
            // 
            // MasterEntry_menu
            // 
            this.MasterEntry_menu.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.toolStripMenuItem1,
            this.toolStripMenuItem2,
            this.barcodePrintToolStripMenuItem});
            this.MasterEntry_menu.Name = "metroContextMenu1";
            this.MasterEntry_menu.Size = new System.Drawing.Size(147, 70);
            this.MasterEntry_menu.Text = "Master Entry";
            this.MasterEntry_menu.Theme = MetroFramework.MetroThemeStyle.Dark;
            // 
            // toolStripMenuItem1
            // 
            this.toolStripMenuItem1.Name = "toolStripMenuItem1";
            this.toolStripMenuItem1.Size = new System.Drawing.Size(146, 22);
            this.toolStripMenuItem1.Text = "Person Detail";
            this.toolStripMenuItem1.Click += new System.EventHandler(this.toolStripMenuItem1_Click);
            // 
            // toolStripMenuItem2
            // 
            this.toolStripMenuItem2.Name = "toolStripMenuItem2";
            this.toolStripMenuItem2.Size = new System.Drawing.Size(146, 22);
            this.toolStripMenuItem2.Text = "Product Entry";
            this.toolStripMenuItem2.Click += new System.EventHandler(this.toolStripMenuItem2_Click);
            // 
            // barcodePrintToolStripMenuItem
            // 
            this.barcodePrintToolStripMenuItem.Name = "barcodePrintToolStripMenuItem";
            this.barcodePrintToolStripMenuItem.Size = new System.Drawing.Size(146, 22);
            this.barcodePrintToolStripMenuItem.Text = "Barcode Print";
            this.barcodePrintToolStripMenuItem.Click += new System.EventHandler(this.barcodePrintToolStripMenuItem_Click);
            // 
            // Master_bt
            // 
            this.Master_bt.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("Master_bt.BackgroundImage")));
            this.Master_bt.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Center;
            this.Master_bt.ContextMenuStrip = this.MasterEntry_menu;
            this.Master_bt.FontSize = MetroFramework.MetroButtonSize.Tall;
            this.Master_bt.FontWeight = MetroFramework.MetroButtonWeight.Regular;
            this.Master_bt.Location = new System.Drawing.Point(49, 64);
            this.Master_bt.Name = "Master_bt";
            this.Master_bt.Size = new System.Drawing.Size(133, 95);
            this.Master_bt.TabIndex = 12;
            this.Master_bt.Text = "Master Entry";
            this.Master_bt.TextAlign = System.Drawing.ContentAlignment.BottomCenter;
            this.Master_bt.Theme = MetroFramework.MetroThemeStyle.Dark;
            this.Master_bt.UseSelectable = true;
            this.Master_bt.Click += new System.EventHandler(this.metroButton1_Click);
            // 
            // Sale_bt
            // 
            this.Sale_bt.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("Sale_bt.BackgroundImage")));
            this.Sale_bt.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Center;
            this.Sale_bt.ContextMenuStrip = this.Sale_menu;
            this.Sale_bt.FontSize = MetroFramework.MetroButtonSize.Tall;
            this.Sale_bt.FontWeight = MetroFramework.MetroButtonWeight.Regular;
            this.Sale_bt.Location = new System.Drawing.Point(186, 64);
            this.Sale_bt.Name = "Sale_bt";
            this.Sale_bt.Size = new System.Drawing.Size(133, 95);
            this.Sale_bt.TabIndex = 13;
            this.Sale_bt.Text = "Sale";
            this.Sale_bt.TextAlign = System.Drawing.ContentAlignment.BottomCenter;
            this.Sale_bt.Theme = MetroFramework.MetroThemeStyle.Dark;
            this.Sale_bt.UseSelectable = true;
            this.Sale_bt.Click += new System.EventHandler(this.Sale_bt_Click);
            // 
            // Sale_menu
            // 
            this.Sale_menu.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.toolStripMenuItem3,
            this.toolStripMenuItem4});
            this.Sale_menu.Name = "Sale_menu";
            this.Sale_menu.Size = new System.Drawing.Size(137, 48);
            this.Sale_menu.Text = "Sale";
            // 
            // toolStripMenuItem3
            // 
            this.toolStripMenuItem3.Name = "toolStripMenuItem3";
            this.toolStripMenuItem3.Size = new System.Drawing.Size(136, 22);
            this.toolStripMenuItem3.Text = "Sale Invoice";
            this.toolStripMenuItem3.Click += new System.EventHandler(this.toolStripMenuItem3_Click);
            // 
            // toolStripMenuItem4
            // 
            this.toolStripMenuItem4.Name = "toolStripMenuItem4";
            this.toolStripMenuItem4.Size = new System.Drawing.Size(136, 22);
            this.toolStripMenuItem4.Text = "Sale Report";
            this.toolStripMenuItem4.Click += new System.EventHandler(this.toolStripMenuItem4_Click);
            // 
            // Purchase_bt
            // 
            this.Purchase_bt.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("Purchase_bt.BackgroundImage")));
            this.Purchase_bt.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Center;
            this.Purchase_bt.ContextMenuStrip = this.Purchase_Menu;
            this.Purchase_bt.FontSize = MetroFramework.MetroButtonSize.Tall;
            this.Purchase_bt.FontWeight = MetroFramework.MetroButtonWeight.Regular;
            this.Purchase_bt.Location = new System.Drawing.Point(327, 64);
            this.Purchase_bt.Name = "Purchase_bt";
            this.Purchase_bt.Size = new System.Drawing.Size(133, 95);
            this.Purchase_bt.TabIndex = 14;
            this.Purchase_bt.Text = "Purchase";
            this.Purchase_bt.TextAlign = System.Drawing.ContentAlignment.BottomCenter;
            this.Purchase_bt.Theme = MetroFramework.MetroThemeStyle.Dark;
            this.Purchase_bt.UseSelectable = true;
            this.Purchase_bt.Click += new System.EventHandler(this.Purchase_bt_Click);
            // 
            // Purchase_Menu
            // 
            this.Purchase_Menu.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.purchaseNewToolStripMenuItem,
            this.purchaseReportToolStripMenuItem,
            this.purchaseDateVendorWiseToolStripMenuItem,
            this.purchaseDateItemWiseToolStripMenuItem,
            this.purchaseBillToolStripMenuItem});
            this.Purchase_Menu.Name = "Purchase_Menu";
            this.Purchase_Menu.Size = new System.Drawing.Size(218, 114);
            // 
            // purchaseNewToolStripMenuItem
            // 
            this.purchaseNewToolStripMenuItem.Name = "purchaseNewToolStripMenuItem";
            this.purchaseNewToolStripMenuItem.Size = new System.Drawing.Size(217, 22);
            this.purchaseNewToolStripMenuItem.Text = "Purchase New";
            // 
            // purchaseReportToolStripMenuItem
            // 
            this.purchaseReportToolStripMenuItem.Name = "purchaseReportToolStripMenuItem";
            this.purchaseReportToolStripMenuItem.Size = new System.Drawing.Size(217, 22);
            this.purchaseReportToolStripMenuItem.Text = "Purchase Date Wise Report";
            this.purchaseReportToolStripMenuItem.Click += new System.EventHandler(this.purchaseReportToolStripMenuItem_Click);
            // 
            // purchaseDateVendorWiseToolStripMenuItem
            // 
            this.purchaseDateVendorWiseToolStripMenuItem.Name = "purchaseDateVendorWiseToolStripMenuItem";
            this.purchaseDateVendorWiseToolStripMenuItem.Size = new System.Drawing.Size(217, 22);
            this.purchaseDateVendorWiseToolStripMenuItem.Text = "Purchase Date Vendor Wise";
            // 
            // purchaseDateItemWiseToolStripMenuItem
            // 
            this.purchaseDateItemWiseToolStripMenuItem.Name = "purchaseDateItemWiseToolStripMenuItem";
            this.purchaseDateItemWiseToolStripMenuItem.Size = new System.Drawing.Size(217, 22);
            this.purchaseDateItemWiseToolStripMenuItem.Text = "Purchase Date Item Wise";
            // 
            // purchaseBillToolStripMenuItem
            // 
            this.purchaseBillToolStripMenuItem.Name = "purchaseBillToolStripMenuItem";
            this.purchaseBillToolStripMenuItem.Size = new System.Drawing.Size(217, 22);
            this.purchaseBillToolStripMenuItem.Text = "Purchase Bill";
            this.purchaseBillToolStripMenuItem.Click += new System.EventHandler(this.purchaseBillToolStripMenuItem_Click);
            // 
            // Setting_bt
            // 
            this.Setting_bt.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("Setting_bt.BackgroundImage")));
            this.Setting_bt.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Center;
            this.Setting_bt.ContextMenuStrip = this.MasterEntry_menu;
            this.Setting_bt.FontSize = MetroFramework.MetroButtonSize.Tall;
            this.Setting_bt.FontWeight = MetroFramework.MetroButtonWeight.Regular;
            this.Setting_bt.Location = new System.Drawing.Point(466, 64);
            this.Setting_bt.Name = "Setting_bt";
            this.Setting_bt.Size = new System.Drawing.Size(133, 95);
            this.Setting_bt.TabIndex = 15;
            this.Setting_bt.Text = "Setting";
            this.Setting_bt.TextAlign = System.Drawing.ContentAlignment.BottomCenter;
            this.Setting_bt.Theme = MetroFramework.MetroThemeStyle.Dark;
            this.Setting_bt.UseSelectable = true;
            // 
            // Stock_bt
            // 
            this.Stock_bt.ActiveControl = null;
            this.Stock_bt.Location = new System.Drawing.Point(807, 465);
            this.Stock_bt.Name = "Stock_bt";
            this.Stock_bt.Size = new System.Drawing.Size(175, 65);
            this.Stock_bt.TabIndex = 16;
            this.Stock_bt.Text = "Stock";
            this.Stock_bt.TileTextFontSize = MetroFramework.MetroTileTextSize.Tall;
            this.Stock_bt.TileTextFontWeight = MetroFramework.MetroTileTextWeight.Regular;
            this.Stock_bt.UseSelectable = true;
            this.Stock_bt.Click += new System.EventHandler(this.Stock_bt_Click);
            // 
            // metroTile3
            // 
            this.metroTile3.ActiveControl = null;
            this.metroTile3.Location = new System.Drawing.Point(807, 109);
            this.metroTile3.Name = "metroTile3";
            this.metroTile3.Size = new System.Drawing.Size(175, 70);
            this.metroTile3.TabIndex = 17;
            this.metroTile3.Text = "Product List Report";
            this.metroTile3.TileTextFontSize = MetroFramework.MetroTileTextSize.Tall;
            this.metroTile3.TileTextFontWeight = MetroFramework.MetroTileTextWeight.Regular;
            this.metroTile3.UseSelectable = true;
            this.metroTile3.Click += new System.EventHandler(this.metroTile3_Click);
            // 
            // MainFrm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1114, 594);
            this.Controls.Add(this.metroTile3);
            this.Controls.Add(this.Stock_bt);
            this.Controls.Add(this.Setting_bt);
            this.Controls.Add(this.Purchase_bt);
            this.Controls.Add(this.Sale_bt);
            this.Controls.Add(this.Master_bt);
            this.Controls.Add(this.metroTile2);
            this.Controls.Add(this.metroTile1);
            this.Controls.Add(this.Product_tl);
            this.Controls.Add(this.metroLabel2);
            this.Controls.Add(this.Login_lb);
            this.Controls.Add(this.PurchaseRpt_tl);
            this.Controls.Add(this.SaleRpt_tl);
            this.Controls.Add(this.Expense_tl);
            this.Controls.Add(this.Income_tl);
            this.Controls.Add(this.Purchase_Tl);
            this.Controls.Add(this.Sale_Tl);
            this.Name = "MainFrm";
            this.ShadowType = MetroFramework.Forms.MetroFormShadowType.AeroShadow;
            this.Text = "Accounting Project";
            this.Theme = MetroFramework.MetroThemeStyle.Dark;
            this.WindowState = System.Windows.Forms.FormWindowState.Maximized;
            this.Load += new System.EventHandler(this.MainFrm_Load);
            this.MasterEntry_menu.ResumeLayout(false);
            this.Sale_menu.ResumeLayout(false);
            this.Purchase_Menu.ResumeLayout(false);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private MetroFramework.Controls.MetroTile Sale_Tl;
        private MetroFramework.Controls.MetroTile Purchase_Tl;
        private MetroFramework.Controls.MetroTile Income_tl;
        private MetroFramework.Controls.MetroTile Expense_tl;
        private MetroFramework.Controls.MetroTile SaleRpt_tl;
        private MetroFramework.Controls.MetroTile PurchaseRpt_tl;
        private MetroFramework.Controls.MetroLabel metroLabel2;
        public MetroFramework.Controls.MetroLabel Login_lb;
        private MetroFramework.Controls.MetroTile Product_tl;
        private MetroFramework.Controls.MetroTile metroTile1;
        private MetroFramework.Controls.MetroTile metroTile2;
        private MetroFramework.Controls.MetroContextMenu MasterEntry_menu;
        private System.Windows.Forms.ToolStripMenuItem toolStripMenuItem1;
        private System.Windows.Forms.ToolStripMenuItem toolStripMenuItem2;
        private MetroFramework.Controls.MetroButton Master_bt;
        private MetroFramework.Controls.MetroButton Sale_bt;
        private MetroFramework.Controls.MetroButton Purchase_bt;
        private MetroFramework.Controls.MetroButton Setting_bt;
        private MetroFramework.Controls.MetroTile Stock_bt;
        private MetroFramework.Controls.MetroContextMenu Sale_menu;
        private System.Windows.Forms.ToolStripMenuItem toolStripMenuItem3;
        private System.Windows.Forms.ToolStripMenuItem toolStripMenuItem4;
        private MetroFramework.Controls.MetroTile metroTile3;
        private MetroFramework.Controls.MetroContextMenu Purchase_Menu;
        private System.Windows.Forms.ToolStripMenuItem purchaseNewToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem purchaseReportToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem purchaseDateVendorWiseToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem purchaseDateItemWiseToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem purchaseBillToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem barcodePrintToolStripMenuItem;
    }
}