# - coding: utf-8 -*-
##############################################################################
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{

    'name': 'Lending invoice report',

    'version': '1.0',

    'category': 'Lending',

    'summary': 'Lending invoice report',

    'author': 'OPENPYME S.R.L',

    'website': 'openpyme.com.ar',

    'depends': [

        'bo_customization',
        'bo_lending',

    ],

    'data': [

        'report/invoice_report_action.xml',
        'report/invoice_report.xml',
        'views/lending_invoice.xml',
        'wizard/lending_invoice_report_wizard.xml',
        'data/debit_motive.xml',

    ],

    'installable': True,

    'auto_install': False,

    'application': True,

    'description': """
Lending invoice report
======================================
* .
""",

}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
