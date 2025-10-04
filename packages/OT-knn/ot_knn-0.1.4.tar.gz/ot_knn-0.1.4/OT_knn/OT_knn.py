import ot
import numpy as np
import anndata as ad
from typing import Optional, Sequence, List
from .data_process import process
from anndata import AnnData


# find the k nearest nrighbors
def Neighbor(k, D):
    Neighbor_index = np.zeros(D.shape)
    Neighbor_D = np.empty((D.shape[0],k))
    for i in range(D.shape[0]):
        D_i = D[i,:]
        Neighbor_D[i,:] = np.sort(D_i)[:(k+1)][1:(k+1)]
        D_cut = np.max(Neighbor_D[i,:])
        for j in range(D.shape[0]):
            if (D[i,j] <= D_cut):
                Neighbor_index[i,j]=1
    return (Neighbor_index, Neighbor_D)

# assign weight to each neighbor
def Weight(q, k, D):
    Neighbor_index = Neighbor(k,D)[0]
    Neighbor_D = Neighbor(k,D)[1]
    Neighbor_q = np.quantile(Neighbor_D,q)
    Neighbor_weight = np.zeros(D.shape)
    for i in range(D.shape[0]):
        tau = np.max(Neighbor_D[i,:])
        for j in range(D.shape[0]):
            if (Neighbor_index[i,j]==0):
                Neighbor_weight[i,j]=0
            elif (D[i,j] == 0):
                Neighbor_weight[i,j]=1
            elif(0 < D[i,j] <= Neighbor_q[0]):
                Neighbor_weight[i,j]=np.exp(-0.5*D[i,j]/tau)
            elif(Neighbor_q[0] < D[i,j] <= Neighbor_q[1]):
                Neighbor_weight[i,j]=np.exp(-1*D[i,j]/tau)
            else:
                Neighbor_weight[i,j]=np.exp(-2*D[i,j]/tau)
    return Neighbor_weight


# refines each spot’s gene expression profile by a distance-weighted average of its k neighbors
def weighted_sum (X_pca, q, k, D):
    X = np.zeros(X_pca.shape)
    neighbor_index = Neighbor(k=k, D=D)[0]
    neighbor_weight = Weight(q=q, k=k, D=D)
    for i in range(len(X)):
        #label = np.where(neighbor_index[i,:] != 0)
        #label = label[0]
        #n = len(label)
        for j in range(len(X)):
            #X[i,:] = X[i,:] + neighbor_weight[i,label[j]]*X_pca[label[j],:]
            X[i,:] = X[i,:] + neighbor_weight[i,j]*X_pca[j,:]
        X[i,:] = X[i,:]/np.sum(neighbor_weight[i,:])
    return X



def OT_knn(
    sliceA: AnnData,
    sliceB: AnnData,
    a_distribution: Optional[Sequence[float]] = None, 
    b_distribution: Optional[Sequence[float]] = None,
    #Q: list[float] = [0.25,0.5,0.75],
    Q: List[float] = [0.25, 0.5, 0.75],
    K_A: int = 100,
    K_B: int = 100,
    numItermax: int = 200):
    """
    OT-knn alignment between two AnnData slices.
    Args:
        sliceA (AnnData): First slice.
        sliceB (AnnData): Second slice.
        a_distribution (Sequence[float], optional): Distribution weights for slice A.
        b_distribution (Sequence[float], optional): Distribution weights for slice B.
        Q (Sequence[float], optional): Quantile thresholds. Defaults to [0.25, 0.5, 0.75].
        K_A (int): Number of neighbors in slice A. Defaults to 100.
        K_B (int): Number of neighbors in slice B. Defaults to 100.
        numItermax (int): Maximum number of iterations for OT solver. Defaults to 200.
    Returns:
        Alignment between spots of two slices.
    """
    # common genes 
    indexA = sliceA.var.index
    indexB = sliceB.var.index
    common_genes = indexA.intersection(indexB)
    sliceA = sliceA[:, common_genes]
    sliceB = sliceB[:, common_genes]
    # spatial distance
    coordinatesA = sliceA.obsm['spatial'].copy()
    coordinatesB = sliceB.obsm['spatial'].copy()
    D_A = ot.dist(coordinatesA,coordinatesA, metric='euclidean')
    D_B = ot.dist(coordinatesB,coordinatesB, metric='euclidean')
    if a_distribution is None:
        a = np.ones((sliceA.shape[0],))/sliceA.shape[0]
    else:
        a = a_distribution
    if b_distribution is None:
           b = np.ones((sliceB.shape[0],))/sliceB.shape[0]
    else:
        b = b_distribution
    A_X_pca, B_X_pca = process(sliceA,sliceB)
    # refines each spot’s gene expression profile by a distance-weighted average of its k neighbors 
    A_X_N = weighted_sum(X_pca=A_X_pca,q=Q,k=K_A, D=D_A)
    B_X_N = weighted_sum(X_pca=B_X_pca,q=Q,k=K_B, D=D_B)
    # get the alignment using optimal transport
    M = ot.dist(A_X_N,B_X_N)
    pi = ot.emd(a=a, b=b, M=M, numItermax=5000000000000000)
    # get the one-to-one matching
    best_match_1 = []
    best_match_2 = []
    if (pi.shape[0] >= pi.shape[1]):
        for i in range(pi.shape[0]):
            row = pi[i,:]
            M = np.max(row)
            if M >0:
                max_indices = np.flatnonzero(row == M)
                for j in max_indices:  # append each pair separately
                    best_match_1.append(i)
                    best_match_2.append(j)
    else:  
        for j in range(pi.shape[1]):
            col = pi[:, j]
            M = np.max(col)
            if M > 0:
                max_indices = np.flatnonzero(col == M)
                for i in max_indices:  # append each pair separately
                    best_match_1.append(i)
                    best_match_2.append(j)
    best_match = np.column_stack((best_match_1, best_match_2))
    return (pi, best_match)

    




        





