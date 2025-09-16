from pydantic import BaseModel

from agents import Agent

# A sub‑agent focused on analyzing market trends and opportunities.
MARKET_ANALYSIS_PROMPT = (
    "You are a market analyst focused on identifying business opportunities, market trends, "
    "and growth potential. Given a collection of web search results about a market, industry, "
    "or business idea, write a concise analysis of market size, trends, opportunities, "
    "and competitive landscape. Pull out key market data, growth rates, and emerging trends. "
    "Keep it under 2 paragraphs."
)


class AnalysisSummary(BaseModel):
    summary: str
    """Short text summary for this aspect of the analysis."""


market_analysis_agent = Agent(
    name="MarketAnalysisAgent",
    instructions=MARKET_ANALYSIS_PROMPT,
    output_type=AnalysisSummary,
)
