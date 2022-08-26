using Accounting_Project.Forms;
using Accounting_Project.Project;
using Maharashtra;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Accounting_Project
{
    static class Program
    {
        /// <summary>
        /// The main entry point for the application.
        /// </summary>
        [STAThread]
        static void Main()
        {
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            Application.Run(new LoginFrm());

            //Application.Run(new FormMain());
            //Application.Run(new ProductEntryFrm ());

            //Application.Run(new PurchaseFrm());
         
        }
    }
}
