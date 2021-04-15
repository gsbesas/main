# -*- coding: utf-8 -*-
##############################################################################
#
#    Spellbound soft solution.
#    Copyright (C) 2017-TODAY Spellbound soft solution(<http://www.spellboundss.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': """Invoice New Template""",
    'version': "14.0.1.0",
    'summary': """Profarma Invoice Report""",
    'depends': ['base','sale'],
    'data': [
        'report/proforma_invoice_report.xml',
        'report/proforma_invoice_report_template.xml',
    ],
    'category': "Sale",
    'author': 'Spellbound Soft Solutions',
    'website': 'http://spellboundss.com/',
    'maintainer': 'Spellbound Soft Solutions',
    'company': 'Spellbound Soft Solutions',
    'license': 'AGPL-3',
    'auto_install': False,
    'installable': True,
    'application': True,
}
