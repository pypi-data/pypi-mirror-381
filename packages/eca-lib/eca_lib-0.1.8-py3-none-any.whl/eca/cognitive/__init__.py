# -*- coding: utf-8 -*-
"""Módulo cognitivo da ECA-Lib.

Este módulo estende a arquitetura ECA com capacidades cognitivas avançadas,
incluindo grafos de conhecimento, propagação de ativação e raciocínio
baseado em relações conceituais.

O módulo é projetado para trabalhar em conjunto com o mecanismo de atenção
existente, oferecendo uma camada adicional de processamento cognitivo que
vai além do RAG tradicional.
"""

from .types import (
    NodeType,
    EdgeType,
    CognitiveNode,
    CognitiveEdge
)

from .repository import CognitiveGraphRepository
from .activation import ActivationPropagator
from .graph_attention import CognitiveGraphAttention

__all__ = [
    'NodeType',
    'EdgeType', 
    'CognitiveNode',
    'CognitiveEdge',
    'CognitiveGraphRepository',
    'ActivationPropagator',
    'CognitiveGraphAttention'
]