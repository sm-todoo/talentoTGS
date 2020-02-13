
#LFPV - Todoo SAS

import json
import logging
import werkzeug
from datetime import datetime
from math import ceil

from odoo import fields, http, SUPERUSER_ID
from odoo.http import request
from odoo.tools import ustr
from odoo.addons.survey.controllers.main import Survey
from odoo.http import request
import html2text

_logger = logging.getLogger(__name__)


class WebsiteSurveyExtend(Survey):
    
    @http.route(['/survey/print/<model("survey.survey"):survey>',
                 '/survey/print/<model("survey.survey"):survey>/<string:token>'],
                type='http', auth='public', website=True)
    def print_survey(self, survey, token=None, **post):
       

        survey_question = request.env['survey.question']
        user_input = request.env['survey.user_input']
        user_input_line = request.env['survey.user_input_line']

        question_ids = survey_question.sudo().search([('type', '=', 'upload_file'), ('survey_id', '=', survey.id)])
        user_input_id = user_input.sudo().search([('token', '=', token), ('survey_id', '=', survey.id)])

        user_input_line_upload_file = []
        for question in question_ids:
            user_input_line = user_input_line.search([
                ('user_input_id', '=', user_input_id.id),
                ('survey_id', '=', survey.id),
                ('question_id', '=', question.id),
                ('answer_type', '=', 'upload_file')
            ])
            user_input_line_upload_file.append(user_input_line)
        return request.render('survey.survey_print',
                              {'survey': survey,
                               'token': token,
                               'page_nr': 0,
                               'quizz_correction': True if survey.quizz_mode and token else False,
                               'user_input_line_upload_file': user_input_line_upload_file})
