{
    'name': 'Gestión de Riesgos',
    'version': '17.0.1.0.0',
    'category': 'Risk Management',
    'summary': 'Sistema de gestión de riesgos empresariales',
 
    'author': 'Prueba',
    
    'depends': ['base', 'mail','hr'],
    'images': '/sgr/static/description/icon.png',

    'assets': {
        'web.assets_backend': [
           # 'sgr/static/src/css/risk_matrix.css', 
        ],
    },
'data': [
        # 1. Primero la seguridad (permisos de acceso unificados)
         'security/security_groups.xml',        
         'security/ir.model.access.csv',        
         'security/record_rules.xml', 
        
        # 2. Datos base (secuencias, datos maestros)
        'data/risk_sequence.xml',
        
        # 3. Vistas de los modelos
        'views/risk_category_views.xml',
        'views/risk_management_views.xml',
        
        'views/evaluation_plan_views.xml', 
        # 4. Reportes PDF
        'reports/risk_report_action.xml',
        'reports/risk_report_template.xml',
        
        # 5. Menús 
        'views/risk_menu.xml',
        
    ],
    'demo': ['demo/demo_data.xml'],
    
    'demo': [],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}