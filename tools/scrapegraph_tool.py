from typing import Any, Type

from crewai.tools import BaseTool
from pydantic import BaseModel, Field

from scrapegraph_py import (
    ScrapeGraphAI,
    ExtractRequest,
)

from config import SGAI_API_KEY



# ==========================================================
# Input Schema
# ==========================================================

class ScrapeGraphInput(BaseModel):

    url: str = Field(
        ...,
        description="The webpage URL to scrape."
    )


    prompt: str = Field(
        ...,
        description=(
            "Instructions describing exactly what "
            "information should be extracted."
        )
    )



# ==========================================================
# ScrapeGraph Tool
# ==========================================================

class ScrapeGraphTool(BaseTool):


    name: str = "scrapegraph"



    description: str = (
        "Extract structured information from a webpage "
        "using ScrapeGraph AI. Use this tool when "
        "information needs to be collected from a URL."
    )



    args_schema: Type[BaseModel] = ScrapeGraphInput




    def _run(
        self,
        url: str,
        prompt: str,
    ) -> dict[str, Any]:


        if not SGAI_API_KEY:

            raise ValueError(
                "SGAI_API_KEY is missing. "
                "Add it to your .env file."
            )



        # Create ScrapeGraph client during execution
        client = ScrapeGraphAI(
            api_key=SGAI_API_KEY
        )



        request = ExtractRequest(

            url=url,

            prompt=prompt,

        )



        response = client.extract(
            request
        )



        return response.model_dump()