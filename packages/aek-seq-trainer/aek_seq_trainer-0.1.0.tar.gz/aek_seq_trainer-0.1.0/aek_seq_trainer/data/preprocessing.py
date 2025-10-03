import re
from collections import Counter
import torch

class TextPreprocessor:
    def __init__(self, min_freq: int = 2, max_vocab_size: int = 10000):
        self.min_freq = min_freq
        self.max_vocab_size = max_vocab_size
        self.word2idx = {"<PAD>": 0, "<UNK>": 1}
        self.idx2word = {0: "<PAD>", 1: "<UNK>"}
        self.vocab_built = False

    def tokenize(self, text: str):

        text = text.lower()
        tokens = re.findall(r"\b\w+\b", text)
        return tokens
    
    def build_vocab(self, texts):
        counter = Counter()
        for text in texts:
            tokens = self.tokenize(text)
            counter.update(tokens)
        
        most_common = [w for w, f in counter.items() if f >= self.min_freq]
        most_common = most_common[: self.max_vocab_size - len(self.word2idx)]

        for i, word in enumerate(most_common, start=len(self.word2idx)):
            self.word2idx[word] = i
            self.idx2word[i] = word

        self.vocab_built = True
    
    def encode(self, text: str):
        tokens = self.tokenize(text)
        return [self.word2idx.get(t, self.word2idx["<UNK>"]) for t in tokens]
    
    def decode(self, indices):
        return [self.idx2word.get(i, "<UNK>") for i in indices]
    
    def pad_sequence(self, sequence, max_len: int):
        if len(sequence) < max_len:
            sequence += [self.word2idx["<PAD>"]] * (max_len - len(sequence))
        else:
            sequence = sequence[:max_len]
        return sequence
    
    def preprocess_batch(self, texts, max_len: int = 50):
        encoded = [self.encode(t) for t in texts]
        padded = [self.pad_sequence(seq, max_len) for seq in encoded]
        return torch.tensor(padded, dtype=torch.long)
    