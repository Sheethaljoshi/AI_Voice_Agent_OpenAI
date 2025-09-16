import asyncio

from .manager import FinancialResearchManager
from dotenv import load_dotenv

load_dotenv()


# Run this as `python -m examples.financial_research_agent.main` and enter a

async def main() -> None:
    query = input("Enter a financial research query: ")
    mgr = FinancialResearchManager()
    await mgr.run(query)


if __name__ == "__main__":
    asyncio.run(main())
