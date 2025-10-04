from __future__ import annotations

from collections import OrderedDict
import datetime
from importlib.resources import files, as_file
import io
import json
import logging
import os
import requests
import time
from typing import Any, Callable
import zipfile

import numpy as np
import pyhocon
from pyhocon.converter import HOCONConverter
from pyhocon import ConfigTree

from .datatypes import Document, Mention, Entity, Passage


logger = logging.getLogger(__name__)


########
# IO utilities
########


def read_lines(path: str, encoding: str = "utf-8") -> list[str]:
    with open(path, encoding=encoding) as f:
        lines = [l.strip() for l in f]
    return lines


def read_json(path: str, encoding: str | None = None) -> dict[Any, Any]:
    if encoding is None:
        with open(path) as f:
            dct = json.load(f)
    else:
        with io.open(path, "rt", encoding=encoding) as f:
            line = f.read()
            dct = json.loads(line)
    return dct


def write_json(path: str, dct: dict[Any, Any], ensure_ascii: bool = True) -> None:
    with open(path, "w") as f:
        json.dump(dct, f, ensure_ascii=ensure_ascii, indent=4)


def read_vocab(path: str) -> dict[str, int]:
    # begin_time = time.time()
    # logger.info("Loading a vocabulary from %s" % path)
    vocab = OrderedDict()
    for line in open(path):
        items = line.strip().split("\t")
        if len(items) == 2:
            word, word_id = items
        elif len(items) == 3:
            word, word_id, freq = items
        else:
            raise Exception("Invalid line: %s" % items)
        vocab[word] = int(word_id)
    # end_time = time.time()
    # logger.info("Loaded. %f [sec.]" % (end_time - begin_time))
    # logger.info("Vocabulary size: %d" % len(vocab))
    return vocab


def write_vocab(
    path: str,
    data: list[tuple[str, int]] | list[str],
    write_frequency: bool = True
) -> None:
    with open(path, "w") as f:
        if write_frequency:
            for word_id, (word, freq) in enumerate(data):
                f.write("%s\t%d\t%d\n" % (word, word_id, freq))
        else:
            for word_id, word in enumerate(data):
                f.write("%s\t%d\n" % (word, word_id))


def get_hocon_config(config_path: str, config_name: str | None = None) -> ConfigTree:
    config = pyhocon.ConfigFactory.parse_file(config_path)
    if config_name is not None:
        config = config[config_name]
    config.config_path = config_path
    config.config_name = config_name
    # logger.info(pyhocon.HOCONConverter.convert(config, "hocon"))
    return config


def dump_hocon_config(path_out: str, config: ConfigTree) -> None:
    with open(path_out, "w") as f:
        f.write(HOCONConverter.to_hocon(config) + "\n")


def mkdir(path: str, newdir: str | None = None) -> None:
    if newdir is None:
        target = path
    else:
        target = os.path.join(path, newdir)
    if not os.path.exists(target):
        os.makedirs(target)
        logger.info("Created a new directory: %s" % target)


def print_list(
    lst: list[Any],
    with_index: bool = False,
    process: Callable[[Any], Any] | None = None
) -> None:
    for i, x in enumerate(lst):
        if process is not None:
            x = process(x)
        if with_index:
            logger.info(f"{i}: {x}")
        else:
            logger.info(x)


def safe_json_loads(
    generated_text: str,
    fallback: Any = None,
    list_type: bool = False
) -> Any:
    """
    Parse the report into a JSON object
    """
    if list_type:
        begin_index = generated_text.find("[")
        end_index = generated_text.rfind("]")
    else:
        begin_index = generated_text.find("{")
        end_index = generated_text.rfind("}")
    if begin_index < 0 or end_index < 0:
        logger.info(f"Failed to parse the generated text into a JSON object: '{generated_text}'")
        return fallback

    json_text = generated_text[begin_index: end_index + 1]

    try:
        json_obj = json.loads(json_text)
    except Exception as e:
        logger.info(f"Failed to parse the generated text into a JSON object: '{json_text}'")
        logger.info(e)
        return fallback

    if list_type:
        if not isinstance(json_obj, list):
            logger.info(f"The parsed JSON object is not a list: '{json_obj}'")
            return fallback
    else:
        if not isinstance(json_obj, dict):
            logger.info(f"The parsed JSON object is not a dictionary: '{json_obj}'")
            return fallback

    return json_obj


# def download_folder_if_needed(dest: str, url: str, chunk_size: int = 8192) -> None:
#     # Skip, if destination (folter) exists and is non-empty
#     if os.path.exists(dest) and os.path.isdir(dest) and os.listdir(dest):
#         return

#     # Prepare download location
#     parent_dir = os.path.dirname(dest)
#     mkdir(parent_dir)

#     # Define zip path as "<parent_dir>/<basename(dest)>.zip"
#     zip_filename = os.path.basename(dest) + ".zip"
#     zip_path = os.path.join(parent_dir, zip_filename)

#     try:
#         # Download the zip
#         with requests.get(url, stream=True, timeout=10) as response:
#             response.raise_for_status()  # Raise an error for bad status codes

#             total_size = int(response.headers.get("content-length", 0))
#             progress_bar = tqdm(
#                 total=total_size,
#                 unit='B',
#                 unit_scale=True,
#                 desc=f"Downloading {os.path.basename(zip_filename)}"
#             )

#             with open(zip_path, "wb") as f:
#                 for chunk in response.iter_content(chunk_size=chunk_size):
#                     if chunk:
#                         f.write(chunk)
#                         progress_bar.update(len(chunk))

#             progress_bar.close()

#         # Extract zip to dest
#         with zipfile.ZipFile(zip_path, "r") as zip_ref:
#             zip_ref.extractall(dest)

#     except Exception as e:
#         # Clean up on failure
#         if os.path.exists(zip_path):
#             os.remove(zip_path)
#         raise RuntimeError(f"Failed to download or extract {url} → {dest}: {e}")

#     finally:
#         # Clean up zip file
#         if os.path.exists(zip_path):
#             os.remove(zip_path)


########
# Data utilities
########


def flatten_lists(list_of_lists: list[list[Any]]) -> list[Any]:
    return [elem for lst in list_of_lists for elem in lst]


def pretty_format_dict(dct: dict[Any, Any]) -> str:
    return "{}".format(json.dumps(dct, indent=4))


########
# Time utilities
########


def get_current_time() -> str:
    return datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")


class StopWatch(object):

    def __init__(self):
        self.dictionary: dict[str | None, dict[str, float]] = {}

    def start(self, name: str | None = None):
        start_time = time.time()
        self.dictionary[name] = {}
        self.dictionary[name]["start"] = start_time

    def stop(self, name: str | None = None):
        stop_time = time.time()
        self.dictionary[name]["stop"] = stop_time

    def get_time(self, name: str | None = None, minute: bool = False) -> float:
        start_time = self.dictionary[name]["start"]
        stop_time = self.dictionary[name]["stop"]
        span = stop_time - start_time
        if minute:
            span /= 60.0
        return span


########
# Training utilities
########


class BestScoreHolder(object):

    def __init__(self, scale: float = 1.0, higher_is_better: bool = True):
        self.scale = scale
        self.higher_is_better = higher_is_better

        if higher_is_better:
            self.comparison_function = lambda best, cur: best < cur
        else:
            self.comparison_function = lambda best, cur: best > cur

        if higher_is_better:
            self.best_score = -np.inf
        else:
            self.best_score = np.inf
        self.best_step = 0
        self.patience = 0

    def init(self) -> None:
        if self.higher_is_better:
            self.best_score = -np.inf
        else:
            self.best_score = np.inf
        self.best_step = 0
        self.patience = 0

    def compare_scores(self, score: float, step: int) -> bool:
        if self.comparison_function(self.best_score, score):
            # Update the score
            logger.info("(best_score = %.02f, best_step = %d, patience = %d) -> (%.02f, %d, %d)" % \
                    (self.best_score * self.scale, self.best_step, self.patience,
                     score * self.scale, step, 0))
            self.best_score = score
            self.best_step = step
            self.patience = 0
            return True
        else:
            # Increment the patience
            logger.info("(best_score = %.02f, best_step = %d, patience = %d) -> (%.02f, %d, %d)" % \
                    (self.best_score * self.scale, self.best_step, self.patience,
                     self.best_score * self.scale, self.best_step, self.patience+1))
            self.patience += 1
            return False

    def ask_finishing(self, max_patience: int) -> bool:
        if self.patience >= max_patience:
            return True
        else:
            return False


########
# Task-specific utilities
########


def aggregate_mentions_to_entities(document: Document, mentions: list[Mention]):
    entity_id_to_info: dict[str, dict[str, Any]] = {}
    for m_i in range(len(document["mentions"])):
        name = document["mentions"][m_i]["name"]
        entity_type = document["mentions"][m_i]["entity_type"]
        entity_id = mentions[m_i]["entity_id"]
        if entity_id in entity_id_to_info:
            entity_id_to_info[entity_id]["mention_indices"].append(m_i)
            entity_id_to_info[entity_id]["mention_names"].append(name)
            # TODO
            # Confliction of entity types can appear, if EL model does not care about it.
            # assert (
            #     entity_id_to_info[entity_id]["entity_type"]
            #     == entity_type
            # )
        else:
            entity_id_to_info[entity_id] = {}
            entity_id_to_info[entity_id]["mention_indices"] = [m_i]
            entity_id_to_info[entity_id]["mention_names"] = [name]
            # TODO
            entity_id_to_info[entity_id]["entity_type"] = entity_type
    entities: list[Entity] = []
    for entity_id in entity_id_to_info.keys():
        mention_indices = entity_id_to_info[entity_id]["mention_indices"]
        mention_names = entity_id_to_info[entity_id]["mention_names"]
        entity_type = entity_id_to_info[entity_id]["entity_type"]
        entities.append({
            "mention_indices": mention_indices,
            "mention_names": mention_names,
            "entity_type": entity_type,
            "entity_id": entity_id,
        })
    return entities


def create_text_from_passage(passage: Passage, sep: str) -> str:
    if not "title" in passage:
        text = passage["text"]
    elif passage["text"].strip() == "":
        text = passage["title"]
    else:
        text = passage["title"] + sep + passage["text"]
    return text


def read_prompt_template(prompt_template_name_or_path: str) -> str:
    # List text files in "prompt_template" directory
    prompt_template_names = [
        x.name for x in files("kapipe.prompt_templates").iterdir()
        if x.name.endswith(".txt") and x.is_file() and not x.name.startswith("_")
    ]

    # Load the prompt template
    candidate_filename = prompt_template_name_or_path + ".txt"        
    if candidate_filename in prompt_template_names:
        template_path = files("kapipe.prompt_templates").joinpath(candidate_filename)
        with as_file(template_path) as path:
            with open(path, "r", encoding="utf-8") as f:
                return f.read()
    else:
        assert os.path.isfile(prompt_template_name_or_path)
        with open(prompt_template_name_or_path, "r", encoding="utf-8") as f:
            return f.read()


def create_intra_inter_map(document) -> dict[str, str]:
    intra_inter_map = {}

    # We first create token-index-to-sentence-index mapping
    token_index_to_sent_index = [] # dict[int, int], i.e., list[int]
    for sent_i, sent in enumerate(document["sentences"]):
        sent_words = sent.split()
        token_index_to_sent_index.extend(
            [sent_i for _ in range(len(sent_words))]
        )
    # We then create mention-index-to-sentence-index mapping
    mention_index_to_sentence_index = [] # list[int]
    for mention in document["mentions"]:
        begin_token_index, end_token_index = mention["span"]
        sentence_index = token_index_to_sent_index[begin_token_index]
        assert token_index_to_sent_index[end_token_index] == sentence_index
        mention_index_to_sentence_index.append(sentence_index)

    entities = document["entities"]
    for u_entity_i in range(len(entities)):
        u_entity = entities[u_entity_i]
        u_mention_indices = u_entity["mention_indices"]
        u_sent_indices = [
            mention_index_to_sentence_index[i] for i in u_mention_indices
        ]
        u_sent_indices = set(u_sent_indices)
        for v_entity_i in range(u_entity_i, len(entities)):
            v_entity = entities[v_entity_i]
            v_mention_indices = v_entity["mention_indices"]
            v_sent_indices = [
                mention_index_to_sentence_index[i] for i in v_mention_indices
            ]
            v_sent_indices = set(v_sent_indices)
            if len(u_sent_indices & v_sent_indices) == 0:
                # No co-occurent mention pairs
                intra_inter_map[f"{u_entity_i}-{v_entity_i}"] = "inter"
                intra_inter_map[f"{v_entity_i}-{u_entity_i}"] = "inter"
            else:
                # There is at least one co-occurent mention pairs
                intra_inter_map[f"{u_entity_i}-{v_entity_i}"] = "intra"
                intra_inter_map[f"{v_entity_i}-{u_entity_i}"] = "intra"
    return intra_inter_map


def create_seen_unseen_map(
    document,
    seen_pairs: set[tuple[str, str]]
) -> dict[str, str]:
    seen_unseen_map = {}
    entities = document["entities"]
    for u_entity_i in range(len(entities)):
        u_entity = entities[u_entity_i]
        u_entity_id = u_entity["entity_id"]
        for v_entity_i in range(u_entity_i, len(entities)):
            v_entity = entities[v_entity_i]
            v_entity_id = v_entity["entity_id"]
            if (
                ((u_entity_id, v_entity_id) in seen_pairs)
                or
                ((v_entity_id, u_entity_id) in seen_pairs)
            ):
                seen_unseen_map[f"{u_entity_id}-{v_entity_id}"] = "seen"
                seen_unseen_map[f"{v_entity_id}-{u_entity_id}"] = "seen"
            else:
                seen_unseen_map[f"{u_entity_id}-{v_entity_id}"] = "unseen"
                seen_unseen_map[f"{v_entity_id}-{u_entity_id}"] = "unseen"
    return seen_unseen_map

