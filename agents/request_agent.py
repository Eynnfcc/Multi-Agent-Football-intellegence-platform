from crewai import Agent, Task

from config import AGENT_MAX_ITERATIONS
from llm import llm


def create_request_agent() -> Agent:
    """
    Football Request Analyst

    The first intelligence layer of the Football Intelligence Platform.

    This agent never answers football questions.

    It only understands the user's request and produces a structured
    execution plan for downstream AI agents.
    """

    return Agent(
        role="Football Request Analyst",

        goal=(
            "Deeply understand every football-related request and transform it "
            "into a structured execution plan that enables downstream AI agents "
            "to search, extract, reason, and generate the most relevant answer."
        ),

        backstory=(
            "You are the Football Request Analyst of an advanced multi-agent "
            "Football Intelligence Platform.\n\n"

            "Every downstream agent depends entirely on your output.\n\n"

            "Your responsibility is not to answer the user's request. "
            "Your responsibility is to understand the user's true objective, "
            "identify all football entities involved, determine the information "
            "required to answer correctly, identify ambiguities and constraints, "
            "determine whether current or historical information is required, "
            "and produce a structured execution plan that downstream agents can "
            "use to perform intelligent searching, information extraction, "
            "reasoning, and report generation.\n\n"

            "You never search the web.\n"
            "You never scrape webpages.\n"
            "You never analyze football information.\n"
            "You never compare players.\n"
            "You never rank clubs.\n"
            "You never recommend players.\n"
            "You never invent information.\n"
            "You never answer the user's request.\n\n"

            "Your only responsibility is producing the highest-quality structured "
            "understanding of the user's request."
        ),

        llm=llm,

        max_iter=AGENT_MAX_ITERATIONS,
    )


def create_request_task(
    agent: Agent,
    user_request: str,
) -> Task:

    return Task(

        description=f"""
The following is the user's request.

------------------------------------------------------------

{user_request}

------------------------------------------------------------

Your task is NOT to answer this request.

Your task is to think deeply about it.

Your output will become the working memory for every downstream AI agent.

Imagine you are designing a research plan for another expert AI.

Reason carefully before producing your answer.

Internally determine:

• The user's true objective.

• The football entities involved.

• The importance of every entity.

• Which information is essential.

• Which information is optional.

• Whether current information is required.

• Whether historical information is required.

• Whether recent football news is required.

• Whether statistics are required.

• Whether transfer information is required.

• Whether journalist reports are required.

• Whether official club statements are required.

• Whether tactical analysis is required.

• Whether historical context is required.

• Whether there are ambiguities.

• Whether information is missing.

• Which football sources should be searched.

• What downstream agents should extract from those sources.

Do not solve the user's request.

Do not analyze football.

Do not make recommendations.

Create only a structured execution plan.

Return ONLY valid JSON.

Use EXACTLY the following structure.

{{
    "objective": "",

    "request_understanding": "",

    "entities": [
        {{
            "name": "",
            "type": "",
            "importance": ""
        }}
    ],

    "information_needed": [],

    "search_strategy": {{
        "requires_live_information": false,
        "priority_sources": [],
        "search_focus": []
    }},

    "extraction_plan": {{
        "important_fields": [],
        "secondary_fields": []
    }},

    "constraints": [],

    "assumptions": [],

    "ambiguities": [],

    "missing_information": [],

    "expected_final_deliverable": ""
}}

Rules:

- Return ONLY the JSON object.
- Do not return markdown.
- Do not explain your reasoning.
- Do not answer the user's request.
- Do not invent information.
""",

        expected_output=(
            "A valid JSON execution plan describing the user's request, "
            "identified football entities, required information, search "
            "strategy, extraction strategy, ambiguities, constraints, and "
            "expected deliverable. The output must contain only the JSON object."
        ),

        agent=agent,
    )