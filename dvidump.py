#!/usr/bin/env python3
""" dvidump.py

    Print a human-friendly dump of the opcodes in a dvi file.

    Usage:

        dvidump <myfile.dvi>

    Installation:

        sudo ln -s $(pwd)/dvidump.py /usr/local/bin/dvidump
"""


# ______________________________________________________________________________
# Internal Notes
#
# I created this script using the very nice file format writeup found here:
# https://web.archive.org/web/20070403030353/http://www.math.umd.edu/~asnowden/comp-cont/dvi.html
#
# My thanks to Andrew Snowden for that excellent summary.
#
# The one technical piece that is not clear from the above page is exactly which
# parameters to opcodes are signed and which are unsigned. I have made educated
# guesses for all opcodes.
#


# ______________________________________________________________________________
# Imports

import string
import sys


# ______________________________________________________________________________
# Globals

opcodes = None


# ______________________________________________________________________________
# Functions

def make_opcode(name=None, comment='', params=[]):
    return {
            'name': name,
            'comment': comment,
            'params': params
    }

def make_p(p_name, p_len, p_type):
    return {
            'name': p_name,
            'len': p_len,
            'type': p_type
    }

def init_opcodes():

    global opcodes

    opcodes = []
    printable = string.printable

    # 0-127 set_char_[i]
    for i in range(128):
        opcodes.append(make_opcode(
                name = 'set_char_%d' % i,
                comment = chr(i) if chr(i) in printable else ''
        ))

    # 128-131 set[i]
    for i in [1, 2, 3, 4]:
        opcodes.append(make_opcode(
                name = 'set%d' % i,
                params = [make_p('c', i, 'U')]
        ))

    # 132 set_rule
    opcodes.append(make_opcode(
            name = 'set_rule',
            params = [make_p('a', 4, 'S'), make_p('b', 4, 'S')]
    ))

    # 133-136 put[i]
    for i in [1, 2, 3, 4]:
        opcodes.append(make_opcode(
                name = 'put%d' % i,
                params = [make_p('c', i, 'U')]
        ))

    # 137 put_rule
    opcodes.append(make_opcode(
            name = 'put_rule',
            params = [make_p('a', 4, 'S'), make_p('b', 4, 'S')]
    ))

    # 138 nop
    opcodes.append(make_opcode(
            name = 'nop'
    ))

    # 139 bop
    params = [make_p('c_%d' % i, 4, 'U') for i in range(10)]
    params.append(make_p('p', 4, 'S'))
    opcodes.append(make_opcode(
            name = 'bop',
            params = params
    ))

    # 140 eop
    opcodes.append(make_opcode(
            name = 'eop'
    ))

    # 141 push
    opcodes.append(make_opcode(
            name = 'push'
    ))

    # 142 pop
    opcodes.append(make_opcode(
            name = 'pop'
    ))

    # 143-146 right[i]
    for i in [1, 2, 3, 4]:
        opcodes.append(make_opcode(
                name = 'right%d' % i,
                params = [make_p('b', i, 'S')]
        ))

    # 147 w0
    opcodes.append(make_opcode(
            name = 'w0'
    ))

    assert len(opcodes) == 148

    # 148-151 w[i]
    for i in [1, 2, 3, 4]:
        opcodes.append(make_opcode(
                name = 'w%d' % i,
                params = [make_p('b', i, 'S')]
        ))

    # 152 x0
    opcodes.append(make_opcode(
            name = 'x0'
    ))

    # 153-156 x[i]
    for i in [1, 2, 3, 4]:
        opcodes.append(make_opcode(
                name = 'x%d' % i,
                params = [make_p('b', i, 'S')]
        ))

    # 157-160 down[i]
    for i in [1, 2, 3, 4]:
        opcodes.append(make_opcode(
                name = 'down%d' % i,
                params = [make_p('a', i, 'S')]
        ))

    # 161 y0
    opcodes.append(make_opcode(
            name = 'y0'
    ))

    # 162-165 y[i]
    for i in [1, 2, 3, 4]:
        opcodes.append(make_opcode(
                name = 'y%d' % i,
                params = [make_p('a', i, 'S')]
        ))

    # 166 z0
    opcodes.append(make_opcode(
            name = 'z0'
    ))

    # 167-170 z[i]
    for i in [1, 2, 3, 4]:
        opcodes.append(make_opcode(
                name = 'z%d' % i,
                params = [make_p('a', i, 'S')]
        ))

    # 171-234 fnt_num_[i]
    for i in range(64):
        opcodes.append(make_opcode(
                name = 'fnt_num_%d' % i
        ))

    # 235-238 fnt[i]
    for i in [1, 2, 3, 4]:
        opcodes.append(make_opcode(
                name = 'fnt%d' % i,
                params = [make_p('k', i, 'U')]
        ))

    # 239-242 xxx[i]
    for i in [1, 2, 3, 4]:
        opcodes.append(make_opcode(
                name = 'xxx%d' % i,
                params = [make_p('k', i, 'U'), make_p('x', [0], 'str')]
        ))

    # 243-246 fnt_def[i]
    for i in [1, 2, 3, 4]:
        params = [
                make_p('k', i, 'U'),
                make_p('c', 4, 'U'),
                make_p('s', 4, 'U'),
                make_p('d', 4, 'U'),
                make_p('a', 1, 'U'),
                make_p('l', 1, 'U'),
                make_p('n', [4, 5], 'str')
        ]
        opcodes.append(make_opcode(
                name = 'fnt_def%d' % i,
                params = params
        ))

    assert len(opcodes) == 247

    # 247 pre
    params = [
            make_p('i',   1, 'U'),
            make_p('num', 4, 'U'),
            make_p('den', 4, 'U'),
            make_p('mag', 4, 'U'),
            make_p('k',   1, 'U'),
            make_p('x',   [4], 'str')
    ]
    opcodes.append(make_opcode(
            name = 'pre',
            params = params
    ))

    # 248 post
    params = [
            make_p('p',   4, 'U'),
            make_p('num', 4, 'U'),
            make_p('den', 4, 'U'),
            make_p('mag', 4, 'U'),
            make_p('l',   4, 'U'),
            make_p('u',   4, 'U'),
            make_p('s',   2, 'U'),
            make_p('t',   2, 'U')
    ]
    opcodes.append(make_opcode(
            name = 'post',
            params = params
    ))

    # 249 post_post
    opcodes.append(make_opcode(
            name = 'post_post',
            params = [make_p('q', 4, 'U'), make_p('i', 1, 'U')]
    ))

    assert len(opcodes) == 250

    for i in range(len(opcodes), 256):
        opcodes.append(make_opcode(name = 'undefined'))

def get_val_len(param, vals):

    type_ = param['type']

    if type(param['len']) is int:
        return param['len'], type_
    
    # Otherwise we have a list of indexes into `vals` to be added.
    val_len = 0
    for idx in param['len']:
        val_len += vals[idx]

    return val_len, type_

def read_val(f, val_len, val_type):

    seq = f.read(val_len)

    if val_type is 'str':
        return seq

    if val_type is 'U':
        return int.from_bytes(seq, 'big', signed=False)

    if val_type is 'S':
        return int.from_bytes(seq, 'big', signed=True)

    assert False

def get_val_str(param, val):
    if param['type'] is 'str':
        val_s = val.decode('utf-8')
    else:
        val_s = '%d' % val
    return '%3s   %s' % (param['name'], val_s)

def print_next_opcode(f):

    global opcodes

    opbyte = f.read(1)
    if len(opbyte) == 0:
        return False  # Treat this as end-of-file.

    opcode = ord(opbyte)
    op = opcodes[opcode]
    name, comment, params = op['name'], op['comment'], op['params']
    
    print('%03d   %12s   %s' % (opcode, name, comment))

    vals = []
    for param in params:
        val_len, val_type = get_val_len(param, vals)
        vals.append(read_val(f, val_len, val_type))
        print(' ' * 21 + get_val_str(param, vals[-1]))

    # After key opcodes, we print out a clear visual separator.
    if name in ['eop', 'pre']:
        print('\n' + '_' * 70 + '\n')

    if name == 'post_post':
        opcodes[223] = make_opcode(name='final_pad')

    return True  # True indicates success (not end-of-file).

def dump_file(dvifile):

    init_opcodes()

    with open(dvifile, 'rb') as f:
        while True:
            did_read = print_next_opcode(f)
            if not did_read:
                break
        

# ______________________________________________________________________________
# Main

if __name__ == '__main__':

    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(0)

    dump_file(sys.argv[1])
