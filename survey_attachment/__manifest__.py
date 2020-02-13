# -*- encoding: utf-8 -*-

{
    'name': 'Adjuntos en Encuestas - Todoo SAS',
    'summary': """
        Adjutos en Encuestas Odoo Versión 13""",
    'version': '12.0',
    'category': 'Survey',
    'description': """
        Add attachment to survey
    """,
    'author': 'Luis Felipe Paternina Vital',
    'website': '',
    'depends': ['survey'],
    'images': ['static/description/survey.jpg'],
    'data': [
        'views/survey_question_template.xml',
        'views/survey_user_input_line_view.xml',
    ],
}
