# -*- coding: utf-8 -*-
"""Testes para o sistema cognitivo com cenários realistas de agentes inteligentes.

Esta suíte demonstra o poder completo do sistema cognitivo da ECA-Lib,
incluindo grafos de conhecimento, propagação de ativação e raciocínio complexo.
"""

import pytest
import uuid
from unittest.mock import Mock, patch
from datetime import datetime
from typing import List, Dict, Any

from eca.orchestrator import ECAOrchestrator
from eca.memory.types import SemanticMemory
from eca.models import Persona, PersonaConfig


class TestCognitiveSystem:
    """Testes abrangentes do sistema cognitivo."""

    @pytest.fixture
    def mock_postgres_connection(self):
        """Mock da conexão PostgreSQL para testes."""
        return "postgresql://test:test@localhost:5432/test_eca_cognitive"

    @pytest.fixture
    def cognitive_embedding_function(self):
        """Função de embedding mais realista para testes cognitivos."""
        def embedding_func(text: str) -> List[float]:
            # Simula embeddings mais realistas baseados em conteúdo semântico
            words = text.lower().split()
            embedding = [0.0] * 384
            
            # Mapeia palavras-chave para dimensões específicas
            keyword_mappings = {
                # Conceitos de negócio
                "vendas": 0, "faturamento": 1, "receita": 2, "lucro": 3,
                "estoque": 10, "produto": 11, "inventário": 12, "armazém": 13,
                "cliente": 20, "comprador": 21, "consumidor": 22,
                "marketing": 30, "campanha": 31, "publicidade": 32,
                
                # Conceitos de café (domínio específico)
                "café": 50, "grãos": 51, "moagem": 52, "preparo": 53,
                "temperatura": 60, "água": 61, "pressão": 62,
                "arábica": 70, "robusta": 71, "blend": 72,
                
                # Conceitos temporais
                "hoje": 80, "ontem": 81, "semana": 82, "mês": 83,
                "trimestre": 84, "ano": 85,
                
                # Conceitos quantitativos
                "alto": 90, "baixo": 91, "crescimento": 92, "queda": 93,
                "aumento": 94, "diminuição": 95
            }
            
            for word in words:
                if word in keyword_mappings:
                    dim = keyword_mappings[word]
                    embedding[dim] = 0.8
                    # Adiciona ativação nas dimensões vizinhas
                    if dim > 0:
                        embedding[dim-1] = 0.3
                    if dim < 383:
                        embedding[dim+1] = 0.3
            
            # Adiciona ruído baseado no hash para diferenciação
            for i, char in enumerate(text[:20]):
                dim = (ord(char) + i) % 384
                embedding[dim] += 0.1
            
            return embedding
        
        return embedding_func

    @pytest.fixture
    def coffee_business_memories(self, cognitive_embedding_function):
        """Memórias semânticas para um negócio de café."""
        embed = cognitive_embedding_function
        
        return [
            # Conhecimento sobre produtos
            SemanticMemory(
                id="coffee_001",
                domain_id="sales_analyst",
                type="product_knowledge",
                text_content="Café Arábica Premium é nosso produto estrela, com margem de 45% e alta demanda matinal",
                embedding=embed("café arábica premium produto estrela margem alta demanda matinal")
            ),
            
            SemanticMemory(
                id="coffee_002", 
                domain_id="sales_analyst",
                type="market_insight",
                text_content="Vendas de café aumentam 30% durante o inverno e em segundas-feiras",
                embedding=embed("vendas café aumentam inverno segundas-feiras sazonal")
            ),
            
            SemanticMemory(
                id="coffee_003",
                domain_id="barista_expert",
                type="brewing_knowledge", 
                text_content="Temperatura ideal para extração do café é 90-96°C, tempo de contato 4 minutos",
                embedding=embed("temperatura ideal extração café 90 96 graus tempo contato 4 minutos")
            ),
            
            SemanticMemory(
                id="coffee_004",
                domain_id="barista_expert", 
                type="quality_control",
                text_content="Grãos torrados há mais de 15 dias perdem 40% dos óleos essenciais e sabor",
                embedding=embed("grãos torrados 15 dias perdem óleos essenciais sabor qualidade")
            ),
            
            # Conhecimento sobre clientes
            SemanticMemory(
                id="customer_001",
                domain_id="sales_analyst",
                type="customer_behavior",
                text_content="Clientes corporativos preferem compras em grande volume com desconto progressivo",
                embedding=embed("clientes corporativos compras grande volume desconto progressivo")
            ),
            
            SemanticMemory(
                id="customer_002",
                domain_id="marketing_specialist", 
                type="segmentation",
                text_content="Millennials valorizam origem sustentável e certificação orgânica do café",
                embedding=embed("millennials valorizam origem sustentável certificação orgânica café")
            ),
            
            # Conhecimento operacional
            SemanticMemory(
                id="ops_001",
                domain_id="inventory_manager",
                type="supply_chain",
                text_content="Fornecedor brasileiro entrega em 7 dias, colombiano em 15 dias úteis",
                embedding=embed("fornecedor brasileiro entrega 7 dias colombiano 15 dias úteis")
            ),
            
            SemanticMemory(
                id="ops_002",
                domain_id="inventory_manager",
                type="storage_rule", 
                text_content="Café em grão deve ser armazenado em local seco, temperatura máxima 25°C",
                embedding=embed("café grão armazenado local seco temperatura máxima 25 graus")
            ),
            
            # Insights de negócio
            SemanticMemory(
                id="insight_001",
                domain_id="business_analyst",
                type="correlation",
                text_content="Aumento de 10% no preço do café reduz vendas em 15% mas aumenta margem total",
                embedding=embed("aumento 10 preço café reduz vendas 15 aumenta margem total")
            ),
            
            SemanticMemory(
                id="insight_002",
                domain_id="business_analyst", 
                type="trend_analysis",
                text_content="Cafés especiais crescem 25% ao ano enquanto café commodity decresce 5%",
                embedding=embed("cafés especiais crescem 25 ano commodity decresce 5 tendência")
            )
        ]

    @pytest.fixture
    def specialized_personas(self):
        """Personas especializadas para negócio de café."""
        return {
            "sales_analyst": Persona(
                id="sales_analyst",
                name="VENDAX-CAFÉ",
                semantic_description="Especialista em análise de vendas de café e bebidas",
                config=PersonaConfig(
                    persona="Você é VENDAX-CAFÉ, especialista em análise de vendas no mercado de café",
                    objective="Maximizar receita através de análise profunda de dados de vendas de café",
                    tone_of_voice=["Analítico", "Orientado a dados", "Estratégico"],
                    verbosity="detailed",
                    output_format="Inicie com métricas-chave, seguido de insights acionáveis e recomendações",
                    forbidden_topics=["Informações de fornecedores", "Custos internos"],
                    golden_rules=[
                        "Sempre correlacionar vendas com fatores sazonais",
                        "Considerar margem e volume simultaneamente",
                        "Identificar padrões de comportamento do cliente"
                    ]
                )
            ),
            
            "barista_expert": Persona(
                id="barista_expert", 
                name="MASTER-BREW",
                semantic_description="Especialista em preparo e qualidade de café",
                config=PersonaConfig(
                    persona="Você é MASTER-BREW, mestre em técnicas de preparo e qualidade do café",
                    objective="Garantir excelência na qualidade e preparo do café",
                    tone_of_voice=["Técnico", "Apaixonado", "Detalhista"],
                    verbosity="normal",
                    output_format="Explique o processo passo a passo com justificativas técnicas",
                    forbidden_topics=["Preços de venda", "Estratégias comerciais"],
                    golden_rules=[
                        "Qualidade sempre vem antes de velocidade",
                        "Cada grão tem seu método ideal de preparo", 
                        "Temperatura e tempo são fundamentais"
                    ]
                )
            ),
            
            "marketing_specialist": Persona(
                id="marketing_specialist",
                name="CAFÉ-MARKETING",
                semantic_description="Especialista em marketing para mercado de café",
                config=PersonaConfig(
                    persona="Você é CAFÉ-MARKETING, especialista em estratégias de marketing para café",
                    objective="Criar campanhas efetivas que conectem consumidores ao café ideal",
                    tone_of_voice=["Criativo", "Persuasivo", "Centrado no cliente"],
                    verbosity="concise",
                    output_format="Apresente a estratégia com públicos-alvo, mensagens e canais",
                    forbidden_topics=["Dados financeiros confidenciais"],
                    golden_rules=[
                        "Cada segmento tem suas motivações únicas",
                        "História e origem do café são poderosas",
                        "Experiência sensorial é fundamental"
                    ]
                )
            ),
            
            "business_analyst": Persona(
                id="business_analyst",
                name="CAFÉ-STRATEGY", 
                semantic_description="Analista estratégico para negócios de café",
                config=PersonaConfig(
                    persona="Você é CAFÉ-STRATEGY, analista estratégico especializado no mercado de café",
                    objective="Fornecer insights estratégicos para crescimento sustentável do negócio",
                    tone_of_voice=["Estratégico", "Visionário", "Baseado em evidências"],
                    verbosity="detailed",
                    output_format="Estruture como: Situação Atual -> Análise -> Oportunidades -> Recomendações",
                    forbidden_topics=["Informações de concorrentes específicos"],
                    golden_rules=[
                        "Sempre considerar tendências de longo prazo",
                        "Balancear crescimento com sustentabilidade",
                        "Dados devem guiar todas as decisões estratégicas"
                    ]
                )
            )
        }

    def test_cognitive_system_available(self):
        """Testa se o sistema cognitivo está disponível."""
        try:
            from eca.cognitive import CognitiveGraphAttention, CognitiveGraphRepository
            assert True, "Sistema cognitivo disponível"
        except ImportError:
            pytest.skip("Sistema cognitivo não disponível (PostgreSQL/pgvector não configurado)")

    @patch('eca.cognitive.repository.CognitiveGraphRepository')
    def test_cognitive_attention_integration(self, mock_repo_class, specialized_personas, coffee_business_memories, cognitive_embedding_function):
        """Testa integração completa do sistema de atenção cognitiva."""
        # Mock do repository
        mock_repo = Mock()
        mock_repo_class.return_value = mock_repo
        
        # Mock dos métodos do repository
        mock_repo.find_similar_nodes.return_value = []
        mock_repo.get_edges_from_node.return_value = []
        mock_repo.get_edges_to_node.return_value = []
        
        try:
            from eca.cognitive import CognitiveGraphAttention
            
            # Cria attention cognitivo
            cognitive_attention = CognitiveGraphAttention(
                embedding_function=cognitive_embedding_function,
                repository=mock_repo,
                semantic_weight=0.3,
                graph_weight=0.7
            )
            
            # Testa ranqueamento cognitivo
            user_query = "Como melhorar as vendas de café durante o verão?"
            relevant_memories = [
                mem for mem in coffee_business_memories 
                if "vendas" in mem.text_content or "café" in mem.text_content
            ]
            
            ranked_memories = cognitive_attention.rank(user_query, relevant_memories)
            
            # Verifica se o ranqueamento funcionou
            assert len(ranked_memories) > 0
            assert ranked_memories[0] in relevant_memories
            
            # Testa versão com detalhes
            attention_result = cognitive_attention.rank_with_details(user_query, relevant_memories)
            
            assert attention_result.memories is not None
            assert attention_result.metadata is not None
            assert attention_result.explanation is not None
            
        except ImportError:
            pytest.skip("Sistema cognitivo não disponível")

    def test_sales_analysis_scenario(self, specialized_personas, coffee_business_memories):
        """Cenário: Análise de vendas com raciocínio cognitivo."""
        # Setup mocks
        persona_provider = Mock()
        persona_provider.detect_domain.return_value = "sales_analyst"
        persona_provider.get_persona_by_id.return_value = specialized_personas["sales_analyst"]

        memory_provider = Mock()
        memory_provider.fetch_semantic_memories.return_value = [
            mem for mem in coffee_business_memories
            if mem.domain_id == "sales_analyst"
        ]
        memory_provider.fetch_episodic_memories.return_value = []

        # Mock workspace mais realista
        from eca.models import CognitiveWorkspace, DomainState
        mock_workspace = CognitiveWorkspace(
            user_id="gerente_vendas",
            current_focus="sales_analyst",
            active_domains={"sales_analyst": DomainState(status="active")}
        )

        session_provider = Mock()
        session_provider.get_workspace.return_value = mock_workspace

        # Cria orquestrador
        orchestrator = ECAOrchestrator(
            persona_provider=persona_provider,
            memory_provider=memory_provider,
            session_provider=session_provider
        )

        # Consulta complexa sobre vendas
        user_query = "Preciso entender por que as vendas de café caíram 15% no último mês e como reverter essa tendência"

        # Gera contexto
        context = orchestrator.generate_context_object(
            user_id="gerente_vendas",
            user_input=user_query
        )

        # Gera prompt final
        final_prompt = orchestrator.generate_final_prompt(
            user_id="gerente_vendas", 
            user_input=user_query
        )

        # Validações
        assert "[IDENTITY:VENDAX-CAFÉ|SALES_ANALYST|" in final_prompt
        assert "Maximizar receita através de análise profunda" in final_prompt
        assert "vendas de café caíram 15%" in final_prompt
        assert len(context.active_domains) > 0

    def test_barista_consultation_scenario(self, specialized_personas, coffee_business_memories):
        """Cenário: Consulta técnica ao especialista em café."""
        # Setup mocks
        persona_provider = Mock()
        persona_provider.detect_domain.return_value = "barista_expert"
        persona_provider.get_persona_by_id.return_value = specialized_personas["barista_expert"]

        memory_provider = Mock()
        memory_provider.fetch_semantic_memories.return_value = [
            mem for mem in coffee_business_memories
            if mem.domain_id == "barista_expert"
        ]
        memory_provider.fetch_episodic_memories.return_value = []

        # Mock workspace mais realista
        from eca.models import CognitiveWorkspace, DomainState
        mock_workspace = CognitiveWorkspace(
            user_id="barista_junior",
            current_focus="barista_expert",
            active_domains={"barista_expert": DomainState(status="active")}
        )

        session_provider = Mock()
        session_provider.get_workspace.return_value = mock_workspace

        orchestrator = ECAOrchestrator(
            persona_provider=persona_provider,
            memory_provider=memory_provider,
            session_provider=session_provider
        )

        # Consulta técnica sobre preparo
        user_query = "Os clientes reclamam que o café está amargo. Como ajustar o preparo para melhorar o sabor?"

        final_prompt = orchestrator.generate_final_prompt(
            user_id="barista_junior",
            user_input=user_query
        )

        # Validações específicas do domínio
        assert "[IDENTITY:MASTER-BREW|BARISTA_EXPERT|" in final_prompt
        assert "Garantir excelência na qualidade" in final_prompt
        assert "Qualidade sempre vem antes de velocidade" in final_prompt
        assert "café está amargo" in final_prompt

    def test_multi_domain_cognitive_reasoning(self, specialized_personas, coffee_business_memories):
        """Cenário: Raciocínio cognitivo complexo envolvendo múltiplos domínios."""
        # Setup para simular troca de contexto
        persona_provider = Mock()
        
        def dynamic_domain_detection(user_input: str) -> str:
            if "vendas" in user_input.lower() or "faturamento" in user_input.lower():
                return "sales_analyst"
            elif "marketing" in user_input.lower() or "campanha" in user_input.lower():
                return "marketing_specialist"
            elif "preparo" in user_input.lower() or ("qualidade" in user_input.lower() and "campanha" not in user_input.lower()):
                return "barista_expert"
            else:
                return "business_analyst"
        
        persona_provider.detect_domain.side_effect = dynamic_domain_detection
        persona_provider.get_persona_by_id.side_effect = lambda pid: specialized_personas.get(pid)
        
        memory_provider = Mock()
        memory_provider.fetch_semantic_memories.side_effect = lambda ui, domain_id=None: [
            mem for mem in coffee_business_memories if not domain_id or mem.domain_id == domain_id
        ]
        memory_provider.fetch_episodic_memories.return_value = []
        
        session_provider = Mock()
        # Mock workspace inicial
        from eca.models import CognitiveWorkspace, DomainState
        mock_workspace = CognitiveWorkspace(
            user_id="strategy_team",
            current_focus="sales_analyst",
            active_domains={}
        )
        session_provider.get_workspace.return_value = mock_workspace
        session_provider.save_workspace.return_value = None
        
        orchestrator = ECAOrchestrator(
            persona_provider=persona_provider,
            memory_provider=memory_provider,
            session_provider=session_provider
        )
        
        # Sequência de consultas que demonstra raciocínio multi-domínio
        queries = [
            ("Nossas vendas de café especial estão baixas", "sales_analyst"),
            ("Isso pode ser problema de qualidade no preparo?", "barista_expert"),
            ("Como criar uma campanha para destacar a qualidade?", "marketing_specialist"),
            ("Qual o impacto estratégico dessas ações?", "business_analyst")
        ]
        
        contexts = []
        prompts = []
        
        for query, expected_domain in queries:
            context = orchestrator.generate_context_object("strategy_team", query)
            prompt = orchestrator.generate_final_prompt("strategy_team", query)
            
            contexts.append(context)
            prompts.append(prompt)
            
            # Valida detecção de domínio
            assert context.current_focus == expected_domain
            
            # Valida persona correta no prompt
            expected_name = specialized_personas[expected_domain].name
            assert f"[IDENTITY:{expected_name}|" in prompt
        
        # Valida que o sistema mantém contexto entre trocas
        assert len(contexts) == 4
        assert len(prompts) == 4

    def test_cognitive_memory_activation_patterns(self, coffee_business_memories, cognitive_embedding_function):
        """Testa padrões de ativação cognitiva em memórias relacionadas."""
        try:
            from eca.cognitive import CognitiveGraphAttention
            from eca.cognitive.repository import CognitiveGraphRepository
            
            # Mock do repository
            mock_repo = Mock()
            mock_repo.find_similar_nodes.return_value = []
            mock_repo.get_edges_from_node.return_value = []
            mock_repo.get_edges_to_node.return_value = []
            
            cognitive_attention = CognitiveGraphAttention(
                embedding_function=cognitive_embedding_function,
                repository=mock_repo
            )
            
            # Consulta que deve ativar múltiplos conceitos relacionados
            complex_query = "Como a temperatura de preparo afeta as vendas de café premium?"
            
            # Memórias que deveriam ser altamente relevantes
            relevant_memories = [
                mem for mem in coffee_business_memories
                if any(keyword in mem.text_content.lower() for keyword in 
                       ["temperatura", "preparo", "vendas", "premium", "qualidade"])
            ]
            
            # Executa atenção cognitiva
            result = cognitive_attention.rank_with_details(complex_query, relevant_memories)
            
            # Validações cognitivas
            assert result.metadata is not None
            assert "cognitive_process_used" in result.metadata
            
            if result.metadata.get("cognitive_process_used", False):
                assert "activated_concepts" in result.metadata
                assert len(result.metadata["activated_concepts"]) > 0
                
                # Verifica se conceitos relacionados foram ativados
                activated = result.metadata["activated_concepts"]
                assert any("temperatura" in concept.lower() for concept in activated)
            
        except ImportError:
            pytest.skip("Sistema cognitivo não disponível")

    def test_business_intelligence_scenario(self, specialized_personas, coffee_business_memories):
        """Cenário avançado: Análise de inteligência de negócios."""
        # Simula uma consulta complexa de BI
        persona_provider = Mock()
        persona_provider.detect_domain.return_value = "business_analyst"
        persona_provider.get_persona_by_id.return_value = specialized_personas["business_analyst"]
        
        memory_provider = Mock()
        # Retorna todas as memórias para análise cruzada
        memory_provider.fetch_semantic_memories.return_value = coffee_business_memories
        memory_provider.fetch_episodic_memories.return_value = []
        
        session_provider = Mock()
        # Mock workspace mais realista
        from eca.models import CognitiveWorkspace, DomainState
        mock_workspace = CognitiveWorkspace(
            user_id="ceo_coffee_corp",
            current_focus="business_analyst",
            active_domains={"business_analyst": DomainState(status="active")}
        )
        session_provider.get_workspace.return_value = mock_workspace
        
        orchestrator = ECAOrchestrator(
            persona_provider=persona_provider,
            memory_provider=memory_provider,
            session_provider=session_provider
        )
        
        # Consulta estratégica complexa
        strategic_query = """
        Considerando que nossos cafés especiais crescem 25% ao ano mas representam baixo volume,
        e que clientes millennials valorizam sustentabilidade, qual estratégia devemos adotar
        para os próximos 2 anos para maximizar receita e market share?
        """
        
        final_prompt = orchestrator.generate_final_prompt(
            user_id="ceo_coffee_corp",
            user_input=strategic_query
        )
        
        # Validações estratégicas
        assert "[IDENTITY:CAFÉ-STRATEGY|BUSINESS_ANALYST|" in final_prompt
        assert "crescimento sustentável do negócio" in final_prompt
        assert "Situação Atual -> Análise -> Oportunidades -> Recomendações" in final_prompt
        assert "cafés especiais crescem 25%" in final_prompt
        assert "millennials valorizam sustentabilidade" in final_prompt
        
        # Verifica se memórias relevantes foram incluídas
        assert "RELEVANT_MEMORY" in final_prompt

if __name__ == "__main__":
    pytest.main([__file__, "-v"])