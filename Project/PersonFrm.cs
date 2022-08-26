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
    public partial class PersonFrm : MetroFramework.Forms.MetroForm
    {
        OleDbConnection con = new OleDbConnection(ConfigurationManager.AppSettings["Con"]);


        public PersonFrm()
        {
            InitializeComponent();
        }

        private void PersonFrm_Load(object sender, EventArgs e)
        {

        }

        private void btClose_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        void clear()
        {
            txDetail.Clear();
            txEmail.Clear();
            txMobile.Clear();
            txName.Clear();
            txtAddress.Clear();
            txOpeningAmt.Clear();
        }

        private void btSave_Click(object sender, EventArgs e)
        {
            if (MetroFramework.MetroMessageBox.Show(this, "Do you want to Save ?", "Save Box", MessageBoxButtons.OKCancel, MessageBoxIcon.Information) == DialogResult.OK)
            {
                //Person Table
                {
                    string insertPur = "Insert into [Person] (PersonName,Email,Mobile,Address,Detail,OpeningAmt) values ( '" + txName.Text.ToUpper().Trim() + "'  , '" + txEmail.Text.Trim() + "' ,'" + txMobile.Text.ToUpper().Trim() + "','" + txtAddress.Text.ToUpper().Trim() + "' ,'" + txDetail.Text.ToUpper().Trim() + "'," + txOpeningAmt.Text + "  ) ";

                    OleDbDataAdapter da = new OleDbDataAdapter(insertPur, con);
                    DataSet ds = new DataSet();
                    da.Fill(ds);
                    MessageBox.Show("Saved Successfully : " + txName.Text);
                    clear();
                    txName.Focus();
                }
            }
        }
    }
}
