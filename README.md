<!-- PROJECT LOGO -->
<br />
<p align="center">

  <h1 align="center"><a href="">Overprinting with Tomographic Volumetric Additive Manufacturing</a></h1>



  <p align="center">
    <br />
    <a href="https://www.felixwechsler.science/"><strong>Felix Wechsler</strong></a>
    ·
    <a href=""><strong>Viola Sgarminato/strong></a>
    ·
    <a href=""><strong>Riccardo Rizzo</strong></a>
    ·
    <a href=""><strong>Baptiste Nicolet</strong></a>
    ·
    <a href=""><strong>Wenzel Jakob</strong></a>
    ·
    <a href=""><strong>Christophe Moser</strong></a>
  </p>

  <p align="center">
    <a href='https://www.nature.com/articles/s41467-026-73477-3'>
      <img src='https://img.shields.io/badge/Paper-PDF-red?style=flat-square' alt='Paper PDF'>
    </a>
  </p>
</p>

  <a href="">
    <img src="https://raw.githubusercontent.com/EPFL-LAPD/Overprinting-with-Tomographic-Volumetric-Additive-Manufacturing/refs/heads/main/overview.jpg" alt="Logo" width="100%">
  </a>



This is the supplementary code and configuration files for the paper published in [Nature Communications](https://www.nature.com/articles/s41467-026-73477-3):

```bibtex
@article{wechsler_overprinting_TVAM,
   title={Overprinting with tomographic volumetric additive manufacturing},
   author={Wechsler, Felix and Sgarminato, Viola and Rizzo, Riccardo and Nicolet, Baptiste and Jakob, Wenzel and Moser, Christophe},
   rights={2026 The Author(s)},
   ISSN={2041-1723},
   url={https://www.nature.com/articles/s41467-026-73477-3},
   DOI={10.1038/s41467-026-73477-3},
   journal={Nature Communications},
   publisher={Nature Publishing Group},
   year={2026},
   month=jun,
   language={en}
}
```


# Dr.TVAM
We used [Dr.TVAM](https://github.com/rgl-epfl/drtvam) (version 0.7.0) to optimize those configuration files.

For example, the patterns for the perfusion system can be optimized by calling:
```
# install drtvam first
pip install drtvam==0.6.0

# optimize patterns
drtvam spheres_bio_channels/config.json
```

# arXiv version
This repository might change in future but the state of the arXiv preprint can be found [here](https://github.com/EPFL-LAPD/Overprinting-with-Tomographic-Volumetric-Additive-Manufacturing/releases/tag/arXiv2507.13842).


# License
The following configuration files are compatible with [Dr.TVAM](https://github.com/rgl-epfl/drtvam) and are only allowed to use for academic, non-commercial purposes only. See [LICENSE](LICENSE) for more details.
