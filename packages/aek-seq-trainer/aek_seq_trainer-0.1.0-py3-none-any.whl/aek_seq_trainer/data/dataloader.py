import torch
from torch.utils.data import Dataset, DataLoader
from .preprocessing import TextPreprocessor
class SentimentDataset(Dataset):
    def __init__(self, texts, labels, preprocessor, max_len=50):
        self.texts = texts
        self.labels = labels
        self.preprocessor = preprocessor
        self.max_len = max_len

    def __len__(self):
        return len(self.texts)
    
    def __getitem__(self, idx):
        text = self.texts[idx]
        label = self.labels[idx]
        encoded = self.preprocessor.encode(text)
        padded = self.preprocessor.pad_sequence(encoded, self.max_len)
        return torch.tensor(padded, dtype=torch.long), torch.tensor(label, dtype=torch.long)
    
def create_dataloader(texts, labels, preprocessor, batch_size=32, max_len=50, shuffle=True):
    dataset = SentimentDataset(texts, labels, preprocessor, max_len)
    return DataLoader(dataset, batch_size=batch_size, shuffle=shuffle)
