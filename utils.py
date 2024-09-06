# Description: This file contains the configuration for the Neo4j and OpenAI clients.
# Environment variables for NEO4J_URI (usually `bolt://localhost:7687` ), NEO4J_PASSWORD, NEO4J_USERNAME, and OPENAI_API_KEY should be set.
# The OpenAI API key can be obtained from the OpenAI website.
# The Neo4j URI, username, and password can be obtained from the Neo4j Desktop or Aura console.

import os
from neo4j import GraphDatabase
from openai import OpenAI

# Create a Neo4j driver instance
neo4j_driver = GraphDatabase.driver(os.environ.get("NEO4J_URI"),
    auth=(os.environ.get("NEO4J_USERNAME"), os.environ.get("NEO4J_PASSWORD")),
)

# Create an OpenAI client instance
open_ai_client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)