# dvidump

*human-friendly opcode viewer for dvi files*

This small utility allows you to see exactly what the output of a TeX run is
providing you. The `dvi` (device independent) file format is actually very
simple - it indicates where to place which characters on pages in x, y
coordinates, and contains page breaks. It contains external references to font
files, but otherwise has no font data. It does not directly support graphics,
although it does have *extenion* opcodes (`xxx1`-`xxx4`) which can be anything
supported by both your dvi-creator and your dvi-reader.

You can read more about the `dvi` file format
[on wikipedia](https://en.wikipedia.org/wiki/Device_independent_file_format) or
in technical detail at
[this `dvi` spec
page](https://web.archive.org/web/20070403030353/http://www.math.umd.edu/~asnowden/comp-cont/dvi.html).

## Installing

```
git clone https://github.com/tylerneylon/dvidump.git
sudo ln -s $(cd dvidump; pwd)/dvidump.py /usr/local/bin/dvidump
```

## Example

I made a very simple file called `a.dvi`; below is the output of `dvidump`
on this file.

```
$ dvidump a.dvi

247            pre   
                       i   2
                     num   25400000
                     den   473628672
                     mag   1000
                       k   27
                       x    TeX output 2018.11.22:2325

______________________________________________________________________

139            bop   
                     c_0   1
                     c_1   0
                     c_2   0
                     c_3   0
                     c_4   0
                     c_5   0
                     c_6   0
                     c_7   0
                     c_8   0
                     c_9   0
                       p   -1
141           push   
159          down3   
                       a   -917504
142            pop   
160          down4   
                       a   42152922
141           push   
160          down4   
                       a   -41497562
141           push   
145         right3   
                       b   1310720
243       fnt_def1   
                       k   0
                       c   1274110073
                       s   655360
                       d   655360
                       a   0
                       l   5
                       n   cmr10
171      fnt_num_0   
084    set_char_84   T
104   set_char_104   h
105   set_char_105   i
115   set_char_115   s
150             w3   
                       b   218453
105   set_char_105   i
115   set_char_115   s
147             w0   
116   set_char_116   t
104   set_char_104   h
101   set_char_101   e
147             w0   
099    set_char_99   c
111   set_char_111   o
110   set_char_110   n
149             w2   
                       b   -18205
116   set_char_116   t
101   set_char_101   e
110   set_char_110   n
147             w0   
116   set_char_116   t
150             w3   
                       b   218453
111   set_char_111   o
102   set_char_102   f
147             w0   
097    set_char_97   a
046    set_char_46   .
116   set_char_116   t
120   set_char_120   x
116   set_char_116   t
046    set_char_46   .
142            pop   
142            pop   
159          down3   
                       a   1572864
141           push   
146         right4   
                       b   15229091
049    set_char_49   1
142            pop   
140            eop   

______________________________________________________________________

248           post   
                       p   42
                     num   25400000
                     den   473628672
                     mag   1000
                       l   43725786
                       u   30785863
                       s   2
                       t   1
243       fnt_def1   
                       k   0
                       c   1274110073
                       s   655360
                       d   655360
                       a   0
                       l   5
                       n   cmr10
249      post_post   
                       q   185
                       i   2
223      final_pad   
223      final_pad   
223      final_pad   
223      final_pad   
223      final_pad   
223      final_pad   
223      final_pad   
```
