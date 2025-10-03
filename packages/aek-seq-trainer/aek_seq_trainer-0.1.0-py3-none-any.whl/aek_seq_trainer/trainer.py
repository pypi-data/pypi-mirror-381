import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader

from aek_seq_trainer.models.lstm import LSTMClassifier
from aek_seq_trainer.utils.metrics import compute_metrics
from aek_seq_trainer.utils.logger import get_logger

class SentimentTrainer:

    def __init__(self, model: nn.Module,
                 train_loader: DataLoader, val_loader: DataLoader = None,
                 lr: float = 1e-3, num_epochs: int = 10,
                 device: str = None, logger_name: str = "aek-seq-trainer"):
        
        self.device = torch.device(device if device else ("cuda" if torch.cuda.is_available() else "cpu"))
        self.model = model.to(self.device)
        self.train_loader = train_loader
        self.val_loader = val_loader
        self.num_epochs = num_epochs
        self.logger = get_logger(logger_name)
        self.criterion = nn.CrossEntropyLoss()
        self.optimizer = optim.AdamW(self.model.parameters(), lr=lr)

    def train(self):
        self.model.train()
        for epoch in range(1, self.num_epochs + 1):
            running_loss = 0.0
            for batch_idx, (inputs, labels) in enumerate(self.train_loader):
                inputs, labels = inputs.to(self.device), labels.to(self.device)

                self.optimizer.zero_grad()
                outputs = self.model(inputs)
                loss = self.criterion(outputs, labels)
                loss.backward()
                self.optimizer.step()
                running_loss += loss.item()
            
            avg_loss = running_loss / len(self.train_loader)
            self.logger.info(f"epoch [{epoch}/{self.num_epochs}] - train loss: {avg_loss:.4f}")

            if self.val_loader:
                val_metrics = self.evaluate()
                self.logger.info(f"epoch [{epoch}/{self.num_epochs}] - val metrics: {val_metrics}")

    def evaluate(self):
        self.model.eval()
        all_preds = []
        all_labels = []

        with torch.no_grad():
            for inputs, labels in self.val_loader:
                inputs, labels  = inputs.to(self.device), labels.to(self.device)
                outputs = self.model(inputs)
                preds = torch.argmax(outputs, dim=1)
                all_preds.extend(preds.cpu().numpy())
                all_labels.extend(labels.cpu().numpy())
        metrics = compute_metrics(all_labels, all_preds)
        self.model.train()
        return metrics
    
    def predict(self, inputs):

        self.model.eval()
        if not isinstance(inputs, torch.Tensor):
            raise ValueError("inputs must be a torch.Tensor")
        inputs = inputs.to(self.device)
        with torch.no_grad():
            logits = self.model(inputs)
            preds = torch.argmax(logits, dim=1)