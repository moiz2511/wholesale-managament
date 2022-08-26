﻿using System;
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

namespace Accounting_Project.Forms
{
    public partial class CustomerDeposit : MetroFramework.Forms.MetroForm
    {

        OleDbConnection con = new OleDbConnection(ConfigurationManager.AppSettings["Con"]);

        public CustomerDeposit()
        {
            InitializeComponent();
        }

        private void CustomerDeposit_Load(object sender, EventArgs e)
        {

        }

        private void Close_bt_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void View_bt_Click(object sender, EventArgs e)
        {

            {
                try
                {


                    string str = "SELECT * FROM [CustomerDepositTbl] WHERE [DepositDate] =#" + metroDateTime1.Value.Date.ToShortDateString() + "#   ";
                    OleDbDataAdapter da = new OleDbDataAdapter(str, con);
                    DataTable dt = new DataTable();
                    da.Fill(dt);

                    dataGridView1.DataSource = dt;


                }
                catch (Exception x)
                {

                }
            }
        }

        private void Type_cb_Enter(object sender, EventArgs e)
        {

        }

        private void cbCustomer_Enter(object sender, EventArgs e)
        {

            // For Product list
            try
            {
                //For Clearing item 
                cbCustomer.Items.Clear();

                //For Dropp down list

                cbCustomer.DroppedDown = true;


                OleDbDataAdapter da = new OleDbDataAdapter("Select * from [Person] order by [PersonName] Asc", con);
                DataSet ds = new DataSet();
                da.Fill(ds);

                for (int i = 0; i < ds.Tables[0].Rows.Count; i++)
                {
                    cbCustomer.Items.Add(ds.Tables[0].Rows[i]["PersonName"].ToString());
                }


            }
            catch (Exception x)
            {
                //MetroFramework.MetroMessageBox.Show(this, "Error" + x, "Stop", MessageBoxButtons.OK, MessageBoxIcon.Stop);
            }

        }

        private void cbCustomer_SelectedIndexChanged(object sender, EventArgs e)
        {

        }
        void funOpening()
        {
            // For opening Amoount
            try
            {
                //For Clearing item 
                txtOpeningAmt.Clear();

                OleDbDataAdapter da = new OleDbDataAdapter("Select * from [Person] where [PersonName]='" + cbCustomer.Text + "'  ", con);
                DataTable dt = new DataTable();
                da.Fill(dt);
                if (dt.Rows.Count > 0)
                    txtOpeningAmt.Text = dt.Rows[0]["OpeningAmt"].ToString();
                else
                    txtOpeningAmt.Text = "00.00";
            }
            catch (Exception x)
            {
                //MetroFramework.MetroMessageBox.Show(this, "Error" + x, "Stop", MessageBoxButtons.OK, MessageBoxIcon.Stop);
            }
        }

        void funSaleTotal()
        {
            // For opening Amoount
            try
            {
                //For Clearing item 
                txtSaleAmt.Clear();

                OleDbDataAdapter da = new OleDbDataAdapter("Select Sum(TotalAmt) from [Sale] where [CustomerName]='" + cbCustomer.Text + "'  ", con);
                DataTable dt = new DataTable();
                da.Fill(dt);
                //string 
                if (!string.IsNullOrEmpty(dt.Rows[0][0].ToString()))
                    txtSaleAmt.Text = dt.Rows[0][0].ToString();
                else
                    txtSaleAmt.Text = "00.00";
            }
            catch (Exception x)
            {
                //MetroFramework.MetroMessageBox.Show(this, "Error" + x, "Stop", MessageBoxButtons.OK, MessageBoxIcon.Stop);
            }
        }
        void funDepositTotal()
        {
            // For opening Amoount
            try
            {
                //For Clearing item 
                txtDepositAmt.Clear();

                OleDbDataAdapter da = new OleDbDataAdapter("Select Sum(CashAmt) from [CustomerDepositTbl] where [CustomerName]='" + cbCustomer.Text + "'  ", con);
                DataTable dt = new DataTable();
                da.Fill(dt);
                if (!string.IsNullOrEmpty(dt.Rows[0][0].ToString()))
                    txtDepositAmt.Text = dt.Rows[0][0].ToString();
                else
                    txtDepositAmt.Text = "00.00";
            }
            catch (Exception x)
            {
                //MetroFramework.MetroMessageBox.Show(this, "Error" + x, "Stop", MessageBoxButtons.OK, MessageBoxIcon.Stop);
            }
        }

        void funAmount()
        {
            try
            {
                double amt = 0;
                amt = (Convert.ToDouble(txtOpeningAmt.Text) + Convert.ToDouble(txtSaleAmt.Text)) - Convert.ToDouble(txtDepositAmt.Text);
                txtTotalAmt.Text = amt.ToString("00.00");
            }
            catch
            {
                txtTotalAmt.Text = "00.00";
            }
        }


        private void mbtnViewCustomer_Click(object sender, EventArgs e)
        {
            funOpening();
            funSaleTotal();
            funDepositTotal();
            funAmount();
        }

        void funCash()
        {
            try
            {
                double amt = 0;
                amt = (Convert.ToDouble(txtTotalAmt.Text) - Convert.ToDouble(txtCash.Text));
                txtBalance.Text = amt.ToString("00.00");
            }
            catch
            {
                txtBalance.Text = "00.00";
            }
        }

        private void txtCash_TextChanged(object sender, EventArgs e)
        {
            funCash();
        }

        void funClear()
        {
            cbCustomer.Text = "";
            txtTotalAmt.Text = "";
            txtCash.Text = "";
            txtBalance.Text = "";
            txtOpeningAmt.Text = "00.00";
            txtSaleAmt.Text = "00.00";
            txtDepositAmt.Text = "00.00";
        }
        private void Save_bt_Click(object sender, EventArgs e)
        {
            try
            {

                OleDbDataAdapter da = new OleDbDataAdapter("Insert into [CustomerDepositTbl] (CustomerName,DepositDate,TotalAmt,CashAmt,BalanceAmt) values('" + cbCustomer.Text + "' ,'" + DateTime.Now.ToShortDateString() + "' ," + txtTotalAmt.Text + "," + txtCash.Text + "," + txtBalance.Text + "  ) ", con);
                DataTable dt = new DataTable();
                da.Fill(dt);

                MessageBox.Show("Saved Succussfully.." + cbCustomer.Text);
                funClear();//..for clearing after inserting values
                cbCustomer.Focus();
                cbCustomer.DroppedDown = true;

            }
            catch (Exception x)
            {
                MetroFramework.MetroMessageBox.Show(this, "Error" + x, "Stop", MessageBoxButtons.OK, MessageBoxIcon.Stop);
            }
        }

        private void Delete_bt_Click(object sender, EventArgs e)
        {
            try
            {

                OleDbDataAdapter da = new OleDbDataAdapter("Delete from [CustomerDepositTbl] where [CustomerDepID]=  " + dataGridView1.SelectedRows[0].Cells[0].Value.ToString() + " ", con);
                DataTable dt = new DataTable();
                da.Fill(dt);  

                MessageBox.Show("Deleted Succussfully.." );
                View_bt_Click(null, null);

            }
            catch (Exception x)
            {
                MetroFramework.MetroMessageBox.Show(this, "Error" + x, "Stop", MessageBoxButtons.OK, MessageBoxIcon.Stop);
            }
        }
    }
}
