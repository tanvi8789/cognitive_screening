<div align="center">

# AI Cognitive Wellness Screening

**Analysing spontaneous speech to surface early signals of cognitive change.**

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white)
![Whisper](https://img.shields.io/badge/ASR-Whisper-412991?style=flat-square&logo=openai&logoColor=white)
![scikit-learn](https://img.shields.io/badge/ML-scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)

</div>

---

## Overview

This tool analyses a short speech recording and generates a **cognitive-communication profile**. From spontaneous speech it extracts temporal, fluency, lexical and semantic features — communication patterns that research has linked to cognitive health — and presents them through an interactive dashboard with a downloadable report.

The goal is to demonstrate how accessible, speech-based screening could complement traditional cognitive assessment, which is often clinical, time-consuming and inaccessible.

> **Disclaimer.** This is a research and educational project. It does **not** diagnose any medical condition and is **not** a substitute for professional clinical assessment. Results are indicative signals only.

---

## Results

The dashboard summarises each recording across the four analysis dimensions and produces an exportable profile.

<div align="center">

![Dashboard overview](assets/dashboard.png)
*Interactive screening dashboard*

![Generated profile](assets/results.png)
*Cognitive-communication profile with per-dimension scores*

</div>

> Replace `dashboard.png` / `results.png` with the actual filenames of the screenshots in your `assets/` folder.

---

## How It Works

```
 Speech recording
        │
        ▼
 Transcription  ──────────────  Whisper (speech → text)
        │
        ▼
 Four parallel analyses
   ├─ Temporal    →  speech rate, pauses, silence ratio
   ├─ Fluency     →  hesitations, filler/disruption patterns
   ├─ Lexical     →  vocabulary richness, lexical diversity
   └─ Semantic    →  topic consistency (sentence embeddings)
        │
        ▼
 Cognitive-communication profile  →  dashboard + downloadable report
```

| Dimension | What it measures | Key library |
|---|---|---|
| **Temporal** | Speech rate, pause frequency and length, silence ratio | Librosa |
| **Fluency** | Disruptions and hesitation patterns in delivery | Librosa / custom |
| **Lexical** | Lexical diversity and vocabulary richness | scikit-learn |
| **Semantic** | Topic consistency and coherence across the response | Sentence-Transformers |

---

## Tech Stack

- **Language:** Python
- **Speech-to-text:** Whisper
- **Audio features:** Librosa
- **Semantic analysis:** Sentence-Transformers
- **Modelling:** scikit-learn
- **Dashboard & visualisation:** Streamlit, Plotly

---

## Project Structure

```
cognitive_screening/
├── assets/            # Screenshots and static assets
├── datasets/          # Input data (not committed if restricted)
├── models/            # Saved models / artifacts
├── src/
│   └── app.py         # Streamlit entry point
├── requirements.txt
└── README.md
```

---

## Getting Started

```bash
# 1. Clone
git clone https://github.com/tanvi8789/cognitive_screening.git
cd cognitive_screening

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the dashboard
streamlit run src/app.py
```

Upload a speech recording through the interface to generate a profile.

---

## Limitations

- Validated on a limited dataset; not tested across diverse accents, languages or recording conditions.
- Feature thresholds are indicative and have not been clinically calibrated.
- Output is a screening signal, not a diagnosis.

---

## Future Work

- SHAP-based explainability for per-feature contribution.
- Longitudinal tracking to detect change over time rather than a single snapshot.
- Integration of established clinical voice biomarkers.
