from __future__ import annotations

import logging
import os
from os.path import expanduser

from ..datatypes import (
    Config,
    Document,
    CandidateEntitiesForDocument,
)
from .. import utils
from .dummy_entity_retriever import DummyEntityRetriever
from .blink_bi_encoder import BlinkBiEncoder


logger = logging.getLogger(__name__)


class EDRetrieval:
    
    def __init__(self, identifier: str, gpu : int = 0):
        self.identifier = identifier
        self.gpu = gpu

        root_config: Config = utils.get_hocon_config(
            os.path.join(expanduser("~"), ".kapipe", "download", "config")
        )
        self.component_config: Config = root_config["ed_retrieval"][identifier]

        # # Download the configurations
        # utils.download_folder_if_needed(
        #     dest=self.component_config["snapshot"],
        #     url=self.component_config["url"]
        # )
       
        # Initialize the ED-Retrieval retriever
        if self.component_config["method"] == "dummy_entity_retriever":
            self.retriever = DummyEntityRetriever()
        elif self.component_config["method"] == "blink_bi_encoder": 
            self.retriever = BlinkBiEncoder(
                device=f"cuda:{self.gpu}",
                path_snapshot=self.component_config["snapshot"]
            )
            # Build the index based on the pre-computed embeddings
            self.retriever.make_index(use_precomputed_entity_vectors=True)
        else:
            raise Exception(f"Invalid method: {self.component_config['method']}")

    def search(
        self,
        document: Document,
        num_candidate_entities: int = 10
    ) -> tuple[Document, CandidateEntitiesForDocument]:
        # Apply the retriever to the document
        return self.retriever.search(
            document=document,
            retrieval_size=num_candidate_entities
        )

