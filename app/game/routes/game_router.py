from fastapi import APIRouter

from app.game.service.simulation import Simulation

game_router = APIRouter(prefix='/game')


@game_router.get('/simulate')
async def simulate():
    simulation = Simulation(300, 1000)
    results = simulation.run()
    return {
        "vencedor": results.get('most_winner'),
        "jogadores": results.get('players')
    }