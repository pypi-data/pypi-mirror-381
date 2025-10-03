import torch
import torch.nn as nn

class LSTMClassifier(nn.Module):

    def __init__(self, vocab_size, embed_dim=128, hidden_dim=128, num_layers=1, num_classes=2, dropout=0.2):
        super(LSTMClassifier, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim, padding_idx=0)
        self.lstm = nn.LSTM(
            input_size=embed_dim,
            hidden_size=hidden_dim,
            num_layers=num_layers,
            batch_first=True,
            dropout=dropout if num_layers > 1 else 0.0,
            bidirectional=False
        )
        self.fc = nn.Linear(hidden_dim, num_classes)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x):

        emb = self.embedding(x)
        lstm_out, (h_n, c_n) = self.lstm(emb)
        last_hidden = lstm_out[:, -1, :]
        out = self.dropout(last_hidden)
        logits = self.fc(out)
        return logits
    