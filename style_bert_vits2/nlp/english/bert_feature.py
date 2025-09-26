from __future__ import annotations

from kabosu_plus.sbv2.nlp.english import bert_feature

from collections.abc import Sequence
from typing import TYPE_CHECKING, Optional, Union, Any

import numpy as np

if TYPE_CHECKING:
    import torch

if TYPE_CHECKING:
    import torch


def extract_bert_feature(
    text: str,
    word2ph: list[int],
    onnx_providers: Sequence[Union[str, tuple[str, dict[str, Any]]]],
    assist_text: Optional[str] = None,
    assist_text_weight: float = 0.7,
) -> torch.Tensor:
    """
    英語のテキストから BERT の特徴量を抽出する (PyTorch 推論)

    Args:
        text (str): 英語のテキスト
        word2ph (list[int]): 元のテキストの各文字に音素が何個割り当てられるかを表すリスト
        device (str): 推論に利用するデバイス
        assist_text (Optional[str], optional): 補助テキスト (デフォルト: None)
        assist_text_weight (float, optional): 補助テキストの重み (デフォルト: 0.7)

    Returns:
        torch.Tensor: BERT の特徴量
    """

    import torch

    out = bert_feature.extract_bert_feature_onnx(text=text,
                                                 word2ph=word2ph,
                                                 onnx_providers=onnx_providers,
                                                 assist_text=assist_text,
                                                 assist_text_weight=assist_text_weight)
    
    out = torch.from_numpy(out.astype(np.float32)).clone()
    return out