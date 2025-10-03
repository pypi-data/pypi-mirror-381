# k-nickname

A simple Python package to generate fun Korean-style nicknames like:

- 빠른여우42
- 심쿵고래7
- 멋진호랑이88

## Installation

```bash
pip install k-nickname
```

## Usage

```python
from k_nickname import generate_nickname

print(generate_nickname())
# 예: '심쿵고래7'
```

```python
from k_nickname import generate_nickname

for _ in range(5):
    print(generate_nickname())
```

출력 예:

```txt
빠른여우42
심쿵고래7
고독한펭귄55
귀여운사자8
행복한토끼91
```
