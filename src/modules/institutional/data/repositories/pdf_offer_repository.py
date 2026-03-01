from pathlib import Path

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    ListFlowable,
    ListItem
)

from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

from src.modules.institutional.domain.entities.lead import Lead
from src.modules.institutional.domain.entities.offer import Offer
from src.modules.institutional.domain.repositories.i_offer_repository import IOfferRepository


class PDFOfferRepository(IOfferRepository):

    def __init__(self):
        self.output_dir = Path('src/modules/institutional/data/generated_offers')
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def _format_currency(self, value: float) -> str:
        formatted = f'{value:,.2f}'
        formatted = formatted.replace(',', 'X').replace('.', ',').replace('X', '.')
        return f'R$ {formatted}'

    def generate_offer(self, lead: Lead, offer: Offer):

        _lead = lead._to_dict()

        file_name = f'offer_{offer.id}_{offer.date.strftime("%Y%m%d")}.pdf'
        file_path = self.output_dir / file_name

        doc = SimpleDocTemplate(
            str(file_path),
            rightMargin=30,
            leftMargin=30,
            topMargin=35,
            bottomMargin=30
        )

        elements = []
        styles = getSampleStyleSheet()

        normal = ParagraphStyle(
            name='NormalSmall',
            parent=styles['Normal'],
            fontSize=9,
            leading=12
        )

        section = ParagraphStyle(
            name='SectionSmall',
            parent=styles['Heading2'],
            fontSize=11,
            spaceAfter=4
        )

        title = ParagraphStyle(
            name='TitleSmall',
            parent=styles['Heading1'],
            fontSize=14,
            spaceAfter=8
        )

        SPACE_XS = Spacer(1, 0.05 * inch)
        SPACE_SM = Spacer(1, 0.1 * inch)
        SPACE_MD = Spacer(1, 0.15 * inch)

        # ---------------- TÍTULO ----------------

        elements.append(Paragraph('Proposta de Organização e Automação de Projetos', title))
        elements.append(SPACE_SM)

        elements.append(Paragraph(
            f'<b>Cliente:</b> {_lead["lead"]} | '
            f'<b>Data:</b> {offer.date.strftime("%d/%m/%Y")} | '
            f'<b>Validade:</b> {offer.expires_at.strftime("%d/%m/%Y")}',
            normal
        ))

        elements.append(SPACE_MD)

        # ---------------- DIAGNÓSTICO ----------------

        elements.append(Paragraph('Diagnóstico Atual', section))
        elements.append(SPACE_XS)

        elements.append(Paragraph(
            f'Sua operação utiliza {_lead["sheet_tool"]}, com '
            f'{_lead["sheet_amount"]} e volume médio de '
            f'{_lead["register_amount"]}.',
            normal
        ))

        elements.append(SPACE_XS)

        elements.append(Paragraph(
            f'<b>Principal desafio:</b> {_lead["current_challenge"]}',
            normal
        ))

        elements.append(SPACE_XS)

        elements.append(Paragraph(
            f'Esse cenário gera retrabalho, risco de erro e perda de '
            f'clareza nas decisões.',
            normal
        ))

        elements.append(SPACE_MD)

        # ---------------- SOLUÇÃO ----------------

        elements.append(Paragraph('Solução Proposta', section))
        elements.append(SPACE_XS)

        solution = [
            'Eliminar processos manuais repetitivos',
            'Reduzir erros operacionais',
            'Padronizar informações',
            'Gerar relatórios automáticos',
            'Aumentar clareza na tomada de decisão'
        ]

        elements.append(
            ListFlowable(
                [ListItem(Paragraph(item, normal)) for item in solution],
                bulletType='bullet',
                leftIndent=10
            )
        )

        elements.append(SPACE_SM)

        elements.append(Paragraph(
            'Prazo estimado: 7 a 15 dias úteis após envio das planilhas base.',
            normal
        ))

        elements.append(SPACE_MD)

        # ---------------- INVESTIMENTO ----------------

        elements.append(Paragraph('Investimento', section))
        elements.append(SPACE_XS)

        elements.append(Paragraph(
            f'<b>Implantação personalizada:</b> '
            f'{self._format_currency(offer.implantation_value)}',
            normal
        ))

        elements.append(SPACE_XS)

        elements.append(Paragraph(
            f'<b>Plano opcional de evolução contínua:</b> '
            f'{self._format_currency(offer.maintence_value)} / mês',
            normal
        ))

        elements.append(SPACE_XS)

        elements.append(Paragraph(
            'Inclui suporte técnico, melhorias estruturais e ajustes contínuos.',
            normal
        ))

        elements.append(SPACE_MD)

        # ---------------- CONDIÇÕES ----------------

        elements.append(Paragraph(
            '<b>Pagamento:</b> 50% na aprovação | 50% na entrega',
            normal
        ))

        elements.append(SPACE_XS)

        elements.append(Paragraph(
            'Garantia de ajustes por 7 dias após entrega.',
            normal
        ))

        elements.append(SPACE_XS)

        elements.append(Paragraph(
            'Processamento seguro e confidencial, sem armazenamento permanente de dados.',
            normal
        ))

        elements.append(SPACE_MD)

        # ---------------- FRASE ESTRATÉGICA ----------------

        elements.append(Paragraph(
            'Essa proposta foi estruturada para que sua operação ganhe organização '
            'e previsibilidade sem aumentar sua complexidade.',
            normal
        ))

        elements.append(SPACE_MD)

        # ---------------- ASSINATURA ----------------

        elements.append(Paragraph(
            'Bruno Minelli | Consultor em Automação de Processos',
            normal
        ))

        elements.append(Paragraph(
            'contato@brunominelli.dev.br',
            normal
        ))

        doc.build(elements)

        return {
            'offer_id': offer.id,
            'file_path': file_path,
        }