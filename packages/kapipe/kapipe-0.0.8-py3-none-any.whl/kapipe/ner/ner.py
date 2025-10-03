from __future__ import annotations

import logging
import os
from os.path import expanduser

from .biaffine_ner import BiaffineNER
from .llm_ner import LLMNER
from ..demonstration_retrieval import DemonstrationRetriever
from .. import utils
from ..datatypes import (
    Config,
    Document,
    DemonstrationsForOneExample
)


logger = logging.getLogger(__name__)


class NER:

    def __init__(
        self,
        identifier: str,
        gpu: int = 0,
        user_defined_entity_types: list[dict[str,str]] | None = None
    ):
        self.identifier = identifier
        self.gpu = gpu
        self.user_defined_entity_types = user_defined_entity_types

        root_config: Config = utils.get_hocon_config(
            os.path.join(expanduser("~"), ".kapipe", "download", "config")
        )
        self.module_config: Config = root_config["ner"][identifier]

        # # Download the configurations
        # utils.download_folder_if_needed(
        #     dest=self.module_config["snapshot"],
        #     url=self.module_config["url"]
        # )

        # Initialize the NER extractor
        if self.module_config["method"] == "biaffine_ner":
            self.extractor = BiaffineNER(
                device=f"cuda:{self.gpu}",
                path_snapshot=self.module_config["snapshot"]
            )
        elif self.module_config["method"] == "llm_ner":
            if user_defined_entity_types is None:
                # Use pre-defined entity types corresponding to the identifier
                self.extractor = LLMNER(
                    device=f"cuda:{self.gpu}",
                    path_snapshot=self.module_config["snapshot"],
                    model=None,
                )
            else:
                # Use the user-defined entity types
                self.extractor = LLMNER(
                    device=f"cuda:{self.gpu}",
                    vocab_etype={
                        x["entity_type"]: i
                        for i, x in enumerate(user_defined_entity_types)
                    },
                    etype_meta_info={
                        x["entity_type"]: {
                            "Pretty Name": x["entity_type"],
                            "Definition": x["definition"]
                        }
                        for x in user_defined_entity_types
                    },
                    path_snapshot=self.module_config["snapshot"],
                    model=None,
                )

            # Initialize the demonstration retriever
            self.demonstration_retriever = DemonstrationRetriever(
                path_demonstration_pool=self.extractor.prompt_processor.path_demonstration_pool,
                method="count",
                task="ner"
            )
        else:
            raise Exception(f"Invalid method: {self.module_config['method']}")

    def extract(self, document: Document) -> Document:
        if self.module_config["method"] == "llm_ner":
            # Get demonstrations for this document
            demonstrations_for_doc: DemonstrationsForOneExample = (
                self.demonstration_retriever.search(
                    document=document,
                    top_k=5
                )
            )
            # Apply the extractor to the document
            return self.extractor.extract(
                document=document,
                demonstrations_for_doc=demonstrations_for_doc
            )
        else:
            # Apply the extractor to the document
            return self.extractor.extract(document=document)

