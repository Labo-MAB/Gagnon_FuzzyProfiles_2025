![Python](https://img.shields.io/badge/Python-3.11-green6)
[![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](https://jupyter.org/try)

## **Embracing the fuzziness of cognition and behavior and its relationship with environmental factors: A multi-cohort study.**

Authors: Anthony Gagnon<sup>1</sup>, Virginie Gillet<sup>1</sup>, Anne-Sandrine Desautels<sup>1</sup>, Jean-François Lepage<sup>1</sup>, Andrea Baccarelli<sup>2</sup>, Jonathan Posner<sup>3</sup>, Maxime Descoteaux<sup>4</sup>, Marie Brunet<sup>1</sup>, Larissa Takser<sup>1</sup>.

Affiliations:\
<sup>1</sup> Department of Pediatrics, University of Sherbrooke, Québec, Canada\
<sup>2</sup> Department of Environmental Health, Harvard T. H. Chan School of Public Health, Boston, MA, USA\
<sup>3</sup> Department of Psychiatry and Behavioral Sciences, Duke University, Durham, NC, USA\
<sup>4</sup> Sherbrooke Connectivity Imaging Lab (SCIL), University of Sherbrooke, Quebec, Canada

The present repository contains all relevant code and scripts to reproduce the results found in Gagnon et al. 2024. 

### **To use the fuzzy profiles in your own population**

In the `models/` folder, you can find the PCA model used for dimensionality reduction of the ABCD cohort. In addition, you will also find the **centroids** needed for the projection of your data in the profiles' space. To use it in your research, simply follow the steps regarding the GESTE and BANDA cohorts in the jupyter notebooks located in the `notebooks/` folder. Briefly, you should follow the residualization, reduction (EFA/CFA), harmonization, and imputation (if needed) steps found in `notebooks/2-DataPreprocessing.ipynb`, then you can proceed with the projection by following the steps in `notebooks/3-FCMeansClustering.ipynb`. **Please raise an issue if you have any questions.**

#### **Setting up**

If you do not have the required packages installed, it is recommended that you setup a new python virtual environment in which we will install the required dependencies. 

**Installing `virtualenv`**

Please run the following in your terminal window:
```bash
pipx install virtualenv
```

**Setting up a new `virtualenv` with python 3.11**

```bash
virtualenv --python 3.11 /path/to/your/destination/folder/

# Activate your newly created environment

source /path/to/your/destination/folder/bin/activate
```

**Installing `NeuroStatX`**

> [!IMPORTANT]
> Run the following commands from within your virtual environment.

```bash
pip install neurostatx==0.1.0

# Test the installation by calling the help of a CLI script.

AddNodesAttributes -h
```

**Installing `GraphViz`**

For visualization of semplots from the `semopy` python package, `GraphViz` is required. If you do not have it installed, please run the following if you are on Linux `sudo apt get graphviz` or `brew install graphviz` if you are on MacOS.

#### **Output file structure.**

By design, the notebooks are made to be run in a particular order (denoted by the numbering in the file name). If you run all of them, you should obtain this specific output file structure:

```bash
<output_directory>
├── awp
│   ├── AWP_ABCD
│   │   ├── null_distributions_AD.xlsx
│   │   ├── null_distributions_ADHD.xlsx
│   │   ├── null_distributions_CD.xlsx
│   │   ├── null_distributions_DD.xlsx
│   │   ├── null_distributions_OCD.xlsx
│   │   ├── null_distributions_ODD.xlsx
│   │   ├── null_distributions_PSYPATHO.xlsx
│   │   ├── parameters.txt
│   │   ├── statistics_AD.xlsx
│   │   ├── statistics_ADHD.xlsx
│   │   ├── statistics_CD.xlsx
│   │   ├── statistics_DD.xlsx
│   │   ├── statistics_OCD.xlsx
│   │   ├── statistics_ODD.xlsx
│   │   └── statistics_PSYPATHO.xlsx
│   ├── AWP_BANDA
│   │   ├── null_distributions_AD.xlsx
│   │   ├── null_distributions_ADHD.xlsx
│   │   ├── null_distributions_DD.xlsx
│   │   ├── null_distributions_OCD.xlsx
│   │   ├── null_distributions_ODD.xlsx
│   │   ├── null_distributions_PSYPATHO.xlsx
│   │   ├── parameters.txt
│   │   ├── statistics_AD.xlsx
│   │   ├── statistics_ADHD.xlsx
│   │   ├── statistics_DD.xlsx
│   │   ├── statistics_OCD.xlsx
│   │   ├── statistics_ODD.xlsx
│   │   └── statistics_PSYPATHO.xlsx
│   ├── AWP_GESTE
│   │   ├── null_distributions_ADHD.xlsx
│   │   ├── null_distributions_PSYPATHO.xlsx
│   │   ├── parameters.txt
│   │   ├── statistics_ADHD.xlsx
│   │   └── statistics_PSYPATHO.xlsx
│   └── AWP_GLOBAL
│       ├── null_distributions_AD.xlsx
│       ├── null_distributions_ADHD.xlsx
│       ├── null_distributions_CD.xlsx
│       ├── null_distributions_DD.xlsx
│       ├── null_distributions_OCD.xlsx
│       ├── null_distributions_ODD.xlsx
│       ├── null_distributions_PSYPATHO.xlsx
│       ├── parameters.txt
│       ├── statistics_AD.xlsx
│       ├── statistics_ADHD.xlsx
│       ├── statistics_CD.xlsx
│       ├── statistics_DD.xlsx
│       ├── statistics_OCD.xlsx
│       ├── statistics_ODD.xlsx
│       └── statistics_PSYPATHO.xlsx
├── datagathering
│   ├── abcd_data.xlsx
│   ├── abcd_dx_labels.xlsx
│   ├── banda_data.xlsx
│   ├── banda_dx_labels.xlsx
│   └── geste_data.xlsx
├── demographicstable
│   └── demo_table.xlsx
├── fuzzyclustering
│   ├── ABCDFuzzyCMeans
│   │   ├── CENTROIDS
│   │   │   ├── clusters_centroids_10.xlsx
│   │   │   ├── clusters_centroids_11.xlsx
│   │   │   ├── clusters_centroids_12.xlsx
│   │   │   ├── clusters_centroids_13.xlsx
│   │   │   ├── clusters_centroids_14.xlsx
│   │   │   ├── clusters_centroids_15.xlsx
│   │   │   ├── clusters_centroids_16.xlsx
│   │   │   ├── clusters_centroids_17.xlsx
│   │   │   ├── clusters_centroids_18.xlsx
│   │   │   ├── clusters_centroids_19.xlsx
│   │   │   ├── clusters_centroids_2.xlsx
│   │   │   ├── clusters_centroids_20.xlsx
│   │   │   ├── clusters_centroids_3.xlsx
│   │   │   ├── clusters_centroids_4.xlsx
│   │   │   ├── clusters_centroids_5.xlsx
│   │   │   ├── clusters_centroids_6.xlsx
│   │   │   ├── clusters_centroids_7.xlsx
│   │   │   ├── clusters_centroids_8.xlsx
│   │   │   └── clusters_centroids_9.xlsx
│   │   ├── MEMBERSHIP_DF
│   │   │   ├── clusters_membership_10.xlsx
│   │   │   ├── clusters_membership_11.xlsx
│   │   │   ├── clusters_membership_12.xlsx
│   │   │   ├── clusters_membership_13.xlsx
│   │   │   ├── clusters_membership_14.xlsx
│   │   │   ├── clusters_membership_15.xlsx
│   │   │   ├── clusters_membership_16.xlsx
│   │   │   ├── clusters_membership_17.xlsx
│   │   │   ├── clusters_membership_18.xlsx
│   │   │   ├── clusters_membership_19.xlsx
│   │   │   ├── clusters_membership_2.xlsx
│   │   │   ├── clusters_membership_20.xlsx
│   │   │   ├── clusters_membership_3.xlsx
│   │   │   ├── clusters_membership_4.xlsx
│   │   │   ├── clusters_membership_5.xlsx
│   │   │   ├── clusters_membership_6.xlsx
│   │   │   ├── clusters_membership_7.xlsx
│   │   │   ├── clusters_membership_8.xlsx
│   │   │   └── clusters_membership_9.xlsx
│   │   ├── MEMBERSHIP_MAT
│   │   │   ├── clusters_membership_10.npy
│   │   │   ├── clusters_membership_11.npy
│   │   │   ├── clusters_membership_12.npy
│   │   │   ├── clusters_membership_13.npy
│   │   │   ├── clusters_membership_14.npy
│   │   │   ├── clusters_membership_15.npy
│   │   │   ├── clusters_membership_16.npy
│   │   │   ├── clusters_membership_17.npy
│   │   │   ├── clusters_membership_18.npy
│   │   │   ├── clusters_membership_19.npy
│   │   │   ├── clusters_membership_2.npy
│   │   │   ├── clusters_membership_20.npy
│   │   │   ├── clusters_membership_3.npy
│   │   │   ├── clusters_membership_4.npy
│   │   │   ├── clusters_membership_5.npy
│   │   │   ├── clusters_membership_6.npy
│   │   │   ├── clusters_membership_7.npy
│   │   │   ├── clusters_membership_8.npy
│   │   │   └── clusters_membership_9.npy
│   │   ├── METRICS
│   │   │   ├── chi.png
│   │   │   ├── dbi.png
│   │   │   ├── dendrogram.png
│   │   │   ├── fpc.png
│   │   │   ├── gap.png
│   │   │   ├── ss.png
│   │   │   └── wss.png
│   │   ├── PARALLEL_PLOTS
│   │   ├── PCA
│   │   │   ├── barplot_loadings.png
│   │   │   ├── components.xlsx
│   │   │   ├── pca_model.pkl
│   │   │   ├── transformed_data.xlsx
│   │   │   └── variance_explained.xlsx
│   │   ├── RADAR_PLOTS
│   │   │   ├── radar_plot_10clusters.png
│   │   │   ├── radar_plot_11clusters.png
│   │   │   ├── radar_plot_12clusters.png
│   │   │   ├── radar_plot_13clusters.png
│   │   │   ├── radar_plot_14clusters.png
│   │   │   ├── radar_plot_15clusters.png
│   │   │   ├── radar_plot_16clusters.png
│   │   │   ├── radar_plot_17clusters.png
│   │   │   ├── radar_plot_18clusters.png
│   │   │   ├── radar_plot_19clusters.png
│   │   │   ├── radar_plot_20clusters.png
│   │   │   ├── radar_plot_2clusters.png
│   │   │   ├── radar_plot_3clusters.png
│   │   │   ├── radar_plot_4clusters.png
│   │   │   ├── radar_plot_5clusters.png
│   │   │   ├── radar_plot_6clusters.png
│   │   │   ├── radar_plot_7clusters.png
│   │   │   ├── radar_plot_8clusters.png
│   │   │   └── radar_plot_9clusters.png
│   │   ├── parameters.txt
│   │   ├── validation_indices.xlsx
│   │   └── viz_multiple_cluster_nb.png
│   ├── BANDAProjected
│   │   ├── BARPLOTS
│   │   ├── PARALLEL_PLOTS
│   │   ├── RADAR_PLOTS
│   │   │   └── radar_plot_7clusters.png
│   │   ├── parameters.txt
│   │   └── predicted_membership_matrix.xlsx
│   ├── GESTEProjected
│   │   ├── BARPLOTS
│   │   ├── PARALLEL_PLOTS
│   │   ├── RADAR_PLOTS
│   │   │   └── radar_plot_7clusters.png
│   │   ├── parameters.txt
│   │   └── predicted_membership_matrix.xlsx
│   ├── GraphNetwork
│   │   ├── graph_network_parameters.txt
│   │   ├── membership_distribution.png
│   │   └── network_graph_file.gml
│   ├── GraphNetwork.gml
│   ├── VizNetwork
│   │   ├── graph_network.png
│   │   └── nodes_attributes_parameters.txt
│   ├── VizNetworkDxABCD
│   │   ├── graph_network.png
│   │   ├── graph_network_AD.png
│   │   ├── graph_network_ADHD.png
│   │   ├── graph_network_CD.png
│   │   ├── graph_network_DD.png
│   │   ├── graph_network_OCD.png
│   │   ├── graph_network_ODD.png
│   │   ├── graph_network_PSYPATHO.png
│   │   └── nodes_attributes_parameters.txt
│   ├── VizNetworkDxBANDA
│   │   ├── graph_network.png
│   │   ├── graph_network_AD.png
│   │   ├── graph_network_ADHD.png
│   │   ├── graph_network_CD.png
│   │   ├── graph_network_DD.png
│   │   ├── graph_network_OCD.png
│   │   ├── graph_network_ODD.png
│   │   ├── graph_network_PSYPATHO.png
│   │   └── nodes_attributes_parameters.txt
│   ├── VizNetworkDxGESTE
│   │   ├── graph_network.png
│   │   ├── graph_network_ADHD.png
│   │   ├── graph_network_PSYPATHO.png
│   │   └── nodes_attributes_parameters.txt
│   ├── VizNetworkDxGlobal
│   │   ├── graph_network.png
│   │   ├── graph_network_AD.png
│   │   ├── graph_network_ADHD.png
│   │   ├── graph_network_CD.png
│   │   ├── graph_network_DD.png
│   │   ├── graph_network_OCD.png
│   │   ├── graph_network_ODD.png
│   │   ├── graph_network_PSYPATHO.png
│   │   └── nodes_attributes_parameters.txt
│   └── merged_fcm_data.xlsx
├── preprocessing
│   ├── ABCD_CFA
│   │   ├── CFA_report
│   │   │   ├── css
│   │   │   │   └── bootstrap.min.css
│   │   │   ├── js
│   │   │   │   └── bootstrap.min.js
│   │   │   ├── plots
│   │   │   │   ├── 1
│   │   │   │   ├── 1.png
│   │   │   │   ├── 2
│   │   │   │   ├── 2.png
│   │   │   │   ├── 3
│   │   │   │   ├── 3.png
│   │   │   │   ├── 4
│   │   │   │   └── 4.png
│   │   │   └── report.html
│   │   ├── cfa_model.pkl
│   │   ├── cfa_scores.xlsx
│   │   ├── cfa_stats.xlsx
│   │   ├── parameters.txt
│   │   ├── semplot
│   │   └── semplot.png
│   ├── ABCD_CFA_Apply
│   │   ├── parameters.txt
│   │   └── transformed_dataset.xlsx
│   ├── ABCD_EFA
│   │   ├── EFA_model.pkl
│   │   ├── EFA_scores.xlsx
│   │   ├── Heatmap.png
│   │   ├── barplot_loadings.png
│   │   ├── communalities.xlsx
│   │   ├── eigenvalues.xlsx
│   │   ├── horns_parallel_screeplot.png
│   │   ├── loadings.xlsx
│   │   ├── parameters.txt
│   │   ├── scree_plot.png
│   │   ├── test_dataset.xlsx
│   │   └── train_dataset.xlsx
│   ├── BANDA_CFA
│   │   ├── CFA_report
│   │   │   ├── css
│   │   │   │   └── bootstrap.min.css
│   │   │   ├── js
│   │   │   │   └── bootstrap.min.js
│   │   │   ├── plots
│   │   │   │   ├── 1
│   │   │   │   ├── 1.png
│   │   │   │   ├── 2
│   │   │   │   ├── 2.png
│   │   │   │   ├── 3
│   │   │   │   ├── 3.png
│   │   │   │   ├── 4
│   │   │   │   └── 4.png
│   │   │   └── report.html
│   │   ├── cfa_model.pkl
│   │   ├── cfa_scores.xlsx
│   │   ├── cfa_stats.xlsx
│   │   ├── parameters.txt
│   │   ├── semplot
│   │   └── semplot.png
│   ├── BANDA_CFA_Apply
│   │   ├── parameters.txt
│   │   └── transformed_dataset.xlsx
│   ├── BANDA_EFA
│   │   ├── EFA_model.pkl
│   │   ├── EFA_scores.xlsx
│   │   ├── Heatmap.png
│   │   ├── barplot_loadings.png
│   │   ├── communalities.xlsx
│   │   ├── eigenvalues.xlsx
│   │   ├── horns_parallel_screeplot.png
│   │   ├── loadings.xlsx
│   │   ├── parameters.txt
│   │   ├── scree_plot.png
│   │   ├── test_dataset.xlsx
│   │   └── train_dataset.xlsx
│   ├── GESTE_CFA
│   │   ├── CFA_report
│   │   │   ├── css
│   │   │   │   └── bootstrap.min.css
│   │   │   ├── js
│   │   │   │   └── bootstrap.min.js
│   │   │   ├── plots
│   │   │   │   ├── 1
│   │   │   │   ├── 1.png
│   │   │   │   ├── 2
│   │   │   │   ├── 2.png
│   │   │   │   ├── 3
│   │   │   │   ├── 3.png
│   │   │   │   ├── 4
│   │   │   │   └── 4.png
│   │   │   └── report.html
│   │   ├── cfa_model.pkl
│   │   ├── cfa_scores.xlsx
│   │   ├── cfa_stats.xlsx
│   │   ├── parameters.txt
│   │   ├── semplot
│   │   └── semplot.png
│   ├── GESTE_CFA_Apply
│   │   ├── parameters.txt
│   │   └── transformed_dataset.xlsx
│   ├── GESTE_EFA
│   │   ├── EFA_model.pkl
│   │   ├── EFA_scores.xlsx
│   │   ├── Heatmap.png
│   │   ├── barplot_loadings.png
│   │   ├── communalities.xlsx
│   │   ├── eigenvalues.xlsx
│   │   ├── horns_parallel_screeplot.png
│   │   ├── loadings.xlsx
│   │   ├── parameters.txt
│   │   ├── scree_plot.png
│   │   ├── test_dataset.xlsx
│   │   └── train_dataset.xlsx
│   ├── abcd_data_preprocessed.xlsx
│   ├── abcd_data_residualized.xlsx
│   ├── banda_data_preprocessed.xlsx
│   ├── banda_data_residualized.xlsx
│   ├── geste_data_preprocessed.xlsx
│   └── geste_data_residualized.xlsx
├── profileanalysis
│   ├── ABCD_coef1.png
│   ├── ABCD_coef2.png
│   ├── ABCD_coef3.png
│   ├── ABCD_coef4.png
│   ├── ABCD_coef5.png
│   ├── ABCD_coef6.png
│   ├── ABCD_coef7.png
│   ├── ABCD_plsr_coef.xlsx
│   ├── ABCD_plsr_coef_pval.xlsx
│   ├── ABCD_plsr_coef_pval_fdr_corrected.xlsx
│   ├── ABCD_plsr_stats.xlsx
│   ├── GESTE_coef1.png
│   ├── GESTE_coef2.png
│   ├── GESTE_coef3.png
│   ├── GESTE_coef4.png
│   ├── GESTE_coef5.png
│   ├── GESTE_coef6.png
│   ├── GESTE_coef7.png
│   ├── GESTE_plsr_coef.xlsx
│   ├── GESTE_plsr_coef_pval.xlsx
│   ├── GESTE_plsr_coef_pval_fdr_corrected.xlsx
│   └── GESTE_plsr_stats.xlsx
└── viz
    ├── ANOVA_results.xlsx
    ├── NetworkCohort.png
    ├── RadarPlotABCD.png
    ├── RadarPlotBANDA.png
    ├── RadarPlotCombined.png
    └── RadarPlotGESTE.png

```
