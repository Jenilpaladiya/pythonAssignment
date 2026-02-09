# Data Engineering Portfolio (DLMDSEDE02) — Batch Processing Pipeline

A reproducible **batch-processing** data architecture using **Docker Compose + PostgreSQL + Python microservices**:

- **postgres** service: data storage (warehouse)
- **ingestion** service: loads raw CSV files into `retail_raw` (chunked)
- **processing** service: creates analytics tables:
  - `daily_metrics`
  - `top_products_daily`
  - `customer_features_quarterly`
- **serving** service: FastAPI service that exposes results via:
  - **Dashboard:** `/dashboard`
  - **API docs:** `/docs`
  - **Metrics endpoints:** `/metrics/*`

---

## FULL GUIDE (1 → END) — Single Terminal Block

```text
1) Architecture (high-level)
------------------------------------------------------------
NOTE: Mermaid diagrams do NOT render inside a single code block.
If you want the diagram to render, keep it in a separate ```mermaid``` block.

Flow:
CSV dataset (raw) 
  -> (Docker volume mount) Ingestion service (Python)
  -> INSERT into PostgreSQL table: retail_raw
  -> Processing service (Python SQL)
     -> daily_metrics
     -> top_products_daily
     -> customer_features_quarterly
  -> Serving service (FastAPI)
     -> /dashboard (HTML)
     -> /metrics/* (JSON API)

2) Prerequisites
------------------------------------------------------------
- Docker Desktop (Docker + Docker Compose v2)
- Git (optional, for pushing to GitHub)

Check:
docker --version
docker compose version

3) Project Structure (important paths)
------------------------------------------------------------
project/
├─ docker-compose.yml
├─ .env                 # (DO NOT COMMIT)
├─ .env.example         # commit this
├─ db/
│  └─ init.sql
├─ dataset/
│  ├─ raw/              # raw CSV(s)
│  ├─ sample/           # small sample CSV
│  └─ processed/        # optional outputs
└─ services/
   ├─ ingestion/
   │  ├─ Dockerfile
   │  ├─ ingest.py
   │  └─ requirements.txt
   ├─ processing/
   │  ├─ Dockerfile
   │  ├─ process.py
   │  └─ requirements.txt
   └─ serving/
      ├─ Dockerfile
      ├─ main.py
      └─ requirements.txt

4) Dataset
------------------------------------------------------------
Place your CSV files into:
dataset/raw/

Example files used:
dataset/raw/Year 2009-2010.csv
dataset/raw/Year 2010-2011.csv

(Optional) create a smaller sample:
head -n 1 "dataset/raw/Year 2009-2010.csv" > dataset/sample/online_retail_sample.csv
tail -n 10000 "dataset/raw/Year 2009-2010.csv" >> dataset/sample/online_retail_sample.csv

WARNING:
Do not commit large raw datasets to GitHub. Add them to .gitignore (see Step 11).

5) Environment Variables
------------------------------------------------------------
Create .env in the project root (same folder as docker-compose.yml).

Example (.env):
POSTGRES_DB=warehouse
POSTGRES_USER=de_user
POSTGRES_PASSWORD=de_password

Also keep an .env.example (same keys, safe values) for GitHub.

6) Run the Pipeline (Start -> End)
------------------------------------------------------------
Step 6.1 — Recreate database (runs db/init.sql)
WARNING: This deletes DB volume and recreates from scratch:
docker compose down -v
docker compose up -d postgres

Step 6.2 — Run ingestion (loads >1M rows into retail_raw)
docker compose run --rm ingestion

Step 6.3 — Run processing (creates analytics + features tables)
docker compose run --rm processing

Step 6.4 — Start serving (dashboard + API)
docker compose up -d serving

7) Serving (Dashboard + API)
------------------------------------------------------------
After processing completes, open:

Dashboard (HTML):
http://localhost:8000/dashboard

API docs (Swagger):
http://localhost:8000/docs

Daily metrics (JSON):
http://localhost:8000/metrics/daily?limit=5

Top products by day (JSON):
http://localhost:8000/metrics/top-products?day=YYYY-MM-DD&limit=10

Screenshots (placeholders)
- Dashboard: docs/screenshots/dashboard.png
- API JSON Output: docs/screenshots/api-json.png
- Swagger Docs: docs/screenshots/swagger.png

8) Verify Outputs (SQL checks)
------------------------------------------------------------
Step 8.1 — Check raw row count
docker exec -it de_postgres psql -U de_user -d warehouse -c "SELECT COUNT(*) FROM retail_raw;"

Expected (example from my run):
retail_raw ≈ 1,067,371 rows

Step 8.2 — Check processed tables
docker exec -it de_postgres psql -U de_user -d warehouse -c "SELECT COUNT(*) FROM daily_metrics;"
docker exec -it de_postgres psql -U de_user -d warehouse -c "SELECT COUNT(*) FROM top_products_daily;"
docker exec -it de_postgres psql -U de_user -d warehouse -c "SELECT COUNT(*) FROM customer_features_quarterly;"

Expected (example from my run):
daily_metrics = 604
top_products_daily = 6040
customer_features_quarterly = 5942

9) View Logs / Debug
------------------------------------------------------------
docker compose ps
docker compose logs -f postgres
docker compose logs -f ingestion
docker compose logs -f processing
docker compose logs -f serving

Open Postgres shell:
docker exec -it de_postgres psql -U de_user -d warehouse

10) Stop / Cleanup
------------------------------------------------------------
Stop containers:
docker compose down

Stop + delete DB volume (FULL reset):
docker compose down -v

11) Push to GitHub (clean + safe)
------------------------------------------------------------
Step 11.1 — Create .gitignore (project root)

# secrets
.env

# datasets (avoid pushing large files)
dataset/raw/
dataset/processed/

# python
__pycache__/
*.pyc
.venv/
.envrc

# OS
.DS_Store

Step 11.2 — Create .env.example
POSTGRES_DB=warehouse
POSTGRES_USER=de_user
POSTGRES_PASSWORD=de_password

Step 11.3 — Git commands
git add .
git commit -m "Phase 3: add serving dashboard and update documentation"
git push

DONE:
After pushing, paste your GitHub repo link into the Phase 2 TXT file and reuse the same link for Phase 3.
