# -*- coding: utf-8 -*-
"""Testes de integração avançados para demonstrar o poder completo do sistema cognitivo.

Estes testes simulam agentes reais trabalhando em cenários complexos de negócio,
demonstrando como o sistema cognitivo permite raciocínio sofisticado e tomada de decisão.
"""

import pytest
import json
from datetime import datetime, timedelta
from unittest.mock import Mock, patch
from typing import List, Dict, Any

from eca.orchestrator import ECAOrchestrator
from eca.memory.types import SemanticMemory, EpisodicMemory, InteractionLog
from eca.models import Persona, PersonaConfig


class TestAdvancedCognitiveScenarios:
    """Testes de cenários cognitivos avançados com simulação de agentes reais."""

    @pytest.fixture
    def enterprise_coffee_memories(self):
        """Base de conhecimento mais robusta para empresa de café."""
        memories = []
        
        # Conhecimento financeiro avançado
        memories.extend([
            SemanticMemory(
                id="fin_001",
                domain_id="financial_analyst",
                type="financial_metric",
                text_content="EBITDA do segmento premium cresceu 45% no Q3, impulsionado por blends exclusivos e certificação orgânica",
                embedding=[0.8] + [0.1] * 383
            ),
            
            SemanticMemory(
                id="fin_002", 
                domain_id="financial_analyst",
                type="cost_analysis",
                text_content="Custo de aquisição de grãos especiais aumentou 20% devido à seca na Colômbia, impactando margem em 3%",
                embedding=[0.7] + [0.1] * 383
            ),
            
            SemanticMemory(
                id="fin_003",
                domain_id="financial_analyst", 
                type="pricing_strategy",
                text_content="Análise de elasticidade mostra que aumento de 8% no preço do café premium reduz demanda em apenas 3%",
                embedding=[0.9] + [0.1] * 383
            )
        ])
        
        # Conhecimento de supply chain
        memories.extend([
            SemanticMemory(
                id="supply_001",
                domain_id="supply_chain_manager",
                type="supplier_relationship",
                text_content="Cooperativa Santa Isabel oferece grãos A+ com entrega em 10 dias, mas requer pedido mínimo de 5 toneladas",
                embedding=[0.8] + [0.2] * 383
            ),
            
            SemanticMemory(
                id="supply_002",
                domain_id="supply_chain_manager", 
                type="inventory_optimization",
                text_content="Estoque de segurança deve ser 30 dias para grãos premium e 15 dias para commodities, baseado em variabilidade histórica",
                embedding=[0.7] + [0.2] * 383
            ),
            
            SemanticMemory(
                id="supply_003",
                domain_id="supply_chain_manager",
                type="quality_assurance", 
                text_content="Processo de cupping identifica defeitos em 0.2% dos lotes, reduzindo reclamações de qualidade em 85%",
                embedding=[0.9] + [0.2] * 383
            )
        ])
        
        # Inteligência de mercado
        memories.extend([
            SemanticMemory(
                id="market_001",
                domain_id="market_intelligence",
                type="competitive_analysis",
                text_content="Concorrente A lançou linha sustentável com 30% de share em 6 meses, usando parcerias com fazendas familiares",
                embedding=[0.8] + [0.3] * 383
            ),
            
            SemanticMemory(
                id="market_002",
                domain_id="market_intelligence",
                type="trend_analysis", 
                text_content="Mercado de cold brew cresce 25% ao ano, principalmente em demografias 25-40 anos em áreas urbanas",
                embedding=[0.7] + [0.3] * 383
            ),
            
            SemanticMemory(
                id="market_003",
                domain_id="market_intelligence",
                type="consumer_behavior",
                text_content="62% dos consumidores premium pagam até 40% mais por café com certificação social e ambiental",
                embedding=[0.9] + [0.3] * 383
            )
        ])
        
        # Conhecimento técnico de produto
        memories.extend([
            SemanticMemory(
                id="product_001",
                domain_id="product_development",
                type="flavor_profile",
                text_content="Blend Signature combina 60% Arábica colombiano, 30% etíope e 10% brasileiro, resultando em notas frutadas e corpo médio",
                embedding=[0.8] + [0.4] * 383
            ),
            
            SemanticMemory(
                id="product_002",
                domain_id="product_development", 
                type="innovation_pipeline",
                text_content="Novo processo de fermentação controlada reduz acidez em 15% mantendo perfil aromático, teste piloto aprovado",
                embedding=[0.9] + [0.4] * 383
            )
        ])
        
        return memories

    @pytest.fixture
    def enterprise_personas(self):
        """Personas executivas para cenários empresariais."""
        return {
            "ceo": Persona(
                id="ceo",
                name="CEO-VISIONARY",
                semantic_description="CEO focado em crescimento estratégico e inovação",
                config=PersonaConfig(
                    persona="Você é o CEO visionário de uma empresa de café premium em expansão",
                    objective="Liderar crescimento sustentável e inovação disruptiva no mercado de café",
                    tone_of_voice=["Visionário", "Decisivo", "Orientado a impacto"],
                    verbosity="executive",
                    output_format="Executive Summary: Situação, Implicações Estratégicas, Decisões Requeridas, Timeline",
                    golden_rules=[
                        "Decisões devem considerar impacto de longo prazo",
                        "Inovação e sustentabilidade são pilares estratégicos",
                        "Crescimento deve ser sustentável e escalável"
                    ]
                )
            ),
            
            "financial_analyst": Persona(
                id="financial_analyst",
                name="CFO-METRICS",
                semantic_description="Analista financeiro sênior especializado em métricas de performance",
                config=PersonaConfig(
                    persona="Você é o CFO analítico, especialista em métricas financeiras e otimização de performance",
                    objective="Maximizar rentabilidade através de análise financeira rigorosa e controle de custos",
                    tone_of_voice=["Analítico", "Preciso", "Baseado em dados"],
                    verbosity="detailed",
                    output_format="Análise Financeira: KPIs Atuais, Variações, Drivers, Projeções, Recomendações",
                    golden_rules=[
                        "Toda decisão deve ter justificativa financeira clara",
                        "ROI e payback são métricas fundamentais",
                        "Riscos financeiros devem ser quantificados"
                    ]
                )
            ),
            
            "supply_chain_manager": Persona(
                id="supply_chain_manager", 
                name="SCM-OPTIMIZER",
                semantic_description="Gerente de supply chain focado em eficiência e qualidade",
                config=PersonaConfig(
                    persona="Você é o gerente de supply chain, especialista em otimização logística e qualidade",
                    objective="Garantir abastecimento eficiente com máxima qualidade e mínimo custo",
                    tone_of_voice=["Operacional", "Eficiente", "Orientado a qualidade"],
                    verbosity="operational",
                    output_format="Status Operacional: Situação Atual, Gargalos, Oportunidades, Plano de Ação",
                    golden_rules=[
                        "Qualidade nunca pode ser comprometida por custo",
                        "Redundância é essencial para fornecimento crítico",
                        "Relacionamentos com fornecedores são ativos estratégicos"
                    ]
                )
            ),
            
            "market_intelligence": Persona(
                id="market_intelligence",
                name="MI-STRATEGIST", 
                semantic_description="Especialista em inteligência de mercado e análise competitiva",
                config=PersonaConfig(
                    persona="Você é o especialista em inteligência de mercado, analista de tendências e competitividade",
                    objective="Fornecer insights de mercado para vantagem competitiva sustentável",
                    tone_of_voice=["Estratégico", "Investigativo", "Centrado em oportunidades"],
                    verbosity="strategic",
                    output_format="Intelligence Brief: Cenário Atual, Movimentos Competitivos, Oportunidades, Ameaças",
                    golden_rules=[
                        "Antecipe tendências antes que se tornem óbvias",
                        "Movimentos dos concorrentes revelam oportunidades",
                        "Dados externos são tão importantes quanto internos"
                    ]
                )
            )
        }

    @pytest.fixture
    def episodic_business_events(self):
        """Eventos episódicos representando histórico de decisões empresariais."""
        base_time = datetime.now() - timedelta(days=30)
        
        return [
            EpisodicMemory(
                id="ep_001",
                user_id="ceo",
                domain_id="ceo",
                timestamp=base_time,
                context_summary="Reunião estratégica Q3 - Decisão de expansão para mercado premium",
                interaction_log=InteractionLog(
                    input_text="Devemos focar expansão em premium ou volume?",
                    output_text="Análise indica maior rentabilidade no premium com menor risco. Recomendo expansão gradual em premium com parcerias estratégicas.",
                    metadata={"decision": "premium_expansion", "confidence": 0.85}
                )
            ),
            
            EpisodicMemory(
                id="ep_002", 
                user_id="financial_analyst",
                domain_id="financial_analyst",
                timestamp=base_time + timedelta(days=5),
                context_summary="Análise de impacto financeiro da expansão premium",
                interaction_log=InteractionLog(
                    input_text="Qual o impacto financeiro da expansão premium nos próximos 18 meses?",
                    output_text="Investimento inicial de R$ 2.5M, breakeven em 14 meses, ROI projetado de 35% em 18 meses com margem de segurança de 15%.",
                    metadata={"investment": 2500000, "breakeven_months": 14, "roi_18m": 0.35}
                )
            ),
            
            EpisodicMemory(
                id="ep_003",
                user_id="supply_chain_manager", 
                domain_id="supply_chain_manager",
                timestamp=base_time + timedelta(days=10),
                context_summary="Avaliação de fornecedores para linha premium",
                interaction_log=InteractionLog(
                    input_text="Conseguimos garantir fornecimento de grãos especiais para a expansão?", 
                    output_text="Cooperativa Santa Isabel pode fornecer 80% da demanda. Recomendo diversificar com 2 fornecedores menores para reduzir risco.",
                    metadata={"primary_supplier": "santa_isabel", "capacity": 0.8, "diversification": True}
                )
            )
        ]

    def test_strategic_decision_making_scenario(self, enterprise_personas, enterprise_coffee_memories, episodic_business_events):
        """Cenário: Tomada de decisão estratégica em nível executivo."""
        # Setup para simulação de decisão executiva
        persona_provider = Mock()
        persona_provider.detect_domain.return_value = "ceo"
        persona_provider.get_persona_by_id.return_value = enterprise_personas["ceo"]
        
        memory_provider = Mock()
        memory_provider.fetch_semantic_memories.return_value = enterprise_coffee_memories
        memory_provider.fetch_episodic_memories.return_value = episodic_business_events
        
        # Mock workspace mais realista
        from eca.models import CognitiveWorkspace, DomainState
        mock_workspace = CognitiveWorkspace(
            user_id="board_meeting",
            current_focus="ceo",
            active_domains={"ceo": DomainState(status="active")}
        )
        
        session_provider = Mock()
        session_provider.get_workspace.return_value = mock_workspace
        
        orchestrator = ECAOrchestrator(
            persona_provider=persona_provider,
            memory_provider=memory_provider,
            session_provider=session_provider
        )
        
        # Consulta estratégica complexa
        strategic_query = """
        Considerando nossa expansão no segmento premium em andamento, a seca na Colômbia 
        afetando custos de matéria-prima, e o crescimento do mercado de cold brew,
        qual deve ser nossa estratégia para os próximos 24 meses para manter
        crescimento de receita acima de 20% ao ano?
        """
        
        # Gera contexto e prompt
        context = orchestrator.generate_context_object("board_meeting", strategic_query)
        final_prompt = orchestrator.generate_final_prompt("board_meeting", strategic_query)
        
        # Validações de nível executivo
        assert "[IDENTITY:CEO-VISIONARY|CEO|" in final_prompt
        assert "crescimento sustentável e inovação disruptiva" in final_prompt
        assert "Executive Summary:" in final_prompt
        assert "expansão no segmento premium" in final_prompt
        assert "seca na Colômbia" in final_prompt
        assert "cold brew" in final_prompt
        
        # Verifica se memórias relevantes foram incluídas
        assert any("RELEVANT_MEMORY" in final_prompt for _ in range(1))
        
        # Verifica se histórico episódico foi considerado
        assert "RECENT_HISTORY" in final_prompt or "EPISODIC_MEMORY" in final_prompt or "INTERACTION_HISTORY" in final_prompt

    def test_multi_stakeholder_analysis(self, enterprise_personas, enterprise_coffee_memories):
        """Cenário: Análise multi-stakeholder para decisão complexa."""
        # Simula consulta que requer input de múltiplos especialistas
        stakeholder_responses = {}
        
        # Configuração para cada stakeholder
        stakeholders = ["financial_analyst", "supply_chain_manager", "market_intelligence"]
        
        for stakeholder_id in stakeholders:
            persona_provider = Mock()
            persona_provider.detect_domain.return_value = stakeholder_id
            persona_provider.get_persona_by_id.return_value = enterprise_personas[stakeholder_id]
            
            memory_provider = Mock()
            # Filtra memórias relevantes para cada stakeholder
            relevant_memories = [
                mem for mem in enterprise_coffee_memories 
                if mem.domain_id == stakeholder_id
            ]
            memory_provider.fetch_semantic_memories.return_value = relevant_memories
            memory_provider.fetch_episodic_memories.return_value = []
            
            # Mock workspace mais realista
            from eca.models import CognitiveWorkspace, DomainState
            mock_workspace = CognitiveWorkspace(
                user_id="strategy_committee",
                current_focus=stakeholder_id,
                active_domains={stakeholder_id: DomainState(status="active")}
            )
            
            session_provider = Mock()
            session_provider.get_workspace.return_value = mock_workspace
            
            orchestrator = ECAOrchestrator(
                persona_provider=persona_provider,
                memory_provider=memory_provider,
                session_provider=session_provider
            )
            
            # Consulta específica para cada stakeholder
            query = f"""
            A empresa está considerando lançar uma nova linha de café cold brew premium
            com certificação orgânica. Qual sua análise e recomendações específicas
            da perspectiva de {stakeholder_id.replace('_', ' ')}?
            """
            
            final_prompt = orchestrator.generate_final_prompt("strategy_committee", query)
            stakeholder_responses[stakeholder_id] = final_prompt
        
        # Validações por stakeholder
        # Financial Analyst
        fin_response = stakeholder_responses["financial_analyst"]
        assert "[IDENTITY:CFO-METRICS|FINANCIAL_ANALYST|" in fin_response
        assert "ROI e payback são métricas fundamentais" in fin_response
        assert "cold brew premium" in fin_response
        
        # Supply Chain Manager  
        scm_response = stakeholder_responses["supply_chain_manager"]
        assert "[IDENTITY:SCM-OPTIMIZER|SUPPLY_CHAIN_MANAGER|" in scm_response
        assert "Qualidade nunca pode ser comprometida" in scm_response
        
        # Market Intelligence
        mi_response = stakeholder_responses["market_intelligence"]
        assert "[IDENTITY:MI-STRATEGIST|MARKET_INTELLIGENCE|" in mi_response
        assert "Antecipe tendências antes que se tornem óbvias" in mi_response
        
        # Verifica que cada stakeholder recebeu memórias relevantes
        for response in stakeholder_responses.values():
            assert "RELEVANT_MEMORY" in response

    @patch('eca.cognitive.repository.CognitiveGraphRepository')
    def test_cognitive_graph_reasoning_simulation(self, mock_repo_class, enterprise_coffee_memories):
        """Simula raciocínio em grafo cognitivo para decisão complexa."""
        try:
            from eca.cognitive import CognitiveGraphAttention
            from eca.cognitive.types import CognitiveNode, CognitiveEdge, NodeType, EdgeType
            
            # Mock do repository com dados mais ricos
            mock_repo = Mock()
            mock_repo_class.return_value = mock_repo
            
            # Simula nós do grafo cognitivo
            cognitive_nodes = [
                CognitiveNode(
                    id="concept_cold_brew",
                    node_type=NodeType.CONCEPT,
                    content="Cold brew é método de extração a frio que resulta em bebida menos ácida",
                    embedding=[0.9] + [0.1] * 383,
                    activation_level=0.8
                ),
                CognitiveNode(
                    id="concept_premium_market", 
                    node_type=NodeType.CONCEPT,
                    content="Mercado premium valoriza qualidade, origem e experiência diferenciada",
                    embedding=[0.8] + [0.1] * 383,
                    activation_level=0.7
                ),
                CognitiveNode(
                    id="experience_expansion_success",
                    node_type=NodeType.EXPERIENCE, 
                    content="Expansão anterior no premium teve ROI de 35% em 18 meses",
                    embedding=[0.7] + [0.1] * 383,
                    activation_level=0.6
                )
            ]
            
            # Simula edges do grafo
            cognitive_edges = [
                CognitiveEdge(
                    id="edge_1",
                    source_id="concept_cold_brew",
                    target_id="concept_premium_market",
                    edge_type=EdgeType.ASSOCIATED_WITH,
                    weight=0.8,
                    metadata={"reason": "cold_brew_appeals_to_premium_consumers"}
                ),
                CognitiveEdge(
                    id="edge_2",
                    source_id="experience_expansion_success",
                    target_id="concept_premium_market", 
                    edge_type=EdgeType.ENABLES,
                    weight=0.9,
                    metadata={"reason": "past_success_enables_future_expansion"}
                )
            ]
            
            # Configura mocks do repository
            mock_repo.find_similar_nodes.return_value = cognitive_nodes
            mock_repo.get_edges_from_node.return_value = cognitive_edges
            mock_repo.get_edges_to_node.return_value = cognitive_edges
            
            # Função de embedding simplificada
            def simple_embedding(text):
                return [0.5] * 384
            
            # Cria attention cognitivo
            cognitive_attention = CognitiveGraphAttention(
                embedding_function=simple_embedding,
                repository=mock_repo,
                semantic_weight=0.3,
                graph_weight=0.7
            )
            
            # Query complexa que deveria ativar o grafo
            complex_query = "Devemos lançar cold brew premium considerando nossa experiência de expansão anterior?"
            
            # Executa atenção cognitiva
            result = cognitive_attention.rank_with_details(complex_query, enterprise_coffee_memories)
            
            # Validações do processo cognitivo
            assert result.metadata is not None
            
            if result.metadata.get("cognitive_process_used", False):
                assert "activated_concepts" in result.metadata
                assert len(result.metadata["activated_concepts"]) > 0
                
                # Verifica se o processo de spreading activation foi simulado
                mock_repo.find_similar_nodes.assert_called()
                
        except ImportError:
            pytest.skip("Sistema cognitivo não disponível")

    def test_crisis_management_scenario(self, enterprise_personas, enterprise_coffee_memories):
        """Cenário: Gestão de crise usando inteligência cognitiva."""
        # Simula uma crise: problema de qualidade em lote de café
        persona_provider = Mock()
        persona_provider.detect_domain.return_value = "supply_chain_manager" 
        persona_provider.get_persona_by_id.return_value = enterprise_personas["supply_chain_manager"]
        
        memory_provider = Mock()
        # Inclui memórias de qualidade e processos
        crisis_memories = [
            mem for mem in enterprise_coffee_memories 
            if any(keyword in mem.text_content.lower() for keyword in 
                   ["qualidade", "defeitos", "cupping", "processo"])
        ]
        memory_provider.fetch_semantic_memories.return_value = crisis_memories
        memory_provider.fetch_episodic_memories.return_value = []
        
        # Mock workspace mais realista
        from eca.models import CognitiveWorkspace, DomainState
        mock_workspace = CognitiveWorkspace(
            user_id="crisis_team",
            current_focus="supply_chain_manager",
            active_domains={"supply_chain_manager": DomainState(status="active")}
        )
        
        session_provider = Mock()
        session_provider.get_workspace.return_value = mock_workspace
        
        orchestrator = ECAOrchestrator(
            persona_provider=persona_provider,
            memory_provider=memory_provider,
            session_provider=session_provider
        )
        
        # Consulta de crise
        crisis_query = """
        URGENTE: Clientes reportam sabor anômalo em lotes do café premium produzidos
        na última semana. Pode afetar 15% do estoque atual. Preciso de plano de ação
        imediato para contenção de danos e correção do problema.
        """
        
        final_prompt = orchestrator.generate_final_prompt("crisis_team", crisis_query)
        
        # Validações de resposta à crise
        assert "[IDENTITY:SCM-OPTIMIZER|SUPPLY_CHAIN_MANAGER|" in final_prompt
        assert "Qualidade nunca pode ser comprometida" in final_prompt
        assert "sabor anômalo" in final_prompt
        assert "URGENTE" in final_prompt
        assert "15% do estoque" in final_prompt
        
        # Verifica se conhecimento de qualidade foi ativado
        assert "RELEVANT_MEMORY" in final_prompt

    def test_innovation_pipeline_scenario(self, enterprise_personas, enterprise_coffee_memories):
        """Cenário: Desenvolvimento de inovação usando conhecimento técnico."""
        persona_provider = Mock()
        persona_provider.detect_domain.return_value = "product_development"
        
        # Cria persona de desenvolvimento de produto para este teste
        product_persona = Persona(
            id="product_development",
            name="INNOVATION-LAB",
            semantic_description="Especialista em desenvolvimento de produtos e inovação",
            config=PersonaConfig(
                persona="Você é o líder de inovação em produtos de café",
                objective="Desenvolver produtos inovadores que criem vantagem competitiva",
                tone_of_voice=["Criativo", "Técnico", "Visionário"],
                verbosity="detailed"
            )
        )
        
        persona_provider.get_persona_by_id.return_value = product_persona
        
        memory_provider = Mock()
        # Filtra memórias técnicas e de produto
        innovation_memories = [
            mem for mem in enterprise_coffee_memories
            if mem.domain_id == "product_development" or "inovação" in mem.text_content.lower()
        ]
        memory_provider.fetch_semantic_memories.return_value = innovation_memories
        memory_provider.fetch_episodic_memories.return_value = []
        
        # Mock workspace mais realista
        from eca.models import CognitiveWorkspace, DomainState
        mock_workspace = CognitiveWorkspace(
            user_id="innovation_team",
            current_focus="product_development",
            active_domains={"product_development": DomainState(status="active")}
        )
        
        session_provider = Mock()
        session_provider.get_workspace.return_value = mock_workspace
        
        orchestrator = ECAOrchestrator(
            persona_provider=persona_provider,
            memory_provider=memory_provider,
            session_provider=session_provider
        )
        
        # Consulta de inovação
        innovation_query = """
        Preciso desenvolver um novo produto de café que combine sustentabilidade,
        conveniência e experiência premium. O mercado indica demanda por produtos
        ready-to-drink com perfil sensorial diferenciado. Quais são as possibilidades
        técnicas e recomendações para desenvolvimento?
        """
        
        final_prompt = orchestrator.generate_final_prompt("innovation_team", innovation_query)
        
        # Validações de inovação
        assert "[IDENTITY:INNOVATION-LAB|PRODUCT_DEVELOPMENT|" in final_prompt
        assert "produtos inovadores" in final_prompt
        assert "sustentabilidade" in final_prompt
        assert "ready-to-drink" in final_prompt
        assert "perfil sensorial" in final_prompt


if __name__ == "__main__":
    pytest.main([__file__, "-v"])