# ExoBengal

Standardized tools for ML-based exoplanet candidate classification on NASA data, plus a companion docs website.

This repo contains:

- Python package `exobengal`:
  - `DetectExoplanet` for training/inference (RandomForest, CNN, kNN)
  - `ExoParams` convenience container for feature inputs
- Pretrained model artifacts in `models/`
- Example dataset(s) in `data/`
- Next.js docs site in `website/`

Full documentation is in `docs/`:

- Installation and requirements: `docs/installation.md`
- API reference: `docs/api.md`
- Data reference and preprocessing: `docs/data.md`
- Models and artifacts: `docs/models.md`
- Notebook walkthrough: `docs/notebook.md`

## Quick Start

Install the package from PyPI (or your local environment):

```bash
pip install exobengal
```

Make a prediction with the bundled RandomForest model:

```python
from exobengal.exobengal import DetectExoplanet

detector = DetectExoplanet()
sample = [365.0, 1.0, 288.0, 1.0, 4.44, 5778, 0.1, 5.0, 100.0]
print(detector.random_forest(sample))
```

## Project Structure

```
exobengal/           # Python package
  exobengal.py      # DetectExoplanet class and helpers
models/              # Trained models (.pkl, .h5, scaler)
data/                # Dataset CSVs
website/             # Next.js static website + docs
```

## Python API (quick view)

Constructor:

```python
DetectExoplanet(
  rf_model_path="models/random_forest_classifier.pkl",
  cnn_model_path="models/cnn_model.h5",
  knn_model_path="models/knn_model.pkl",
  scaler_path="models/scaler.pkl",
  imputer_path="models/imputer.pkl",
)
```

Training:

```python
detector.train_random_forest(data_path="data/cumulative_2025.09.20_12.15.37.csv")
detector.train_cnn(data_path="data/cumulative_2025.09.20_12.15.37.csv")
detector.train_knn(data_path="data/cumulative_2025.09.20_12.15.37.csv")
```

Inference (all return the same schema):

```python
from exobengal.exobengal import ExoParams

sample = [koi_period, koi_prad, koi_teq, koi_srad, koi_slogg, koi_steff, koi_impact, koi_duration, koi_depth]
detector.random_forest(sample)
detector.cnn(sample)
detector.knn(sample)

# Or use ExoParams for clarity
params = ExoParams(period=365.0, prad=1.0, teq=288.0, srad=1.0, slog_g=4.44, steff=5778, impact=0.1, duration=5.0, depth=100.0)
detector.random_forest(params)
```

Utility:

```python
detector.calculate_esi(koi_prad=1.05, koi_teq=290)
```

For full API and feature details, see `docs/api.md`.

## Models

Artifacts live in `models/`. See `docs/models.md` for details and retraining notes.

## Requirements

Python 3.8+. See `docs/installation.md` or `requirements.txt`.

## Website

The Next.js site (in `website/`) includes a docs experience. See its `README.md` for running locally.

## Development

Website (Node 20):

```bash
cd website
npm ci
npm run dev
```

Static export is enabled via `output: 'export'` and deployed to GitHub Pages with Actions.

## License

MIT License – see `LICENSE`.