
# gpuR is the official R package for working with GPUs and CUDA

[This](https://cran.r-project.org/web/packages/gpuR/gpuR.pdf) is the official page for gpuR.

Install [R](https://www.r-project.org/) and [RTools](https://cran.r-project.org/bin/windows/Rtools/)(for building packages from source).

Install gpuR: 

```

> install.packages('gpuR')
Warning in install.packages("gpuR") :
  'lib = "C:/Program Files/R/R-3.4.3/library"' is not writable
--- Please select a CRAN mirror for use in this session ---
also installing the dependencies ‘mime’, ‘glue’, ‘magrittr’, ‘stringi’, ‘evaluate’, ‘highr’, ‘markdown’, ‘stringr’, ‘yaml’, ‘assertive.base’, ‘assertive.properties’, ‘assertive.types’, ‘assertive.numbers’, ‘assertive.strings’, ‘assertive.datetimes’, ‘assertive.files’, ‘assertive.sets’, ‘assertive.matrices’, ‘assertive.models’, ‘assertive.data’, ‘assertive.data.uk’, ‘assertive.data.us’, ‘assertive.reflection’, ‘assertive.code’, ‘knitr’, ‘Rcpp’, ‘assertive’, ‘RcppEigen’, ‘RViennaCL’, ‘BH’

Package which is only available in source form, and may need
  compilation of C/C++/Fortran: ‘gpuR’
Do you want to attempt to install these from sources?
y/n: 

```

Installed as personal library, might have to change that if we do standard software builds for people.
