# -*- coding: utf-8 -*-
"""Mecanismo de atenção cognitiva que integra grafos de conhecimento.

Este módulo implementa um mecanismo de atenção avançado que combina
a busca semântica tradicional com raciocínio baseado em grafo cognitivo
e propagação de ativação, seguindo os padrões da arquitetura ECA.
"""

from typing import List, Callable, Dict, Optional, Tuple
import uuid
from datetime import datetime, timezone

from ..attention.base import AttentionMechanism, MemoryType, AttentionResult
from ..attention.vector_attention import VectorizedSemanticAttention
from .repository import CognitiveGraphRepository
from .activation import ActivationPropagator
from .types import CognitiveNode, CognitiveEdge, NodeType, EdgeType


class CognitiveGraphAttention(VectorizedSemanticAttention):
    """Mecanismo de atenção baseado em grafo cognitivo com propagação de ativação.
    
    Esta implementação estende o mecanismo de atenção vetorizada tradicional
    com capacidades de raciocínio baseado em grafo cognitivo persistido no
    PostgreSQL com pgvector. O sistema combina similaridade semântica
    tradicional com propagação de ativação através de um grafo de conhecimento.
    
    A classe segue o padrão established na arquitetura ECA, mantendo
    compatibilidade com a interface AttentionMechanism enquanto adiciona
    capacidades cognitivas avançadas.
    
    Attributes:
        repository: Repository para acesso ao grafo cognitivo
        activation_propagator: Sistema de propagação de ativação
        semantic_weight: Peso da atenção semântica tradicional
        graph_weight: Peso da atenção baseada em grafo
        activation_threshold: Threshold mínimo para ativação
        auto_create_concepts: Se deve criar conceitos automaticamente
    """
    
    def __init__(
        self, 
        embedding_function: Callable[[str], List[float]],
        repository: CognitiveGraphRepository,
        semantic_weight: float = 0.4,
        graph_weight: float = 0.6,
        activation_threshold: float = 0.1,
        auto_create_concepts: bool = True
    ):
        """Inicializa o mecanismo de atenção cognitiva.
        
        Args:
            embedding_function: Função que converte texto em embeddings
            repository: Repository para persistir o grafo no PostgreSQL
            semantic_weight: Peso da atenção semântica tradicional (0.0-1.0)
            graph_weight: Peso da atenção baseada em grafo (0.0-1.0)
            activation_threshold: Threshold mínimo para ativação
            auto_create_concepts: Se deve criar conceitos automaticamente
        """
        super().__init__(embedding_function)
        self.repository = repository
        self.activation_propagator = ActivationPropagator(repository)
        
        # Pesos para combinar diferentes tipos de atenção
        self.semantic_weight = semantic_weight
        self.graph_weight = graph_weight
        self.activation_threshold = activation_threshold
        self.auto_create_concepts = auto_create_concepts
        
        # Cache para embeddings de conceitos
        self._concept_embeddings: Dict[str, List[float]] = {}
    
    def rank(self, user_input: str, memories: List[MemoryType]) -> List[MemoryType]:
        """Rankeia memórias usando combinação de atenção semântica e grafo cognitivo.
        
        Esta implementação combina a atenção semântica tradicional (herdada da
        classe pai) com raciocínio baseado em grafo cognitivo, permitindo uma
        compreensão mais profunda das relações entre conceitos.
        
        Args:
            user_input: Entrada do usuário para ranqueamento
            memories: Lista de memórias a serem ranqueadas
            
        Returns:
            Lista de memórias ranqueadas por relevância cognitiva
        """
        if not memories:
            return []
        
        try:
            # 1. Atenção semântica tradicional (baseline)
            semantic_scores = self._compute_semantic_scores(user_input, memories)
            
            # 2. Atenção cognitiva baseada em grafo
            cognitive_scores = self._compute_cognitive_scores(user_input, memories)
            
            # 3. Combina as duas formas de atenção
            combined_scores = self._combine_attention_scores(
                semantic_scores, cognitive_scores, memories
            )
            
            # 4. Ordena por score combinado
            ranked_memories = sorted(
                combined_scores, 
                key=lambda x: x[1], 
                reverse=True
            )
            
            return [memory for memory, score in ranked_memories]
            
        except Exception as e:
            print(f"Erro no mecanismo de atenção cognitiva: {e}")
            # Fallback para atenção semântica tradicional
            return super().rank(user_input, memories)
    
    def _compute_semantic_scores(
        self, 
        user_input: str, 
        memories: List[MemoryType]
    ) -> Dict[str, float]:
        """Computa scores de atenção semântica tradicional.
        
        Args:
            user_input: Entrada do usuário
            memories: Lista de memórias
            
        Returns:
            Mapeamento de memory_id -> score semântico
        """
        input_embedding = self.embed(user_input)
        semantic_scores = {}
        
        for i, memory in enumerate(memories):
            memory_id = f"memory_{i}"
            
            if hasattr(memory, 'embedding') and memory.embedding:
                score = self._cosine_similarity(input_embedding, memory.embedding)
                semantic_scores[memory_id] = score
            else:
                semantic_scores[memory_id] = 0.0
        
        return semantic_scores
    
    def _compute_cognitive_scores(
        self, 
        user_input: str, 
        memories: List[MemoryType]
    ) -> Dict[str, float]:
        """Computa scores usando propagação de ativação no grafo cognitivo.
        
        Args:
            user_input: Entrada do usuário
            memories: Lista de memórias
            
        Returns:
            Mapeamento de memory_id -> score cognitivo
        """
        try:
            # 1. Encontra conceitos relevantes na entrada
            relevant_concepts = self._find_relevant_concepts(user_input)
            
            # 2. Ativação inicial baseada nos conceitos
            initial_activation = self._compute_initial_activation(relevant_concepts)
            
            if not initial_activation:
                return {f"memory_{i}": 0.0 for i in range(len(memories))}
            
            # 3. Propaga ativação pelo grafo
            activation_map = self.activation_propagator.propagate_activation(initial_activation)
            
            # 4. Mapeia ativação para scores das memórias
            return self._map_activation_to_memories(activation_map, memories)
            
        except Exception as e:
            print(f"Erro no cálculo de scores cognitivos: {e}")
            return {f"memory_{i}": 0.0 for i in range(len(memories))}
    
    def _find_relevant_concepts(self, user_input: str) -> List[CognitiveNode]:
        """Encontra conceitos relevantes no grafo para a entrada do usuário.
        
        Args:
            user_input: Entrada do usuário
            
        Returns:
            Lista de nós cognitivos relevantes
        """
        try:
            input_embedding = self.embed(user_input)
            
            # Busca conceitos similares usando pgvector
            similar_nodes = self.repository.find_similar_nodes(
                embedding=input_embedding,
                limit=10,
                similarity_threshold=0.3
            )
            
            # Filtra apenas conceitos
            relevant_concepts = [
                node for node in similar_nodes 
                if node.node_type == NodeType.CONCEPT
            ]
            
            # Se não encontrou conceitos e auto_create está habilitado, cria novos
            if not relevant_concepts and self.auto_create_concepts:
                new_concept = self._create_concept_from_input(user_input)
                if new_concept:
                    relevant_concepts = [new_concept]
            
            return relevant_concepts
            
        except Exception as e:
            print(f"Erro ao encontrar conceitos relevantes: {e}")
            return []
    
    def _create_concept_from_input(self, user_input: str) -> Optional[CognitiveNode]:
        """Cria um novo conceito a partir da entrada do usuário.
        
        Args:
            user_input: Entrada do usuário
            
        Returns:
            Novo nó cognitivo ou None se houve erro
        """
        try:
            concept_embedding = self.embed(user_input)
            
            concept_node = CognitiveNode(
                id=f"concept_{uuid.uuid4().hex[:8]}",
                content=user_input,
                node_type=NodeType.CONCEPT,
                embedding=concept_embedding,
                activation_level=0.5,  # ativação inicial moderada
                access_count=1,
                created_at=datetime.now(timezone.utc),
                last_accessed=datetime.now(timezone.utc),
                metadata={'auto_created': True, 'source': 'user_input'}
            )
            
            # Salva no banco
            self.repository.save_node(concept_node)
            return concept_node
            
        except Exception as e:
            print(f"Erro ao criar conceito automático: {e}")
            return None
    
    def _compute_initial_activation(self, concepts: List[CognitiveNode]) -> Dict[str, float]:
        """Computa ativação inicial para os conceitos identificados.
        
        Args:
            concepts: Lista de conceitos relevantes
            
        Returns:
            Mapeamento de conceito_id -> ativação inicial
        """
        if not concepts:
            return {}
        
        # Distribui ativação com base na similaridade e acesso
        initial_activation = {}
        total_weight = 0
        
        for concept in concepts:
            # Peso baseado no histórico de acesso e ativação atual
            weight = 1.0 + (concept.access_count * 0.1) + concept.activation_level
            initial_activation[concept.id] = weight
            total_weight += weight
        
        # Normaliza para que a soma seja 1.0
        if total_weight > 0:
            for concept_id in initial_activation:
                initial_activation[concept_id] /= total_weight
        
        return initial_activation
    
    def _map_activation_to_memories(
        self, 
        activation_map: Dict[str, float], 
        memories: List[MemoryType]
    ) -> Dict[str, float]:
        """Mapeia ativação do grafo para scores das memórias.
        
        Args:
            activation_map: Mapeamento de ativação do grafo
            memories: Lista de memórias
            
        Returns:
            Mapeamento de memory_id -> score cognitivo
        """
        cognitive_scores = {}
        
        for i, memory in enumerate(memories):
            memory_id = f"memory_{i}"
            total_activation = 0.0
            
            try:
                # Busca nós relacionados à memória no grafo
                related_nodes = self._find_nodes_related_to_memory(memory)
                
                # Soma ativação dos nós relacionados
                for node_id in related_nodes:
                    if node_id in activation_map:
                        total_activation += activation_map[node_id]
                
            except Exception as e:
                print(f"Erro ao mapear ativação para memória {i}: {e}")
                total_activation = 0.0
            
            cognitive_scores[memory_id] = total_activation
        
        return cognitive_scores
    
    def _find_nodes_related_to_memory(self, memory: MemoryType) -> List[str]:
        """Encontra nós do grafo relacionados a uma memória específica.
        
        Args:
            memory: Memória para encontrar nós relacionados
            
        Returns:
            Lista de IDs de nós relacionados
        """
        related_nodes = []
        
        try:
            # Se a memória tem conteúdo, busca conceitos similares
            if hasattr(memory, 'content'):
                memory_embedding = None
                
                if hasattr(memory, 'embedding') and memory.embedding:
                    memory_embedding = memory.embedding
                else:
                    # Gera embedding para o conteúdo da memória
                    memory_embedding = self.embed(str(memory.content))
                
                if memory_embedding:
                    # Busca nós similares usando pgvector
                    similar_nodes = self.repository.find_similar_nodes(
                        embedding=memory_embedding,
                        limit=5,
                        similarity_threshold=0.2  # threshold mais baixo para memórias
                    )
                    
                    related_nodes = [node.id for node in similar_nodes]
        
        except Exception as e:
            print(f"Erro ao encontrar nós relacionados à memória: {e}")
        
        return related_nodes
    
    def _combine_attention_scores(
        self, 
        semantic_scores: Dict[str, float], 
        cognitive_scores: Dict[str, float], 
        memories: List[MemoryType]
    ) -> List[Tuple[MemoryType, float]]:
        """Combina scores semânticos e cognitivos.
        
        Args:
            semantic_scores: Scores de atenção semântica
            cognitive_scores: Scores de atenção cognitiva
            memories: Lista de memórias
            
        Returns:
            Lista de tuplas (memória, score_combinado)
        """
        combined_scores = []
        
        for i, memory in enumerate(memories):
            memory_id = f"memory_{i}"
            
            semantic_score = semantic_scores.get(memory_id, 0.0)
            cognitive_score = cognitive_scores.get(memory_id, 0.0)
            
            # Combinação ponderada
            final_score = (
                self.semantic_weight * semantic_score + 
                self.graph_weight * cognitive_score
            )
            
            combined_scores.append((memory, final_score))
        
        return combined_scores
    
    def add_concept(
        self, 
        concept_text: str, 
        node_type: NodeType = NodeType.CONCEPT,
        metadata: Optional[Dict] = None
    ) -> str:
        """Adiciona um novo conceito ao grafo cognitivo.
        
        Args:
            concept_text: Texto do conceito
            node_type: Tipo do nó
            metadata: Metadados adicionais
            
        Returns:
            ID do conceito criado
        """
        concept_embedding = self.embed(concept_text)
        
        node = CognitiveNode(
            id=f"{node_type.value}_{uuid.uuid4().hex[:8]}",
            content=concept_text,
            node_type=node_type,
            embedding=concept_embedding,
            created_at=datetime.utcnow(),
            metadata=metadata or {}
        )
        
        self.repository.save_node(node)
        return node.id
    
    def add_relationship(
        self, 
        source_concept: str, 
        target_concept: str, 
        relationship_type: EdgeType,
        weight: float = 1.0,
        context: Optional[str] = None
    ) -> str:
        """Adiciona uma relação entre dois conceitos.
        
        Args:
            source_concept: ID do conceito origem
            target_concept: ID do conceito destino
            relationship_type: Tipo da relação
            weight: Peso da relação
            context: Contexto da relação
            
        Returns:
            ID da aresta criada
        """
        edge = CognitiveEdge(
            id=f"edge_{uuid.uuid4().hex[:8]}",
            source_id=source_concept,
            target_id=target_concept,
            edge_type=relationship_type,
            weight=weight,
            context=context,
            created_at=datetime.utcnow()
        )
        
        self.repository.save_edge(edge)
        return edge.id
    
    def rank_with_details(
        self, 
        user_input: str, 
        memories: List[MemoryType]
    ) -> AttentionResult:
        """Versão estendida que retorna detalhes do processamento cognitivo.
        
        Esta implementação fornece informações detalhadas sobre o processo
        de raciocínio cognitivo para enriquecer o contexto do LLM.
        """
        if not memories:
            return AttentionResult(
                memories=[], 
                scores=[], 
                metadata={},
                explanation="No memories to rank"
            )

        try:
            # 1. Encontra conceitos relevantes
            relevant_concepts = self._find_relevant_concepts(user_input)
            
            # 2. Computa ativação inicial
            initial_activation = self._compute_initial_activation(relevant_concepts)
            
            # 3. Propaga ativação (se há conceitos)
            activation_map = {}
            if initial_activation:
                activation_map = self.activation_propagator.propagate_activation(initial_activation)
            
            # 4. Rankeia memórias
            ranked_memories = self.rank(user_input, memories)
            
            # 5. Computa scores detalhados
            semantic_scores = self._compute_semantic_scores(user_input, memories)
            cognitive_scores = self._compute_cognitive_scores(user_input, memories)
            
            # 6. Prepara metadados ricos
            metadata = {
                'cognitive_process_used': len(relevant_concepts) > 0,
                'activated_concepts': [concept.content for concept in relevant_concepts],
                'initial_activation_strength': sum(initial_activation.values()) if initial_activation else 0.0,
                'total_activated_nodes': len(activation_map),
                'semantic_weight': self.semantic_weight,
                'graph_weight': self.graph_weight,
                'activation_threshold': self.activation_threshold,
                'auto_concepts_created': sum(1 for c in relevant_concepts if c.metadata.get('auto_created', False)),
                'avg_semantic_score': sum(semantic_scores.values()) / len(semantic_scores) if semantic_scores else 0.0,
                'avg_cognitive_score': sum(cognitive_scores.values()) / len(cognitive_scores) if cognitive_scores else 0.0
            }
            
            # 7. Identifica clusters de ativação
            if activation_map:
                clusters = self.activation_propagator.get_activation_clusters(activation_map)
                metadata['activation_clusters'] = [len(cluster) for cluster in clusters]
                metadata['num_clusters'] = len(clusters)
            else:
                metadata['activation_clusters'] = []
                metadata['num_clusters'] = 0
            
            # 8. Gera explicação do raciocínio
            explanation = self._generate_reasoning_explanation(
                user_input, relevant_concepts, activation_map, len(ranked_memories)
            )
            
            return AttentionResult(
                memories=ranked_memories,
                scores=list(semantic_scores.values()) + list(cognitive_scores.values()),
                metadata=metadata,
                explanation=explanation
            )
            
        except Exception as e:
            # Fallback para atenção semântica tradicional
            fallback_result = super().rank_with_details(user_input, memories)
            fallback_result.metadata = {
                'cognitive_process_used': False,
                'fallback_reason': str(e),
                'semantic_weight': 1.0,
                'graph_weight': 0.0
            }
            return fallback_result
    
    def _generate_reasoning_explanation(
        self, 
        user_input: str, 
        concepts: List, 
        activation_map: Dict[str, float], 
        num_memories: int
    ) -> str:
        """Gera explicação human-readable do processo de raciocínio."""
        if not concepts:
            return f"Used semantic similarity only to rank {num_memories} memories"
        
        concept_names = [c.content for c in concepts[:3]]
        activated_nodes = len(activation_map)
        
        explanation = f"Cognitive reasoning: Activated {len(concepts)} concepts ({', '.join(concept_names)})"
        
        if activated_nodes > len(concepts):
            explanation += f", propagated to {activated_nodes} total nodes"
        
        explanation += f", ranked {num_memories} memories using hybrid attention"
        
        return explanation