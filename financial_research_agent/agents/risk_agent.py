from pydantic import BaseModel

from agents import Agent

# A sub‑agent specializing in competitive analysis and market challenges.
COMPETITIVE_ANALYSIS_PROMPT = (
    "You are a competitive analyst looking for market challenges, competitive threats, "
    "and potential obstacles for a startup idea. Given background research, produce a short "
    "analysis of competitive landscape, market barriers, regulatory challenges, or other "
    "risks that could impact startup success. Keep it under 2 paragraphs."
)


class AnalysisSummary(BaseModel):
    summary: str
    """Short text summary for this aspect of the analysis."""


competitive_analysis_agent = Agent(
    name="CompetitiveAnalysisAgent",
    instructions=COMPETITIVE_ANALYSIS_PROMPT,
    output_type=AnalysisSummary,
)
