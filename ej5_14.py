from typing import Any, Optional


def eliminar_arista(self, vertice, destino) -> Optional [Any]:
        pos_origen = self.search(vertice, 'value')
        if pos_origen is None:
            return None
        
        arista_eliminada = self[pos_origen].edges.delete_value(destino, 'destination')
        
        if not self.is_dir and arista_eliminada is not None:
            pos_destino = self.search(destino, 'value')
            if pos_destino is not None:
                self[pos_destino].edges.delete_value(vertice, 'destination')
                
        return arista_eliminada

        def existe_paso(self, origen, destino) -> bool:
            def _explorar(grafo, nodo_actual, nodo_destino) -> bool:
                pos_actual = grafo.search(nodo_actual, 'value')
            if pos_actual is None:
                return False
                
            grafo[pos_actual].visited = True
            
            if grafo[pos_actual].value == nodo_destino:
                return True
                
            for arista in grafo[pos_actual].edges:
                pos_vecino = grafo.search(arista.destination, 'value')
                if pos_vecino is not None and not grafo[pos_vecino].visited:
                    if _explorar(grafo, grafo[pos_vecino].value, nodo_destino):
                        return True
                        
            return False

        for vertex in self:
            vertex.visited = False

        return _explorar(self, origen, destino)