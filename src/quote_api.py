"""Simple Python Flask API to support CS7319 Homework 1."""


from flask import Flask, jsonify, render_template_string

from quote_utils import get_random_quotes, load_quotes


class QuoteController:
    """Rest Controller to provide hello world and welcome messages."""

    def __init__(self, port=8080):
        """Initialize rest controller class."""
        self.app = Flask(__name__)
        self.port = port
        # Load quotes once at startup
        self.quotes = load_quotes("src/data/quotes_extended.jsonl")
        self.setup_routes()


    def setup_routes(self):
        """Set up flask routes for homepage and API."""
        @self.app.route("/")
        def homepage(quote_num=5):
            """
            Return a minimal static page with quotes generated server-side.
            """
            # Get random quotes server-side
            random_quotes = get_random_quotes(self.quotes, quote_num)
            
            # Build quotes HTML
            quotes_html = ""
            for quote in random_quotes:
                quotes_html += f'"{quote["text"]}<br>'
                quotes_html += "&nbsp;&nbsp;&nbsp;&nbsp;- " + \
                              f'{quote["author"]}<br><br>'
            
            html = f"""
            <!DOCTYPE html>
            <html>
            <head><title>Quotes</title></head>
            <body>
                <h1>Inspirational Quotes</h1>
                <div>{quotes_html}</div>
            </body>
            </html>
            """
            return render_template_string(html)

        @self.app.route("/api/quotes")
        def api_quotes():
            """
            Return a JSON array of random quotes (default 4).
            """
            from flask import request
            count = request.args.get('count', default=4, type=int)
            n = min(count, len(self.quotes))
            return jsonify(get_random_quotes(self.quotes, n))

    def run(self):
        """Run the Flask application."""
        self.app.run(host="0.0.0.0", port=self.port, debug=False)


if __name__ == "__main__":
    controller = QuoteController()
    controller.run()
