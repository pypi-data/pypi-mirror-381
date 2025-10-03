# -*- coding: utf-8 -*-
"""Repository para persistir o grafo cognitivo no PostgreSQL com pgvector.

Este módulo implementa a camada de persistência para o grafo cognitivo,
seguindo o padrão Adapter estabelecido na arquitetura ECA. Utiliza PostgreSQL
com a extensão pgvector para armazenamento e busca eficiente de embeddings.
"""

from typing import List, Optional, Dict, Set
import json
import psycopg2
from psycopg2.extras import RealDictCursor
from datetime import datetime

from .types import CognitiveNode, CognitiveEdge, NodeType, EdgeType


class CognitiveGraphRepository:
    """Repository para persistir o grafo cognitivo no PostgreSQL com pgvector.
    
    Este repository implementa as operações fundamentais para gerenciar
    o grafo cognitivo em uma base de dados PostgreSQL, aproveitando a
    extensão pgvector para busca semântica eficiente.
    
    Attributes:
        connection_string: String de conexão PostgreSQL
    """
    
    def __init__(self, connection_string: str):
        """Inicializa o repository com a string de conexão do PostgreSQL.
        
        Args:
            connection_string: String de conexão PostgreSQL
                ex: "postgresql://user:pass@localhost:5432/dbname"
        """
        self.connection_string = connection_string
        self._ensure_tables_exist()
    
    def _get_connection(self):
        """Cria uma nova conexão com o banco."""
        return psycopg2.connect(self.connection_string)
    
    def _ensure_tables_exist(self) -> None:
        """Garante que as tabelas necessárias existem no banco."""
        with self._get_connection() as conn:
            with conn.cursor() as cur:
                # Habilita extensão pgvector
                cur.execute("CREATE EXTENSION IF NOT EXISTS vector;")
                
                # Tabela de nós cognitivos
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS cognitive_nodes (
                        id VARCHAR PRIMARY KEY,
                        content TEXT NOT NULL,
                        node_type VARCHAR NOT NULL,
                        embedding vector(384),  -- ajuste dimensão conforme seu modelo
                        activation_level FLOAT DEFAULT 0.0,
                        access_count INTEGER DEFAULT 0,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        last_accessed TIMESTAMP,
                        metadata JSONB DEFAULT '{}'
                    );
                """)
                
                # Tabela de arestas cognitivas
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS cognitive_edges (
                        id VARCHAR PRIMARY KEY,
                        source_id VARCHAR NOT NULL REFERENCES cognitive_nodes(id) ON DELETE CASCADE,
                        target_id VARCHAR NOT NULL REFERENCES cognitive_nodes(id) ON DELETE CASCADE,
                        edge_type VARCHAR NOT NULL,
                        weight FLOAT DEFAULT 1.0,
                        strength FLOAT DEFAULT 1.0,
                        context TEXT,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        metadata JSONB DEFAULT '{}'
                    );
                """)
                
                # Índices para performance
                cur.execute("""
                    CREATE INDEX IF NOT EXISTS idx_cognitive_nodes_embedding 
                    ON cognitive_nodes USING ivfflat (embedding vector_cosine_ops);
                """)
                
                cur.execute("""
                    CREATE INDEX IF NOT EXISTS idx_cognitive_nodes_type 
                    ON cognitive_nodes(node_type);
                """)
                
                cur.execute("""
                    CREATE INDEX IF NOT EXISTS idx_cognitive_edges_source 
                    ON cognitive_edges(source_id);
                """)
                
                cur.execute("""
                    CREATE INDEX IF NOT EXISTS idx_cognitive_edges_target 
                    ON cognitive_edges(target_id);
                """)
                
                conn.commit()
    
    def save_node(self, node: CognitiveNode) -> None:
        """Salva ou atualiza um nó no banco.
        
        Args:
            node: Nó cognitivo a ser salvo
        """
        with self._get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO cognitive_nodes 
                    (id, content, node_type, embedding, activation_level, 
                     access_count, created_at, last_accessed, metadata)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                    ON CONFLICT (id) DO UPDATE SET
                        content = EXCLUDED.content,
                        node_type = EXCLUDED.node_type,
                        embedding = EXCLUDED.embedding,
                        activation_level = EXCLUDED.activation_level,
                        access_count = EXCLUDED.access_count,
                        last_accessed = EXCLUDED.last_accessed,
                        metadata = EXCLUDED.metadata;
                """, (
                    node.id,
                    node.content,
                    node.node_type.value,
                    node.embedding,
                    node.activation_level,
                    node.access_count,
                    node.created_at,
                    node.last_accessed,
                    json.dumps(node.metadata or {})
                ))
                conn.commit()
    
    def save_edge(self, edge: CognitiveEdge) -> None:
        """Salva ou atualiza uma aresta no banco.
        
        Args:
            edge: Aresta cognitiva a ser salva
        """
        with self._get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO cognitive_edges 
                    (id, source_id, target_id, edge_type, weight, 
                     strength, context, created_at, metadata)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                    ON CONFLICT (id) DO UPDATE SET
                        source_id = EXCLUDED.source_id,
                        target_id = EXCLUDED.target_id,
                        edge_type = EXCLUDED.edge_type,
                        weight = EXCLUDED.weight,
                        strength = EXCLUDED.strength,
                        context = EXCLUDED.context,
                        metadata = EXCLUDED.metadata;
                """, (
                    edge.id,
                    edge.source_id,
                    edge.target_id,
                    edge.edge_type.value,
                    edge.weight,
                    edge.strength,
                    edge.context,
                    edge.created_at,
                    json.dumps(edge.metadata or {})
                ))
                conn.commit()
    
    def get_node(self, node_id: str) -> Optional[CognitiveNode]:
        """Busca um nó pelo ID.
        
        Args:
            node_id: ID do nó a ser buscado
            
        Returns:
            Nó cognitivo ou None se não encontrado
        """
        with self._get_connection() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute("""
                    SELECT * FROM cognitive_nodes WHERE id = %s;
                """, (node_id,))
                
                row = cur.fetchone()
                if row:
                    return self._row_to_node(row)
                return None
    
    def get_edges_from_node(self, node_id: str) -> List[CognitiveEdge]:
        """Busca todas as arestas que partem de um nó.
        
        Args:
            node_id: ID do nó origem
            
        Returns:
            Lista de arestas cognitivas
        """
        with self._get_connection() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute("""
                    SELECT * FROM cognitive_edges WHERE source_id = %s;
                """, (node_id,))
                
                return [self._row_to_edge(row) for row in cur.fetchall()]
    
    def get_edges_to_node(self, node_id: str) -> List[CognitiveEdge]:
        """Busca todas as arestas que chegam a um nó.
        
        Args:
            node_id: ID do nó destino
            
        Returns:
            Lista de arestas cognitivas
        """
        with self._get_connection() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute("""
                    SELECT * FROM cognitive_edges WHERE target_id = %s;
                """, (node_id,))
                
                return [self._row_to_edge(row) for row in cur.fetchall()]
    
    def find_similar_nodes(
        self, 
        embedding: List[float], 
        limit: int = 10, 
        similarity_threshold: float = 0.3
    ) -> List[CognitiveNode]:
        """Busca nós similares usando pgvector.
        
        Args:
            embedding: Vetor de embedding para busca
            limit: Número máximo de resultados
            similarity_threshold: Threshold mínimo de similaridade
            
        Returns:
            Lista de nós similares ordenados por similaridade
        """
        with self._get_connection() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                # Converte embedding para string de array PostgreSQL
                embedding_str = '[' + ','.join(map(str, embedding)) + ']'
                
                cur.execute("""
                    SELECT *, (1 - (embedding <=> %s::vector)) as similarity
                    FROM cognitive_nodes 
                    WHERE embedding IS NOT NULL
                    AND (1 - (embedding <=> %s::vector)) > %s
                    ORDER BY embedding <=> %s::vector
                    LIMIT %s;
                """, (embedding_str, embedding_str, similarity_threshold, embedding_str, limit))
                
                return [self._row_to_node(row) for row in cur.fetchall()]
    
    def get_nodes_by_type(self, node_type: NodeType) -> List[CognitiveNode]:
        """Busca nós por tipo.
        
        Args:
            node_type: Tipo de nó a ser buscado
            
        Returns:
            Lista de nós do tipo especificado
        """
        with self._get_connection() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute("""
                    SELECT * FROM cognitive_nodes WHERE node_type = %s;
                """, (node_type.value,))
                
                return [self._row_to_node(row) for row in cur.fetchall()]
    
    def get_subgraph(self, center_node_ids: List[str], max_depth: int = 2) -> Dict:
        """Busca um subgrafo centrado nos nós especificados.
        
        Args:
            center_node_ids: IDs dos nós centrais
            max_depth: Profundidade máxima de busca
            
        Returns:
            Dicionário contendo nós e arestas do subgrafo
        """
        visited_nodes = set()
        nodes_to_process = set(center_node_ids)
        all_nodes = {}
        all_edges = []
        
        for depth in range(max_depth + 1):
            if not nodes_to_process:
                break
                
            current_level = nodes_to_process.copy()
            nodes_to_process.clear()
            
            for node_id in current_level:
                if node_id in visited_nodes:
                    continue
                    
                visited_nodes.add(node_id)
                
                # Busca o nó
                node = self.get_node(node_id)
                if node:
                    all_nodes[node_id] = node
                
                # Busca arestas de saída
                outgoing_edges = self.get_edges_from_node(node_id)
                all_edges.extend(outgoing_edges)
                
                # Busca arestas de entrada
                incoming_edges = self.get_edges_to_node(node_id)
                all_edges.extend(incoming_edges)
                
                # Adiciona vizinhos para próximo nível
                if depth < max_depth:
                    for edge in outgoing_edges + incoming_edges:
                        neighbor_id = edge.target_id if edge.source_id == node_id else edge.source_id
                        if neighbor_id not in visited_nodes:
                            nodes_to_process.add(neighbor_id)
        
        return {
            'nodes': all_nodes,
            'edges': all_edges
        }
    
    def _row_to_node(self, row) -> CognitiveNode:
        """Converte linha do banco para CognitiveNode.
        
        Args:
            row: Linha retornada pela consulta SQL
            
        Returns:
            Objeto CognitiveNode
        """
        return CognitiveNode(
            id=row['id'],
            content=row['content'],
            node_type=NodeType(row['node_type']),
            embedding=list(row['embedding']) if row['embedding'] else None,
            activation_level=row['activation_level'] or 0.0,
            access_count=row['access_count'] or 0,
            created_at=row['created_at'],
            last_accessed=row['last_accessed'],
            metadata=row['metadata'] or {}
        )
    
    def _row_to_edge(self, row) -> CognitiveEdge:
        """Converte linha do banco para CognitiveEdge.
        
        Args:
            row: Linha retornada pela consulta SQL
            
        Returns:
            Objeto CognitiveEdge
        """
        return CognitiveEdge(
            id=row['id'],
            source_id=row['source_id'],
            target_id=row['target_id'],
            edge_type=EdgeType(row['edge_type']),
            weight=row['weight'] or 1.0,
            strength=row['strength'] or 1.0,
            context=row['context'],
            created_at=row['created_at'],
            metadata=row['metadata'] or {}
        )