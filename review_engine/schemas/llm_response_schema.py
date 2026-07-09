"""
LLM Response Schema

Defines the expected JSON structure returned by Gemini.
"""

LLM_RESPONSE_SCHEMA = {
    "type": "object",
    "properties": {
        "executive_summary": {
            "type": "string"
        },
        "overall_assessment": {
            "type": "string"
        },
        "architecture_maturity": {
            "type": "object",
            "properties": {
                "level": {
                    "type": "string"
                },
                "reason": {
                    "type": "string"
                }
            },
            "required": [
                "level",
                "reason"
            ]
        },
        "future_focus": {
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "review_confidence": {
            "type": "object",
            "properties": {
                "level": {
                    "type": "string"
                },
                "reason": {
                    "type": "string"
                }
            },
            "required": [
                "level",
                "reason"
            ]
        }
    },
    "required": [
        "executive_summary",
        "overall_assessment",
        "architecture_maturity",
        "future_focus",
        "review_confidence"
    ]
}