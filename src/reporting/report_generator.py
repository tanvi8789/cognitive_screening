import json


def generate_report(profile):

    report = []

    report.append(
        "\n===== COGNITIVE COMMUNICATION REPORT =====\n"
    )

    # ====================================
    # TEMPORAL
    # ====================================

    temporal = profile["temporal"]

    report.append(
        "\nTEMPORAL INDICATORS"
    )

    report.append(
        "-" * 25
    )

    report.append(
        f"Pause Count: {temporal['pause_count']}"
    )

    report.append(
        f"Average Pause: {temporal['average_pause_duration']} sec"
    )

    report.append(
        f"Silence Percentage: {temporal['silence_percentage']}%"
    )

    # ====================================
    # FLUENCY
    # ====================================

    fluency = profile["fluency"]

    report.append(
        "\nFLUENCY INDICATORS"
    )

    report.append(
        "-" * 25
    )

    report.append(
        f"Words Per Minute: {fluency['words_per_minute']}"
    )

    report.append(
        f"Speaking Ratio: {fluency['speaking_ratio']}%"
    )

    # ====================================
    # LANGUAGE
    # ====================================

    language = profile["language"]

    report.append(
        "\nLANGUAGE INDICATORS"
    )

    report.append(
        "-" * 25
    )

    report.append(
        f"Lexical Diversity: {language['lexical_diversity']}"
    )

    report.append(
        f"Unique Words: {language['unique_words']}"
    )

    # ====================================
    # SEMANTICS
    # ====================================

    semantic = profile["semantic"]

    report.append(
        "\nSEMANTIC INDICATORS"
    )

    report.append(
        "-" * 25
    )

    report.append(
        f"Topic Consistency Score: {semantic['topic_consistency_score']}"
    )

    report.append(
        f"Average Sentence Length: {semantic['avg_sentence_length']}"
    )

    # ====================================
    # OBSERVATIONS
    # ====================================

    report.append(
        "\nOBSERVATIONS"
    )

    report.append(
        "-" * 25
    )

    if temporal["silence_percentage"] > 25:

        report.append(
            "• Elevated silence percentage detected."
        )

    if temporal["pause_count"] > 15:

        report.append(
            "• Frequent pauses observed."
        )

    if fluency["words_per_minute"] < 120:

        report.append(
            "• Reduced speech rate detected."
        )

    if semantic["topic_consistency_score"] < 55:

        report.append(
            "• Lower topic consistency observed."
        )

    if language["lexical_diversity"] < 0.50:

        report.append(
            "• Limited vocabulary diversity detected."
        )

    if len(report) < 20:

        report.append(
            "• No major communication irregularities detected."
        )

    return "\n".join(report)


if __name__ == "__main__":

    with open(
        "output/profile.json",
        "r"
    ) as f:

        profile = json.load(f)

    report = generate_report(
        profile
    )

    print(report)

    with open(
        "output/report.txt",
        "w"
    ) as f:

        f.write(report)

    print(
        "\nReport saved:\noutput/report.txt"
    )