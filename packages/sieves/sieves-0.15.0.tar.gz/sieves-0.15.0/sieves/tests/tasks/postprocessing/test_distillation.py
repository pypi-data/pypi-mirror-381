# mypy: ignore-errors
import os
from pathlib import Path
from tempfile import TemporaryDirectory

import datasets
import model2vec
import model2vec.inference
import model2vec.train
import numpy as np
import openai
import outlines
import pytest
import setfit

from sieves import Doc, Pipeline, GenerationSettings
from sieves.engines import EngineType
from sieves.serialization import Config
from sieves.tasks import Distillation, DistillationFramework, Classification
from sieves.tasks.predictive import classification


def _get_docs() -> list[Doc]:
    science_text = (
        "Scientists report that plasma is a state of matter. They published an academic paper. This is about science -"
        " scientists, papers, experiments, laws of nature."
    )
    politics_text = (
        "A new law has been passed. The opposition doesn't support it, but parliament has voted on it. This is about "
        "politics - parliament, laws, parties, politicians."
    )

    return [
        *[Doc(text=f"{i}. {science_text}") for i in range(5)],
        *[Doc(text=f"{i}. {politics_text}") for i in range(5)],
    ]


@pytest.mark.parametrize("batch_runtime", (EngineType.huggingface,), indirect=["batch_runtime"])
@pytest.mark.parametrize("distillation_framework", DistillationFramework.all())
def test_distillation_classification(batch_runtime, distillation_framework) -> None:
    seed = 42
    base_model_id = "sentence-transformers/paraphrase-mpnet-base-v2"
    if distillation_framework == DistillationFramework.model2vec:
        base_model_id = "minishlab/potion-base-32M"

    docs = _get_docs()

    with TemporaryDirectory() as tmp_dir:
        classifier = classification.Classification(
            task_id="classifier",
            labels=["science", "politics"],
            model=batch_runtime.model,
            generation_settings=batch_runtime.generation_settings,
            label_descriptions={
                "science": "Topics related to scientific disciplines and research",
                "politics": "Topics related to government, elections, and political systems",
            },
        )
        pipe = Pipeline(
            [
                classifier,
                Distillation(
                    target_task_id="classifier",
                    base_model_id=base_model_id,
                    framework=distillation_framework,
                    output_path=Path(tmp_dir),
                    train_frac=0.5,
                    val_frac=0.5,
                    seed=seed,
                ),
            ],
        )

        if distillation_framework == DistillationFramework.sentence_transformers:
            with pytest.raises(NotImplementedError):
                list(pipe(docs))
            return
        else:
            docs = list(pipe(docs))

        assert pipe["Distillation"].target_task == classifier

        # Ensure equality of saved with original dataset.
        hf_dataset = classifier.to_hf_dataset(docs)
        hf_dataset = classifier._split_dataset(hf_dataset, 0.5, 0.5, seed)
        hf_dataset_loaded = datasets.DatasetDict.load_from_disk(Path(tmp_dir) / "data")
        for split in ("train", "val"):
            assert hf_dataset_loaded[split].info == hf_dataset[split].info
            assert hf_dataset_loaded[split]["text"] == hf_dataset[split]["text"]
            assert hf_dataset_loaded[split]["labels"] == hf_dataset[split]["labels"]

        # Assert predictions of distilled models look as expected.
        test_sents = ["This is about the galaxy and laws of nature.", "This is about political election and lobbying."]

        match distillation_framework:
            case DistillationFramework.setfit:
                model = setfit.SetFitModel.from_pretrained(tmp_dir)
                preds = model.predict(test_sents, as_numpy=True)
                assert preds.shape == (2, 2)

            case DistillationFramework.model2vec:
                model = model2vec.inference.StaticModelPipeline.from_pretrained(tmp_dir)
                preds = model.predict(test_sents)
                assert set(np.unique(preds).tolist()) <= {"science", "politics"}
                assert preds.shape[0] == 2
                assert preds.shape[1] in (1, 2)


@pytest.mark.parametrize("batch_runtime", [EngineType.huggingface], indirect=["batch_runtime"])
def test_serialization(classification_docs, batch_runtime) -> None:
    seed = 42
    dir_path: str | None

    with TemporaryDirectory() as tmp_dir:
        dir_path = tmp_dir
        classifier = classification.Classification(
            task_id="classifier",
            labels=["science", "politics"],
            model=batch_runtime.model,
            generation_settings=batch_runtime.generation_settings,
            label_descriptions={
                "science": "Topics related to scientific disciplines and research",
                "politics": "Topics related to government, elections, and political systems",
            },
        )
        pipe = Pipeline(
            [
                classifier,
                Distillation(
                    target_task_id="classifier",
                    base_model_id="sentence-transformers/paraphrase-mpnet-base-v2",
                    framework=DistillationFramework.setfit,
                    output_path=Path(tmp_dir),
                    train_frac=0.5,
                    val_frac=0.5,
                    seed=seed,
                ),
            ],
        )

    config = pipe.serialize()
    assert config.model_dump() == {'cls_name': 'sieves.pipeline.core.Pipeline',
 'tasks': {'is_placeholder': False,
           'value': [{'cls_name': 'sieves.tasks.predictive.classification.core.Classification',
                      'fewshot_examples': {'is_placeholder': False,
                                           'value': ()},
                      'generation_settings': {'is_placeholder': False,
                                              'value': {'batch_size': -1,
                                                        'config_kwargs': None,
                                                        'inference_kwargs': None,
                                                        'init_kwargs': None,
                                                        'strict_mode': False}},
                      'include_meta': {'is_placeholder': False, 'value': True},
                      'label_descriptions': {'is_placeholder': False,
                                             'value': {'politics': 'Topics '
                                                                   'related to '
                                                                   'government, '
                                                                   'elections, '
                                                                   'and '
                                                                   'political '
                                                                   'systems',
                                                       'science': 'Topics '
                                                                  'related to '
                                                                  'scientific '
                                                                  'disciplines '
                                                                  'and '
                                                                  'research'}},
                      'labels': {'is_placeholder': False,
                                 'value': ['science', 'politics']},
                      'model': {'is_placeholder': True,
                                'value': 'transformers.pipelines.zero_shot_classification.ZeroShotClassificationPipeline'},
                      'prompt_signature_desc': {'is_placeholder': False,
                                                'value': None},
                      'prompt_template': {'is_placeholder': False,
                                          'value': None},
                      'task_id': {'is_placeholder': False,
                                  'value': 'classifier'},
                      'version': Config.get_version()},
                     {'base_model_id': {'is_placeholder': False,
                                        'value': 'sentence-transformers/paraphrase-mpnet-base-v2'},
                      'cls_name': 'sieves.tasks.postprocessing.distillation.core.Distillation',
                      'framework': {'is_placeholder': False, 'value': 'setfit'},
                      'include_meta': {'is_placeholder': False, 'value': False},
                      'init_kwargs': {'is_placeholder': False, 'value': {}},
                      'output_path': {'is_placeholder': False, 'value': str(dir_path)},
                      'target_task_id': {'is_placeholder': False,
                                         'value': 'classifier'},
                      'task_id': {'is_placeholder': False,
                                  'value': 'Distillation'},
                      'threshold': {'is_placeholder': False, 'value': 0.5},
                      'train_frac': {'is_placeholder': False, 'value': 0.5},
                      'train_kwargs': {'is_placeholder': False, 'value': {}},
                      'val_frac': {'is_placeholder': False, 'value': 0.5},
                      'version': Config.get_version()}]},
 'use_cache': {'is_placeholder': False, 'value': True},
 'version': Config.get_version()}



    Pipeline.deserialize(config=config, tasks_kwargs=[{"model": batch_runtime.model}, {}])


@pytest.mark.skip(reason="No OpenAI API key available in GitHub CI yet")
def test_distillation_with_openai_model() -> None:
    """Test distillation with an OpenAI model.

    See https://github.com/MantisAI/sieves/issues/162.
    """
    client = openai.OpenAI(api_key=os.environ['OPENAI_API_KEY'])
    model = outlines.from_openai(client=client, model_name='gpt-5-nano')

    classifier = Classification(
        task_id='classifier',
        labels=['Fruit', 'Vegetable'],
        model=model,
        generation_settings=GenerationSettings(batch_size=32, strict_mode=False),
    )

    distiller = Distillation(
        target_task_id='classifier',
        base_model_id='sentence-transformers/paraphrase-mpnet-base-v2',
        framework=DistillationFramework.setfit,
        output_path='./model',
        train_frac=.5,
        val_frac=.5,
    )

    pipe = classifier + distiller
    list(pipe([Doc(text='Apple'), Doc(text='Cucumber'), Doc(text="Broccoli"), Doc(text='Pomegranate')]))
