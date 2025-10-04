import scanpy as sc
import anndata as ad

def process(sliceA, sliceB):
    joint_adata = ad.concat([sliceA, sliceB])
    sc.pp.normalize_total(joint_adata, inplace=True)
    sc.pp.log1p(joint_adata)
    sc.pp.highly_variable_genes(joint_adata, n_top_genes=5000)
    sc.pp.pca(joint_adata, 50)
    joint_datamatrix = joint_adata.obsm['X_pca']
    A_X_pca = joint_datamatrix[:sliceA.shape[0], :]
    B_X_pca = joint_datamatrix[sliceA.shape[0]:, :]
    return (A_X_pca, B_X_pca)
