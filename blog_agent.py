#!/usr/bin/env python
from dotenv import load_dotenv
load_dotenv()

import logging
import time
import anthropic  # To catch the APIStatusError
from agno.agent import Agent
from agno.models.anthropic import Claude    
from agno.tools.duckduckgo import DuckDuckGoTools

def main():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    
    topic = input("Enter a topic: ").strip()
    if not topic:
        logging.error("No topic provided. Exiting.")
        return

    # Define a query that instructs the agent to research and summarise the topic into a short blog post.
    query = (f"Research and summarise the topic: {topic}. "
             "Generate a short blog post with key insights and actionable takeaways.")

    # Create an Agent with Anthropic as the model and DuckDuckGo for web search.
    agent = Agent(
        model=Claude(id="claude-3-5-sonnet-20241022"),  # Replace with your Anthropic model id if needed
        tools=[DuckDuckGoTools()],
        description="You are a skilled blog writer who researches topics and writes concise and engaging blog posts.",
        instructions=("Search the web for the given topic using DuckDuckGo, gather key information, "
                      "and summarise it into a short, engaging blog post with actionable insights."),
        markdown=True,
        show_tool_calls=True,
    )

    max_attempts = 3
    base_delay = 5  # Base delay in seconds
    
    for attempt in range(1, max_attempts + 1):
        try:
            logging.info("Starting agent response for topic: %s (Attempt %d)", topic, attempt)
            agent.print_response(query, stream=True)
            break  # Exit loop on success
        except anthropic.APIStatusError as err:
            error_message = str(err).lower()
            if 'overloaded' in error_message:
                if attempt == max_attempts:
                    logging.error("Max retries (%d) reached. Exiting.", max_attempts)
                else:
                    delay = base_delay * (2 ** (attempt - 1))
                    logging.warning("API is overloaded (attempt %d/%d). Retrying in %d seconds...", attempt, max_attempts, delay)
                    time.sleep(delay)
            else:
                logging.error("Unexpected error occurred: %s", err)
                raise

if __name__ == "__main__":
    main() 