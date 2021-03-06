
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'INITIALcorchete_C corchete_O letters num parentesis_C parentesis_O\n    INITIAL : corchete_O L_INTS corchete_C\n            | parentesis_O L_INTS parentesis_C\n            | L_INTS\n    \n    L_INTS : L_INTS INTS\n           | INTS\n    \n    INTS : num\n         | letters\n         | corchete_O L_INTS corchete_C\n         | parentesis_O L_INTS parentesis_C\n    '
    
_lr_action_items = {'corchete_O':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,],[2,8,8,8,-5,-6,-7,8,8,8,-4,8,8,-8,8,-9,-8,-9,]),'parentesis_O':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,],[4,10,10,10,-5,-6,-7,10,10,10,-4,10,10,-8,10,-9,-8,-9,]),'num':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,],[6,6,6,6,-5,-6,-7,6,6,6,-4,6,6,-8,6,-9,-8,-9,]),'letters':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,],[7,7,7,7,-5,-6,-7,7,7,7,-4,7,7,-8,7,-9,-8,-9,]),'$end':([1,3,5,6,7,11,14,16,17,18,],[0,-3,-5,-6,-7,-4,-1,-2,-8,-9,]),'corchete_C':([5,6,7,9,11,13,17,18,],[-5,-6,-7,14,-4,17,-8,-9,]),'parentesis_C':([5,6,7,11,12,15,17,18,],[-5,-6,-7,-4,16,18,-8,-9,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'INITIAL':([0,],[1,]),'L_INTS':([0,2,4,8,10,],[3,9,12,13,15,]),'INTS':([0,2,3,4,8,9,10,12,13,15,],[5,5,11,5,5,11,5,11,11,11,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> INITIAL","S'",1,None,None,None),
  ('INITIAL -> corchete_O L_INTS corchete_C','INITIAL',3,'p_INITIAL','analizador.py',61),
  ('INITIAL -> parentesis_O L_INTS parentesis_C','INITIAL',3,'p_INITIAL','analizador.py',62),
  ('INITIAL -> L_INTS','INITIAL',1,'p_INITIAL','analizador.py',63),
  ('L_INTS -> L_INTS INTS','L_INTS',2,'p_L_INTS','analizador.py',77),
  ('L_INTS -> INTS','L_INTS',1,'p_L_INTS','analizador.py',78),
  ('INTS -> num','INTS',1,'p_INTS','analizador.py',89),
  ('INTS -> letters','INTS',1,'p_INTS','analizador.py',90),
  ('INTS -> corchete_O L_INTS corchete_C','INTS',3,'p_INTS','analizador.py',91),
  ('INTS -> parentesis_O L_INTS parentesis_C','INTS',3,'p_INTS','analizador.py',92),
]
