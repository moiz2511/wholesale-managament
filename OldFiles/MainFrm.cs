using Accounting_Project.Forms;
using Accounting_Project.Reports;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Accounting_Project.Project
{
    public partial class MainFrm : MetroFramework .Forms .MetroForm 
    {
        public MainFrm()
        {
            InitializeComponent();
        }

        private void MainFrm_Load(object sender, EventArgs e)
        {

        }

        private void metroLabel2_Click(object sender, EventArgs e)
        {

        }

        private void Product_tl_Click(object sender, EventArgs e)
        {
            // For Prodcutentry form Show
            Project.ProductEntryFrm f = new ProductEntryFrm();
            f.Show();
        }

        private void Sale_Tl_Click(object sender, EventArgs e)
        {
            SaleFrm sf = new SaleFrm();
            sf.Show();
        }

        private void metroButton1_Click(object sender, EventArgs e)
        {
            //For Context Menu showing and position on master button
            MasterEntry_menu.Show(Master_bt, 0, Master_bt.Height);
        }

        private void toolStripMenuItem1_Click(object sender, EventArgs e)
        {
            PersonFrm f = new PersonFrm();
            f.Show();
        }

        private void toolStripMenuItem2_Click(object sender, EventArgs e)
        {
            ProductEntryFrm p = new ProductEntryFrm();
            p.Show();
        }

        private void SaleRpt_tl_Click(object sender, EventArgs e)
        {
            SaleReport sr = new SaleReport();
            sr.Show();
        }

        private void Purchase_Tl_Click(object sender, EventArgs e)
        {
            PurchaseFrm pf = new PurchaseFrm();
            pf.Show();
        }

        private void PurchaseRpt_tl_Click(object sender, EventArgs e)
        {
            PurchaseDateWiseReport pr = new PurchaseDateWiseReport();
            pr.Show();
        }

        private void Income_tl_Click(object sender, EventArgs e)
        {
            IncomeFrm i=new IncomeFrm ();
            i.Show();

        }

        private void Expense_tl_Click(object sender, EventArgs e)
        {
            Expense s = new Expense();
            s.Show();
        }

        private void metroTile1_Click(object sender, EventArgs e)
        {
            BackupRecoveryFrm b = new BackupRecoveryFrm();
            b.Show();
        }

        private void metroTile2_Click(object sender, EventArgs e)
        {
            PersonFrm f = new PersonFrm();
            f.Show();
        }

        private void Stock_bt_Click(object sender, EventArgs e)
        {
            StockFrm s = new StockFrm();
            s.Show();
        }

        private void Sale_bt_Click(object sender, EventArgs e)
        {
            Sale_menu.Show(Sale_bt, 0, Sale_bt.Height);
        }

        private void toolStripMenuItem3_Click(object sender, EventArgs e)
        {
            //This code will click function ,so there is no need to write again

            Sale_Tl_Click(null, null);
        }

        private void toolStripMenuItem4_Click(object sender, EventArgs e)
        {
            SaleRpt_tl_Click(null, null);
        }

        private void metroTile3_Click(object sender, EventArgs e)
        {
            ProductListReport r = new ProductListReport();
            r.Show();
        }

        private void Purchase_bt_Click(object sender, EventArgs e)
        {
            Purchase_Menu.Show(Purchase_bt, 0, Purchase_bt.Height);
        }

        private void purchaseBillToolStripMenuItem_Click(object sender, EventArgs e)
        {
            PurchaseBill b = new PurchaseBill();
            b.Show();
        }

        private void purchaseReportToolStripMenuItem_Click(object sender, EventArgs e)
        {
            PurchaseDateWiseReport f = new PurchaseDateWiseReport();
            f.Show();
        }

        private void barcodePrintToolStripMenuItem_Click(object sender, EventArgs e)
        {
            BarcodeFrm f = new BarcodeFrm();
            f.Show();
        }
    }
}
