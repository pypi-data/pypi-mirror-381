try:
    from deepeval import evaluate
    from deepeval.evaluate import DisplayConfig
    from deepeval.test_case import LLMTestCase, LLMTestCaseParams
    from deepeval.metrics import GEval
    from deepeval.evaluate.types import EvaluationResult

    from deepeval.metrics import AnswerRelevancyMetric
    from deepeval.metrics import FaithfulnessMetric
    from deepeval.metrics import ContextualRelevancyMetric
    from deepeval.metrics import HallucinationMetric
    from deepeval.metrics import ContextualPrecisionMetric
    from deepeval.metrics import ContextualRecallMetric

    _DEEPEVAL_AVAILABLE = True
except ImportError:
    _DEEPEVAL_AVAILABLE = False

import litellm
from litellm import acompletion

from ragformance.models.answer import AnswerModel
from ragformance.models.corpus import DocModel
from typing import List

if _DEEPEVAL_AVAILABLE:
    from deepeval.test_case import LLMTestCase, LLMTestCaseParams


def _raise_deepeval_import_error():
    raise ImportError(
        "deepeval is not installed. Please install deepeval to use these features:\n"
        "    pip install ragformance[deepeval]"
    )


def convert_answers_to_deepeval_format(
    corpus: List[DocModel], answers: List[AnswerModel]
) -> List["LLMTestCase"]:
    """
    Convert answers to DeepEval format.
    """
    if not _DEEPEVAL_AVAILABLE:
        _raise_deepeval_import_error()

    deepeval_answers = []
    corpus_as_dict = {doc.id: doc for doc in corpus}

    for answer in answers:
        expected_context = []

        for doc_id in answer.query.relevant_document_ids:
            if doc_id.corpus_id in corpus_as_dict:
                expected_context.append(corpus_as_dict[doc_id.corpus_id].text)

        retrieved_context = []

        for doc_id in answer.retrieved_documents_ids:
            if doc_id in corpus_as_dict:
                retrieved_context.append(corpus_as_dict[doc_id].text)

        test_case = LLMTestCase(
            input=answer.query.query_text,
            actual_output=answer.query.ref_answer,
            expected_output=answer.model_answer,
            context=expected_context,
            retrieval_context=retrieved_context,
        )

        deepeval_answers.append(test_case)
    return deepeval_answers


class LiteLLMWrapper("DeepEvalBaseLLM" if _DEEPEVAL_AVAILABLE else object):
    def __init__(
        self,
        model="qwen/qwen3-32b:free",
        base_url="https://openrouter.ai/api/v1",
        llm_api_key="your_api_key_here",  # Replace with your actual API key
        **kwargs,
    ):
        self.model = model
        self.base_url = base_url
        self.llm_api_key = llm_api_key

    def load_model(self):
        return self.model

    def generate(self, prompt: str) -> str:
        return (
            litellm.completion(
                model="openai/" + self.model,
                base_url=self.base_url,
                api_key=self.llm_api_key,
                messages=[{"content": prompt, "role": "user"}],
            )
            .choices[0]
            .message.content.strip()
        )

    async def a_generate(self, prompt: str) -> str:
        res = await acompletion(
            model="openai/" + self.model,
            base_url=self.base_url,
            api_key=self.llm_api_key,
            messages=[{"content": prompt, "role": "user"}],
        )
        return res.choices[0].message.content.strip()

    def get_model_name(self):
        return "Custom LiteLLM Model"


def metric_deepeval_geval(
    test_cases: List["LLMTestCase"],
    geval_name="Correctness",
    geval_criteria="Determine if the 'actual output' is correct based on the 'expected output'.",
    additional_metrics: dict = {},
    **kwargs,
):
    if not _DEEPEVAL_AVAILABLE:
        _raise_deepeval_import_error()

    model = LiteLLMWrapper(**kwargs)

    correctness_metric = GEval(
        name=geval_name,
        criteria=geval_criteria,
        evaluation_params=[
            LLMTestCaseParams.ACTUAL_OUTPUT,
            LLMTestCaseParams.EXPECTED_OUTPUT,
        ],
        threshold=0.5,
        model=model,
    )
    metrics = [correctness_metric]

    if (
        "AnswerRelevancyMetric" in additional_metrics
        and additional_metrics["AnswerRelevancyMetric"]
    ):
        metrics.append(
            AnswerRelevancyMetric(threshold=0.7, model=model, include_reason=True)
        )

    if (
        "FaithfulnessMetric" in additional_metrics
        and additional_metrics["FaithfulnessMetric"]
    ):
        metrics.append(
            FaithfulnessMetric(threshold=0.7, model=model, include_reason=True)
        )

    if (
        "ContextualRelevancyMetric" in additional_metrics
        and additional_metrics["ContextualRelevancyMetric"]
    ):
        metrics.append(
            ContextualRelevancyMetric(threshold=0.7, model=model, include_reason=True)
        )

    if (
        "HallucinationMetric" in additional_metrics
        and additional_metrics["HallucinationMetric"]
    ):
        metrics.append(
            HallucinationMetric(threshold=0.5, model=model, include_reason=True)
        )
    if (
        "ContextualPrecisionMetric" in additional_metrics
        and additional_metrics["ContextualPrecisionMetric"]
    ):
        metrics.append(
            ContextualPrecisionMetric(threshold=0.7, model=model, include_reason=True)
        )
    if (
        "ContextualRecallMetric" in additional_metrics
        and additional_metrics["ContextualRecallMetric"]
    ):
        metrics.append(
            ContextualRecallMetric(threshold=0.7, model=model, include_reason=True)
        )

    return evaluate(
        test_cases, metrics, display_config=DisplayConfig(show_indicator=False)
    )


def deepeval_output_to_metric_list(result: "EvaluationResult") -> List[dict]:
    """
    Convert DeepEval output to a list of metrics.
    """
    if not _DEEPEVAL_AVAILABLE:
        _raise_deepeval_import_error()

    metrics = []
    normalized_metrics = {}
    for single_result in result.test_results:
        for metric in single_result.metrics_data:
            metrics.append({metric.name: metric.score})
            normalized_metrics[metric.name] = metric.score + normalized_metrics.get(
                metric.name, 0
            )

    for metric_name, score in normalized_metrics.items():
        normalized_metrics[metric_name] = score / len(result.test_results)

    return metrics, normalized_metrics


def compute_deepeval_metrics(
    corpus, answers, additional_metrics={}, **kwargs
) -> List[dict]:
    """
    Compute DeepEval metrics for the given corpus and answers.
    """
    if not _DEEPEVAL_AVAILABLE:
        _raise_deepeval_import_error()

    deep_eval_answers = convert_answers_to_deepeval_format(corpus, answers)
    output = metric_deepeval_geval(
        deep_eval_answers[:2], additional_metrics=additional_metrics, **kwargs
    )
    return deepeval_output_to_metric_list(output)
