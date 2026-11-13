import sys
import numpy as np
import pandas as pd

print("Python:", sys.version.split()[0])
print("NumPy:", np.__version__)
print("pandas:", pd.__version__)

scores = np.array([78, 85, 92, 66, 88, 95, 73, 81])
print(f"mean={scores.mean():.1f}, std={scores.std():.1f}, max={scores.max()}")

df = pd.DataFrame({"score": scores})
df["level"] = pd.cut(df["score"], bins=[0, 60, 80, 100],
                     labels=["不及格", "及格", "优秀"])
summary = df["level"].value_counts().to_string()

report = f"""环境自检报告
Python: {sys.version.split()[0]}
NumPy: {np.__version__}
pandas: {pd.__version__}
平均分: {scores.mean():.1f}
分布:
{summary}
"""
with open("day01/report.txt", "w", encoding="utf-8") as f:
    f.write(report)

print(report)
