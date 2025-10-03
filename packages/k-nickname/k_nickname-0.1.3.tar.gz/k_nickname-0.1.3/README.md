# k-nickname

A simple Python package to generate fun Korean-style nicknames like:

- 잔망스러운햄스터37
- 부드러운앵무새
- 순수한문어🎛
- 붉은불사조519

## Installation

```bash
pip install k-nickname
```

## Usage

```python
from k_nickname.generator import Generator

gen = Generator()
print(gen.generate_k_nickname()) # 심쿵고래7

gen2 = Generator(use_number=False, use_emoji=True)
print(gen.generate_k_nickname()) # 상쾌한곰🎅
```
