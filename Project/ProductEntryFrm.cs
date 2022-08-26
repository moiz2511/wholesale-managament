using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

using System.Data.OleDb;
using System.Configuration;

namespace Accounting_Project.Project
{
    public partial class ProductEntryFrm : Form
    {
        OleDbConnection con = new OleDbConnection(ConfigurationManager .AppSettings ["Con"]);
        //Or You could use easy connection 
        OleDbConnection conn = new OleDbConnection(@"Provider=Microsoft.ACE.OLEDB.12.0;Jet OLEDB:Database Password=54321;Data Source=G:\Account\AccountDBS.accdb");
       

        public ProductEntryFrm()
        {
            InitializeComponent();
        }

        private void ProductEntryFrm_Load(object sender, EventArgs e)
        {
            //For showing datagrid Table Value on loading
            ViewData();
        }

        private void label2_Click(object sender, EventArgs e)
        {

        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox3_TextChanged(object sender, EventArgs e)
        {

        }

        private void label4_Click(object sender, EventArgs e)
        {

        }

        private void Save_bt_Click(object sender, EventArgs e)
        {
            //Inserting items in table
            OleDbDataAdapter da = new OleDbDataAdapter("insert into [Product] (Pid,Product,Rate,MRP) values("+ID_tx .Text +",'" + ProductName_tx .Text  +"',"+Rate_tx .Text +","+MRP_tx .Text +"    )", conn);
            DataSet ds = new DataSet();
            da.Fill(ds);

            //It is for view data in table after saving
            ViewData();
            ClearData();

        }

        void ViewData()
        {
            OleDbDataAdapter da = new OleDbDataAdapter("Select * from [Product]",conn);
            DataSet ds = new DataSet();
            da.Fill(ds);
            dataGridView1.DataSource = ds.Tables[0];

        }

        void ClearData()
        {
            //For clearing data after inserting ,updating,deleting
            ID_tx.Clear();
            ProductName_tx.Clear();
            Rate_tx.Clear();
            MRP_tx.Clear();
        }

        private void dataGridView1_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }

        private void Exit_bt_Click(object sender, EventArgs e)
        {
            this.Close();   
        }

        private void Udate_bt_Click(object sender, EventArgs e)
        {

            OleDbDataAdapter da = new OleDbDataAdapter("update [Product] set [Product]='" + ProductName_tx.Text + "' ,[Rate]=" + Rate_tx.Text + ",[Mrp]=" + MRP_tx.Text + "  where [PID]=" + ID_tx.Text + "  ", conn);
            DataSet ds = new DataSet();
            da.Fill(ds);

            ViewData();
            ClearData();


            /*
             * NOte : '" "'= is use for text value
             * " " =is use for Numeric value
             * other wise it will not insert value
             */

        }

        private void Delete_bt_Click(object sender, EventArgs e)
        {
            OleDbDataAdapter da = new OleDbDataAdapter("DELETE FROM [Product]  where [PID]=" + ID_tx.Text + "  ", conn);
            DataSet ds = new DataSet();
            da.Fill(ds);

            ViewData();
            ClearData();
        }

        private void ID_tx_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (char.IsDigit(e.KeyChar))
            {
                //if values is digit,numeric then it will do nothing
            }
            else
            {
                //if the value is not digit ,numeric then it will disable keypress
                e.Handled = true;
            }
        }

        private void Rate_tx_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (char.IsDigit(e.KeyChar) || e.KeyChar ==(char )Keys .Delete )
            {
                //if values is digit,numeric  and decimal then it will do nothing 
            }
            else
            {
                //if the value is not digit ,numeric then it will disable keypress
                e.Handled = true;
            }
        }

        private void MRP_tx_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (char.IsDigit(e.KeyChar) || e.KeyChar == (char)Keys.Delete)
            {
                //if values is digit,numeric and decimal then it will do nothing
            }
            else
            {
                //if the value is not digit ,numeric then it will disable keypress
                e.Handled = true;
            }
        }

        private void ProductName_tx_KeyPress(object sender, KeyPressEventArgs e)
        {
            //It will convert the product name to Upper case
            e.KeyChar = char.ToUpper(e.KeyChar); 


        }

    }
}
