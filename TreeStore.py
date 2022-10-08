from typing import List


class TreeStore:

    def __init__(self, source_array: List[dict]):  # стиль названия методов продиктован ТЗ,
        self.source_arr = source_array             # использования camelCase противоречит pep8!!!!!!!
        self._write_nodes_to_dict()

    def getAll(self):
        return self.source_arr

    def getItem(self, id: int):
        return self.tree_dIct.get(id, {})

    def getChildren(self, id: int):
        if self.getItem(id):
            try:
                return self.child_dict.get(id)['childs']
            except KeyError:
                return []

    def getAllParents(self, id):
        parents_list = []
        while self.tree_dIct.get(id)['parent'] != 'root':
            id = self.tree_dIct.get(id)['parent']
            parents_list.append(self.tree_dIct.get(id))
        return parents_list

    def _write_nodes_to_dict(self):
        self.tree_dIct = {}
        self.child_dict = {}
        for item in self.source_arr:
            child_item = item.copy()
            self.tree_dIct[item['id']] = item
            if child_item['parent'] != 'root':
                try:
                    self.child_dict[child_item['parent']]['childs'].append(child_item)
                except KeyError:
                    self.child_dict[child_item['parent']]['childs'] = []
                    self.child_dict[child_item['parent']]['childs'].append(child_item)
            self.child_dict[child_item['id']] = item.copy()
