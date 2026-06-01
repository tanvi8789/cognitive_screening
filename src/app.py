import streamlit as st
import tempfile
import os

from src.cognitive_features.profile_generator import (
    generate_profile
)

from src.reporting.report_generator import (
    generate_report
)

from src.reporting.interpreter import (
    interpret_profile
)

from src.services.chart_generator import (
    create_radar_chart
)


st.set_page_config(
    page_title="AI Cognitive Wellness Screening",
    layout="wide"
)

st.title(
    "AI Cognitive Wellness Screening System"
)

st.write(
    "Upload a speech recording to generate a cognitive communication profile."
)

uploaded_file = st.file_uploader(
    "Upload Audio",
    type=["wav", "mp3"]
)

if uploaded_file:

    st.header("Uploaded Audio")

    st.audio(uploaded_file)

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".wav"
    ) as temp:

        temp.write(
            uploaded_file.read()
        )

        audio_path = temp.name

    with st.spinner(
        "Analyzing speech..."
    ):

        profile = generate_profile(
            audio_path
        )

        observations = (
            interpret_profile(
                profile
            )
        )

        report_text = generate_report(
            profile
        )

    # =========================
    # Transcript
    # =========================

    st.header("Transcript")

    st.write(
        profile["transcript"]
    )

    # =========================
    # Metrics
    # =========================

    st.header(
        "Cognitive Communication Profile"
    )

    chart = create_radar_chart(
        profile
    )

    st.plotly_chart(
        chart,
        use_container_width=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.subheader(
            "Temporal"
        )

        st.metric(
            "Pause Count",
            profile["temporal"][
                "pause_count"
            ]
        )

        st.metric(
            "Silence %",
            profile["temporal"][
                "silence_percentage"
            ]
        )

        st.metric(
            "Avg Pause (sec)",
            profile["temporal"][
                "average_pause_duration"
            ]
        )

    with col2:

        st.subheader(
            "Fluency"
        )

        st.metric(
            "Words / Minute",
            profile["fluency"][
                "words_per_minute"
            ]
        )

        st.metric(
            "Speaking Ratio %",
            profile["fluency"][
                "speaking_ratio"
            ]
        )

        st.metric(
            "Word Count",
            profile["fluency"][
                "word_count"
            ]
        )

    with col3:

        st.subheader(
            "Language"
        )

        st.metric(
            "Lexical Diversity",
            profile["language"][
                "lexical_diversity"
            ]
        )

        st.metric(
            "Unique Words",
            profile["language"][
                "unique_words"
            ]
        )

        st.metric(
            "Topic Consistency",
            profile["semantic"][
                "topic_consistency_score"
            ]
        )

    # =========================
    # Interpretation
    # =========================

    st.header(
        "Interpretation"
    )

    silence = profile[
        "temporal"
    ][
        "silence_percentage"
    ]

    if silence < 10:

        st.success(
            "Low silence percentage observed."
        )

    elif silence < 25:

        st.warning(
            "Moderate silence percentage observed."
        )

    else:

        st.error(
            "Elevated silence percentage observed."
        )

    for observation in observations:

        st.write(
            f"• {observation}"
        )


    st.text(report_text)

    st.download_button(
        label="⬇️ Download Report",
        data=report_text,
        file_name="cognitive_report.txt",
        mime="text/plain"
    )

    # =========================
    # Raw Metrics
    # =========================

    with st.expander(
        "View Full Profile"
    ):

        st.json(profile)

    os.remove(
        audio_path
    )
    