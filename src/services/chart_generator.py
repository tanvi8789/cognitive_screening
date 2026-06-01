import plotly.graph_objects as go


def create_radar_chart(profile):

    silence = profile["temporal"][
        "silence_percentage"
    ]

    pause_count = profile["temporal"][
        "pause_count"
    ]

    speaking_ratio = profile[
        "fluency"
    ][
        "speaking_ratio"
    ]

    lexical_diversity = profile[
        "language"
    ][
        "lexical_diversity"
    ]

    topic_consistency = profile[
        "semantic"
    ][
        "topic_consistency_score"
    ]

    # ---------------------
    # Normalize
    # ---------------------

    pause_control = max(
        0,
        100 - pause_count * 5
    )

    silence_control = max(
        0,
        100 - silence
    )

    vocabulary = (
        lexical_diversity * 100
    )

    categories = [

        "Pause Control",

        "Silence Control",

        "Speaking Ratio",

        "Vocabulary",

        "Topic Consistency"
    ]

    values = [

        pause_control,

        silence_control,

        speaking_ratio,

        vocabulary,

        topic_consistency
    ]

    categories.append(
        categories[0]
    )

    values.append(
        values[0]
    )

    fig = go.Figure()

    fig.add_trace(

        go.Scatterpolar(

            r=values,

            theta=categories,

            fill="toself",

            name="Profile"
        )
    )

    fig.update_layout(

        polar=dict(

            radialaxis=dict(

                visible=True,

                range=[0, 100]
            )
        ),

        showlegend=False,

        height=500
    )

    return fig