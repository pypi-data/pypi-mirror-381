# -*- coding: utf-8 -*-
"""Sistema de propagação de ativação para o grafo cognitivo.

Este módulo implementa algoritmos de propagação de ativação inspirados em
modelos de redes neurais e teorias cognitivas. A propagação permite simular
como conceitos ativados influenciam conceitos relacionados no grafo.
"""

from typing import Dict, List, Set, Optional
from .repository import CognitiveGraphRepository
from .types import EdgeType
import math


class ActivationPropagator:
    """Gerencia a propagação de ativação no grafo cognitivo persistido.
    
    Este componente implementa algoritmos de propagação de ativação que
    simulam como a ativação de conceitos se espalha através das conexões
    no grafo cognitivo, similar aos processos de spreading activation
    em redes semânticas.
    
    Attributes:
        repository: Repository para acesso ao grafo
        max_iterations: Número máximo de iterações de propagação
        decay_factor: Fator de decaimento por iteração
        min_activation: Ativação mínima para propagação
        edge_weights: Pesos por tipo de aresta
    """
    
    def __init__(
        self, 
        repository: CognitiveGraphRepository,
        max_iterations: int = 5,
        decay_factor: float = 0.7,
        min_activation: float = 0.01,
        edge_type_weights: Optional[Dict[EdgeType, float]] = None
    ):
        """Inicializa o propagador de ativação.
        
        Args:
            repository: Repository para acesso ao grafo cognitivo
            max_iterations: Número máximo de iterações de propagação
            decay_factor: Fator de decaimento da ativação por iteração
            min_activation: Threshold mínimo para propagação de ativação
            edge_type_weights: Pesos customizados por tipo de aresta
        """
        self.repository = repository
        self.max_iterations = max_iterations
        self.decay_factor = decay_factor
        self.min_activation = min_activation
        
        # Pesos padrão para diferentes tipos de arestas
        self.edge_weights = edge_type_weights or {
            EdgeType.CAUSES: 0.9,
            EdgeType.REQUIRES: 0.8,
            EdgeType.SIMILAR_TO: 0.7,
            EdgeType.TEMPORAL_SEQUENCE: 0.6,
            EdgeType.PART_OF: 0.8,
            EdgeType.ENABLES: 0.7,
            EdgeType.CONFLICTS_WITH: -0.3,  # conexões negativas
            EdgeType.ASSOCIATED_WITH: 0.5
        }
    
    def propagate_activation(
        self, 
        initial_activation: Dict[str, float],
        bidirectional: bool = True
    ) -> Dict[str, float]:
        """Propaga ativação através do grafo persistido.
        
        Args:
            initial_activation: Mapeamento de nó_id -> ativação inicial
            bidirectional: Se deve propagar em ambas as direções
            
        Returns:
            Mapeamento final de nó_id -> nível de ativação
        """
        
        # Inicializa ativação
        activation_map = initial_activation.copy()
        processed_nodes = set()
        
        for iteration in range(self.max_iterations):
            new_activations = {}
            iteration_decay = self.decay_factor ** iteration
            
            # Para cada nó ativo
            for node_id, activation in activation_map.items():
                if activation < self.min_activation or node_id in processed_nodes:
                    continue
                
                # Busca arestas de saída
                outgoing_edges = self.repository.get_edges_from_node(node_id)
                self._propagate_through_edges(
                    outgoing_edges, activation, iteration_decay, new_activations, forward=True
                )
                
                # Busca arestas de entrada (se bidirectional)
                if bidirectional:
                    incoming_edges = self.repository.get_edges_to_node(node_id)
                    self._propagate_through_edges(
                        incoming_edges, activation, iteration_decay * 0.5, new_activations, forward=False
                    )
                
                processed_nodes.add(node_id)
            
            # Merge ativações
            for node_id, new_activation in new_activations.items():
                if node_id not in activation_map:
                    activation_map[node_id] = 0
                activation_map[node_id] += new_activation
                
                # Normaliza para evitar explosão de ativação
                activation_map[node_id] = min(1.0, activation_map[node_id])
            
            # Se não há novas ativações significativas, para
            if not any(v >= self.min_activation for v in new_activations.values()):
                break
        
        # Remove ativações muito baixas
        return {k: v for k, v in activation_map.items() if v >= self.min_activation}
    
    def _propagate_through_edges(
        self, 
        edges: List, 
        source_activation: float, 
        decay: float, 
        new_activations: Dict[str, float],
        forward: bool = True
    ) -> None:
        """Propaga ativação através de uma lista de arestas.
        
        Args:
            edges: Lista de arestas para propagação
            source_activation: Ativação do nó fonte
            decay: Fator de decaimento atual
            new_activations: Dicionário para acumular novas ativações
            forward: Se é propagação direta (True) ou reversa (False)
        """
        for edge in edges:
            edge_weight = self.edge_weights.get(edge.edge_type, 0.5)
            
            # Calcula ativação propagada
            propagated = (
                source_activation * 
                edge_weight * 
                edge.strength * 
                decay
            )
            
            if abs(propagated) >= self.min_activation:
                target_id = edge.target_id if forward else edge.source_id
                
                if target_id not in new_activations:
                    new_activations[target_id] = 0
                new_activations[target_id] += propagated
    
    def get_activation_clusters(
        self, 
        activation_map: Dict[str, float], 
        min_cluster_size: int = 2
    ) -> List[List[str]]:
        """Identifica clusters de nós altamente ativados.
        
        Args:
            activation_map: Mapeamento de ativação atual
            min_cluster_size: Tamanho mínimo para considerar um cluster
            
        Returns:
            Lista de clusters (cada cluster é uma lista de nós)
        """
        clusters = []
        visited = set()
        
        # Ordena nós por ativação
        sorted_nodes = sorted(
            activation_map.items(), 
            key=lambda x: x[1], 
            reverse=True
        )
        
        for node_id, activation in sorted_nodes:
            if node_id in visited or activation < self.min_activation:
                continue
            
            # Encontra cluster conectado
            cluster = self._find_connected_cluster(node_id, activation_map, visited)
            
            if len(cluster) >= min_cluster_size:
                clusters.append(cluster)
        
        return clusters
    
    def _find_connected_cluster(
        self, 
        start_node: str, 
        activation_map: Dict[str, float], 
        visited: Set[str]
    ) -> List[str]:
        """Encontra cluster de nós conectados e ativados.
        
        Args:
            start_node: Nó inicial para busca do cluster
            activation_map: Mapeamento de ativação
            visited: Conjunto de nós já visitados
            
        Returns:
            Lista de nós que formam o cluster
        """
        cluster = []
        queue = [start_node]
        local_visited = set()
        
        while queue:
            current = queue.pop(0)
            
            if current in local_visited or current in visited:
                continue
            
            if current not in activation_map or activation_map[current] < self.min_activation:
                continue
            
            local_visited.add(current)
            visited.add(current)
            cluster.append(current)
            
            # Busca vizinhos ativados
            outgoing_edges = self.repository.get_edges_from_node(current)
            incoming_edges = self.repository.get_edges_to_node(current)
            
            all_neighbors = set()
            for edge in outgoing_edges:
                all_neighbors.add(edge.target_id)
            for edge in incoming_edges:
                all_neighbors.add(edge.source_id)
            
            for neighbor in all_neighbors:
                if (neighbor in activation_map and 
                    activation_map[neighbor] >= self.min_activation and
                    neighbor not in local_visited):
                    queue.append(neighbor)
        
        return cluster