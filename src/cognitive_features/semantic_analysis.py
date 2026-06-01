import re
from collections import Counter

import numpy as np

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


print("Loading Sentence Transformer...")

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

print("Sentence Transformer loaded.")


def calculate_topic_consistency(transcript):

    sentences = re.split(
        r"[.!?,;]+",
        transcript
    )

    sentences = [

        s.strip()

        for s in sentences

        if s.strip()
    ]

    if len(sentences) < 2:

        return {

            "sentence_count": len(sentences),

            "topic_consistency_score": 0
        }

    embeddings = model.encode(
        sentences
    )

    similarities = []

    for i in range(
        len(embeddings) - 1
    ):

        similarity = cosine_similarity(

            [embeddings[i]],

            [embeddings[i + 1]]

        )[0][0]

        similarities.append(
            similarity
        )

    avg_similarity = np.mean(
        similarities
    )

    topic_score = (

        (avg_similarity + 1)
        / 2

    ) * 100

    return {

        "sentence_count":
            len(sentences),

        "topic_consistency_score":
            round(
                float(topic_score),
                1
            )
    }


def analyze_semantics(transcript):

    transcript = transcript.lower()

    words = transcript.split()

    # ------------------------
    # Filler Detection
    # ------------------------

    fillers = [

        "um",
        "uh",
        "erm",
        "ah",
        "like"
    ]

    filler_count = sum(

        1

        for word in words

        if word.strip(".,!?")

        in fillers
    )

    filler_rate = (

        filler_count
        / len(words)
        * 100

    ) if words else 0

    # ------------------------
    # Sentence Length
    # ------------------------

    sentences = re.split(
        r"[.!?,;]+",
        transcript
    )

    sentences = [

        s.strip()

        for s in sentences

        if s.strip()
    ]

    avg_sentence_length = (

        sum(
            len(sentence.split())
            for sentence
            in sentences
        )

        / len(sentences)

    ) if sentences else 0

    # ------------------------
    # Lexical Diversity
    # ------------------------

    unique_words = len(
        set(words)
    )

    lexical_diversity = (

        unique_words
        / len(words)

    ) if words else 0

    # ------------------------
    # Repeated Phrases
    # ------------------------

    trigrams = [

        " ".join(
            words[i:i+3]
        )

        for i in range(
            len(words) - 2
        )
    ]

    trigram_counts = Counter(
        trigrams
    )

    repeated_phrases = {

        phrase: count

        for phrase, count

        in trigram_counts.items()

        if count > 1
    }

    # ------------------------
    # Topic Consistency
    # ------------------------

    topic_results = (

        calculate_topic_consistency(
            transcript
        )
    )

    return {

        "filler_count":
            filler_count,

        "filler_rate":
            round(
                filler_rate,
                2
            ),

        "avg_sentence_length":
            round(
                avg_sentence_length,
                2
            ),

        "lexical_diversity":
            round(
                lexical_diversity,
                3
            ),

        "repeated_phrase_count":
            len(
                repeated_phrases
            ),

        "repeated_phrases":
            repeated_phrases,

        "sentence_count":
            topic_results[
                "sentence_count"
            ],

        "topic_consistency_score":
            topic_results[
                "topic_consistency_score"
            ]
    }