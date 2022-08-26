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
    public partial class SaleBill :MetroFramework .Forms .MetroForm 
    {
        OleDbConnection con = new OleDbConnection(ConfigurationManager.AppSettings["Con"]);

        public string invoice;


        public SaleBill()
        {
            InitializeComponent();
        }

        private void SaleBill_Load(object sender, EventArgs e)
        {

        }
        public void Printbill()
        {

            try
            {
                ReportDocument crys = new ReportDocument();

                //For Purchase Table
                string insertPur = "SELECT * FROM [Sale] where [invoice]=" + invoice + " ";

                OleDbDataAdapter da = new OleDbDataAdapter(insertPur, con);
                DataSet ds = new DataSet();
                da.Fill(ds, "Sale");

               

                //For PurchaseItem Table
                string str = "SELECT * FROM [SaleItem]  ";

                OleDbDataAdapter da2 = new OleDbDataAdapter(str, con);
                DataSet ds2 = new DataSet();
                da2.Fill(ds2, "SaleItem");


                crys.Load(@"Crystal_Report\SaleBill.rpt");

                
                 crys.SetDataSource(ds2);

                 crys.SetDataSource(ds);

            
               
                crystalReportViewer1.ReportSource = crys;

            }
            catch (Exception x)
            {
                MessageBox.Show(x + "");
            }


        }

    
        private void View_bt_Click(object sender, EventArgs e)
        {
            invoice = Bill_cb.Text;

            Printbill();
        }

        private void Print_bt_Click(object sender, EventArgs e)
        {
            crystalReportViewer1.PrintReport();
        }

        private void Export_bt_Click(object sender, EventArgs e)
        {
            crystalReportViewer1.ExportReport();
        }

        private void Name_cb_Enter(object sender, EventArgs e)
        {

            try
            {
                Name_cb.Items.Clear();

                string str = "SELECT DISTINCT [CustomerName] FROM [Sale]  ";

                OleDbDataAdapter da = new OleDbDataAdapter(str,con);
                DataTable dt = new DataTable();

                da.Fill(dt);

                for (int i = 0; i <  dt.Rows.Count ; i++)
                {
                    Name_cb.Items.Add(dt.Rows[i][0].ToString());
                }
            }
            catch(Exception x)
            {

                MessageBox.Show(x + "");
            }
           

        }

        private void Bill_cb_Enter(object sender, EventArgs e)
        {

            try
            {
                Bill_cb.Items.Clear();

                string str = "SELECT [Invoice] FROM [Sale] WHERE [CustomerName]='" + Name_cb .Text+ "' ";
                 
                OleDbDataAdapter da = new OleDbDataAdapter(str, con);

                DataTable dt = new DataTable();

                da.Fill(dt);
                              

                foreach (DataRow dtrow in dt.Rows)
                {
                    Bill_cb.Items.Add(dtrow[0].ToString());
                }

                
            }
            catch (Exception x)
            {

                MessageBox.Show(x + "");
            }
           
        }
    }
}

















