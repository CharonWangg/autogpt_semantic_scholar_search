## Auto-GPT Semantic Scholar Search Plugin

A plugin adding [Semantic Scholar API](https://www.semanticscholar.org/) integration into Auto GPT

## Features(more coming soon!)

- Retrieve related papers via an [unofficial semantic scholar library](https://github.com/danielnsilva/semanticscholar) via the `search_papers` command

## Installation

1. Clone this repo as instructed in the main repository
2. Add this chunk of code to the `.env` file within AutoGPT:

```
################################################################################
### SEMANTIC SCHOLAR SEARCH SETTINGS
################################################################################

SS_SEARCH_YEAR=2022 # limit of search year , default: None
SS_SEARCH_LIMIT=100 # limit of kept results (sreened by citation), default: 100
SS_SEARCH_FIELDS_OF_STUDY=['Computer Science'] # limit of search fields of study, default: None

```

