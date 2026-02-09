
### Option B: **Everything in ONE single block (whole part)**
If you literally want Step 2 + Step 3 + Step 4 all inside **one** box:

```markdown
## 2) Prerequisites + 3) Project Structure + 4) Dataset (single block)

```text
PREREQUISITES
- Docker Desktop (Docker + Docker Compose v2)
- Git (optional, for pushing to GitHub)

Check:
docker --version
docker compose version

PROJECT STRUCTURE
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
   └─ processing/
      ├─ Dockerfile
      ├─ process.py
      └─ requirements.txt

DATASET
Place your CSV files into:
dataset/raw/

Example files used:
dataset/raw/Year 2009-2010.csv
dataset/raw/Year 2010-2011.csv

(Optional) create a smaller sample:
head -n 1 "dataset/raw/Year 2009-2010.csv" > dataset/sample/online_retail_sample.csv
tail -n 10000 "dataset/raw/Year 2009-2010.csv" >> dataset/sample/online_retail_sample.csv
