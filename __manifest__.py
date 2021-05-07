{
    'name': 'Nomina en Excel OPS',
    'version': '1.0',
    'category': 'payroll',
    'sequence': 60,
    'summary': 'Muestra un informe de nómina en formato xlsx',
    'description': "Muestra el informe de nómina en Excel para un tiempo determinado",
    'author':'Ariel Cerrato',
    'depends': ['base','hr', 'hr_payroll','ops_sumatoria_vacaciones','contrato_generacion_ops','ops_supervisor_horas',],
    'data': ['security/ir.model.access.csv',
             'wizard/payroll_report_wiz.xml',
             'views/vista_acumulado.xml',
      ],
    'installable': True,
    'auto_install': False,
    'application': False,
}