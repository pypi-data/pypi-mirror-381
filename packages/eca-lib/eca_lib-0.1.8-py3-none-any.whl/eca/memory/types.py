# -*- coding: utf-8 -*-
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any
from datetime import datetime


@dataclass
class SemanticMemory:
    """Representa uma única unidade de conhecimento na memória de longo prazo.

    Esta estrutura de dados encapsula um "fato", "regra" ou qualquer outra
    peça de informação que o agente conhece. É independente de qualquer
    conversa específica (context-free) e forma a base de conhecimento do agente.

    Attributes:
        id (str): Um identificador único para esta unidade de memória.
        domain_id (str): A categoria ou domínio ao qual esta memória pertence
            (ex: "fiscal", "vendas").
        type (str): O tipo específico de memória (ex: "fato", "regra_procedural").
        text_content (str): O conteúdo da memória em texto legível por humanos.
        embedding (Optional[List[float]]): Opcional. A representação vetorial
            (embedding) do `text_content`, usada para buscas de similaridade
            semântica.
        metadata (Dict[str, Any]): Um dicionário para armazenar quaisquer dados
            adicionais e flexíveis associados a esta memória.
    """
    id: str
    domain_id: str
    type: str
    text_content: str
    embedding: Optional[List[float]] = None
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class EpisodicMemory:
    """Representa um único turno de interação na memória de curto prazo.

    Esta estrutura de dados registra uma troca completa entre um usuário e o
    assistente, formando o histórico da conversa. É a base para a capacidade

    do agente de se lembrar do que foi dito anteriormente em uma sessão.

    Attributes:
        user_id (str): O identificador único do usuário envolvido na interação.
        domain_id (str): O domínio de conhecimento em que a interação ocorreu.
        user_input (str): O texto exato que o usuário enviou.
        assistant_output (str): A resposta exata que o assistente forneceu.
        timestamp (str): O momento em que a interação ocorreu, geralmente em
            formato ISO 8601.
    """
    user_id: str
    domain_id: str
    user_input: str
    assistant_output: str
    timestamp: str


@dataclass
class InteractionLog:
    """Log de uma interação específica entre usuário e assistente.
    
    Esta classe representa uma única troca de pergunta/resposta,
    incluindo metadados sobre o contexto e qualidade da interação.
    
    Attributes:
        input_text (str): Texto de entrada do usuário
        output_text (str): Resposta gerada pelo assistente
        timestamp (Optional[datetime]): Momento da interação
        metadata (Dict[str, Any]): Metadados adicionais sobre a interação
    """
    input_text: str
    output_text: str
    timestamp: Optional[datetime] = None
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def __post_init__(self):
        """Inicializa timestamp se não fornecido."""
        if self.timestamp is None:
            self.timestamp = datetime.now()


@dataclass
class EpisodicMemory:
    """Representa um único turno de interação na memória de curto prazo.

    Esta estrutura de dados registra uma troca completa entre um usuário e o
    assistente, formando o histórico da conversa. É a base para a capacidade
    do agente de se lembrar do que foi dito anteriormente em uma sessão.

    Attributes:
        id (str): Identificador único da memória episódica
        user_id (str): O identificador único do usuário envolvido na interação.
        domain_id (str): O domínio de conhecimento em que a interação ocorreu.
        timestamp (datetime): O momento em que a interação ocorreu.
        context_summary (str): Resumo do contexto da interação
        interaction_log (InteractionLog): Log detalhado da interação
        metadata (Dict[str, Any]): Metadados adicionais
    """
    id: str
    user_id: str
    domain_id: str
    timestamp: datetime
    context_summary: str
    interaction_log: InteractionLog
    metadata: Dict[str, Any] = field(default_factory=dict)