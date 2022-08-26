using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;

using System.Windows.Forms;



using System.Data.SqlClient;

using System.Configuration;

using Maharashtra;
using Accounting_Project.Forms;
using Accounting_Project.Reports;
using Accounting_Project.Project;




namespace Maharashtra
{
    public partial class FormMain : MetroFramework.Forms.MetroForm
    {
        SqlConnection cn = new SqlConnection(ConfigurationManager.AppSettings["conn"]);
        //SqlConnection cn = new SqlConnection(@"Provider=Microsoft.ACE.Sql.12.0;Jet Sql:Database Password=73057305;Data Source=d:\Oceandb\Ocean.accdb");
        public FormMain()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void personDetailsToolStripMenuItem_Click(object sender, EventArgs e)
        {


        }

        private void itemsDetailsToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }

        private void saleToolStripMenuItem1_Click(object sender, EventArgs e)
        {
            //   Fruit .SalePattiFrm f = new  Fruit.SalePattiFrm ();
            ////   f.MdiParent = this;
            //   f.Show();
        }

        private void returnItemsToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }

        private void purchaseToolStripMenuItem1_Click(object sender, EventArgs e)
        {
            //Fruit .PurchasePattiFrm  f = new  Fruit.PurchasePattiFrm ();
            //   f.MdiParent = this;
            //f.Show();
        }

        private void passwordToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }

        private void customerDepositToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }

        private void dealerDepositToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }

        private void bllToolStripMenuItem_Click(object sender, EventArgs e)
        {
            SaleBill f = new SaleBill();
            f.Show();
        }

        private void statementToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }

        private void returnToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }

        private void depositReportToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }
        public void login1()
        {
            FormMain obj = new FormMain();
            try
            {

                SqlDataAdapter da = new SqlDataAdapter("select * from PWD where [PwdKey]='009 665 0859 64' ", cn);
                DataSet ds = new DataSet();

                da.Fill(ds);


                if (ds.Tables[0].Rows.Count > 0)
                {


                    this.Hide();
                    this.Close();


                }
                else
                {

                    //   MessageBox.Show("ID or Password incorrect !", "Error", MessageBoxButtons.OK, MessageBoxIcon.Stop);
                    //  textBox1.Text = "";
                    //  maskedTextBox1.Text = "";

                }
            }
            catch (Exception m)
            {
                MessageBox.Show(m.Message);
                this.Hide();
            }
        }


        void check()
        {
            try
            {
                string folderpath, filepath;
                //folderpath = @"c:\ProgramData";
                folderpath = @"ProgramData";

                // filepath = @"c:\ProgramData\Purchase.bat";
                filepath = @"ProgramData\Ocean11.bat";


                System.IO.DirectoryInfo d2 = new System.IO.DirectoryInfo(folderpath);
                if (!d2.Exists)
                {
                    d2.Create();
                }

                System.IO.FileInfo f = new System.IO.FileInfo(filepath);

                if (!f.Exists)
                {
                    f.Create();
                }
                else
                {
                    //System.IO.BinaryWriter bw;
                    //System.IO.BinaryReader br;
                    //string view;

                    //bw = new System.IO.BinaryWriter(new System.IO.FileStream(filepath, System.IO.FileMode.Create));
                    ////  bw.Write(DateTime .Now .ToShortDateString ());
                    //Purchase_Key.Encode en = new Purchase_Key.Encode();
                    //en.Encodes(attemptsToolStripMenuItem.Text);
                    //str = en.ret;
                    //bw.Write(str);
                    //bw.Close();


                    //br = new System.IO.BinaryReader(new System.IO.FileStream(filepath, System.IO.FileMode.Open));
                    //view = (br.ReadString()).ToString();
                    //Purchase_Key.Decode d = new Purchase_Key.Decode();
                    //d.Decodes(view);
                    //getpwd = d.ret;
                    //str = d.ret;
                    //br.Close();


                }
            }
            catch (Exception ex)
            {
                //MessageBox .Show ("Error" + ex.ToString());
            }

        }

        string str, getpwd;


        void dateFormat()
        {
            //string  dt;

            //dt = dateTimePicker1.Value.Date.ToString("dd-MMM-yy");
            //string datestr = maskedTextBox1.Text.ToString();
            //datestr = dt;
            //if (dt != datestr)
            //{
            //    MessageBox.Show("Change the Date Format to Eg:( 10-Jan-11) or (dd-MMM-yy)");
            //}
        }
        // public string ver;
        //#region load
        private void FormMain_Load(object sender, EventArgs e)
        {
            //  mVersion_lb.Text = ver;


            this.WindowState = FormWindowState.Maximized;
            dateFormat();


            //// MessageBox.Show(str + "");
            //if (valueToolStripMenuItem.Text == "0")
            //{
            //    reportsToolStripMenuItem.Enabled = false;
            //    settingToolStripMenuItem.Enabled = false;
            //    reportsToolStripMenuItem.Enabled = false;
            //    moneyToolStripMenuItem.Visible = false;
            //    pToolStripMenuItem.Enabled = false;
            //    stockToolStripMenuItem.Enabled = false;
            //    returnItemsToolStripMenuItem.Enabled = false;
            //    creditToolStripMenuItem.Enabled = false;
            //    debitToolStripMenuItem.Enabled = false;

            //    cancelPurchaseToolStripMenuItem.Enabled = false;
            //    cancelSaleBillToolStripMenuItem.Enabled = false;
            //    returnToolStripMenuItem.Enabled = false;

            //    retutnItemsToolStripMenuItem.Visible = false;
            //    debitToolStripMenuItem.Visible = false;
            //    dealerDepositToolStripMenuItem.Visible = false;

            //    customerDepositToolStripMenuItem.Enabled = false;
            //}
            // else
            {
                if (userToolStripMenuItem.Text == "Admin")
                { }
                else
                {
                    if (userToolStripMenuItem.Text != "Admin")
                    {
                        //balanceBakhiToolStripMenuItem.Visible = false;
                        //farmerJamaToolStripMenuItem.Visible = false;
                        ////depositBillToolStripMenuItem.Visible = false;
                        //reportsToolStripMenuItem.Visible = false;
                        settingToolStripMenuItem.Visible = false;
                        //reportsToolStripMenuItem.Visible = false;
                        ////moneyToolStripMenuItem.Visible = false;

                        //returnItemsToolStripMenuItem.Visible = false;
                        //creditToolStripMenuItem.Visible = false;
                        //debitToolStripMenuItem.Visible = false;

                        //cancelPurchaseToolStripMenuItem.Visible = false;
                        //cancelSaleBillToolStripMenuItem.Visible = false;
                        //returnToolStripMenuItem.Visible = false;

                        ////retutnItemsToolStripMenuItem.Visible = false;
                        //debitToolStripMenuItem.Visible = false;
                        //dealerDepositToolStripMenuItem.Visible = false;

                        //customerDepositToolStripMenuItem.Visible = false;
                    }
                }
            }
            {
                //FormCrysatal f = new FormCrysatal();
                //f.MdiParent = this;
                //f.Show();          
            }
        }

        //#endregion
        private void formateTablesToolStripMenuItem_Click(object sender, EventArgs e)
        {
        }

        private void retutnItemsToolStripMenuItem_Click(object sender, EventArgs e)
        {
            PurchaseBill b = new PurchaseBill();
            b.Show();

        }

        private void stockReportToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }

        private void incomeToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }

        private void expenseToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }

        private void aboutToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }

        private void incomeToolStripMenuItem1_Click(object sender, EventArgs e)
        {

        }

        private void expenseToolStripMenuItem1_Click(object sender, EventArgs e)
        {

        }

        private void incomeExpenseToolStripMenuItem_Click(object sender, EventArgs e)
        {


        }

        private void creditToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }

        private void moneyToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }

        private void debitToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }

        private void depositBillToolStripMenuItem_Click(object sender, EventArgs e)
        {


        }

        private void cancelSaleBillToolStripMenuItem_Click(object sender, EventArgs e)
        {


        }

        private void saleInvoiceToolStripMenuItem_Click(object sender, EventArgs e)
        {


        }

        private void cancelPurchaseToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }

        private void aboutUsToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }

        private void bakupAndRecoveryToolStripMenuItem_Click(object sender, EventArgs e)
        {


        }

        private void purchaseToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }

        private void logOutToolStripMenuItem_Click(object sender, EventArgs e)
        {



        }

        private void userToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }

        private void updateSaleToolStripMenuItem_Click(object sender, EventArgs e)
        {


        }

        private void settingToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }

        private void purchaseKeyToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }

        private void purchaseKeyToolStripMenuItem1_Click(object sender, EventArgs e)
        {

        }

        private void pToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }

        private void purchaseKeyToolStripMenuItem_Click_1(object sender, EventArgs e)
        {

        }

        private void itemsReportToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }

        private void stockEntryToolStripMenuItem_Click(object sender, EventArgs e)
        {



        }

        private void itemsNameUpdateToolStripMenuItem_Click(object sender, EventArgs e)
        {
            ProductEntryFrm f = new ProductEntryFrm();

            f.Show();


        }

        private void FormMain_FormClosing(object sender, FormClosingEventArgs e)
        {
            //Formlogin  f = new  Formlogin ();
            //f.MdiParent = this;
            //f.Show();
            //this.Hide();
            Application.Exit();
        }

        private void calculatorToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }

        private void notepadToolStripMenuItem_Click(object sender, EventArgs e)
        {


        }

        private void headingToolStripMenuItem_Click(object sender, EventArgs e)
        {
            //   Project .Heading  f = new  Project.Heading ();
            ////   f.MdiParent = this;
            //   f.Show();
        }

        private void notepadToolStripMenuItem1_Click(object sender, EventArgs e)
        {
            System.Diagnostics.Process.Start("Notepad.exe");
        }

        private void calculatorToolStripMenuItem1_Click(object sender, EventArgs e)
        {
            System.Diagnostics.Process.Start("Calc.exe");
        }

        private void purchaseUpdateToolStripMenuItem_Click(object sender, EventArgs e)
        {
            //FormPurchaseUpdate   f = new  FormPurchaseUpdate  ();
            //   f.MdiParent = this;
            //f.Show();
        }

        private void taxToolStripMenuItem_Click(object sender, EventArgs e)
        {
            //FormTax f = new FormTax();
            //   f.MdiParent = this;
            //f.Show();
        }

        private void stockEnteryToolStripMenuItem_Click(object sender, EventArgs e)
        {
            //FormStockEntry f = new FormStockEntry();
            //   f.MdiParent = this;
            //f.Show();
        }

        private void stockDeleteToolStripMenuItem_Click(object sender, EventArgs e)
        {
            //FormStockDelete f = new FormStockDelete();
            // f.MdiParent = this;
            //f.Show();
        }

        private void aboutProjectToolStripMenuItem_Click(object sender, EventArgs e)
        {
            //AboutBoxpro  f = new AboutBoxpro();
            //   f.MdiParent = this;
            //f.Show();
        }

        private void saleToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }

        private void closeAllFormToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }

        private void comissionToolStripMenuItem_Click(object sender, EventArgs e)
        {
            PurchaseBill f = new PurchaseBill();
            // f.MdiParent = this;
            f.Show();
        }

        private void incomeExpenseToolStripMenuItem1_Click(object sender, EventArgs e)
        {
            IncomeFrm inc = new IncomeFrm();
            inc.Show();
        }

        private void salePatti2ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            //Fruit.SalePattiByFarmer  f = new Fruit.SalePattiByFarmer ();
            //f.MdiParent = this;
            //f.Show();
        }

        private void farmerToolStripMenuItem_Click(object sender, EventArgs e)
        {
            //CustomerDetails_Frm  f = new  CustomerDetails_Frm ();
            //f.MdiParent = this;
            //f.Show();
        }

        private void salePurchaseToolStripMenuItem_Click(object sender, EventArgs e)
        {
            //FormSalePurchase  f = new  FormSalePurchase ();
            //    f.MdiParent = this;
            //f.Show();
        }

        private void companyToolStripMenuItem_Click(object sender, EventArgs e)
        {
            //FrmAccount  f = new  FrmAccount ();
            //   f.MdiParent = this;
            //f.Show();
        }

        private void farmerBhusarToolStripMenuItem_Click(object sender, EventArgs e)
        {
            //FarKVKCKCmerBill_frm f = new  FarmerBill_frm ();
            //    f.MdiParent = this;
            //f.Show();
        }

        private void salePattiToolStripMenuItem_Click(object sender, EventArgs e)
        {
            SaleFrm f = new SaleFrm();
            f.Show();
        }

        private void customerToolStripMenuItem_Click(object sender, EventArgs e)
        {
            //FormCredit f = new FormCredit();
            //f.MdiParent = this;
            //f.Show();
        }

        private void customerJamaToolStripMenuItem_Click(object sender, EventArgs e)
        {
            CustomerDeposit d = new CustomerDeposit();
            d.Show();
        }

        private void farmerToolStripMenuItem1_Click(object sender, EventArgs e)
        {
            //FormDebit f = new FormDebit();
            //f.MdiParent = this;
            //f.Show();
        }

        private void farmerJamaToolStripMenuItem_Click(object sender, EventArgs e)
        {
            //FarmerDeposit_Frm f = new FarmerDeposit_Frm();
            //    f.MdiParent = this;
            //f.Show();
        }

        private void salePatti2ToolStripMenuItem1_Click(object sender, EventArgs e)
        {

            //SalePatti_2  f = new   SalePatti_2  ();
            //     f.MdiParent = this;
            //f.userType = userToolStripMenuItem.Text;
            //f.Show();
        }

        private void profitReportToolStripMenuItem_Click(object sender, EventArgs e)
        {
            //SaleProfit_Frm f = new SaleProfit_Frm();

            //f.Show();
        }

        private void ixLllkkToolStripMenuItem_Click(object sender, EventArgs e)
        {
            //CustomerBalance f = new  CustomerBalance ();
            //    f.MdiParent = this;
            //f.Show();
        }

        private void pRINTToolStripMenuItem_Click(object sender, EventArgs e)
        {
            //SaleMultiPrint f = new SaleMultiPrint();
            //   f.MdiParent = this;
            //f.Show();
        }

        private void printMultipleBillToolStripMenuItem_Click(object sender, EventArgs e)
        {
            //SaleMultiPrint f = new SaleMultiPrint();
            //  f.MdiParent = this;
            //f.Show();
        }

        private void rokadToolStripMenuItem_Click(object sender, EventArgs e)
        {
            //FormIncomeExpense  f = new  FormIncomeExpense ();
            //   f.MdiParent = this;
            //f.Show();
        }

        private void balanceReportToolStripMenuItem_Click(object sender, EventArgs e)
        {
            //BalanceFrm2 f = new BalanceFrm2();
            ////f.MdiParent = this;
            //f.Show();
        }

        private void button1_Click_1(object sender, EventArgs e)
        {
            //FormTax f = new FormTax();
            // f.MdiParent = this;
            //f.Show();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //FormItemsUpdate f = new FormItemsUpdate();
            //  f.MdiParent = this;
            //f.Show();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //Fruits.Fruits.Comission_Fm f = new Fruits.Fruits.Comission_Fm();
            // f.MdiParent = this;
            //f.userType = userToolStripMenuItem.Text;
            //f.Show();

        }

        private void button4_Click(object sender, EventArgs e)
        {
            //Fruit.SalePattiByFarmer f = new Fruit.SalePattiByFarmer();
            // f.MdiParent = this;
            //f.Show();
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //SalePatti_2 f = new SalePatti_2();
            //  f.MdiParent = this;
            //f.userType = userToolStripMenuItem.Text;
            //f.Show();
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //CustomerDeposit_Frm f = new CustomerDeposit_Frm();
            // f.MdiParent = this;
            //f.Show();
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //FarmerDeposit_Frm f = new FarmerDeposit_Frm();
            //  f.MdiParent = this;
            //f.Show();
        }

        private void button8_Click(object sender, EventArgs e)
        {
            //SRB.RokadJama f = new SRB.RokadJama();
            //  f.MdiParent = this;
            //f.Show();
        }

        private void checkBox1_CheckedChanged(object sender, EventArgs e)
        {


        }

        private void button10_Click(object sender, EventArgs e)
        {
            //FormBill f = new FormBill();
            // f.MdiParent = this;
            //f.Show();
        }

        private void button12_Click(object sender, EventArgs e)
        {
            //FormDepositBill f = new FormDepositBill();
            // f.MdiParent = this;
            //f.Show();
        }

        private void button14_Click(object sender, EventArgs e)
        {
            //FormDeposit_ f = new FormDeposit_();
            //  f.MdiParent = this;
            //f.Show();
        }

        private void button16_Click(object sender, EventArgs e)
        {
            //FarmerBill_frm f = new FarmerBill_frm();
            //   f.MdiParent = this;
            //f.Show();
        }

        private void button15_Click(object sender, EventArgs e)
        {
            //Balaance_Report f = new Balaance_Report();
            //f.MdiParent = this;
            //f.Show();
        }

        private void button13_Click(object sender, EventArgs e)
        {
            //FormSalePurchase f = new FormSalePurchase();
            //f.MdiParent = this;
            //f.Show();
        }

        private void button11_Click(object sender, EventArgs e)
        {
            //ComissionBill f = new ComissionBill();
            // f.MdiParent = this;
            //f.Show();
        }

        private void button9_Click(object sender, EventArgs e)
        {
            //   BalanceFrm f = new BalanceFrm();
            ////   f.MdiParent = this;
            //   f.Show();
        }

        private void checkBox2_CheckedChanged(object sender, EventArgs e)
        {


        }

        private void toolStripMenuItem1_Click(object sender, EventArgs e)
        {

        }

        private void ExchangeBill_bt_Click(object sender, EventArgs e)
        {
            //Fruits.Fruits.Comission_Fm f = new Fruits.Fruits.Comission_Fm();
            //  f.MdiParent = this;
            //f.userType = userToolStripMenuItem.Text;
            //f.Show();
        }

        private void SaleBill_bt_Click(object sender, EventArgs e)
        {
            //SalePatti_2 f = new SalePatti_2();
            //     f.MdiParent = this;
            //f.userType = userToolStripMenuItem.Text;
            //f.Show();
        }

        private void CancelSale_bt_Click(object sender, EventArgs e)
        {
            //FarmerDetails_fm f = new FarmerDetails_fm();
            //   f.MdiParent = this;
            //f.Show();
        }

        private void UpdateSale_bt_Click(object sender, EventArgs e)
        {
            //CustomerDetails_Frm f = new CustomerDetails_Frm();
            //  f.MdiParent = this;
            //f.Show();
        }

        private void PrintSale_bt_Click(object sender, EventArgs e)
        {
            //SaleMultiPrint f = new SaleMultiPrint();
            //  f.MdiParent = this;
            //f.Show();
        }

        private void PrintExchange_bt_Click(object sender, EventArgs e)
        {
            //ComissionBill f = new ComissionBill();
            // f.MdiParent = this;
            //f.Show();
        }

        private void button18_Click(object sender, EventArgs e)
        {
            //FarmerBill_frm f = new FarmerBill_frm();
            //  f.MdiParent = this;
            //f.Show();
        }

        private void button17_Click(object sender, EventArgs e)
        {
            //FormDeposit_ f = new FormDeposit_();
            //  f.MdiParent = this;
            //f.Show();
        }

        private void button1_Click_2(object sender, EventArgs e)
        {
            //FormIncomeExpense f = new FormIncomeExpense();
            //   f.MdiParent = this;
            //f.Show();
        }

        private void SalesmanReport_bt_Click(object sender, EventArgs e)
        {
            //FormSalePurchase f = new FormSalePurchase();
            //    f.MdiParent = this;
            //f.Show();
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            //Time_bt.Text = DateTime.Now.ToLongDateString() + "\n" + DateTime.Now.ToLongTimeString();

        }

        private void button2_Click_1(object sender, EventArgs e)
        {
            //FormBill f = new FormBill();
            //  f.MdiParent = this;
            //f.Show();
        }

        private void button3_Click_1(object sender, EventArgs e)
        {
            //FormSalePurchase f = new FormSalePurchase();
            //    f.MdiParent = this;
            //f.Show();
        }

        private void groupBox3_Enter(object sender, EventArgs e)
        {

        }

        private void button4_Click_1(object sender, EventArgs e)
        {
            //Fruit.SalePattiByFarmer f = new Fruit.SalePattiByFarmer();
            //    f.MdiParent = this;
            //f.Show();

        }

        private void button5_Click_1(object sender, EventArgs e)
        {
            System.Diagnostics.Process.Start("Calc.exe");
        }

        private void button6_Click_1(object sender, EventArgs e)
        {
            System.Diagnostics.Process.Start("Notepad.exe");
        }

        private void button7_Click_1(object sender, EventArgs e)
        {
            //CustomerDeposit_Frm f = new CustomerDeposit_Frm();
            //   f.MdiParent = this;
            //f.Show();
        }

        private void button8_Click_1(object sender, EventArgs e)
        {
            //FarmerDeposit_Frm f = new FarmerDeposit_Frm();
            //    f.MdiParent = this;
            //f.Show();
        }

        private void button9_Click_1(object sender, EventArgs e)
        {
            //FormDeposit_ f = new FormDeposit_();
            //  f.MdiParent = this;
            //f.Show();
        }

        private void customerFarmerDetailsToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }

        private void button10_Click_1(object sender, EventArgs e)
        {
            //CustomerBalance  f = new  CustomerBalance ();
            //  f.MdiParent = this;
            //f.Show();
        }

        private void stockToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }

        private void balanceReportToolStripMenuItem_Click_1(object sender, EventArgs e)
        {


        }

        private void customerFarmerDetailsToolStripMenuItem1_Click(object sender, EventArgs e)
        {

        }

        private void balanceUpdateToolStripMenuItem_Click(object sender, EventArgs e)
        {

            //BalanceFrm2 f = new BalanceFrm2();
            //  f.MdiParent = this;
            //f.Show();
        }

        private void balanceDetailToolStripMenuItem_Click(object sender, EventArgs e)
        {
            //CustomerBalance f = new CustomerBalance();
            //  f.MdiParent = this;
            //f.Show();


        }

        private void reportsToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }

        private void userPermissionToolStripMenuItem_Click(object sender, EventArgs e)
        {
            //PermissionFrm m = new PermissionFrm();
            //m.Show();
        }

        private void rokadKharchToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Expense f = new Expense();
            f.Show();
        }

        private void customerJamaPavtiToolStripMenuItem_Click(object sender, EventArgs e)
        {
            //CustomerDeposit_Frm f = new CustomerDeposit_Frm();
            //f.MdiParent = this;
            //f.Show();
        }

        private void farmerJamaPavtiToolStripMenuItem_Click(object sender, EventArgs e)
        {
            //FarmerDeposit_Frm f = new FarmerDeposit_Frm();
            //f.MdiParent = this;
            //f.Show();
        }

        private void singleSMSToolStripMenuItem_Click(object sender, EventArgs e)
        {
            //SingleSMS_frm f = new  SingleSMS_frm ();
            //f.MdiParent = this;
            //f.Show();
        }

        private void stockPlaceToolStripMenuItem_Click(object sender, EventArgs e)
        {
            //StockPlace_Fm sp = new StockPlace_Fm();
            //sp.MdiParent = this;
            //sp.Show();
        }

        private void openingAmountToolStripMenuItem_Click(object sender, EventArgs e)
        {
            //OpeningAmount_Report r = new OpeningAmount_Report();
            //r.Show();
        }

        private void comissionExpensesReportToolStripMenuItem_Click(object sender, EventArgs e)
        {
            //Fruits.Fruits.ReportForm.ComissionExpenses_Frm f = new ComissionExpenses_Frm();
            //f.Show();
        }

        private void customerFarmerReportToolStripMenuItem_Click(object sender, EventArgs e)
        {
            //CustomerFarmerDetails f = new CustomerFarmerDetails();
            //  f.MdiParent = this;
            //f.Show();
        }

        private void balanceReportToolStripMenuItem1_Click(object sender, EventArgs e)
        {
            //Maharashtra.Balaance_Report f = new Balaance_Report();
            //  f.MdiParent = this;
            //f.Show();
        }

        private void Comission_Tl_Click(object sender, EventArgs e)
        {
            PurchaseFrm f = new PurchaseFrm();
            //  f.MdiParent = this;
            f.Show();
        }

        private void BhusarPatti_Tl_Click(object sender, EventArgs e)
        {
            //SalePattiByFarmer f = new SalePattiByFarmer();
            //f.Show();
        }

        private void NewPerson_tl_Click(object sender, EventArgs e)
        {
            PersonFrm p = new PersonFrm();
            p.Show();

            //FarmerDetails_fm f = new FarmerDetails_fm();
            //f.MdiParent = this;
            //f.Show();
        }

        private void J_Click(object sender, EventArgs e)
        {
            //CustomerDeposit_Frm f = new CustomerDeposit_Frm();
            //f.Show();
        }

        private void metroTile2_Click(object sender, EventArgs e)
        {
            //FarmerDeposit_Frm f = new FarmerDeposit_Frm();
            //f.Show();
        }

        private void metroTile4_Click(object sender, EventArgs e)
        {
            IncomeFrm f = new IncomeFrm();
            f.Show();

        }

        private void metroTile3_Click(object sender, EventArgs e)
        {
            Expense ex = new Expense();
            ex.Show();
        }

        private void menuStrip1_ItemClicked(object sender, ToolStripItemClickedEventArgs e)
        {

        }

        private void crToolStripTextBox1_Click(object sender, EventArgs e)
        {

        }

        private void metroTile1_Click(object sender, EventArgs e)
        {
            //FormSalePurchase f = new FormSalePurchase();
            ////    f.MdiParent = this;
            //f.Show();
        }

        private void email_Click(object sender, EventArgs e)
        {

        }

        private void FormMain_KeyDown(object sender, KeyEventArgs e)
        {
            if ((e.KeyCode == Keys.Escape))
            {


                if (MessageBox.Show("Do you want Close this Form ?", "Information", MessageBoxButtons.YesNo, MessageBoxIcon.Question) == DialogResult.Yes)
                {
                    Application.Exit();
                }
                else
                {

                }
            }
        }

        private void toolStripStatusLabel1_Click(object sender, EventArgs e)
        {

        }

        private void metroTile5_Click(object sender, EventArgs e)
        {
            SaleFrm f = new SaleFrm();
            f.Show();
        }

        private void emailToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }


    }
}
