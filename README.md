dirichlet
=========

[![image](https://img.shields.io/travis/tdhopper/dirichletprocess.svg)](https://travis-ci.org/tdhopper/dirichletprocess)

[![image](https://img.shields.io/pypi/v/dirichletprocess.svg)](https://pypi.python.org/pypi/dirichletprocess)



Construct a [Dirichlet Process](https://github.com/tdhopper/notes-on-dirichlet-processes) from any random sampler.

```
In [1]: from dp import DirichletProcess

In [2]: from random import normalvariate

In [3]: from collections import Counter

In [4]: dp =  DirichletProcess(lambda: normalvariate(0, 1), alpha=1)

In [7]: Counter(dp() for _ in range(1000))
Out[7]: Counter({-0.029073686274754998: 679, 0.7332646430104509: 301, 0.23296111210571477: 12, -0.7042044460111074: 4, -2.2504937687943922: 4})
```

Install with `pip install dirichletprocess` or `conda install -c tdhopper dirichletprocess`.