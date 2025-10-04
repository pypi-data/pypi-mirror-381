import os
from typing import Optional, Union, List, Dict, Tuple
import numpy as np
import pandas as pd
from numpy.typing import NDArray
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import ListedColormap

from .models import clone_model

def visualize_patterns(extractor, pattern_indices: Optional[List[int]] = None, path: str = 'images/patterns.png',
                      show_rmse_distribution: bool = True, figsize: Optional[Tuple[int, int]] = None, dpi: int = 300, 
                      colors: Optional[Dict[str, str]] = None, save_image: bool = False, show_image: bool = True,
                      title: Optional[str] = None, show_legend: bool = True, show_grid: bool = True,
                      xlabel: Optional[str] = None, ylabel: Optional[str] = None) -> None:
    if pattern_indices is None:
        pattern_indices = list(range(len(extractor.pattern_list)))
    valid_indices = [i for i in pattern_indices if 0 <= i < len(extractor.pattern_list)]
    n_patterns = len(valid_indices)
    colors = colors or {'pattern': 'blue', 'active': 'red'}
    n_cols = 2 if show_rmse_distribution else 1
    figsize = figsize or (16 if show_rmse_distribution else 8, 4 * n_patterns)
    fig, axes = plt.subplots(n_patterns, n_cols, figsize=figsize)
    if n_patterns == 1:
        axes = axes.reshape(1, -1) if show_rmse_distribution else [axes]
    for idx, pattern_idx in enumerate(valid_indices):
        pattern = extractor.pattern_list[pattern_idx]
        start = extractor.pattern_starts[pattern_idx]
        end = extractor.pattern_ends[pattern_idx]
        ax_left = axes[idx, 0] if show_rmse_distribution else axes[idx]
        active_x = range(start, end)
        ax_left.plot(range(len(pattern)), pattern, color=colors['pattern'], alpha=0.3, label='Full Pattern')
        ax_left.plot(active_x, pattern[start:end], color=colors['active'], linewidth=3, label='Active Region')
        ax_left.scatter(active_x, pattern[start:end], c=colors['active'], s=50, zorder=5)
        plot_title = title or f"Pattern {pattern_idx} (positions {start}-{end})"
        if title is None and extractor.multiple_series and extractor.pattern_series_indices:
            plot_title += f", Series {extractor.pattern_series_indices[pattern_idx]}"
        ax_left.set_title(plot_title)
        ax_left.set_xlabel(xlabel or 'Position')
        ax_left.set_ylabel(ylabel or 'Pattern Value')
        if show_legend:
            ax_left.legend()
        if show_grid:
            ax_left.grid(True, alpha=0.3)
        if show_rmse_distribution:
            ax_right = axes[idx, 1]
            series_idx = extractor.pattern_series_indices[pattern_idx] if extractor.multiple_series and extractor.pattern_series_indices else None
            X_data = extractor.X_train[:, series_idx, :] if extractor.multiple_series and series_idx is not None else extractor.X_train
            X_region = X_data[:, start:end]
            rmse_values = extractor.similarity_fn(X_region, pattern[start:end].astype(np.float32)).flatten()
            has_hue = len(np.unique(extractor.y_train)) <= 10
            if has_hue:
                sns.histplot(x=rmse_values, hue=extractor.y_train, bins=100, alpha=0.7, ax=ax_right)
                ax_right.set_title('RMSE Distribution (by Target)')
            else:
                sns.histplot(x=rmse_values, bins=100, alpha=0.7, ax=ax_right)
                ax_right.set_title('RMSE Distribution')
            ax_right.set_xlabel('RMSE')
            ax_right.set_ylabel('Count')
            ax_right.grid(True, alpha=0.3)
    plt.tight_layout()
    if save_image:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        plt.savefig(path, dpi=dpi, bbox_inches='tight')
        print(f"Patterns visualized and saved to: {path}")
    if show_image:
        plt.show()
    else:
        plt.close(fig)

def visualize_pattern_match(extractor, sample_idx: int = 0, pattern_idx: int = 0, 
                           X_data: Optional[Union[NDArray[np.float32], List[NDArray[np.float32]]]] = None, 
                           y_data: Optional[NDArray[np.float32]] = None, path: str = 'images/pattern_match.png',
                           figsize: Tuple[int, int] = (14, 8), dpi: int = 300, save_image: bool = False,
                           show_image: bool = True, title: Optional[str] = None, show_legend: bool = True,
                           show_grid: bool = True, xlabel: Optional[str] = None, ylabel: Optional[str] = None,
                           colors: Optional[Dict[str, str]] = None) -> None:
    X_data = extractor.X_test if X_data is None else X_data
    pattern = extractor.pattern_list[pattern_idx]
    start, end = extractor.pattern_starts[pattern_idx], extractor.pattern_ends[pattern_idx]
    series_idx = extractor.pattern_series_indices[pattern_idx] if extractor.multiple_series and extractor.pattern_series_indices else None
    series_data = (X_data[series_idx][sample_idx] if extractor.multiple_series and series_idx is not None and isinstance(X_data, list)
                  else X_data[sample_idx] if not isinstance(X_data, list) else X_data[0][sample_idx])
    if isinstance(series_data, (pd.DataFrame, pd.Series)):
        series_data = series_data.values.astype(np.float32)
    else:
        series_data = np.asarray(series_data, dtype=np.float32)
    region, pattern_region = series_data[start:end], pattern[start:end]
    score = extractor.similarity_fn(region.reshape(1, -1), pattern_region)[0]
    pattern_scaled = ((pattern_region - pattern_region.mean()) / pattern_region.std() * region.std() + region.mean()
                     if pattern_region.std() > 0 else pattern_region + region.mean())
    colors = colors or {'data': '#2E86AB', 'pattern': '#A23B72', 'region': '#F18F01'}
    sns.set_style("whitegrid")
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=figsize, height_ratios=[1, 1.2])
    ax1.plot(series_data, color=colors['data'], linewidth=2.5, alpha=0.8)
    ax1.axvspan(start, end-1, alpha=0.2, color=colors['region'], label='Pattern Region')
    ax1.set_ylabel(ylabel or 'Signal Value', fontsize=11, fontweight='bold')
    ax1.set_title(title or f"Sample {sample_idx} - Pattern {pattern_idx} Match" + 
                 (f" (Class: {int(y_data[sample_idx])})" if y_data is not None else ""), 
                 fontsize=13, fontweight='bold', pad=15)
    if show_legend:
        ax1.legend(loc='upper right', fontsize=10)
    if show_grid:
        ax1.grid(True, alpha=0.3, linestyle='--')
    ax1.set_xlim(-1, len(series_data))
    x_positions = np.arange(len(region))
    width = 0.35
    ax2.bar(x_positions - width/2, region, width, label='Actual Data', color=colors['data'], alpha=0.7, edgecolor='black', linewidth=1.2)
    ax2.bar(x_positions + width/2, pattern_scaled, width, label='Pattern (scaled)', color=colors['pattern'], alpha=0.7, edgecolor='black', linewidth=1.2)
    ax2.set_xlabel(xlabel or f'Position in Pattern Region ({start}-{end})', fontsize=11, fontweight='bold')
    ax2.set_ylabel(ylabel or 'Signal Value', fontsize=11, fontweight='bold')
    ax2.set_xticks(x_positions[::max(1, len(x_positions)//10)])
    ax2.set_xticklabels([str(start + i) for i in x_positions[::max(1, len(x_positions)//10)]])
    metric_name = 'RMSE' if 'rmse' in str(extractor.similarity_fn).lower() else 'Similarity Score'
    similarity_quality = 'Excellent' if score < 0.5 else 'Good' if score < 1.0 else 'Moderate' if score < 2.0 else 'Poor'
    textstr = f'{metric_name}: {score:.4f}\nMatch Quality: {similarity_quality}'
    ax2.text(0.98, 0.97, textstr, transform=ax2.transAxes, fontsize=11,
            verticalalignment='top', horizontalalignment='right',
            bbox=dict(boxstyle='round,pad=0.8', facecolor='#FFF9E3', edgecolor='#333', linewidth=2, alpha=0.9))
    if show_legend:
        ax2.legend(loc='upper left', fontsize=10, framealpha=0.9)
    if show_grid:
        ax2.grid(True, alpha=0.3, linestyle='--', axis='y')
    plt.tight_layout()
    if save_image:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        plt.savefig(path, dpi=dpi, bbox_inches='tight')
    if show_image:
        plt.show()
    else:
        plt.close(fig)

def visualize_decision_boundary(extractor, pattern_idx1: int = 0, pattern_idx2: int = 1, 
                               features_data: Optional[NDArray[np.float32]] = None, 
                               y_data: Optional[NDArray[np.float32]] = None, path: str = 'images/decision_boundary.png', 
                               resolution: float = 0.02, figsize: Tuple[int, int] = (7, 6), dpi: int = 300,
                               save_image: bool = False, show_image: bool = True, title: Optional[str] = None,
                               show_legend: bool = True, show_grid: bool = False, xlabel: Optional[str] = None,
                               ylabel: Optional[str] = None, colors: Optional[List[str]] = None, marker: str = 'x',
                               marker_size: int = 15, alpha_background: float = 0.6, alpha_points: float = 0.5) -> None:
    features_data = features_data if features_data is not None else np.column_stack(extractor.features_list)
    y_data = y_data or extractor.y_train
    X_2d = np.column_stack([features_data[:, pattern_idx1], features_data[:, pattern_idx2]])
    x_min, x_max = X_2d[:, 0].min() - 0.05, X_2d[:, 0].max() + 0.05
    y_min, y_max = X_2d[:, 1].min() - 0.05, X_2d[:, 1].max() + 0.05
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100), np.linspace(y_min, y_max, 100))
    mesh_points = np.c_[xx.ravel(), yy.ravel()]
    temp_model = clone_model(extractor.model)
    temp_model.fit(X_2d, y_data, None, None)
    Z = temp_model.predict(mesh_points).reshape(xx.shape)
    sns.set_style("whitegrid")
    fig, ax = plt.subplots(figsize=figsize)
    unique_classes = np.unique(y_data)
    n_classes = len(unique_classes)
    bg_colors = colors or ['lightblue', 'lightcoral', 'lightgreen', 'lightsalmon', 'plum']
    bg_cmap = ListedColormap(bg_colors[:n_classes])
    point_colors = colors or ['blue', 'red', 'green', 'orange', 'purple']
    ax.contourf(xx, yy, Z, levels=n_classes - 1, cmap=bg_cmap, alpha=alpha_background, zorder=2)
    for i, cls in enumerate(unique_classes):
        mask = y_data == cls
        ax.scatter(X_2d[mask, 0], X_2d[mask, 1], c=point_colors[i % len(point_colors)], 
                  label=f'Class {int(cls)}', marker=marker, s=marker_size, 
                  alpha=alpha_points, zorder=4, linewidth=1)
    ax.set_xlabel(xlabel or f'RMSE of pattern {pattern_idx1}')
    ax.set_ylabel(ylabel or f'RMSE of pattern {pattern_idx2}')
    ax.set_title(title or f'Decision Boundary: Pattern {pattern_idx1} vs Pattern {pattern_idx2}')
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    if show_legend:
        ax.legend()
    if show_grid:
        ax.grid(True, alpha=0.3)
    plt.tight_layout()
    if save_image:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        plt.savefig(path, dpi=dpi, bbox_inches='tight')
    if show_image:
        plt.show()
    else:
        plt.close(fig)

