# AI Cognitive Wellness Screening System

## Overview

An AI-powered speech analysis platform that evaluates communication patterns through:

- Temporal analysis
- Fluency analysis
- Language analysis
- Semantic analysis

The system generates a cognitive communication profile from an uploaded speech recording.

## Features

- Speech-to-text transcription using Whisper
- Pause and silence detection
- Speech rate analysis
- Lexical diversity analysis
- Topic consistency analysis using Sentence Transformers
- Interactive Streamlit dashboard
- Downloadable reports

## Tech Stack

- Python
- Whisper
- Librosa
- Sentence Transformers
- Streamlit
- Plotly
- Scikit-Learn

## Project Structure

(brief folder tree)

## Running Locally

pip install -r requirements.txt
streamlit run src/app.py

## Future Work

- Clinical voice biomarker integration
- SHAP-based explainability
- Longitudinal tracking