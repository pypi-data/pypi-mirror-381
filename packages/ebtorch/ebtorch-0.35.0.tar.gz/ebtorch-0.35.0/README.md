# :fire: `ebtorch` <a href="https://bucket.ballarin.cc/serve/img/ebtorch_penguin.png"><img src="https://bucket.ballarin.cc/serve/img/ebtorch_penguin.png" align="right" height="139" /></a>

Collection of [PyTorch](https://pytorch.org/) additions, extensions, utilities, *uses and abuses*.

---

### Getting started

Due to the dependency of `ebtorch` on:
- the latest (unpublished) upstream version of [AdverTorch](https://github.com/BorealisAI/advertorch);
- [TorchAttacks](https://github.com/Harry24k/adversarial-attacks-pytorch), which in turn depends (probably too tightly) on `requests~=2.25.1`,

the recommended way of installing `ebtorch`, at the moment, is the following:

```bash
pip install --upgrade "ebtorch>=0.35" "git+https://github.com/BorealisAI/advertorch.git" "requests>=2.32.5"
```

Within [Google Colab](https://colab.research.google.com), it can be installed (together with all missing dependencies) with:

```jupyter
!pip install "fire>=0.6" "medmnist>=3.0.2" "torchattacks>=3.5.1" "git+https://github.com/BorealisAI/advertorch.git" "ebtorch>=0.35" --no-deps
```
