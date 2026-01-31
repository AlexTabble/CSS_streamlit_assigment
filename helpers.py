import pandas as pd
from great_tables import GT, loc, md, style


def show_projects() -> GT:

    df = pd.DataFrame(
        {
            "Apps": [
                "Audio Feature Pipeline",
                "Question Automation",
                "[Chess](https://github.com/AlexTabble/Chess-WinForms.git)",
            ],
            "UFS Assignment": [
                "[Bayesian Network](https://colab.research.google.com/drive/1d7cL77f7zctKEgOFv-8Hx_jsxAvyr9mb?usp=drive_link)",
                "[Churn Prediction](https://colab.research.google.com/drive/1eYw-rapI4ZHVqyLkTeGYbxviA5K7vPqx?usp=drive_link)",
                "[Anomaly Detection](https://alextabble.github.io/EDAB2724_AnomalyDetection/)",
            ],
            "Scripts": [
                "[MNIST Classification](https://alextabble.github.io/Classic-MNIST)",
                "[Spam Detection](https://github.com/AlexTabble/Spam-Detection.git)",
                "",
            ],
            "Misc": [
                "[Neovim Config](https://github.com/AlexTabble/neovim-config.git)",
                "Tmux Config",
                "QYF Assignments",
            ],
        },
        index=[1, 2, 3],  # noqa
    )

    return (
        GT(df)
        .tab_header(title="Stuff I've done", subtitle="Red Projects are not public, Green blocks are websites")
        .tab_style(
            style=style.text(color="red"),
            locations=loc.body(
                columns="Apps",
                rows=[0, 1],
            ),
        )
        .tab_style(
            style=style.text(color="red"),
            locations=loc.body(columns="Misc", rows=[1, 2]),
        )
        .tab_style(
            style=style.fill(color="#98FB98"),
            locations=loc.body(columns="UFS Assignment", rows=[2]),
        )
        .tab_style(
            style=style.fill(color="#98FB98"),
            locations=loc.body(columns="Scripts", rows=[0]),
        )
        .fmt_markdown(columns="Apps", rows=[2])
        .fmt_markdown(columns="UFS Assignment", rows=[0, 1, 2])
        .fmt_markdown(columns="Scripts", rows=[0, 1])
        .fmt_markdown(columns="Misc", rows=[0])
        .tab_source_note(
            source_note=md(
                "Made with `great_tables`. Check it out [here](https://posit-dev.github.io/great-tables/articles/intro.html)"
            )
        )
    )


def get_data_dict() -> GT:

    df = pd.DataFrame(
        {
            "Field": [
                "acousticness",
                "danceability",
                "energy",
                "instrumentalness",
                "liveness",
                "loudness",
                "speechiness",
                "tempo",
                "valence",
            ],
            "Description": [
                "Confidence (0.0 to 1.0) that the track is acoustic.",
                "Suitability for dancing (0.0 to 1.0).",
                "Intensity and liveliness (0.0 to 1.0).",
                "Likelihood of no vocals (0.0 to 1.0).",
                "Probability of a live audience (0.0 to 1.0).",
                "Average loudness in decibels (dB), typically -60 to 0.",
                "Presence of spoken words (0.0 to 1.0).",
                "Estimated tempo in beats per minute (BPM).",
                "Emotional tone (0.0 to 1.0).",
            ],
        }
    )

    return (
        GT(df)
        .tab_source_note(
            source_note=md(
                "**Source** : My own history appended with the *Reccobeats API*"
            )
        )
        .tab_source_note(
            source_note=md(
                "**Reference**: (Music Recommendation and Database API Service | ReccoBeats, 2025) "
            )
        )
        .tab_header(title="Data Dictionary")
    )
