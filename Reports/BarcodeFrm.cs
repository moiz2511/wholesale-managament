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
    public partial class BarcodeFrm : MetroFramework.Forms .MetroForm
    {
        OleDbConnection con = new OleDbConnection(ConfigurationManager.AppSettings["Con"]);

        public BarcodeFrm()
        {
            InitializeComponent();
        }

        private void Export_Bt_Click(object sender, EventArgs e)
        {
            crystalReportViewer1.ExportReport();
        }

        private void Print_Bt_Click(object sender, EventArgs e)
        {
            crystalReportViewer1.PrintReport();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            crystalReportViewer1.ShowFirstPage();
        }

        private void PreviousPage_Bt_Click(object sender, EventArgs e)
        {
            crystalReportViewer1.ShowPreviousPage ();
        }

        private void NextPage_Bt_Click(object sender, EventArgs e)
        {
            crystalReportViewer1.ShowNextPage ();
        }

        private void LastPage_bt_Click(object sender, EventArgs e)
        {
            crystalReportViewer1.ShowLastPage ();
        }

        private void BarcodeFrm_Load(object sender, EventArgs e)
        {

        }

        private void View_Bt_Click(object sender, EventArgs e)
        {
            // 
            try
            {
                ReportDocument cryst = new ReportDocument();

                OleDbDataAdapter da = new OleDbDataAdapter("Select * from [Product] where [PID]=" + Pid_Tx.Text + " ", con);
                DataSet ds = new DataSet();

                //For NO. Of qty 
                for (int i = 1; i <= int.Parse(QTY_Tx.Text);i++ )
                {
                    da.Fill(ds, "Product");
                    cryst.Load(@"G:\VIDEOS\Accounting Project\Accounting Project\Crystal Report\Barcode.rpt");
                    cryst.SetDataSource(ds);
                }


                crystalReportViewer1.ReportSource = cryst;

            }
            catch (Exception x)
            {

                MetroFramework.MetroMessageBox.Show(this, x + "Error", "Error", MessageBoxButtons.OK, MessageBoxIcon.Stop);
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            // 
            try
            {
                ReportDocument cryst = new ReportDocument();

                OleDbDataAdapter da = new OleDbDataAdapter("Select * from [Product]  ", con);
                DataSet ds = new DataSet();



                da.Fill(ds, "Product");
                cryst.Load(@"G:\VIDEOS\Accounting Project\Accounting Project\Crystal Report\Barcode.rpt");
                cryst.SetDataSource(ds);


                crystalReportViewer1.ReportSource = cryst;

            }
            catch (Exception x)
            {

                MetroFramework.MetroMessageBox.Show(this, x + "Error", "Error", MessageBoxButtons.OK, MessageBoxIcon.Stop);
            }
       
        }
    }
}
