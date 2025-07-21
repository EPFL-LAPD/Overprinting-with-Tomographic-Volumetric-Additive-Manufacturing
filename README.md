# Overprinting with Tomographic Volumetric Additive Manufacturing

This is the supplementary code and configuration files for the following pre-print:

```bibtex
@misc{wechsler2025overprintingtomographicvolumetricadditive,
      title={Overprinting with Tomographic Volumetric Additive Manufacturing}, 
      author={Felix Wechsler and Viola Sgarminato and Riccardo Rizzo and Baptiste Nicolet and Wenzel Jakob and Christophe Moser},
      year={2025},
      eprint={2507.13842},
      archivePrefix={arXiv},
      primaryClass={physics.optics},
      url={https://arxiv.org/abs/2507.13842}, 
}
```

<a  href="https://www.youtube.com/watch?v=ePuIFgeUbNk"><img src="channel.jpg"  width="700"></a>



# Dr.TVAM
We used [Dr.TVAM](github.com/rgl-epfl/drtvam) (version 0.3.0) to optimize those configuration files.

For example, the patterns for the perfusion system can be optimized by calling:
```
drtvam spheres_bio_channels/config.json
```


# License
The following configuration files are compatible with [drtvam](https://github.com/rgl-epfl/drtvam) and are only allowed to use for academic, non-commercial purposes only. See [LICENSE](LICENSE) for more details.
