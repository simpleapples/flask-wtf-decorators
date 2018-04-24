import unittest
import json

from flask import Flask
from flask import jsonify

from flask_wtf_decorators import FormValidator
from tests.forms import TestForm


class TestPost(unittest.TestCase):

    def test_legal_form_with_error_handler(self):
        app = self._run_app(with_error_handler=True)

        with app.test_client() as client:
            data = {'test_str': 'hello', 'test_int': 73557344}
            res = client.post(
                '/submit', data=data, headers=[('Accept', 'application/json')])
            self.assertEqual(res.status_code, 200)
            self.assertEqual(res.content_type, 'application/json')
            res_json = json.loads(res.get_data().decode('utf-8'))
            self.assertEqual(res_json['test_str'], 'hello')
            self.assertEqual(res_json['test_int'], 73557344)

    def test_legal_form_without_error_handler(self):
        app = self._run_app(with_error_handler=False)

        with app.test_client() as client:
            data = {'test_str': 'hello', 'test_int': 73557344}
            res = client.post(
                '/submit', data=data, headers=[('Accept', 'application/json')])
            self.assertEqual(res.status_code, 200)
            self.assertEqual(res.content_type, 'application/json')
            res_json = json.loads(res.get_data().decode('utf-8'))
            self.assertEqual(res_json['test_str'], 'hello')
            self.assertEqual(res_json['test_int'], 73557344)

    def test_illegal_form_with_error_handler(self):
        app = self._run_app(with_error_handler=True)

        with app.test_client() as client:
            data = {'test_str': 'hello', 'test_int': 6}
            res = client.post(
                '/submit', data=data, headers=[('Accept', 'application/json')])
            self.assertEqual(res.status_code, 400)
            self.assertEqual(res.content_type, 'application/json')
            res_json = json.loads(res.get_data().decode('utf-8'))
            self.assertEqual(
                res_json['errors']['test_int'], ['Number must be at least 10.'])

    def _run_app(self, with_error_handler=False):
        form_validator = FormValidator()

        if with_error_handler:
            @form_validator.error_handler
            def error_handler(errors):
                return jsonify({'errors': errors}), 400

        secret = '7848a306cdff211b'
        app = Flask(__name__)
        app.config.update({
            'SECRET_KEY': secret, 'WTF_CSRF_SECRET_KEY': secret,
            'WTF_CSRF_ENABLED': False})

        @app.route('/submit', methods=['POST'])
        @form_validator.validate_form(TestForm)
        def post_submit(form):
            return jsonify({
                'test_str': form.test_str.data, 'test_int': form.test_int.data})

        return app
