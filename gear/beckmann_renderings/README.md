# Beckmann plots

Generate `final.npy` with:
`for x in 0.00 0.02 0.04 0.06 0.10 0.30; do drtvam config_$x.json -Dspp_ref=512 -Doutput=gear_$x -Dmax_depth=4 -Dvial.height=200000; done`

And then call: `python plot_all.py`
