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
    public partial class PurchaseDateWiseReport : MetroFramework .Forms .MetroForm 
    {
        OleDbConnection con = new OleDbConnection(ConfigurationManager.AppSettings["Con"]);


        public PurchaseDateWiseReport()
        {
            InitializeComponent();
        }

        private void PurchaseDateWiseReport_Load(object sender, EventArgs e)
        {

        }

        private void View_Bt_Click(object sender, EventArgs e)
        {

            try
            {
                ReportDocument crys = new ReportDocument();

                //For Purchase Table
                string insertPur = "SELECT * FROM [Purchase] where [PurchaseDate]  between    #" + dateTimePicker1.Value.Date.ToString() + "# and     #" + dateTimePicker2.Value.Date.ToString() + "#    ";

                OleDbDataAdapter da = new OleDbDataAdapter(insertPur, con);
                DataSet ds = new DataSet();
                da.Fill(ds, "Purchase");



                ////For PurchaseItem Table
                string str = "SELECT * FROM [PurchaseItem]  ";

                OleDbDataAdapter da2 = new OleDbDataAdapter(str, con);
                DataSet ds2 = new DataSet();
                da2.Fill(ds2, "PurchaseItem");


                crys.Load(@"G:\VIDEOS\Accounting Project\Accounting Project\Crystal Report\DateWisePuchaseReport.rpt");


                crys.SetDataSource(ds2);

                crys.SetDataSource(ds);
              
                crystalReportViewer1.ReportSource = crys;

            }
            catch (Exception x)
            {
                MessageBox.Show(x + "");
            }
          
        }

        private void Print_Bt_Click(object sender, EventArgs e)
        {
            crystalReportViewer1.PrintReport();
        }

        private void Export_Bt_Click(object sender, EventArgs e)
        {
            crystalReportViewer1.ExportReport();
        }

        private void NextPage_Bt_Click(object sender, EventArgs e)
        {
            crystalReportViewer1.ShowNextPage();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            crystalReportViewer1.ShowFirstPage();
        }

        private void PreviousPage_Bt_Click(object sender, EventArgs e)
        {
            crystalReportViewer1.ShowPreviousPage();
        }

        private void LastPage_bt_Click(object sender, EventArgs e)
        {
            crystalReportViewer1.ShowLastPage();
        }
    }
}
