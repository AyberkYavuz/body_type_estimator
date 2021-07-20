from flask import Flask
from flask import render_template
from flask.views import MethodView
from helpers.application_helpers import BackendHelper


app = Flask(__name__)
app.secret_key = BackendHelper.create_random_aplhanumeric_string()


class MainPageSenderAPI(MethodView):
    def get(self):
        return render_template("main_page.html")


main_page_sender_view = MainPageSenderAPI.as_view('main_page_sender_api')
app.add_url_rule('/', view_func=main_page_sender_view, methods=['GET'])

app.run(debug=True)
