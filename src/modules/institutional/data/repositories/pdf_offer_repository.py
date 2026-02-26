from pathlib import Path
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors

from src.modules.institutional.domain.entities.lead import Lead
from src.modules.institutional.domain.entities.offer import Offer
from src.modules.institutional.domain.repositories.i_offer_repository import IOfferRepository


class PDFOfferRepository(IOfferRepository):

    def __init__(self):
        self.output_dir = Path('src/modules/institutional/data/generated_offers')
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def generate_offer(self, lead: Lead, offer: Offer):
        _lead = lead._to_dict()
        file_name = f'offer_{offer.id}_{offer.date.strftime("%Y%m%d")}.pdf'
        file_path = self.output_dir / file_name

        doc = SimpleDocTemplate(str(file_path))
        elements = []

        styles = getSampleStyleSheet()
        title_style = styles['Heading2']
        normal = styles['Normal']

        bold_style = ParagraphStyle(
            name='Bold',
            parent=styles['Normal'],
            fontName='Helvetica-Bold'
        )

        list_style = ParagraphStyle(
            name='List',
            parent=styles['Normal'],
            leftIndent=15
        )

        # ------------------ TÍTULO ------------------
        elements.append(Paragraph(
            'Proposta Comercial - Automação de Dados',
            title_style
        ))
        elements.append(Spacer(1, 0.1 * inch))

        elements.append(Paragraph(f'<b>Cliente:</b> {_lead['lead']}', normal))
        elements.append(Paragraph(f'<b>Data da Proposta:</b> {offer.date}', normal))
        elements.append(Paragraph(f'<b>Validade:</b> {offer.expires_at}', normal))
        elements.append(Spacer(1, 0.1 * inch))

        # ------------------ CONTEXTO ------------------
        elements.append(Paragraph('1. CONTEXTO IDENTIFICADO', bold_style))
        elements.append(Spacer(1, 0.1 * inch))

        context_list = [
            f'   - Ferramenta utilizada: {_lead['sheet_tool']}',
            f'   - Quantidade de planilhas: {_lead['sheet_amount']}',
            f'   - Volume médio de registros: {_lead['register_amount']}',
            f'   - Estrutura atual controla: {_lead['register_type']}',
        ]

        for item in context_list:
            elements.append(Paragraph(item, list_style))

        elements.append(Spacer(1, 0.1 * inch))

        elements.append(Paragraph('<b>Principal desafio relatado:</b>', normal))
        elements.append(Spacer(1, 0.1 * inch))
        elements.append(Paragraph(_lead['current_challenge'], normal))
        elements.append(Spacer(1, 0.125 * inch))

        # ------------------ OBJETIVO ------------------
        elements.append(Paragraph('2. OBJETIVO DO PROJETO', bold_style))
        elements.append(Spacer(1, 0.1 * inch))

        objectives = [
            '   - Reduzir processos manuais',
            '   - Diminuir erros operacionais',
            '   - Padronizar informações',
            '   - Gerar relatórios automáticos',
            '   - Aumentar clareza na tomada de decisão',
        ]

        for item in objectives:
            elements.append(Paragraph(item, list_style))

        elements.append(Spacer(1, 0.125 * inch))

        # ------------------ ESCOPO ------------------
        elements.append(Paragraph('3. ESCOPO DA SOLUÇÃO', bold_style))
        elements.append(Spacer(1, 0.1 * inch))

        scope_items = [
            '   - Estruturação e padronização da planilha atual',
            '   - Definição de regras específicas para o negócio',
            '   - Desenvolvimento de motor automatizado sob medida',
            '   - Geração automática de relatórios',
            '   - Criação de link seguro exclusivo para processamento',
            '   - Processamento sob demanda (sem armazenamento de dados)',
        ]

        for item in scope_items:
            elements.append(Paragraph(item, list_style))

        elements.append(Spacer(1, 0.125 * inch))

        # ------------------ PRAZO ------------------
        elements.append(Paragraph('4. PRAZO DE IMPLEMENTAÇÃO', bold_style))
        elements.append(Spacer(1, 0.1 * inch))
        elements.append(
            Paragraph('7 a 15 dias úteis após validação do escopo.', normal)
        )
        elements.append(Spacer(1, 0.125 * inch))

        # ------------------ INVESTIMENTO ------------------
        elements.append(Paragraph('5. INVESTIMENTO', bold_style))
        elements.append(Spacer(1, 0.1 * inch))

        data = [
            ['Descrição', 'Valor (R$)'],
            ['Implantação Personalizada', f'{offer.implantation_value:,.2f}'],
            ['Manutenção Mensal (Opcional)', f'{offer.maintence_value:,.2f}'],
        ]

        table = Table(data, colWidths=[3.5 * inch, 2 * inch])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
            ('GRID', (0, 0), (-1, -1), 1, colors.grey),
            ('ALIGN', (1, 1), (-1, -1), 'RIGHT'),
        ]))

        elements.append(table)
        elements.append(Spacer(1, 0.125 * inch))

        # ------------------ PAGAMENTO ------------------
        elements.append(Paragraph('6. CONDIÇÕES DE PAGAMENTO', bold_style))
        elements.append(Spacer(1, 0.1 * inch))

        payment = [
            '   - 50% na aprovação da proposta',
            '   - 50% na entrega da solução',
        ]

        for item in payment:
            elements.append(Paragraph(item, list_style))

        elements.append(Spacer(1, 0.125 * inch))

        # ------------------ CONFIDENCIALIDADE ------------------
        elements.append(Paragraph('7. CONFIDENCIALIDADE E SEGURANÇA', bold_style))
        elements.append(Spacer(1, 0.1 * inch))

        security = [
            '   - Dados utilizados exclusivamente para processamento sob demanda',
            '   - Sem armazenamento permanente das informações financeiras',
            '   - Acesso por link seguro e exclusivo',
        ]

        for item in security:
            elements.append(Paragraph(item, list_style))

        elements.append(Spacer(1, 0.125 * inch))

        # ------------------ ASSINATURA ------------------
        elements.append(Paragraph('8. ASSINATURA', bold_style))
        elements.append(Spacer(1, 0.1 * inch))

        elements.append(Paragraph('Bruno Minelli', normal))
        elements.append(Paragraph('Desenvolvedor e Consultor de Automações', normal))
        elements.append(Paragraph('contato@brunominelli.dev', normal))

        doc.build(elements)

        return {
            'offer_id': offer.id,
            'file_path': file_path,
        }