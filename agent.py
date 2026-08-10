# agent.py
import random


class GreedyGridAgent:
    """A simple agent that tries to move around systematically to clear the grid."""

    def __init__(self):
        self.actions_pool = ['Up', 'Down', 'Left', 'Right']

    def sense_and_act(self, percept: dict) -> str:
        # If standing directly on food, or just wander / move towards coordinates
        pos = percept['agent_pos']
        # Simple heuristic or fallback random sweep
        return random.choice(self.actions_pool)
    
#Simple reflex agent
class SimpleReflexAgent:
    
    #get percepts from the enviroment
    def sense_and_act(self,percept):
        
        #check whether the food is at the agent's current position 
        if percept['food_here']:
            return 'suck'
        
        if percept['wall_ahead']:
            return 'turn_right'
        
        return 'move_forward'
 
#model based agent    
class ModelBasedAgent:
    
    def __init__(self):
        self.visited = set()
        self.pos = (0, 0)  # internal estimate of position (assume start at origin)
        self.facing = 'Right'
        self.last_action = None

    def _forward_pos(self, pos, facing):
        x, y = pos
        if facing == 'Up':
            return (x, y + 1)
        if facing == 'Down':
            return (x, y - 1)
        if facing == 'Left':
            return (x - 1, y)
        return (x + 1, y)

    def _left_of(self, facing):
        return {'Up': 'Left', 'Left': 'Down', 'Down': 'Right', 'Right': 'Up'}[facing]

    def _right_of(self, facing):
        return {'Up': 'Right', 'Right': 'Down', 'Down': 'Left', 'Left': 'Up'}[facing]

    def _left_pos(self, pos, facing):
        left = self._left_of(facing)
        return self._forward_pos(pos, left)

    def sense_and_act(self, percept: dict) -> str:
        # Update internal model from the last action
        if self.last_action == 'Forward':
            self.pos = self._forward_pos(self.pos, self.facing)
        elif self.last_action == 'TurnLeft':
            self.facing = self._left_of(self.facing)
        elif self.last_action == 'TurnRight':
            self.facing = self._right_of(self.facing)

        # Record visited cell
        self.visited.add(self.pos)

        # Decision logic using memory
        if percept.get('food_here'):
            action = 'Stay'
        elif percept.get('wall_ahead'):
            left_cell = self._left_pos(self.pos, self.facing)
            if left_cell in self.visited:
                action = 'TurnRight'
            else:
                action = 'TurnLeft'
        else:
            action = 'Forward'

        self.last_action = action
        return action
        
        
        
        
        
        