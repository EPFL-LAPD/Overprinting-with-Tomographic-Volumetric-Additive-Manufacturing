# Gear Overprinting

Optimize first for absorbing and scattering patterns each
```
drtvam gear_4mm_black_smaller_gear/config.json
drtvam gear_4mm_black_smaller_gear/config.json
```


## Re-evaluating the scattering patterns in absorbing condition
This takes existing patterns, uses a different config file to project them and then stores in a new folder:
```
drtvam --forward_mode --patterns gear_4mm_black_smaller_gear/patterns.npz  gear_4mm_smaller_gear/config.json -Doutput=gear_4mm_fwd_smaller_gear/
```
