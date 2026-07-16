"""
PDF Generator

Generates Architecture Review PDF reports.

Responsibilities
----------------
- Build PDF
- Format report sections
- Save PDF

Does NOT
--------
- Fetch review from MongoDB
- Perform business logic
"""

from pathlib import Path
from django.conf import settings

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)
from reportlab.lib import colors
from review_engine.config.pdf_constants import (
    PDF_TITLE,
    AUTHOR,
    SUBJECT,
    CREATOR,
)


class PDFGenerator:

    def __init__(self):

        self.styles = getSampleStyleSheet()

    # =====================================================
    # Public
    # =====================================================

    def generate(
        self,
        review: dict,
        output_path: str,
    ):
        """
        Generate architecture review PDF.
        """

        document = SimpleDocTemplate(
            output_path
        )

        story = []

        # -------------------------------------------------
        # Title
        # -------------------------------------------------

        story.append(
            Paragraph(
                PDF_TITLE,
                self.styles["Title"],
            )
        )

        story.append(
            Spacer(1, 0.25 * inch)
        )

        # -------------------------------------------------
        # Review Information
        # -------------------------------------------------

        self._section_heading(
            story,
            "Review Information",
        )

        self._table(
            story,
            ["Field", "Value"],
            [
                ["Review ID", review["review_id"]],
                ["System Name", review["system_name"]],
                ["Architecture Type", review["architecture_type"]],
                ["Created At", str(review["created_at"])],
                ["Version", review["review_version"]],
            ],
        )

        # -------------------------------------------------
        # Overall Score
        # -------------------------------------------------
        result=review["review_result"]
        
        self._section_heading(
            story,
            "Overall Score",
        )
        

        score = result["overall_score"]

        if score >= 90:
            rating = "Excellent"
        elif score >= 75:
            rating = "Good"
        elif score >= 60:
            rating = "Average"
        else:
            rating = "Needs Improvement"

        self._table(
            story,
            ["Overall Score", "Overall Rating"],
            [
                [
                    f"{score} / 100",
                    rating,
                ]
            ],
        )

        self._section_heading(
            story,
            "Executive Summary",
        )

        self._table(
            story,
            [
                "Metric",
                "Value",
            ],
            [

                [
                    "Overall Rating",
                    rating,
                ],

                [
                    "Strengths",
                    str(len(result["strengths"])),
                ],

                [
                    "Weaknesses",
                    str(len(result["weaknesses"])),
                ],

                [
                    "Recommendations",
                    str(len(result["recommendations"])),
                ],

                [
                    "Rule Violations",
                    str(len(result["violations"])),
                ],

            ],
        )
        
        # -------------------------------------------------
        # Submitted Architecture
        # -------------------------------------------------

        self._section_heading(
            story,
            "Submitted Architecture",
        )

        architecture = review["input_architecture"]

        self._section_heading(
            story,
            "Services",
        )

        service_rows = []

        for service in architecture["services"]:

            service_rows.append(
                [
                    service["name"],
                    service["technology"],
                    str(service["instances"]),
                    "Yes" if service["stateless"] else "No",
                    "Yes" if service["async_processing"] else "No",
                ]
            )

        self._table(
            story,
            [
                "Name",
                "Technology",
                "Instances",
                "Stateless",
                "Async",
            ],
            service_rows,
        )

        self._section_heading(
            story,
            "Databases",
        )

        database_rows = []

        for database in architecture["databases"]:

            database_rows.append(
                [
                    database["name"],
                    database["type"],
                    "Yes" if database["replication"] else "No",
                    "Yes" if database["read_replicas"] else "No",
                    "Yes" if database["sharding"] else "No",
                ]
            )

        self._table(
            story,
            [
                "Name",
                "Type",
                "Replication",
                "Read Replicas",
                "Sharding",
            ],
            database_rows,
        )

        self._section_heading(
            story,
            "Infrastructure",
        )

        self._table(
            story,
            [
                "Component",
                "Status",
                "Type",
            ],
            [

                [
                    "Load Balancer",
                    "Enabled" if architecture["load_balancer"]["enabled"] else "Disabled",
                    "-",
                ],

                [
                    "Cache",
                    "Enabled" if architecture["cache"]["enabled"] else "Disabled",
                    architecture["cache"]["type"],
                ],

                [
                    "Message Queue",
                    "Enabled" if architecture["message_queue"]["enabled"] else "Disabled",
                    architecture["message_queue"]["type"],
                ],

            ],
        )
        # -------------------------------------------------
        # Security
        # -------------------------------------------------

        self._section_heading(
            story,
            "Security",
        )

        security = architecture["security"]

        self._paragraph(
            story,
            f"<b>Authentication:</b> {security['authentication']}"
        )

        self._paragraph(
            story,
            f"<b>Authentication Type:</b> {security['authentication_type']}"
        )

        self._paragraph(
            story,
            f"<b>Authorization:</b> {security['authorization']}"
        )

        self._paragraph(
            story,
            f"<b>Authorization Model:</b> {security['authorization_model']}"
        )

        self._paragraph(
            story,
            f"<b>HTTPS:</b> {security['https']}"
        )

        self._paragraph(
            story,
            f"<b>Encryption At Rest:</b> {security['encrypt_at_rest']}"
        )

        self._paragraph(
            story,
            f"<b>Rate Limiting:</b> {security['rate_limiting']}"
        )

        self._paragraph(
            story,
            f"<b>Input Validation:</b> {security['input_validation']}"
        )

        self._paragraph(
            story,
            f"<b>Secret Management:</b> {security['secret_management']}"
        )

        self._paragraph(
            story,
            f"<b>Default Credentials:</b> {security['default_credentials']}"
        )

        self._paragraph(
            story,
            f"<b>CORS:</b> {security['cors']}"
        )

        self._paragraph(
            story,
            f"<b>Security Headers:</b> {security['security_headers']}"
        )

        # -------------------------------------------------
        # Monitoring
        # -------------------------------------------------

        self._section_heading(
            story,
            "Monitoring",
        )

        monitoring = architecture["monitoring"]

        for key, value in monitoring.items():

            self._paragraph(
                story,
                f"<b>{key.replace('_', ' ').title()}:</b> {value}"
            )

        # -------------------------------------------------
        # Resilience
        # -------------------------------------------------

        self._section_heading(
            story,
            "Resilience",
        )

        resilience = architecture["resilience"]

        for key, value in resilience.items():

            self._paragraph(
                story,
                f"<b>{key.replace('_', ' ').title()}:</b> {value}"
            )

        # -------------------------------------------------
        # Backup
        # -------------------------------------------------

        self._section_heading(
            story,
            "Backup",
        )

        backup = architecture["backup"]

        for key, value in backup.items():

            self._paragraph(
                story,
                f"<b>{key.replace('_', ' ').title()}:</b> {value}"
            )

        # -------------------------------------------------
        # API
        # -------------------------------------------------

        self._section_heading(
            story,
            "API",
        )

        api = architecture["api"]

        for key, value in api.items():

            self._paragraph(
                story,
                f"<b>{key.replace('_', ' ').title()}:</b> {value}"
            )

        # -------------------------------------------------
        # Deployment
        # -------------------------------------------------

        self._section_heading(
            story,
            "Deployment",
        )

        deployment = architecture["deployment"]

        for key, value in deployment.items():

            self._paragraph(
                story,
                f"<b>{key.replace('_', ' ').title()}:</b> {value}"
            )

        # -------------------------------------------------
        # Architecture Design
        # -------------------------------------------------

        self._section_heading(
            story,
            "Architecture Design",
        )

        design = architecture["architecture"]

        for key, value in design.items():

            self._paragraph(
                story,
                f"<b>{key.replace('_', ' ').title()}:</b> {value}"
            )

        # -------------------------------------------------
        # Testing
        # -------------------------------------------------

        self._section_heading(
            story,
            "Testing",
        )

        testing = architecture["testing"]

        for key, value in testing.items():

            self._paragraph(
                story,
                f"<b>{key.replace('_', ' ').title()}:</b> {value}"
            )

        # -------------------------------------------------
        # Documentation
        # -------------------------------------------------

        self._section_heading(
            story,
            "Documentation",
        )

        documentation = architecture["documentation"]

        for key, value in documentation.items():

            self._paragraph(
                story,
                f"<b>{key.replace('_', ' ').title()}:</b> {value}"
            )

        # -------------------------------------------------
        # Configuration
        # -------------------------------------------------

        self._section_heading(
            story,
            "Configuration",
        )

        configuration = architecture["configuration"]

        for key, value in configuration.items():

            self._paragraph(
                story,
                f"<b>{key.replace('_', ' ').title()}:</b> {value}"
            )

        # -------------------------------------------------
        # Category Scores
        # -------------------------------------------------

        self._section_heading(
            story,
            "Category Scores",
        )

        score_rows = []

        for category, score in result[
            "category_scores"
        ].items():

            score_rows.append(
                [
                    category.title(),
                    f"{score}/100",
                ]
            )

        self._table(
            story,
            [
                "Category",
                "Score",
            ],
            score_rows,
        )

        # -------------------------------------------------
        # Strengths
        # -------------------------------------------------

        self._list_section(
            story,
            "Strengths",
            result["strengths"],
        )

        # -------------------------------------------------
        # Weaknesses
        # -------------------------------------------------

        self._list_section(
            story,
            "Weaknesses",
            result["weaknesses"],
        )

        # -------------------------------------------------
        # Recommendations
        # -------------------------------------------------

        recommendations = [
            recommendation.get("description",
                               recommendation.get("title", ""))
            for recommendation in result["recommendations"]
        ]

        self._list_section(
            story,
            "Recommendations",
            recommendations,
        )

        # -------------------------------------------------
        # Rule Evaluation
        # -------------------------------------------------

        self._section_heading(
            story,
            "Rule Evaluation",
        )

        rule_rows = []

        for rule in result["rule_results"]:

            rule_rows.append(
                [
                    rule["rule_id"],
                    rule["category"],
                    rule["status"],
                    rule["severity"],
                ]
            )

        self._table(
            story,
            [
                "Rule ID",
                "Category",
                "Status",
                "Severity",
            ],
            rule_rows,
        )

        # -------------------------------------------------
        # Violations
        # -------------------------------------------------

        self._section_heading(
            story,
            "Rule Violations",
        )

        if result["violations"]:

            for violation in result["violations"]:

                text = (
                    f"{violation['rule_id']} | "
                    f"{violation['category']} | "
                    f"{violation['severity']}"
                )

                self._paragraph(
                    story,
                    text,
                )

        else:

            self._paragraph(
                story,
                "No rule violations."
            )

        # -------------------------------------------------
        # LLM Analysis
        # -------------------------------------------------

        llm = result.get(
            "llm_analysis"
        )

        if llm:

            self._section_heading(
                story,
                "LLM Analysis",
            )

            if isinstance(llm, str):

                self._paragraph(
                story,
                llm,
            )

            else:

                self._paragraph(
                story,
                f"<b>Executive Summary</b><br/>{llm['executive_summary']}"
            )

                self._paragraph(
                story,
                f"<b>Overall Assessment</b><br/>{llm['overall_assessment']}"
            )

                maturity = llm[
                "architecture_maturity"
            ]

                self._paragraph(
                story,
                f"<b>Architecture Maturity</b><br/>"
                f"{maturity['level']}<br/>"
                f"{maturity['reason']}"
            )

                self._section_heading(
                story,
                "Future Focus",
            )

                for item in llm[
                "future_focus"
            ]:

                    self._paragraph(
                    story,
                    f"• {item}"
                )

                confidence = llm[
                "review_confidence"
            ]

                self._paragraph(
                story,
                f"<b>Review Confidence</b><br/>"
                f"{confidence['level']}<br/>"
                f"{confidence['reason']}"
            )

        # -------------------------------------------------
        # Metadata
        # -------------------------------------------------

        document.title = PDF_TITLE
        document.author = AUTHOR
        document.subject = SUBJECT
        document.creator = CREATOR

        document.build(
            story,
            onFirstPage=self._footer,
            onLaterPages=self._footer,
        )

        return Path(
            output_path
        )

    # =====================================================
    # Helpers
    # =====================================================

    def _section_heading(
        self,
        story,
        title,
    ):

        story.append(
            Paragraph(
                f"<b>{title}</b>",
                self.styles["Heading2"],
            )
        )

        story.append(
            Spacer(1, 0.12 * inch)
        )

    def _paragraph(
        self,
        story,
        text,
    ):

        story.append(
            Paragraph(
                text,
                self.styles["BodyText"],
            )
        )

        story.append(
            Spacer(1, 0.06 * inch)
        )

    def _table(
        self,
        story,
        headers,
        rows,
    ):

        data = [headers]
        data.extend(rows)

        table = Table(
            data,
            repeatRows=1,
        )

        style = TableStyle([

            (
                "BACKGROUND",
                (0, 0),
                (-1, 0),
                colors.HexColor("#1F4E79"),
            ),

            (
                "TEXTCOLOR",
                (0, 0),
                (-1, 0),
                colors.white,
            ),

            (
                "FONTNAME",
                (0, 0),
                (-1, 0),
                "Helvetica-Bold",
            ),

            (
                "FONTSIZE",
                (0, 0),
                (-1, 0),
                11,
            ),

            (
                "FONTSIZE",
                (0, 1),
                (-1, -1),
                9,
            ),

            (
                "BOTTOMPADDING",
                (0, 0),
                (-1, 0),
                8,
            ),

            (
                "TOPPADDING",
                (0, 1),
                (-1, -1),
                5,
            ),

            (
                "BOTTOMPADDING",
                (0, 1),
                (-1, -1),
                5,
            ),

            (
                "GRID",
                (0, 0),
                (-1, -1),
                0.4,
                colors.grey,
            ),

            (
                "VALIGN",
                (0, 0),
                (-1, -1),
                "MIDDLE",
            ),

            (
                "ALIGN",
                (0, 0),
                (-1, -1),
                "CENTER",
            ),

        ])

        for row in range(1, len(data)):

            style.add(
                "BACKGROUND",
                (0, row),
                (-1, row),
                colors.white,
            )

            if len(data[row]) >= 3:

                status = str(data[row][2])

                if status == "PASS":

                    style.add(
                        "TEXTCOLOR",
                        (2, row),
                        (2, row),
                        colors.green,
                    )

                elif status == "FAIL":

                    style.add(
                        "TEXTCOLOR",
                        (2, row),
                        (2, row),
                        colors.red,
                    )

        table.setStyle(style)

        story.append(table)

        story.append(
            Spacer(
                1,
                0.2 * inch,
            )
        )

    def _list_section(
        self,
        story,
        title,
        items,
    ):

        self._section_heading(
            story,
            title,
        )

        if not items:

            self._paragraph(
                story,
                "None"
            )

            return

        for item in items:

            self._paragraph(
                story,
                f"• {item}"
            )
    def _footer(
        self,
        canvas,
        doc,
    ):

        canvas.saveState()

        canvas.setFont(
            "Helvetica",
            8,
        )

        canvas.drawString(
            40,
            20,
            "Architecture Review Platform",
        )

        canvas.drawRightString(
            560,
            20,
            f"Page {doc.page}",
        )

        canvas.restoreState()