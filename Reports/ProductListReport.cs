using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Configuration ;
using System.Data.OleDb;
using CrystalDecisions.CrystalReports.Engine;

namespace Accounting_Project.Reports
{
    public partial class ProductListReport : MetroFramework .Forms .MetroForm 
    {
        OleDbConnection con = new OleDbConnection(ConfigurationManager.AppSettings["Con"]);

        //For Crystal report
        ReportDocument cryst = new ReportDocument();


        public ProductListReport()
        {
            InitializeComponent();
        }

        private void ProductListReport_Load(object sender, EventArgs e)
        {
           // By Query Viewing the product list 
            try
            {

                OleDbDataAdapter da = new OleDbDataAdapter("Select * from [Product] ", con);
                DataSet ds = new DataSet();
                da.Fill(ds, "Product");
                cryst.Load(@"G:\Youtube\Projects\Accounting Project\Accounting Project\Crystal Report\ProductReport.rpt");
                cryst.SetDataSource(ds);
                crystalReportViewer1.ReportSource = cryst;

            }
            catch (Exception x)
            { 

                MetroFramework.MetroMessageBox.Show(this , x +"Error" ,"Error",MessageBoxButtons .OK ,MessageBoxIcon .Stop );
            }
        }
    }
}
