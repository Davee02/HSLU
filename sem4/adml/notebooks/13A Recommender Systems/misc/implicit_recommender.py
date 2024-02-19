import implicit
import scipy.sparse as sparse

class ImplicitRecommenderSystem(RecommenderSystem):
    def fit(self, deals: pd.DataFrame, categories: pd.DataFrame):
        self.categories = categories
        self.encodings = self.__generate_encodings__(deals) 
        self.mid_to_idx, self.idx_to_mid, self.uid_to_idx, idx_to_uid = self.encodings
        self.train_csr = self.__to_sparse_matrix__(train, self.mid_to_idx, self.uid_to_idx)

        self.model = implicit.nearest_neighbours.CosineRecommender(K=n_neighbors)
        self.model.fit(self.train_csr, show_progress=True)

        
    def predict(self, deals: pd.DataFrame, n_recommendations: int, n_neighbors: int = -1) -> pd.DataFrame:
        user_to_item_matrix = self.get_user_to_item_matrix(deals, categories)
        
        recommendations = []
        for user_id in tqdm_notebook(train.user_id.unique()):
            rec = [self.idx_to_mid[x] for x, y in self.model.recommend(1, self.train_csr.T.tocsr(), N=n_recommendations)]
            recommendations.append(rec)
        recommendations = pd.DataFrame(data=recommendations)
        recommendations.index = user_to_item_matrix.index
        return recommendations
        
    
    def __generate_encodings__(self, data) -> (dict, dict, dict, dict):
        _mid_to_idx = {}
        _idx_to_mid = {}
        for (idx, mid) in enumerate(data.category_id.unique().tolist()):
            _mid_to_idx[mid] = idx
            _idx_to_mid[idx] = mid
        _uid_to_idx = {}
        _idx_to_uid = {}
        for (idx, uid) in enumerate(data.user_id.unique().tolist()):
            _uid_to_idx[uid] = idx
            _idx_to_uid[idx] = uid
        return _mid_to_idx, _idx_to_mid, _uid_to_idx, _idx_to_uid


    def __to_sparse_matrix__(self, data, mid_to_idx, uid_to_idx) -> sparse.csr_matrix:
        """
        Transforms pandas dataframe into a sparse matrix.
        @param data: Pandas dataframe with columns (user, item, rating) or (item, rating) for anonymous user
        @param mid_to_idx: Encodings for items
        @param uid_to_idx: Encodings for users - can be None for anonymous user
        @return: A sparse matrix
        """
        nb_users = len(uid_to_idx.keys()) if uid_to_idx is not None else 1
        nb_items = len(mid_to_idx.keys())
        items = data.category_id.apply((lambda row, mapper: mapper[row]), args=[mid_to_idx]).values
        users = data.user_id.apply((lambda row, mapper: mapper[row]), args=[uid_to_idx]).values if uid_to_idx is not None else [0] * len(data)
        return sparse.csr_matrix((data.views.values.astype(float), (items, users)), shape=(nb_items, nb_users))

    