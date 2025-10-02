<div align="center">
  <img src="docs/assets/img/ragformance_banner.png" alt="RAGFORmance : Benchmark generators for RAG">
<br/>
  <!-- Link to the documentation -->
  <a href="docs/README.md"><strong> 📚 Explore RAGFORmance docs »</strong></a>
  <br>

</div>

[![Build status](https://github.com/FOR-sight-ai/RAGFORmance/actions/workflows/publish.yml/badge.svg?branch=main)](https://github.com/FOR-sight-ai/ragformance/actions)
[![Version](https://img.shields.io/pypi/v/ragformance?color=blue)](https://pypi.org/project/ragformance/)
[![Python Version](https://img.shields.io/pypi/pyversions/ragformance.svg?color=blue)](https://pypi.org/project/ragformance/)
[![Downloads](https://static.pepy.tech/badge/ragformance)](https://pepy.tech/project/ragformance)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/FOR-sight-ai/ragformance/blob/main/LICENSE)

RAGFORMance is a library for generating benchmarks for Retrieval Augmented Generation systems.

RAGFORMance wraps multiple question/answers dataset generators, such as RAGAS, DeepEval or Your-Bench, as well as proposing different types of generators relevant for testing industrial use cases. Some generators are using LLMs, some are relying on custom logic.

RAGFORMancealso wraps multiple connectors to well known RAG system to be testes, such as OpenWebUI, Haystack, Ragflow, or custom developments on langchain or llama index.

Finally, RAGFORMance offers different metrics by wrapping to state of the art libraries such as TrecEval, LLM metrics from RAGAS or DeepEval, and proposing custom metrics and visualization that are relevant for different types of RAG systems.

# Installation

Install the library using pip: `pip install ragformance` or `pip install ragformance[all]` to install all the generators, RAG wrappers and metrics (including wrappers to RAGAS and DeepEval)

# Usage

## Usage as a library

The library contains 4 types of functions :
* **Generators** that take document as inputs and generates different types of evaluation datasets
* **Data Loaders** that convert well known dataset formats from and to the RAGFORmance format
* **RAG wrappers** that automatically runs the evaluations on a given RAG chain
* **Metrics** that evaluates both the Retrieval capabilities and the end answer


Complete exemples can be found in the documentation, here is a code snippet that should run after installation.

``` python
from ragformance.dataloaders import load_beir_dataset

from ragformance.rag.naive_rag import NaiveRag
from ragformance.rag.config import NaiveRagConfig


corpus, queries = load_beir_dataset(filter_corpus = True)

config = NaiveRagConfig(EMBEDDING_MODEL = "all-MiniLM-L6-v2")

naive_rag = NaiveRag(config)
doc_uploaded_num = naive_rag.upload_corpus(corpus)
answers = naive_rag.ask_queries(queries)


from ragformance.eval import trec_eval_metrics
from ragformance.eval import visualize_semantic_F1, display_semantic_quadrants

metrics = trec_eval_metrics(answers)

quadrants = visualize_semantic_F1(corpus, answers, embedding_config={"model": "all-MiniLM-L6-v2"})

display_semantic_quadrants(quadrants)



```


## Usage as a CLI or python pipeline

The second way to use RAGformance is as a standalone programme or executable, through the command-line interface (CLI) with a configuration file. After installation with pip or through the pre-compiled libraries available on github, you can run the following command :

`ragformance --config your_config.json`

This corresponds to the following python code :

```python
from ragformance.cli.run import run_pipeline

corpus, queries, answers, metrics_data, display_widget = run_pipeline("config.json")
```

### Configuring the pipeline

Data generation and pipelines in particular are controlled via the `generation` section within your `your_config.json` file. Here is an exemple that reproduces the same execution as above : loading the BEIR dataset, testing on Naive_RAG and generating metrics and visualizations

**Example `config.json` snippet for data generation:**
```json
{
    "generation": {
        "type": "alpha",
        "source": {
            "path": "path/to/your/input_data"
        },
        "output": {
            "path": "path/to/your/output_folder"
        },
        "params": {}
    },
    "dataset": {
        "source_type": "beir",
        "path": "scifact",
        "filter_corpus": true
    },
    "data_path": "data",
    "rag": {
        "rag_type": "naive",
        "params": {
            "EMBEDDING_MODEL": "all-MiniLM-L6-v2"
        }
    },
    "steps": {
        "generation": false,
        "upload_hf": false,
        "load_dataset": true,
        "evaluation": true,
        "metrics": true,
        "visualization": true
    }
}

```

## Generate Data

Generators each have specific configuration parameters. They usually take a folder as input and produce a folder as output with the jsonl dataset. Here is an exemple with a generator that does not require an LLM backend :

```python
from forcolate import convert_URLS_to_markdown

query = "Download and convert https://fr.wikipedia.org/wiki/Grand_mod%C3%A8le_de_langage and https://fr.wikipedia.org/wiki/Ascenseur_spatial"

convert_URLS_to_markdown(query, "", "data/wikipedia")

from ragformance.generators.structural_generator import StructuralGenerator, StructuralGeneratorConfig
config = StructuralGeneratorConfig(
    data_path = "data/wikipedia",
    output_path = "data/wikipedia_questions")

corpus, queries = StructuralGenerator().run(config)
```

This can also be run in a full pipeline (cli or library) with the following config file and python command:

```json
{
    "generation": {
        "type": "structural_generator",
        "source": {
            "path": "data/wikipedia"
        },
        "output": {
            "path": "data/wikipedia_questions"
        },
        "params": {}
    },
    "data_path": "data",
    "steps": {
        "generation": true
    }
}

```

```python
from forcolate import convert_URLS_to_markdown

query = "Download and convert https://fr.wikipedia.org/wiki/Grand_mod%C3%A8le_de_langage and https://fr.wikipedia.org/wiki/Ascenseur_spatial"

convert_URLS_to_markdown(query, "", "data/wikipedia")

from ragformance.cli.run import run_pipeline

corpus, queries, answers, metrics_data, display_widget = run_pipeline("config.json")
```

For detailed information on available generators, their specific parameters, and advanced configuration, please refer to the [**Generators Documentation**](ragformance/generators/README.md).


## Dataset Structure
The dataset consists of two files:
- `corpus.jsonl`: A jsonl file containing the corpus of documents. Each document is represented as a json object with the following fields:
    - `_id`: The id of the document.
    - `title`: The title of the document.
    - `text`: The text of the document.
- `queries.jsonl`: A jsonl file containing the queries. Each query is represented as a json object with the following fields:
    - `_id`: The id of the query.
    - `query_text`: The text of the query.
    - `relevant_document_ids`: A list of references to the documents in the corpus. Each reference is represented as a json object with the following fields:
        - `corpus_id`: The id of the document.
        - `score`: The score of the reference.
    - `ref_answer`: The reference answer for the query.
    - `metadata`: A dictionary containing the metadata for the query.

This structure is inspired by the popular BEIR format, with the inclusion of the `qrels`file inside the queries : indeed, BEIR is optimized for Information Retrieval tasks whereas this library aims also to evaluates other tasks (such as end to end generation).


### Answer Output Format
The answers generated by the system are structured as a json lines, with each line corresponding to a processed question. Each entry contains:

- `query`: A dictionary describing the original question, with:
  - `_id`: Unique identifier for the question.
  - `query_text`: The question text.
  - `relevant_document_ids`: A list of corpus documents considered as references for this question, each reference containing:
    - `corpus_id`: The document identifier.
    - `score`: The importance or relevance score.
  - `ref_answer`: The reference (gold standard) answer for the question.
- `model_answer`: The generated answer
- `relevant_documents_ids`: A list of corpus document IDs used as context for generating the answer.
- `retrieved_documents_distances`: A list of relevancy scores for the retrieved documents.

It is based on the following pydantic model
```python
from typing import Dict, List, Optional
from pydantic import BaseModel, Field


class RelevantDocumentModel(BaseModel):
    corpus_id: str
    score: int

class AnnotatedQueryModel(BaseModel):
    id: str = Field(alias="_id")
    query_text: str

    relevant_document_ids: List[RelevantDocumentModel]
    ref_answer: str

    metadata: Optional[Dict] = None

class AnswerModel(BaseModel):
    id: str = Field(alias="_id")

    query: AnnotatedQueryModel

    # model output
    model_answer: str
    retrieved_documents_ids: List[str]
    retrieved_documents_distances: Optional[List[float]] = None
```


## Loading a dataset from jsonl

```python
from typing import List

from ragformance.models.corpus import DocModel
from ragformance.rag.naive_rag import NaiveRag
from pydantic import TypeAdapter

ta = TypeAdapter(List[DocModel])

# load from jsonl file
with open("output/corpus.jsonl","r") as f:
    corpus= ta.validate_python([json.loads(line) for line in f])

naive_rag = NaiveRag()
naive_rag.upload_corpus(corpus=corpus)

```

## Additionnal features

To keep the core library lightweight, but still allow multiple integrations, all the features below are packaged optionnaly in the library. You must install them with a specific command or generally :

```bash
pip install ragformance[all]
```

### Loading a dataset from Hugging face

You can use directly datasets with the correct format that are hosted on Hugging Face. First install optionnal dependencies with :

```bash
pip install ragformance[huggingface]
```

``` python

from typing import List

from ragformance.models.corpus import DocModel
from ragformance.models.answer import AnnotatedQueryModel
from ragformance.rag.naive_rag import NaiveRag
from pydantic import TypeAdapter

from datasets import load_dataset
ta = TypeAdapter(List[DocModel])
taq = TypeAdapter(List[AnnotatedQueryModel])

corpus= ta.validate_python(load_dataset("FOR-sight-ai/ragformance_toloxa", "corpus", split="train"))
queries = taq.validate_python(load_dataset("FOR-sight-ai/ragformance_toloxa", "queries", split="train"))

naive_rag = NaiveRag()
doc_uploaded_num = naive_rag.upload_corpus(corpus=corpus)
answers = naive_rag.ask_queries(queries)


```


### Pushing dataset to Hugging Face Hub
This function pushes the two jsonl files to a Hugging Face Hub dataset repository; you must set the environment variable HF_TOKEN, either in system environment or config.json

``` python
from ragformance.dataloaders import push_to_hub
HFpath = "YOUR_NAME/YOUR_PATH"
push_to_hub(HFpath, "output")
```


### Trec-Eval Metrics and visualization
This library wraps the trec eval tools for Information Retrieval metrics. Make sure to install the optional dependency with:

```bash
pip install ragformance[trec-eval]
```
It provides also a set metrics visualization to help assess if the test dataset is well balanced and if a solution under test has the expected performances.

```python
from ragformance.eval import trec_eval_metrics
from ragformance.eval import visualize_semantic_F1, display_semantic_quadrants

metrics = trec_eval_metrics(answers)

quadrants = visualize_semantic_F1(corpus, answers)

display_semantic_quadrants(quadrants)
```

### Using DeepEval metrics

You can also use DeepEval metrics for LLM-based evaluation. Make sure to install the optional dependency with:

```bash
pip install ragformance[deepeval]
```

Example usage:

```python
from ragformance.eval import compute_deepeval_metrics

additional_metrics = {
    "FaithfulnessMetric": True
}
metric = compute_deepeval_metrics(
    corpus,
    answers,
    llm_api_key="your API key",
    additional_metrics=additional_metrics
)
print(metric)
```

### Tracing

To enable tracing with Arize Phoenix, you need to install the optional Phoenix dependencies:

```bash
pip install ragformance[phoenix]
```

Then add the following section to your `config.json` file (all parameters are optional except `enable`; defaults are shown):

```json
{
  "phoenix": {
    "enable": true,
    "endpoint": "http://localhost:6006",  // Phoenix server address (optional)
    "project_name": "ragformance"         // Project name for tracing (optional)
  },
  ...
}
```

When enabled, RAGformance will automatically instrument the generation pipelines and send traces to the Phoenix server specified in `endpoint` (default: http://localhost:6006). You can start the Phoenix UI with:

```bash
phoenix serve
```

Then open [http://localhost:6006/](http://localhost:6006/) (or your custom endpoint) in your browser to view traces and metrics.

For more details, see the [Phoenix documentation](https://docs.arize.com/phoenix/).

## Acknowledgement

This project received funding from the French ”IA Cluster” program within the Artificial and Natural Intelligence Toulouse Institute (ANITI) and from the "France 2030" program within IRT Saint Exupery. The authors gratefully acknowledge the support of the FOR projects.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
