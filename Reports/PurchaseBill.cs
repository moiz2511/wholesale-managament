using CrystalDecisions.CrystalReports.Engine;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Configuration;
using System.Data;
using System.Data.OleDb;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Accounting_Project.Reports
{
    public partial class PurchaseBill :  MetroFramework .Forms .MetroForm 

    {

        OleDbConnection con = new OleDbConnection(ConfigurationManager.AppSettings["Con"]);

         public  string invoice;


        public PurchaseBill()
        {
            InitializeComponent();
        }


        public void Printbill_By_PurchaseForm()
        {

            try
            {
                if(invoice !="")
                {
                    ReportDocument crys = new ReportDocument();

                    //For Purchase Table
                    string insertPur = "SELECT * FROM [Purchase] where [invoice]=" + invoice + " ";

                    OleDbDataAdapter da = new OleDbDataAdapter(insertPur, con);
                    DataSet ds = new DataSet();
                    da.Fill(ds, "Purchase");



                    //For PurchaseItem Table
                    string str = "SELECT * FROM [PurchaseItem]  ";

                    OleDbDataAdapter da2 = new OleDbDataAdapter(str, con);
                    DataSet ds2 = new DataSet();
                    da2.Fill(ds2, "PurchaseItem");


                    crys.Load(@"G:\VIDEOS\Accounting Project\Accounting Project\Crystal Report\PruchsaseBill.rpt");


                    crys.SetDataSource(ds);
                    crys.SetDataSource(ds2);

                    crystalReportViewer1.ReportSource = crys;

                    // Printing and hiding form

                    crystalReportViewer1.PrintReport();


                    this.Close();

                }
            }
            catch (Exception x)
            {
                MessageBox.Show(x + "");
            }


        }




        private void PurchaseBill_Load(object sender, EventArgs e)
        {

            try
            {
                ReportDocument crys = new ReportDocument();
                crys.Load(@"G:\VIDEOS\Accounting Project\Accounting Project\Crystal Report\Blank.rpt");
                crystalReportViewer1.ReportSource = crys;
            }
            catch { }

            Printbill_By_PurchaseForm();
        }


      public   void Printbill()
        {

            try
            {
                ReportDocument crys = new ReportDocument();
              
                //For Purchase Table
                string insertPur = "SELECT * FROM [Purchase] where [invoice]=" + invoice + " ";

                OleDbDataAdapter da = new OleDbDataAdapter(insertPur, con);
                DataSet ds = new DataSet();
                da.Fill(ds, "Purchase");



                //For PurchaseItem Table
                string str = "SELECT * FROM [PurchaseItem]  ";

                OleDbDataAdapter da2 = new OleDbDataAdapter(str, con);
                DataSet ds2 = new DataSet();
                da2.Fill(ds2, "PurchaseItem");


                crys.Load(@"Crystal_Report\PruchsaseBill.rpt");

               
                crys.SetDataSource(ds);
                crys.SetDataSource(ds2);              
              
                crystalReportViewer1.ReportSource = crys;

            }
            catch (Exception x)
            {
                MessageBox.Show(x+"");
            }
            

        }

        private void Print_bt_Click(object sender, EventArgs e)
        {
            crystalReportViewer1.PrintReport();
        }

        private void Export_bt_Click(object sender, EventArgs e)
        {
            crystalReportViewer1.ExportReport();
        }

        private void View_bt_Click(object sender, EventArgs e)
        {
            invoice = Bill_cb.Text;

            Printbill();


        }
    }
}
