{
    'name': 'Industrial Pipeline & CUPS Inspector',
    'version': '18.0.1.0.0',
    'author': 'Rania Hammad',
    'website': 'https://github.com/raniahammad78',
    'category': 'Manufacturing',
    'summary': 'Manage industrial pipeline integrity, structural pipe supports (CUPS), 9-point visual inspections, and A4 engineering PDF reports.',
    'description': """
        Complete Asset Integrity & External Visual Inspection (EVI) solution for industrial pipelines and Corrosion Under Pipe Supports (CUPS).
        Features an interactive KPI dashboard, 19 structural cup types, a 9-point graded inspection checklist (C, B, A1, A2) with photo evidence, and automated A4 PDF inspection dossiers.
    """,
    'price': 49.00,
    'currency': 'USD',
    'license': 'OPL-1',
    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'data/dashboard_data.xml',
        'views/pipeline_inspector_views.xml',
        'views/dashboard_views.xml',
        'reports/pipeline_report.xml',
        'views/menu.xml',
    ],
'images': [
        'static/description/icon.png'
    ],    'installable': True,
    'application': True,
}
