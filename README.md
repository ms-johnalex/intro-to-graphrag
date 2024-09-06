# Intro to GraphRAG using LangChain and Neo4j

Welcome to my Intro to GraphRAG presentation repo! You'll find the demo files here.

## Setup

* Install either [Neo4j Desktop (local instance)](https://neo4j.com/download/) or [Aura (cloud instance)](https://neo4j.com/product/auradb/)
* Install needed python libraries
* Environment variables for `NEO4J_URI` (usually `bolt://localhost:7687` ), `NEO4J_PASSWORD`, `NEO4J_USERNAME`, and `OPENAI_API_KEY` should be set.

  NOTE: The Neo4j URI, username, and password can be obtained from the Neo4j Desktop or Aura console. The OpenAI API key can be obtained from the OpenAI website.

* Use the default Movies database for querying_the_knowledge_graph.ipynb
* Create a new database for intro_graphrag_w_langchain_neo4j.ipynb
* Install the `APOC` plugin.

## Recommended order of notebooks

* [querying_the_knowledge_graph.ipynb](https://github.com/ms-johnalex/intro-to-graphrag/blob/main/querying_the_knowledge_graph.ipynb)
* [intro_graphrag_w_langchain_neo4j.ipynb](https://github.com/ms-johnalex/intro-to-graphrag/blob/main/intro_graphrag_w_langchain_neo4j.ipynb)

## Resources

* [https://github.com/neo4j-graph-examples/get-started](https://github.com/neo4j-graph-examples/get-started)
* [Enhancing the Accuracy of RAG Applications With Knowledge Graphs | by Tomaz Bratanic](https://medium.com/neo4j/enhancing-the-accuracy-of-rag-applications-with-knowledge-graphs-ad5e2ffab663)
* [Support files repo for Tomaz's blog posts](https://github.com/tomasonjo/blogs/tree/master)
* [Project GraphRAG Web Site](https://aka.ms/graphrag)
* [GraphRAG Python implementation](https://microsoft.github.io/graphrag/)
* [Microsoft GraphRAG Accelerator](https://github.com/Azure-Samples/graphrag-accelerator)
