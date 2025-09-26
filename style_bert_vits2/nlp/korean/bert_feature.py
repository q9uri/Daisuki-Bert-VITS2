import sys

from kabosu_plus.sbv2.constants import Languages
from typing import TYPE_CHECKING, Any, Optional, Union
from numpy.typing import NDArray


from style_bert_vits2.nlp import bert_models

if TYPE_CHECKING:
    import torch




def get_bert_feature(
    text: str,
    word2ph: list[str],
    device: str,
    style_text:Optional[str] = None,
    style_weight: float = 0.7,
):
    if device == "cuda" and not torch.cuda.is_available():
        device = "cpu"
    model = bert_models.load_model(Languages.KO, device_map=device)
    bert_models.transfer_model(Languages.KO, device)

    with torch.no_grad():
        tokenizer = bert_models.load_tokenizer(Languages.KO)
        inputs = tokenizer(text, return_tensors="pt")
        for i in inputs:
            inputs[i] = inputs[i].to(device) # type: ignore
        res = model[device](**inputs, output_hidden_states=True)
        res = torch.cat(res["hidden_states"][-3:-2], -1)[0].cpu()
        if style_text:
            style_inputs = tokenizer(style_text, return_tensors="pt")
            for i in style_inputs:
                style_inputs[i] = style_inputs[i].to(device) # type: ignore
            style_res = model[device](**style_inputs, output_hidden_states=True)
            style_res = torch.cat(style_res["hidden_states"][-3:-2], -1)[0].cpu()
            style_res_mean = style_res.mean(0)
    assert len(word2ph) == res.shape[0], (text, res.shape[0], len(word2ph))
    word2phone = word2ph
    phone_level_feature = []
    for i in range(len(word2phone)):
        if style_text:
            repeat_feature = (
                res[i].repeat(word2phone[i], 1) * (1 - style_weight)
                + style_res_mean.repeat(word2phone[i], 1) * style_weight
            )
        else:
            repeat_feature = res[i].repeat(word2phone[i], 1)
        phone_level_feature.append(repeat_feature)

    phone_level_feature = torch.cat(phone_level_feature, dim=0)
    return phone_level_feature.T
