---
aliases: []
title: DataWhale 9月 大模型实训 T1：大模型介绍与环境配置
date: 2025-09-14
updated:
category:
  - 学习
tags: [DataWhale, LLM]
status:
  - published
description: ""
cover: ""
hidden: false
sidebar: true
outline:
  - 2
  - 3
comment: true
search: true
sticky:
hot:
recommend:
series:
  name:
  order:
badge:
  text:
  type:
readingTime: true
wordCount: true
author:
reproduced: false
source:
sourceLink:
---
# DataWhale 9月 大模型实训 T1：大模型介绍与环境配置

## 相关问题的探讨

### 1. 大模型，大在哪里？
- 首先，大在**参数**。在机器学习中，人们通过程序构建一个模型，再由模型将输入数据得出预期的输出数据。这个“模型”关键就在于其中的参数。统计学习理论指出，当参数量 p 与样本量 n 的比值 p/n ≪ 1 时，泛化误差才受控，一个模型的参数量决定了这个模型的上限（复杂度），参数越多，模型可张成的函数空间维度越高，对复杂映射的逼近能力才跟得上，通俗的说法就是更多次幂的函数可以表示出更复杂的函数图像。有了如此多的参数，大模型便可以更好地拟合训练数据，从而得到一个“聪明”的模型。
- 其次，大在**数据**。在机器学习课程中我们了解到“过拟合”这个概念，也就是说训练数据得到的模型对于训练数据拟合充分、甚至完美，而对于测试数据则表现不佳。导致过拟合的其中一个原因[^1]便是模型过于复杂+训练数据不足，不仅要“多”，还要“杂”——覆盖足够多的分布角落，才能抵消容量带来的记忆倾向，因此对于参数量如此巨大的大模型，需要有更更多的训练数据来减少过拟合的可能性，让大模型“见见世面”。
- 最后，大在**算力**。对于一个既有大参数，也有大数据的模型，一个快速地运算核心是必不可少的，否则将是数周、数月的等待，175 B 参数的 FP16 模型仅权重就占 350 GB，需要 A100 80 GB × 5 台以上做张量并行；更关键的是通信带宽，否则 90 % 时间花在等数据，而非计算。神经网络再度兴起的原因也是因为有了强大的算力支撑，硬件将是未来人们发展算法的强大后盾！
### 2. 大模型和传统的NLP模型有和异同？
传统 NLP 模型（如 BERT、RoBERTa、ALBERT 等）通常是面向单一、小规模问题域构建的“专家”：先人工设计任务格式，再采集对应标注数据，最后在固定场景里调优。 换言之，它们依赖“任务特定数据 + 微调”范式，参数规模一般≤几亿，知识容量有限，跨任务迁移需重新训练或嫁接结构。大模型则走“通才”路线,通过自监督在大规模无标注文本上预训练，隐式存储了广泛的世界知识与语言规律。  

总结来说，  
传统模型 = 小容量·深雕琢·单领域专家； 
大模型 = 大容量·广涉猎·多面手，并且可以后续再用轻量级指令微调或领域 LoRA 即可快速变身“专家”，形成“通才 + 专才”的新范式。

### 3. 大模型只能用作NLP任务吗？
根据问题1提到的几个特点，我们可以判断大模型不仅仅用于所谓的“NLP”任务。例如：ViT、CLIP在计算机视觉领域十分热门，GPT在多模态领域引领新潮，AlphaFold2 把氨基酸序列当 token，单序列即可预测三维结构。大模型早已突破纯文本边界，只要你能把对象切成 token，它就能在大参数空间里拟合复杂映射。

## 课后作业

```python
from modelscope import snapshot_download, AutoModelForCausalLM, AutoTokenizer
import torch

#下载模型
model_dir = snapshot_download(
    'Qwen/Qwen3-4B-Instruct-2507',
    cache_dir='/root/autodl-tmp/model',  
    revision='master'
)

#加载 tokenizer 和模型
tokenizer = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    model_dir,
    torch_dtype="auto",
    device_map="auto",         
    trust_remote_code=True
) 

#构造对话
prompt = "请用三句话介绍一下你自己。"
messages = [{"role": "user", "content": prompt}]
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)
inputs = tokenizer([text], return_tensors="pt").to(model.device) 

#生成回答
with torch.no_grad():
    outputs = model.generate(
        **inputs,
        max_new_tokens=256,      
        do_sample=True,
        temperature=0.7
    )

reply = tokenizer.decode(outputs[0][len(inputs.input_ids[0]):], skip_special_tokens=True)

print("模型回答：", reply)
```
最终得到如下回答：
![[image.png]]
可以看到对于我的指令“三句话”还是执行的很好的。


[^1]:  导致过拟合的原因有很多，包括：**模型太聪明、数据太单薄、约束太松散**，三者任一失衡，都会让模型从“学习”滑向“背诵”。