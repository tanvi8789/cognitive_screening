import re


def analyze_transcript(transcript):

    transcript = transcript.lower()

    transcript = re.sub(
        r"[^\w\s]",
        "",
        transcript
    )

    words = transcript.split()

    total_words = len(words)

    unique_words = len(
        set(words)
    )

    ttr = (
        unique_words
        / total_words
    ) if total_words > 0 else 0

    word_counts = {}

    for word in words:

        word_counts[word] = (
            word_counts.get(word, 0)
            + 1
        )

    repeated_words = sum(

        count - 1

        for count
        in word_counts.values()

        if count > 1
    )

    avg_word_length = (

        sum(
            len(word)
            for word in words
        )

        / total_words

    ) if total_words > 0 else 0

    return {

        "word_count":
            total_words,

        "unique_words":
            unique_words,

        "lexical_diversity":
            round(ttr, 3),

        "repeated_words":
            repeated_words,

        "average_word_length":
            round(
                avg_word_length,
                2
            )
    }