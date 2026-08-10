# simulator.py
from grid_game import GridHuntGame
from agent import GreedyGridAgent
from agent import SimpleReflexAgent
from agent import ModelBasedAgent
from visual_grid_game import VisualGridHuntGame

def run_grid_hunt():
    
    env = VisualGridHuntGame(num_opponents=0)
    agent = ModelBasedAgent()

    print("=== UC Berkeley Style Small Grid Hunt Started ===")
    while not env.is_done():
        percept = env.get_percept(agent)
        action = agent.sense_and_act(percept)
        env.execute_action(action)
        print(
            f"Pos: {percept['agent_pos']} | Action: {action} | "
            f"Visited: {len(agent.visited_cells)} | Score: {env.score}"
        )

    print(f"\nGame Over! Final Score: {env.score} after {env.steps} steps.")

if __name__ == "__main__":
    run_grid_hunt()
