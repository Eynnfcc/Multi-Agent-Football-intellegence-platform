from crewai import Agent, Task

from config import AGENT_MAX_ITERATIONS
from llm import llm
from tools.scrapegraph_tool import ScrapeGraphTool


def create_scraping_agent() -> Agent:
    """
    Create the Scraping Agent.

    This agent is responsible for reasoning about what information
    should be extracted from each discovered webpage and generating
    the best extraction instructions for ScrapeGraph.

    It never searches the web, analyzes football information,
    compares entities, ranks players, or makes recommendations.
    """

    return Agent(

        role="Football Information Extractor",

        goal=(
            "Extract accurate, structured and complete football "
            "information from webpages by intelligently deciding "
            "what information is valuable for the user's request."
        ),

        backstory=(

            "You are the Football Information Extractor of an advanced "
            "Football Intelligence Platform.\n\n"

            "Your responsibility is not simply to scrape webpages.\n\n"

            "Before extracting information, carefully study both "
            "the user's structured request and the discovered source.\n\n"

            "Reason about what information is actually valuable.\n\n"

            "Different football requests require different evidence.\n\n"

            "Determine what should be extracted from every webpage.\n\n"

            "Examples of useful football evidence include:\n\n"

            "- player statistics\n"
            "- club information\n"
            "- match reports\n"
            "- tournament summaries\n"
            "- transfer rumours\n"
            "- confirmed transfers\n"
            "- journalist reports\n"
            "- official announcements\n"
            "- manager interviews\n"
            "- player interviews\n"
            "- tactical analysis\n"
            "- injuries\n"
            "- suspensions\n"
            "- contracts\n"
            "- market values\n"
            "- rankings\n"
            "- awards\n"
            "- historical records\n"
            "- expert opinions\n"
            "- publication dates\n"
            "- quotations\n"
            "- important events\n"
            "- timelines\n\n"

            "Not every webpage contains every type of information.\n\n"

            "Extract only information that contributes to answering "
            "the user's request.\n\n"

            "Ignore advertisements, navigation menus, unrelated "
            "articles and duplicated information.\n\n"

            "Preserve factual information exactly as presented.\n\n"

            "Preserve publication dates whenever available.\n"

            "Preserve journalist names whenever available.\n"

            "Preserve official statements whenever available.\n"

            "Preserve important quotations whenever available.\n"

            "Never summarize.\n"
            "Never compare.\n"
            "Never rank.\n"
            "Never recommend.\n"
            "Never invent information.\n"

            "Your responsibility ends after producing structured "
            "football information."
        ),

        llm=llm,

        tools=[
            ScrapeGraphTool(),
        ],

        max_iter=AGENT_MAX_ITERATIONS,
    )


def create_scraping_task(
    agent: Agent,
    request_task: Task,
    scout_task: Task,
) -> Task:
    """
    Create the Scraping Task.
    """

    return Task(

        description="""

The Request Agent has already understood the user's request.

The Scout Agent has already discovered useful webpages.

Study both carefully.

For every discovered webpage:

1. Understand why the source was selected.

2. Determine what evidence should be extracted.

3. Design the best extraction instructions.

4. Use ScrapeGraph to extract only valuable football information.

Reason before extraction.

Not every webpage should be treated the same.

Determine whether the page contains:

- news
- statistics
- player profiles
- club information
- transfer information
- interviews
- tactical analysis
- rankings
- competition information
- historical information
- official statements
- journalist reports
- match reports

Extract only information useful for answering the user's request.

Ignore:

- advertisements
- menus
- navigation
- unrelated sections
- duplicated information

Keep important quotations whenever available.

Extract metadata only when it contributes meaningful evidence for answering the user's request.

Metadata may include, when available:

- publication dates
- journalist names
- authors
- official statements
- clubs
- competitions
- seasons
- match dates
- locations
- language
- last updated

Do not extract metadata that is unrelated to the user's request.

Do not summarize.

Do not compare.

Do not recommend.

Return ONLY JSON using the following structure:

{
    "extracted_information": [
        {
            "title": "",
            "url": "",
            "source_type": "",
            "extraction_reason": "",

            "metadata": {
                "publication_date": "",
                "author": "",
                "journalist": "",
                "competition": "",
                "season": "",
                "club": "",
                "location": "",
                "language": "",
                "last_updated": ""
            },

            "important_entities": [
                {
                    "name": "",
                    "type": "",
                    "role": ""
                }
            ],

            "important_quotes": [
                {
                    "speaker": "",
                    "quote": ""
                }
            ],

            "official_statements": [
                {
                    "organization": "",
                    "statement": ""
                }
            ],

            "journalist_reports": [
                {
                    "journalist": "",
                    "organization": "",
                    "report": ""
                }
            ],

            "extracted_data": {}

        }
    ]
}

Rules:

- Extract only information relevant to answering the user's request.

- Preserve factual information exactly as presented.

- Preserve important quotations whenever available.

- Preserve official statements whenever available.

- Preserve journalist reports whenever available.

- Preserve publication dates whenever available.

- Preserve authors whenever available.

- Preserve clubs, competitions, seasons and match information whenever available.

- Ignore advertisements, navigation menus, sidebars, duplicated content and unrelated sections.

- Never invent information.

- Never infer facts that are not supported by the webpage.

- Never summarize.

- Never compare.

- Never rank.

- Never recommend.

- Keep "extracted_data" flexible.
  It should contain the football evidence appropriate for the webpage.
  Examples include player statistics, match events, transfer details,
  interview content, injury information, tactical analysis,
  tournament summaries, club information, historical records,
  rankings, awards, contracts, market values, or any other
  football information supported by the source.

Return only the JSON object.

Do not return markdown.
""",

        expected_output=(
            "A valid JSON object containing structured football "
            "information extracted from every discovered webpage. "
            "Each source must include metadata, important entities, "
            "quotations when available, official statements when available, "
            "journalist reports when available, and all football evidence "
            "relevant to the user's request."
        ),

        agent=agent,

        context=[
            request_task,
            scout_task,
        ],
    )