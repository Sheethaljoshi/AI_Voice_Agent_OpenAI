from pydantic import BaseModel

from agents import Agent

# Generate a plan of searches to ground the startup research analysis.
# For a given startup idea or market opportunity, we want to search for
# market trends, competitors, customer insights, business models, and success stories.
PROMPT = (
    "You are a startup research planner. Given a request for startup research or business idea analysis, "
    "produce a set of web searches to gather the context needed. Aim for market trends, competitor analysis, "
    "customer insights, business model examples, funding news, and startup success stories. "
    "Output between 5 and 15 search terms to query for."
)


class StartupSearchItem(BaseModel):
    reason: str
    """Your reasoning for why this search is relevant."""

    query: str
    """The search term to feed into a web (or file) search."""


class StartupSearchPlan(BaseModel):
    searches: list[StartupSearchItem]
    """A list of searches to perform."""


planner_agent = Agent(
    name="StartupPlannerAgent",
    instructions=PROMPT,
    model="o3-mini",
    output_type=StartupSearchPlan,
)
