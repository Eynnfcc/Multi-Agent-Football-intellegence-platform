from typing import Any, Type

from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from tavily import TavilyClient

from config import (
    SEARCH_DEPTH,
    SEARCH_TOPIC,
    TAVILY_API_KEY,
)



# ==========================================================
# Tavily Input Schema
# ==========================================================

class TavilySearchInput(BaseModel):

    query: str = Field(
        ...,
        description="The search query used to search the web."
    )



# ==========================================================
# Tavily Search Tool
# ==========================================================

class TavilySearchTool(BaseTool):

    name: str = "tavily_search"


    description: str = (
        "Search the web for reliable football information including "
        "players, clubs, statistics, transfer news, injuries, market "
        "values, and competitions."
    )


    args_schema: Type[BaseModel] = TavilySearchInput



    def _run(
        self,
        query: str
    ) -> dict[str, Any]:


        if not TAVILY_API_KEY:

            raise ValueError(
                "TAVILY_API_KEY is missing. "
                "Add it to your .env file."
            )


        # Create client only when the tool runs
        client = TavilyClient(
            api_key=TAVILY_API_KEY
        )


        results = client.search(

            query=query,

            search_depth=SEARCH_DEPTH,

            topic=SEARCH_TOPIC,

        )


        return results