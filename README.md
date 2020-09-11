# Plot juicerbox observed/expected matrix

I have to say that .hic file is probably the most efficient format for storing large matrix. However, there is no command line version for `juicerbox.jar`. When I want to have the exact matrix visualization, it is not easy to get them.

This is the pipeline I found.

### step 1: juicer_tools dump with -d

```

python dump_hic.py chrom.size

```

### step 2: modified HiCPlotter.py

```
python HiCPlotter.py -f Jurkat_HiC_homer_tag_Y_PATERNAL_oe.mat -n chrY -chr chrY_paternal -o test.pdf -r 250000 -fh 0  -ext pdf -nl 1 -hmc 3 -hist Jurkat_20copy.PC1.bedGraph.sorted -hl PC1 -hc "143D52" -fhist 1
```

The `HiCplotter.py` is specifically modified to plot negative values and Red White Blue color map.


