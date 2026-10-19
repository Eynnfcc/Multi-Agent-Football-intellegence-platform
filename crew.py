from crewai import Crew, Process

from agents.request_agent import (
    create_request_agent,
    create_request_task,
)

from agents.scout_agent import (
    create_scout_agent,
    create_scout_task,
)

from agents.scraping_agent import (
    create_scraping_agent,
    create_scraping_task,
)

from agents.recommendation_agent import (
    create_recommendation_agent,
    create_recommendation_task,
)

from agents.report_agent import (
    create_report_agent,
    create_report_task,
)


def create_crew(user_request: str) -> Crew:
    """
    Create the Football Scout Crew.

    Workflow:
    1. Request Agent
    2. Scout Agent
    3. Scraping Agent
    4. Recommendation Agent
    5. Report Agent
    """

    # -----------------------------
    # Create Agents
    # -----------------------------

    request_agent = create_request_agent()

    scout_agent = create_scout_agent()

    scraping_agent = create_scraping_agent()

    recommendation_agent = create_recommendation_agent()

    report_agent = create_report_agent()

    # -----------------------------
    # Create Tasks
    # -----------------------------

    request_task = create_request_task(
        request_agent,
        user_request,
    )

    scout_task = create_scout_task(
        scout_agent,
        request_task,
    )

    scraping_task = create_scraping_task(
        scraping_agent,
        request_task,
        scout_task,
    )

    recommendation_task = create_recommendation_task(
        recommendation_agent,
        request_task,
        scraping_task,
    )

    report_task = create_report_task(
        report_agent,
        recommendation_task,
    )

    # -----------------------------
    # Create Crew
    # -----------------------------

    crew = Crew(
        agents=[
            request_agent,
            scout_agent,
            scraping_agent,
            recommendation_agent,
            report_agent,
        ],

        tasks=[
            request_task,
            scout_task,
            scraping_task,
            recommendation_task,
            report_task,
        ],

        process=Process.sequential,

        verbose=True, #I put it true to see the exceutiong logs while developing and debugging . Now After Finishsing U Can make it False
    )

    return crew
