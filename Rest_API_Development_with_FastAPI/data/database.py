
from typing import Dict

class Database:
    
    def __init__(self):
        self.data = {}
        
    def get_all_items(self) -> Dict[str, str]:
        return self.data
    
    def get_item(self, item_name: str) -> str:
        return self.data.get(item_name, "")
    
    def add_item(self, item_name: str, item_description: str) -> None:
        self.data[item_name] = item_description
