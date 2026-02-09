## 4) Dataset

```bash
# Place your CSV files into:
# dataset/raw/
#
# Example files used:
# dataset/raw/Year 2009-2010.csv
# dataset/raw/Year 2010-2011.csv
#
# (Optional) create a smaller sample:
head -n 1 "dataset/raw/Year 2009-2010.csv" > dataset/sample/online_retail_sample.csv
tail -n 10000 "dataset/raw/Year 2009-2010.csv" >> dataset/sample/online_retail_sample.csv
