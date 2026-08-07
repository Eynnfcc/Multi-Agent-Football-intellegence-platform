from crewai import Agent, Task

from config import AGENT_MAX_ITERATIONS
from llm import llm
from tools.tavily_tool import TavilySearchTool


def create_scout_agent() -> Agent:
    """
    Create the Scout Agent.

    This agent is responsible for reasoning about the user's request,
    designing the best search strategy, and discovering the most
    relevant football sources available on the web.

    It never scrapes webpages, analyzes football information,
    compares entities, or makes recommendations.
    """

    return Agent(

        role="Football Intelligence Scout",

        goal=(
            "Understand what evidence is required to answer the user's "
            "football request, design an intelligent search strategy, "
            "and discover the highest-quality football sources available "
            "on the internet."
        ),

        backstory=(
            "You are the Football Intelligence Scout of an advanced "
            "multi-agent football intelligence platform.\n\n"

            "Your responsibility is not simply to search the web.\n\n"

            "Before performing any search, carefully reason about the "
            "user's request and determine what information is actually "
            "required to answer it correctly.\n\n"

            "Think like an experienced football analyst and researcher.\n\n"

            "Decide what evidence is required before generating any "
            "search queries.\n\n"

            "Reason about whether the request requires:\n"

            "- recent information\n"
            "- historical information\n"
            "- official competition data\n"
            "- club information\n"
            "- player information\n"
            "- manager information\n"
            "- match information\n"
            "- tournament information\n"
            "- transfer information\n"
            "- injury information\n"
            "- journalist reports\n"
            "- interviews\n"
            "- tactical analysis\n"
            "- statistical evidence\n"
            "- rankings\n"
            "- performance metrics\n"
            "- scouting reports\n"
            "- market values\n"
            "- expert opinions\n"
            "- multiple independent sources\n\n"

            "Not every request requires every type of evidence.\n\n"

            "Determine the minimum and most relevant evidence needed "
            "for the specific request.\n\n"

            "Design your own search strategy.\n\n"

            "Generate multiple high-quality search queries.\n\n"

            "Prefer trusted football sources whenever possible.\n\n"

            "Avoid duplicate or low-quality webpages.\n\n"

            "Your responsibility ends after discovering useful sources.\n\n"

            "Never scrape webpages.\n"
            "Never summarize information.\n"
            "Never compare football entities.\n"
            "Never make recommendations.\n"
            "Never invent facts."
        ),

        llm=llm,

        tools=[
            TavilySearchTool(),
        ],

        max_iter=AGENT_MAX_ITERATIONS,
    )


def create_scout_task(
    agent: Agent,
    request_task: Task,
) -> Task:
    """
    Create the Scout Task.
    """

    return Task(

        description="""
The Request Agent has already understood the user's request.

Study the structured request carefully.

Before searching, reason about what evidence is actually required.

Determine:

- What information is needed.
- Which football entities are involved.
- Whether recent information is required.
- Whether historical information is required.
- Whether official sources are needed.
- Whether journalist reports are needed.
- Whether statistical information is needed.
- Whether tactical information is needed.
- Whether multiple independent sources should be collected.

Design the best possible search strategy.

Generate multiple precise search queries.

Use Tavily to execute those searches.

Collect only webpages that are likely to provide valuable evidence.

Avoid duplicate sources.

Prefer trustworthy football sources.

Do NOT scrape webpages.

Do NOT summarize information.

Do NOT compare players or clubs.

Do NOT make recommendations.

Return ONLY the following JSON.

{
    "search_strategy": "",
    "required_evidence": [],
    "search_queries": [],
    "sources": [
        {
            "title": "",
            "url": "",
            "source_type": "",
            "reason": ""
        }
    ]
}

Return only the JSON object.

Do not use markdown.

Do not add explanations.
""",

        expected_output=(
            "A JSON object describing the reasoning behind the search "
            "strategy, the required evidence, generated search queries, "
            "and the discovered football sources."
        ),

        agent=agent,

        context=[request_task],
    )