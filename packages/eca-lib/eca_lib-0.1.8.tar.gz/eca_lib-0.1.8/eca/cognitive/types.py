# -*- coding: utf-8 -*-
"""Tipos e estruturas básicas para o sistema cognitivo da ECA.

Este módulo define as estruturas fundamentais para representar nós e arestas
no grafo cognitivo, seguindo os padrões estabelecidos na arquitetura ECA.
"""

from typing import Dict, List, Optional
from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime, timezone


class NodeType(Enum):
    """Tipos de nós no grafo cognitivo.
    
    Define as diferentes categorias de conceitos que podem ser representados
    no grafo de conhecimento cognitivo.
    """
    CONCEPT = "concept"           # Conceitos abstratos
    EXPERIENCE = "experience"     # Experiências vividas
    PROCEDURE = "procedure"       # Sequências de ações
    EMOTION = "emotion"          # Estados emocionais
    CONTEXT = "context"          # Contextos situacionais
    MEMORY = "memory"            # Referência para memórias


class EdgeType(Enum):
    """Tipos de conexões no grafo cognitivo.
    
    Define os diferentes tipos de relações que podem existir entre nós
    no grafo cognitivo, inspirados em teorias de representação do conhecimento.
    """
    CAUSES = "causes"                    # A causa B
    REQUIRES = "requires"                # A requer B
    SIMILAR_TO = "similar_to"           # A é similar a B
    TEMPORAL_SEQUENCE = "temporal_seq"   # A acontece antes de B
    PART_OF = "part_of"                 # A é parte de B
    ENABLES = "enables"                 # A habilita B
    CONFLICTS_WITH = "conflicts_with"   # A conflita com B
    ASSOCIATED_WITH = "associated_with" # A está associado com B


@dataclass
class CognitiveNode:
    """Representa um nó no grafo cognitivo.
    
    Um nó cognitivo encapsula um conceito, experiência ou outro tipo de
    entidade mental, junto com seus metadados e estado de ativação.
    
    Attributes:
        id: Identificador único do nó
        content: Conteúdo textual do nó
        node_type: Tipo do nó (conceito, experiência, etc.)
        embedding: Representação vetorial do conteúdo (opcional)
        activation_level: Nível atual de ativação (0.0-1.0)
        access_count: Número de vezes que o nó foi acessado
        created_at: Timestamp de criação
        last_accessed: Timestamp do último acesso
        metadata: Metadados adicionais
    """
    id: str
    content: str
    node_type: NodeType
    embedding: Optional[List[float]] = None
    activation_level: float = 0.0
    access_count: int = 0
    created_at: Optional[datetime] = None
    last_accessed: Optional[datetime] = None
    metadata: Optional[Dict] = None

    def __post_init__(self):
        """Inicializa campos automáticos após criação."""
        if self.created_at is None:
            self.created_at = datetime.now(timezone.utc)
        if self.metadata is None:
            self.metadata = {}

    def activate(self, strength: float = 1.0) -> None:
        """Ativa o nó com uma determinada força.
        
        Args:
            strength: Força da ativação (0.0-1.0)
        """
        self.activation_level = min(1.0, self.activation_level + strength)
        self.access_count += 1
        self.last_accessed = datetime.now(timezone.utc)

    def decay(self, decay_rate: float = 0.1) -> None:
        """Aplica decaimento à ativação do nó.
        
        Args:
            decay_rate: Taxa de decaimento (0.0-1.0)
        """
        self.activation_level = max(0.0, self.activation_level - decay_rate)


@dataclass
class CognitiveEdge:
    """Representa uma aresta no grafo cognitivo.
    
    Uma aresta cognitiva representa uma relação entre dois nós, definindo
    como conceitos se relacionam e como a ativação pode ser propagada.
    
    Attributes:
        id: Identificador único da aresta
        source_id: ID do nó origem
        target_id: ID do nó destino
        edge_type: Tipo da relação
        weight: Peso da conexão (influencia propagação)
        strength: Força da relação (pode ser aprendida)
        context: Contexto em que a relação é válida
        created_at: Timestamp de criação
        metadata: Metadados adicionais
    """
    id: str
    source_id: str
    target_id: str
    edge_type: EdgeType
    weight: float = 1.0
    strength: float = 1.0
    context: Optional[str] = None
    created_at: Optional[datetime] = None
    metadata: Optional[Dict] = None

    def __post_init__(self):
        """Inicializa campos automáticos após criação."""
        if self.created_at is None:
            self.created_at = datetime.now(timezone.utc)
        if self.metadata is None:
            self.metadata = {}