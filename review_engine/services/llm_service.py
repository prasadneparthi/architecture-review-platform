"""
LLM Service

Generates an AI-powered architecture review.

Responsibilities
----------------
- Build prompt
- Call Gemini
- Parse JSON response
- Return structured LLM analysis

Does NOT
--------
- Calculate scores
- Evaluate rules
- Generate recommendations on its own
"""

import json

import google.generativeai as genai

from review_engine.config.llm_constants import (
    MODEL_NAME,
    TEMPERATURE,
    TOP_P,
    TOP_K,
    MAX_OUTPUT_TOKENS,
    RESPONSE_MIME_TYPE,
)

from review_engine.prompts.arch_rev_prompt import (
    build_prompt,
)

from review_engine.exceptions.custom_exceptions import (
    LLMAnalysisError,
)
from review_engine.schemas.llm_response_schema import (
    LLM_RESPONSE_SCHEMA,
)
from review_engine.logging.logger import (
    logger,
)
logger= logger.get_logger()

class LLMService:

    def __init__(self, api_key: str):

        genai.configure(
            api_key=api_key
        )
        logger.info("Sending request to Gemini.")
        self.model = genai.GenerativeModel(
            model_name=MODEL_NAME,

            generation_config={
                "temperature": TEMPERATURE,
                "top_p": TOP_P,
                "top_k": TOP_K,
                "max_output_tokens": MAX_OUTPUT_TOKENS,
                "response_mime_type": RESPONSE_MIME_TYPE,
                "response_schema": LLM_RESPONSE_SCHEMA,
            },
        )

    # =====================================================
    # Main
    # =====================================================

    def analyze(
        self,
        architecture,
        scores,
        strengths,
        weaknesses,
        recommendations,
    ):

        prompt = build_prompt(
            architecture=architecture,
            scores=scores,
            strengths=strengths,
            weaknesses=weaknesses,
            recommendations=recommendations,
        )

        try:

            response = self.model.generate_content(
                contents=prompt
            )
            logger.info("Gemini response received successfully.")

            if not response.text:

                raise LLMAnalysisError(
                    "Empty response received from Gemini."
                )

            return json.loads(
                response.text
            )

        except json.JSONDecodeError:

            raise LLMAnalysisError(
                "Gemini returned invalid JSON."
            )

        except Exception as exc:
            logger.exception("llm analysis failed.")

            raise LLMAnalysisError(
                f"llm analysis failed: {str(exc)}"
            )