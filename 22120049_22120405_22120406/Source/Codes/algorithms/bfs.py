from .base_search import BaseSearch
from ..data_structures.queue import Queue
from ..core.grid import Grid


class BFS(BaseSearch):
    def __init__(self, grid: Grid, next_node_data_structure: Queue = None) -> None:
        if next_node_data_structure is None:
            next_node_data_structure = Queue()  # Create a new Queue if none is provided
        super().__init__(next_node_data_structure, grid)

    def calculate_g(self, node, push_cost) -> int:
        return 0

    def calculate_h(self, node) -> int:
        return 0
