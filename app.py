from flask import Flask
from .game import Simulation


def create_app():
    app = Flask(__name__)

    @app.route('/', methods=['GET'])
    def index():
        response = {
            "msg": "Game Simulation!"
        }
        return response

    @app.route('/game/simulate', methods=['GET'])
    def simulate():
        simulation = Simulation(300, 1000)
        results = simulation.run()
        return {
            "vencedor": results.get('most_winner'),
            "jogadores": results.get('players')
        }
    return app
