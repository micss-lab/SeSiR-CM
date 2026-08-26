# Semantic-Aware Retrieval of Conceptual Models
## Experimental Replication Package

This repository contains the code, precomputed embeddings, experimental results, and figures used in the paper:

**Semantics-Aware Retrieval of Conceptual Models: Principles and Methodology**

The main purpose of this repository is to help reviewers and researchers inspect the experiments and reproduce the reported results with minimum effort.

---

## 1. What is included

The repository contains experiments for:

- Exhaustive vector search using FAISS Flat
- Classification-guided retrieval
- FAISS IVF
- FAISS IVFPQ
- FAISS HNSW
- Static filtered vector search
- Reciprocal Rank Fusion (RRF)
- Performance-Weighted Reciprocal Rank Fusion (WRRF)
- Query-time measurement
- Effectiveness-efficiency analysis

Four semantic embedding representations are provided and used across the experiments:

- SBERT
- Fine-tuned BERT
- Gemini Embedding
- Qwen3-Embedding-8B

The main retrieval metrics are:

- Precision@K
- Recall@K
- NDCG@K
- MRR

The main cutoff values are:

`K = {1, 5, 10, 20}`

The experiments use a leave-one-out evaluation protocol: each model is used once as a query and is excluded from its own candidate set. Models with the same class label as the query are treated as relevant.

---

## 2. Software requirements

The experiments were run with:

- **Python 3.12.7**

Install the required Python packages from the repository root:

```bash
pip install -r requirements.txt
```

Some embedding files are large and are stored with Git LFS. After cloning the repository, run:

```bash
git lfs install
git lfs pull
```

If a notebook contains a local path from the original experiment environment, change only that path so that it points to the corresponding folder on your machine. Do not change the experiment parameters when reproducing the paper results.

---

## 3. Embedding files

All retrieval experiments use the precomputed embeddings in:

`Embeddings/`

Files:

```text
Embeddings/
─ Gemini_Embedding.xlsx
─ Qwen3_Embedding_8B.xlsx
─ SBERT_Embedding_2_classification.xlsx
─ bert_finetuned_embeddings.xlsx
```

These files are the main inputs to the retrieval notebooks.

Using the provided embeddings is the easiest way to reproduce the retrieval experiments because it avoids the computational cost of generating the embeddings again.

---

# 4. Recommended execution order

For complete reproduction, run the experiments in the following order:

1. Check the embedding files
2. Run FAISS Flat
3. Run Classification-Guided Retrieval
4. Run FAISS IVF
5. Run FAISS IVFPQ
6. Run FAISS HNSW
7. Run Static Filtered Vector Search
8. Run Hybrid RRF (`NoFlat`)
9. Run Hybrid Weighted RRF (`NoFlat`)
10. Run Query-Time evaluation
11. Reproduce the effectiveness-efficiency analysis
12. Regenerate the figures from the saved result files

The hybrid experiments should be run only after the individual retrieval experiments because they combine the ranked outputs of the individual methods.

---

# 5. Experiment 1 - Exhaustive Vector Search (FAISS Flat)

FAISS Flat compares the query with the complete embedding collection and is used as the comparative baseline in the paper.

### Run the experiment

Execute:

```text
IndexFlat2/IndexFlat2-SimSearch.ipynb
```

Run all notebook cells from top to bottom.

### Main result file

The experiment produces:

```text
IndexFlat2/faiss_flatl2_results.xlsx
```

A copy used in the final cross-method analysis is also available at:

```text
All-Results-Excel/faiss_flatl2_results.xlsx
```

### Generate the figures

Execute:

```text
IndexFlat2/IndexFlat2-Charts.ipynb
```

The main generated figures are:

```text
IndexFlat2/FAISS_Flat_Index_NDCG_Recall_Cosine.png
IndexFlat2/FAISS_Flat_Search_Performance_Charts.png
IndexFlat2/FAISS_Flat_Search_Performance_HQ.png
```

For the NDCG@K and Recall@K results reported in the paper, use:

```text
FAISS_Flat_Index_NDCG_Recall_Cosine.png
```

The Excel result file contains the values used to obtain the Precision@K, Recall@K, NDCG@K, and MRR results.

---

# 6. Experiment 2 - Classification-Guided Retrieval

Classification-guided retrieval first uses class predictions to reduce the candidate space and then performs semantic similarity retrieval within the selected candidates.

### Run the experiment

Execute:

```text
Classification-based/Codes/Classification-based-Search.ipynb
```

Run all cells in order.

### Main result file

The generated result file is:

```text
Classification-based/Codes/soft_filtering_results.xlsx
```

### Generate the figures

Execute:

```text
Classification-based/Codes/Charts-generator.ipynb
```

The main figures are:

```text
Classification-based/Codes/Classifier_guided_Retrieval_NDCG_Recall_cosine.png
Classification-based/Codes/Classifier_guided_Retrieval_NDCG_cosine.png
Classification-based/Codes/Classifier_guided_Retrieval_Recall_cosine.png
Classification-based/Codes/Soft_Filtering_Search_Performance_HQ.png
```

An additional all-metrics figure is stored at:

```text
Classification-based/Charts/soft-filtering-all-metrics.png
```

For the main NDCG@K and Recall@K figure reported in the paper, use:

```text
Classifier_guided_Retrieval_NDCG_Recall_cosine.png
```

---

# 7. Experiment 3 - FAISS IVF

IVF reduces the search space by organizing the embeddings into partitions and searching selected partitions instead of processing the complete repository.

### Run the experiment

Execute:

```text
IVF/IVF-SimSearch.ipynb
```

Run all cells in order.

### Main result file

The notebook produces:

```text
IVF/faiss_ivf_results.xlsx
```

### Generate the figures

Execute:

```text
IVF/IVF-Charts.ipynb
```

The generated figures are:

```text
IVF/FAISS_IVF_NDCG_Recall_Cosine.png
IVF/FAISS_IVF_Performance.png
IVF/FAISS_IVF_Performance_HQ.png
```

For the main NDCG@K and Recall@K results in the paper, use:

```text
FAISS_IVF_NDCG_Recall_Cosine.png
```

---

# 8. Experiment 4 - FAISS IVFPQ

IVFPQ combines IVF indexing with product quantization. It is evaluated as a compressed approximate retrieval strategy.

### Run the experiment

Execute:

```text
Quantization/Quantization_SimSearch.ipynb
```

Run all cells from top to bottom.

### Main result file

The notebook produces:

```text
Quantization/faiss_ivfpq_results.xlsx
```

### Generate the figures

Execute:

```text
Quantization/Quantization_Charts.ipynb
```

The generated figures are:

```text
Quantization/FAISS_IVFPQ_Performance.png
Quantization/FAISS_IVFPQ_Performance_HQ.png
Quantization/FAISS_IVFQ_Quantization_NDGC_Accuracy_cosine.png
```

The cosine-based ranking figure used for the corresponding analysis is:

```text
FAISS_IVFQ_Quantization_NDGC_Accuracy_cosine.png
```

---

# 9. Experiment 5 - FAISS HNSW

HNSW performs graph-based vector retrieval and is evaluated as a low-latency retrieval strategy.

### Run the experiment

Execute:

```text
Graph-Based-HSNW/Graph_Based_HSNW.ipynb
```

Run all cells in order.

### Main result file

The notebook produces:

```text
Graph-Based-HSNW/faiss_hnsw_results.xlsx
```

### Generate the figures

Execute:

```text
Graph-Based-HSNW/Graph_Based_HSNW_Charts.ipynb
```

The generated figures include:

```text
Graph-Based-HSNW/FAISS_HNSW_NDGC_Accuracy_cosine.png
Graph-Based-HSNW/FAISS_HNSW_Performance_HQ.png
```

For the cosine-based NDCG/Recall analysis reported in the paper, use:

```text
FAISS_HNSW_NDGC_Accuracy_cosine.png
```

---

# 10. Experiment 6 - Static Filtered Vector Search

This experiment restricts retrieval to models with the same ground-truth class label as the query. It represents an ideal class-filtered reference condition and also includes the adaptive threshold analysis described in the paper.

### Run the experiment

Execute:

```text
Filtered-Vector-Search/Filtered_Vector_Search.ipynb
```

Run all cells in order.

### Main result file

The notebook produces:

```text
Filtered-Vector-Search/filtered_static_threshold_results.xlsx
```

### Generate the figures

Execute:

```text
Filtered-Vector-Search/Filtered_Vector_Charts.ipynb
```

The generated figures include:

```text
Filtered-Vector-Search/Filtered_Vector_Search_NDGC_Accuracy_cosine.png
Filtered-Vector-Search/Filtered_Static_Search_Label_Filter_Ranking_Metrics_HQ.png
Filtered-Vector-Search/Filtered_Static_Search_Threshold_Precision_at_K_cosine_HQ.png
```

The threshold figure is used to inspect the adaptive threshold-based evaluation, while the ranking figure reports the standard retrieval metrics.

---

# 11. Experiment 7 - Hybrid Retrieval with Reciprocal Rank Fusion (RRF)

RRF combines the ranked outputs of the individual retrieval methods. The final paper uses the **NoFlat** configuration: exhaustive FAISS Flat is kept only as a baseline and is not included in the fusion.

### Important

For the final paper results, run only:

```text
Hybrid1-Reciprocal Rank Fusion/Hybrid1_Reciprocal_Rank_Fusion_NoFlat.ipynb
```

Do not add FAISS Flat to the fusion.

### Run the experiment

Execute:

```text
Hybrid1-Reciprocal Rank Fusion/Hybrid1_Reciprocal_Rank_Fusion_NoFlat.ipynb
```

Run all cells in order.

The notebook combines the scalable retrieval components used in the paper and applies Reciprocal Rank Fusion.

### Main output files

The detailed run-level output is:

```text
Hybrid1-Reciprocal Rank Fusion/hybrid_rrf_no_flat_run.csv
```

The aggregated results are:

```text
Hybrid1-Reciprocal Rank Fusion/hybrid_rrf_no_flat_summary.xlsx
```

Use the summary file for the aggregated Precision@K, Recall@K, NDCG@K, and MRR results.

### Generate the figures

Execute:

```text
Hybrid1-Reciprocal Rank Fusion/Hybrid1_Reciprocal_Rank_Fusion_NoFlat_Charts.ipynb
```

The final figures are:

```text
Hybrid1-Reciprocal Rank Fusion/Hybrid1_RRF_NoFlat_NDCG_Recall_cosine.png
Hybrid1-Reciprocal Rank Fusion/Hybrid1_RRF_NoFlat_NDCG_Recall_cosine.pdf
```

These are the RRF figures corresponding to the final configuration used in the paper.

---

# 12. Experiment 8 - Performance-Weighted Reciprocal Rank Fusion (WRRF)

WRRF extends standard RRF by giving different contributions to the participating retrieval strategies according to their observed effectiveness.

As with standard RRF, the final paper uses the **NoFlat** configuration.

### Run the experiment

Execute:

```text
Hybrid2_Performance_Weighted_RRF/Hybrid2_Performance_Weighted_RRF_NoFlat.ipynb
```

Run all cells in order.

### Main output files

Detailed run-level results:

```text
Hybrid2_Performance_Weighted_RRF/hybrid_weighted_rrf_no_flat_run.csv
```

Aggregated results:

```text
Hybrid2_Performance_Weighted_RRF/hybrid_weighted_rrf_no_flat_summary.xlsx
```

The summary file contains the final aggregated ranking metrics used in the paper.

### Generate the figures

Execute:

```text
Hybrid2_Performance_Weighted_RRF/Hybrid2_Performance_Weighted_RRF_NoFlat_Charts.ipynb
```

The final figures are:

```text
Hybrid2_Performance_Weighted_RRF/Hybrid2_Weighted_RRF_NoFlat_Search_NDCG_Recall_cosine.png
Hybrid2_Performance_Weighted_RRF/Hybrid2_Weighted_RRF_NoFlat_Search_NDCG_Recall_cosine.pdf
```

Only the `NoFlat` outputs correspond to the final hybrid configuration reported in the paper.

---

# 13. Experiment 9 - Query-Time Evaluation

This experiment measures the average query latency of the individual vector indexing strategies.

### Run the experiment

Execute:

```text
Query-Time/Query_Time.ipynb
```

Run all cells in order.

### Result file

The latency measurements are saved in:

```text
Query-Time/index_latency_results.xlsx
```

The paper reports latency for the individual vector indexing strategies only.

Hybrid latency is not included in the direct comparison because the hybrid experiments combine previously generated ranked outputs and were not measured using the same end-to-end query-time protocol. Their times are therefore not directly comparable with the index query times.

---

# 14. Effectiveness-Efficiency Analysis

The final effectiveness-efficiency analysis combines retrieval quality with the measured query latency of the individual indexing strategies.

### Input data

The prepared data are available in:

```text
All-Results-Excel/effectiveness_efficiency_scatter_data.xlsx
```

The analysis compares:

- retrieval effectiveness; and
- average query latency.

### Final figure

The figure used for the Pareto analysis is:

```text
All-Results-Excel/Pareto-Frontiers.png
```

This plot shows the effectiveness-efficiency trade-off and identifies the Pareto frontier among the compared individual retrieval strategies.

The hybrid methods are not included in this latency-based Pareto comparison because comparable end-to-end latency measurements were not collected for them.

---

# 15. Which files reproduce which paper results?

The following table provides a direct mapping from each reported experimental result to the exact file that should be executed.

| Paper result | Run this experiment | Result file | Run this chart file | Main figure |
|---|---|---|---|---|
| Exhaustive / Flat | `IndexFlat2/IndexFlat2-SimSearch.ipynb` | `IndexFlat2/faiss_flatl2_results.xlsx` | `IndexFlat2/IndexFlat2-Charts.ipynb` | `FAISS_Flat_Index_NDCG_Recall_Cosine.png` |
| Classification-guided | `Classification-based/Codes/Classification-based-Search.ipynb` | `Classification-based/Codes/soft_filtering_results.xlsx` | `Classification-based/Codes/Charts-generator.ipynb` | `Classifier_guided_Retrieval_NDCG_Recall_cosine.png` |
| IVF | `IVF/IVF-SimSearch.ipynb` | `IVF/faiss_ivf_results.xlsx` | `IVF/IVF-Charts.ipynb` | `FAISS_IVF_NDCG_Recall_Cosine.png` |
| IVFPQ | `Quantization/Quantization_SimSearch.ipynb` | `Quantization/faiss_ivfpq_results.xlsx` | `Quantization/Quantization_Charts.ipynb` | `FAISS_IVFQ_Quantization_NDGC_Accuracy_cosine.png` |
| HNSW | `Graph-Based-HSNW/Graph_Based_HSNW.ipynb` | `Graph-Based-HSNW/faiss_hnsw_results.xlsx` | `Graph-Based-HSNW/Graph_Based_HSNW_Charts.ipynb` | `FAISS_HNSW_NDGC_Accuracy_cosine.png` |
| Static filtered search | `Filtered-Vector-Search/Filtered_Vector_Search.ipynb` | `Filtered-Vector-Search/filtered_static_threshold_results.xlsx` | `Filtered-Vector-Search/Filtered_Vector_Charts.ipynb` | `Filtered_Vector_Search_NDGC_Accuracy_cosine.png` |
| RRF (final NoFlat) | `Hybrid1-Reciprocal Rank Fusion/Hybrid1_Reciprocal_Rank_Fusion_NoFlat.ipynb` | `hybrid_rrf_no_flat_summary.xlsx` | `Hybrid1_Reciprocal_Rank_Fusion_NoFlat_Charts.ipynb` | `Hybrid1_RRF_NoFlat_NDCG_Recall_cosine.png` |
| WRRF (final NoFlat) | `Hybrid2_Performance_Weighted_RRF/Hybrid2_Performance_Weighted_RRF_NoFlat.ipynb` | `hybrid_weighted_rrf_no_flat_summary.xlsx` | `Hybrid2_Performance_Weighted_RRF_NoFlat_Charts.ipynb` | `Hybrid2_Weighted_RRF_NoFlat_Search_NDCG_Recall_cosine.png` |
| Query latency | `Query-Time/Query_Time.ipynb` | `Query-Time/index_latency_results.xlsx` | — | Used in latency table and Pareto analysis |
| Effectiveness-efficiency | Use the prepared result data | `All-Results-Excel/effectiveness_efficiency_scatter_data.xlsx` | — | `All-Results-Excel/Pareto-Frontiers.png` |

---

# 16. Reproducing the Precision@K and MRR tables

The Precision@K and MRR tables in the paper are obtained from the result files generated by each experiment.

Use the following files:

```text
IndexFlat2/faiss_flatl2_results.xlsx
Classification-based/Codes/soft_filtering_results.xlsx
IVF/faiss_ivf_results.xlsx
Quantization/faiss_ivfpq_results.xlsx
Graph-Based-HSNW/faiss_hnsw_results.xlsx
Filtered-Vector-Search/filtered_static_threshold_results.xlsx
Hybrid1-Reciprocal Rank Fusion/hybrid_rrf_no_flat_summary.xlsx
Hybrid2_Performance_Weighted_RRF/hybrid_weighted_rrf_no_flat_summary.xlsx
```

For the hybrid experiments, use the `*_summary.xlsx` files rather than the full `*_run.csv` files when reproducing the aggregated tables in the paper.

The `*_run.csv` files are provided for detailed per-query inspection.

---

# 17. Reproducing the NDCG@K and Recall@K figures

For each method:

1. Run the experiment notebook.
2. Confirm that the corresponding Excel/CSV result file is created.
3. Run the method-specific chart notebook.
4. Compare the generated cosine-based NDCG@K/Recall@K figure with the supplied figure.

The main figure-generating notebooks are:

```text
IndexFlat2/IndexFlat2-Charts.ipynb
Classification-based/Codes/Charts-generator.ipynb
IVF/IVF-Charts.ipynb
Quantization/Quantization_Charts.ipynb
Graph-Based-HSNW/Graph_Based_HSNW_Charts.ipynb
Filtered-Vector-Search/Filtered_Vector_Charts.ipynb
Hybrid1-Reciprocal Rank Fusion/Hybrid1_Reciprocal_Rank_Fusion_NoFlat_Charts.ipynb
Hybrid2_Performance_Weighted_RRF/Hybrid2_Performance_Weighted_RRF_NoFlat_Charts.ipynb
```

---

# 18. Notes about the final hybrid experiments

The final version of the paper intentionally excludes exhaustive FAISS Flat from the two hybrid methods.

Therefore:

- FAISS Flat is used as the comparative baseline.
- RRF uses the final `NoFlat` configuration.
- WRRF uses the final `NoFlat` configuration.
- Only files containing `NoFlat` should be used to reproduce the hybrid results reported in the paper.

This distinction is important when comparing the repository outputs with the paper.

---

# 19. Quick reproduction path

If you want to reproduce only the final reported results without regenerating every visualization, use this shorter sequence:

```text
1. Verify the four files in Embeddings/
2. Run IndexFlat2/IndexFlat2-SimSearch.ipynb
3. Run Classification-based/Codes/Classification-based-Search.ipynb
4. Run IVF/IVF-SimSearch.ipynb
5. Run Quantization/Quantization_SimSearch.ipynb
6. Run Graph-Based-HSNW/Graph_Based_HSNW.ipynb
7. Run Filtered-Vector-Search/Filtered_Vector_Search.ipynb
8. Run Hybrid1-Reciprocal Rank Fusion/Hybrid1_Reciprocal_Rank_Fusion_NoFlat.ipynb
9. Run Hybrid2_Performance_Weighted_RRF/Hybrid2_Performance_Weighted_RRF_NoFlat.ipynb
10. Run Query-Time/Query_Time.ipynb
```

Then compare the generated result files with the result files already included in the repository.

---

# 20. Full figure reproduction path

After completing the experimental runs, execute:

```text
IndexFlat2/IndexFlat2-Charts.ipynb
Classification-based/Codes/Charts-generator.ipynb
IVF/IVF-Charts.ipynb
Quantization/Quantization_Charts.ipynb
Graph-Based-HSNW/Graph_Based_HSNW_Charts.ipynb
Filtered-Vector-Search/Filtered_Vector_Charts.ipynb
Hybrid1-Reciprocal Rank Fusion/Hybrid1_Reciprocal_Rank_Fusion_NoFlat_Charts.ipynb
Hybrid2_Performance_Weighted_RRF/Hybrid2_Performance_Weighted_RRF_NoFlat_Charts.ipynb
```

This regenerates the method-specific figures from the experimental result files.

---

# 21. Expected main outputs

After successful reproduction, the main result files should include:

```text
IndexFlat2/faiss_flatl2_results.xlsx

Classification-based/Codes/soft_filtering_results.xlsx

IVF/faiss_ivf_results.xlsx

Quantization/faiss_ivfpq_results.xlsx

Graph-Based-HSNW/faiss_hnsw_results.xlsx

Filtered-Vector-Search/filtered_static_threshold_results.xlsx

Hybrid1-Reciprocal Rank Fusion/hybrid_rrf_no_flat_run.csv
Hybrid1-Reciprocal Rank Fusion/hybrid_rrf_no_flat_summary.xlsx

Hybrid2_Performance_Weighted_RRF/hybrid_weighted_rrf_no_flat_run.csv
Hybrid2_Performance_Weighted_RRF/hybrid_weighted_rrf_no_flat_summary.xlsx

Query-Time/index_latency_results.xlsx
```

These files provide the main numerical evidence reported in the experimental validation section of the paper.

---

# 22. Troubleshooting

### Embedding file cannot be opened

Make sure Git LFS has downloaded the actual file:

```bash
git lfs pull
```

### Python package is missing

Install the project dependencies again:

```bash
pip install -r requirements.txt
```

### Notebook uses an old local path

Update only the path variable so that it points to the corresponding repository folder on your machine.

### Hybrid experiment cannot find an input

Run all individual retrieval experiments first. The hybrid experiments depend on the ranked outputs generated by the individual methods.

### Results differ after changing parameters

For direct reproduction of the paper, use the parameter values already defined in the notebooks. Parameter changes create a different experimental configuration and may therefore produce different results.

---

# 23. Reproducibility scope

The repository supports two forms of verification.

### Direct inspection

Reviewers can inspect the included Excel and CSV files without rerunning the experiments.

### Full reproduction

Reviewers can execute the notebooks in the order described above and regenerate the numerical results and figures.

Because the semantic embeddings are already provided, the retrieval experiments can be reproduced without regenerating the embedding models themselves.

---

# 24. Citation

If you use the methodology, code, or experimental results, please cite the associated paper:

**Semantics-Aware Retrieval of Conceptual Models: Principles and Methodology**

Bibliographic information will be added after publication.
