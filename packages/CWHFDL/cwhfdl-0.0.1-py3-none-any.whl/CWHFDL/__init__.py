import random

import torchvision
import torch
import torch.nn as nn
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.metrics import roc_curve, auc, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler
from torch.utils.data import DataLoader, TensorDataset, random_split


class FuzzyLayer(nn.Module):
    def __init__(self, in_features, num_memberships):
        super(FuzzyLayer, self).__init__()
        self.in_features = in_features
        self.num_memberships = num_memberships
        self.mu = nn.Parameter(torch.randn(num_memberships, in_features))
        self.sigma = nn.Parameter(torch.ones(num_memberships, in_features))

    def forward(self, a):
        a = a.unsqueeze(1)
        mu = self.mu.unsqueeze(0)
        sigma = self.sigma.unsqueeze(0)
        fuzzy_out = torch.exp(-((a - mu) ** 2) / (sigma ** 2))
        return fuzzy_out


class NeuralRep(nn.Module):
    def __init__(self, in_features, hidden_dim=128, dropout_rate=0.1):
        super(NeuralRep, self).__init__()
        self.fc1 = nn.Linear(in_features, hidden_dim)
        self.fc2 = nn.Linear(hidden_dim, hidden_dim)
        self.dropout = nn.Dropout(p=dropout_rate)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.dropout(x)
        x = torch.relu(self.fc2(x))
        return x


class FusionLayer(nn.Module):
    def __init__(self, in_features, hidden_dim, num_memberships):
        super(FusionLayer, self).__init__()
        self.output_dim = hidden_dim
        self.fusion = nn.Linear(
            num_memberships *
            in_features +
            hidden_dim,
            hidden_dim)

    def forward(self, fuzzy_out, neural_out):
        batch_size = fuzzy_out.size(0)
        fuzzy_flat = fuzzy_out.view(batch_size, -1)
        combined = torch.cat([fuzzy_flat, neural_out], dim=1)
        return torch.relu(self.fusion(combined))


class Classifier(nn.Module):
    def __init__(self, hidden_dim, num_classes):
        super(Classifier, self).__init__()
        self.output = nn.Linear(hidden_dim, num_classes)

    def forward(self, x):
        z = self.output(x)
        return torch.softmax(z, dim=1)


class FDNN(nn.Module):
    def __init__(
            self,
            in_features,
            hidden_dim,
            num_memberships,
            num_classes,
            dropout_rate=0.1):
        super(FDNN, self).__init__()
        self.fuzzy = FuzzyLayer(in_features, num_memberships)
        self.neural = NeuralRep(in_features, hidden_dim, dropout_rate)
        self.fusion = FusionLayer(in_features, hidden_dim, num_memberships)
        self.classifier = Classifier(hidden_dim, num_classes)

    def forward(self, x):
        fuzzy_out = self.fuzzy(x)
        neural_out = self.neural(x)
        fusion_out = self.fusion(fuzzy_out, neural_out)
        return self.classifier(fusion_out)


def initialize_fuzzy_layer(fuzzy_layer, data_loader, num_samples=1000):
    all_inputs = []
    for batch_x, _ in data_loader:
        all_inputs.append(batch_x)
    all_inputs = torch.cat(all_inputs, dim=0)

    if all_inputs.shape[0] > num_samples:
        idx = torch.randperm(all_inputs.shape[0])[:num_samples]
        all_inputs = all_inputs[idx]

    inputs_np = all_inputs.numpy()
    kmeans = KMeans(n_clusters=fuzzy_layer.num_memberships, random_state=32)
    kmeans.fit(inputs_np)

    centers = kmeans.cluster_centers_
    fuzzy_layer.mu.data = torch.tensor(centers, dtype=torch.float32)

    labels = kmeans.labels_
    sigmas = []
    for i in range(fuzzy_layer.num_memberships):
        cluster_points = inputs_np[labels == i]
        if len(cluster_points) > 1:
            distances = ((cluster_points - centers[i]) ** 2).mean(axis=0)
            sigma = distances ** 0.5
        else:
            sigma = np.ones(fuzzy_layer.in_features) * 0.1
        sigmas.append(sigma)

    fuzzy_layer.sigma.data = torch.tensor(sigmas, dtype=torch.float32)


def set_seed(seed):
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False
    np.random.seed(seed)
    random.seed(seed)
