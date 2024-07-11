
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND APOSTROPHE ASSIGN BREAK CASE CLASS COLON COMMA CONST DAPOSTROPHE DECREMENT DEF DIVIDE DO DOT ELSE ELSIF END EQUAL FALSE FOR GETS GLOBAL_VAR GREATEROREQUAL GREATERTHAN ID IF IN INCREMENT INSTANCE_VAR LBRACE LBRACKET LESSOREQUAL LESSTHAN LPAREN MINUS MOD NIL NONE NOT NOTEQUAL NUMBER OR P PLUS PRINT PUTS RBRACE RBRACKET RETURN RPAREN SEMICOLON STRING TIMES TRUE WHEN WHILEcodigo : statement\n              | codigo statementstatement : assign\n              | impression\n              | tupla\n              | conditions\n              | while_loop\n              | case\n              | Sfunction\n              | array\n              | p_SfunctionINV\n              | p_function_one_parameter\n              | p_function_two_parameter\n              | function_call\n              | aritmeticExpresion\n              | operator\n              | dataIn\n              | control_structures\n              | hashvalue : NUMBER\n             | STRING\n             | INSTANCE_VAR\n             | GLOBAL_VAR\n             | IDvalues : value\n              | value COMMA valuesassign : INSTANCE_VAR ASSIGN value\n              | GLOBAL_VAR ASSIGN value\n              | ID ASSIGN value\n              | INSTANCE_VAR ASSIGN data_structure\n              | GLOBAL_VAR ASSIGN data_structure\n              | ID ASSIGN data_structure\n              aritmeticExpresion : value operator value\n                          | aritmeticExpresion operator valueoperator : PLUS\n                | MINUS\n                | TIMES\n                | DIVIDE\n                | MOD\n                | INCREMENT\n                | DECREMENT\n                | LPAREN aritmeticExpresion RPARENdata_structure : array\n                      | tupla\n                      | hasharray : LBRACKET RBRACKETarray : LBRACKET values RBRACKEThash : LBRACE RBRACEhash : LBRACE hash_contents RBRACEhash_contents : hash_pair\n                     | hash_contents COMMA hash_pairhash_pair : value COLON valueconditions : condition\n                  | condition conector conditionscondition : value operComp value\n                 | value operComp aritmeticExpresion conector : AND\n                | ORoperComp : LESSTHAN\n                | GREATERTHAN\n                | GREATEROREQUAL\n                | LESSOREQUAL\n                | EQUAL\n                | NOTEQUALcontrol_structures : if_block\n                          | if_block elsif_blocks\n                          | if_block elsif_blocks else_block\n                          | if_block else_blockif_block : IF LPAREN conditions RPAREN codigo\n                | IF LPAREN conditions RPAREN codigo ENDelsif_blocks : elsif_block\n                    | elsif_blocks elsif_blockelsif_block : ELSIF LPAREN conditions RPAREN codigoelse_block : ELSE codigo ENDwhen : WHEN conditions codigowhens : when\n             | whens whencase : CASE whens ENDSfunction : DEF ID LPAREN RPAREN codigo ENDp_SfunctionINV : ID\n                      | ID LPAREN params RPARENp_function_one_parameter : DEF ID LPAREN param RPAREN codigo ENDp_function_two_parameter : DEF ID LPAREN params RPAREN codigo ENDparam : valueparams : value COMMA valuefunction_call : ID LPAREN RPAREN\n                     | ID LPAREN params RPAREN\n                     | ID LPAREN param RPARENimpression : PRINT LPAREN value RPAREN\n                  | PRINT value\n                  | PUTS value\n                  | PUTS LPAREN value RPAREN\n                  | P LPAREN value RPAREN\n                  | P valuedataIn : ID ASSIGN GETS\n              | INSTANCE_VAR ASSIGN GETS\n              | GLOBAL_VAR ASSIGN GETSwhile_loop : WHILE LPAREN conditions RPAREN codigo ENDtupla : LPAREN values RPAREN'
    
_lr_action_items = {'INSTANCE_VAR':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,23,24,25,26,27,28,32,33,34,35,36,37,38,39,40,41,42,43,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,68,69,70,71,72,73,74,75,78,80,83,84,85,86,88,92,93,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,112,116,117,118,121,124,126,127,128,129,130,131,132,133,134,135,137,138,139,140,142,143,144,145,146,150,154,156,157,158,159,160,161,162,163,164,165,166,167,168,169,],[20,20,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-80,62,62,62,62,-53,62,-35,-36,-37,-38,-39,-40,-41,-65,62,-20,-21,-2,62,62,62,62,62,-59,-60,-61,-62,-63,-64,62,62,62,62,-90,-22,-23,-24,-91,62,62,-94,62,-57,-58,62,62,-46,-66,-68,-71,20,-48,62,-34,-27,-30,-96,-43,-44,-45,62,-33,-55,-56,-28,-31,-97,-29,-32,-95,-86,-99,-42,62,-54,-78,20,62,-47,-67,-72,20,62,-49,62,62,-81,-88,62,-89,-92,-93,20,20,20,-74,20,20,20,20,20,20,20,-98,-79,20,20,20,-70,-82,-83,]),'GLOBAL_VAR':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,23,24,25,26,27,28,32,33,34,35,36,37,38,39,40,41,42,43,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,68,69,70,71,72,73,74,75,78,80,83,84,85,86,88,92,93,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,112,116,117,118,121,124,126,127,128,129,130,131,132,133,134,135,137,138,139,140,142,143,144,145,146,150,154,156,157,158,159,160,161,162,163,164,165,166,167,168,169,],[22,22,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-80,63,63,63,63,-53,63,-35,-36,-37,-38,-39,-40,-41,-65,63,-20,-21,-2,63,63,63,63,63,-59,-60,-61,-62,-63,-64,63,63,63,63,-90,-22,-23,-24,-91,63,63,-94,63,-57,-58,63,63,-46,-66,-68,-71,22,-48,63,-34,-27,-30,-96,-43,-44,-45,63,-33,-55,-56,-28,-31,-97,-29,-32,-95,-86,-99,-42,63,-54,-78,22,63,-47,-67,-72,22,63,-49,63,63,-81,-88,63,-89,-92,-93,22,22,22,-74,22,22,22,22,22,22,22,-98,-79,22,22,22,-70,-82,-83,]),'ID':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,23,24,25,26,27,28,31,32,33,34,35,36,37,38,39,40,41,42,43,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,68,69,70,71,72,73,74,75,78,80,83,84,85,86,88,92,93,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,112,116,117,118,121,124,126,127,128,129,130,131,132,133,134,135,137,138,139,140,142,143,144,145,146,150,154,156,157,158,159,160,161,162,163,164,165,166,167,168,169,],[23,23,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-80,64,64,64,64,-53,79,64,-35,-36,-37,-38,-39,-40,-41,-65,64,-20,-21,-2,64,64,64,64,64,-59,-60,-61,-62,-63,-64,64,64,64,64,-90,-22,-23,-24,-91,64,64,-94,64,-57,-58,64,64,-46,-66,-68,-71,23,-48,64,-34,-27,-30,-96,-43,-44,-45,64,-33,-55,-56,-28,-31,-97,-29,-32,-95,-86,-99,-42,64,-54,-78,23,64,-47,-67,-72,23,64,-49,64,64,-81,-88,64,-89,-92,-93,23,23,23,-74,23,23,23,23,23,23,23,-98,-79,23,23,23,-70,-82,-83,]),'PRINT':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,23,28,33,34,35,36,37,38,39,40,42,43,45,61,62,63,64,68,71,80,83,84,85,86,88,93,95,96,97,98,99,100,102,103,104,105,106,107,108,109,110,112,116,117,121,124,126,128,129,130,131,133,137,138,140,142,143,144,145,146,150,154,156,157,158,159,160,161,162,163,164,165,166,167,168,169,],[24,24,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-80,-53,-35,-36,-37,-38,-39,-40,-41,-65,-20,-21,-2,-90,-22,-23,-24,-91,-94,-46,-66,-68,-71,24,-48,-34,-27,-30,-96,-43,-44,-45,-33,-55,-56,-28,-31,-97,-29,-32,-95,-86,-99,-42,-54,-78,24,-47,-67,-72,24,-49,-81,-88,-89,-92,-93,24,24,24,-74,24,24,24,24,24,24,24,-98,-79,24,24,24,-70,-82,-83,]),'PUTS':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,23,28,33,34,35,36,37,38,39,40,42,43,45,61,62,63,64,68,71,80,83,84,85,86,88,93,95,96,97,98,99,100,102,103,104,105,106,107,108,109,110,112,116,117,121,124,126,128,129,130,131,133,137,138,140,142,143,144,145,146,150,154,156,157,158,159,160,161,162,163,164,165,166,167,168,169,],[26,26,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-80,-53,-35,-36,-37,-38,-39,-40,-41,-65,-20,-21,-2,-90,-22,-23,-24,-91,-94,-46,-66,-68,-71,26,-48,-34,-27,-30,-96,-43,-44,-45,-33,-55,-56,-28,-31,-97,-29,-32,-95,-86,-99,-42,-54,-78,26,-47,-67,-72,26,-49,-81,-88,-89,-92,-93,26,26,26,-74,26,26,26,26,26,26,26,-98,-79,26,26,26,-70,-82,-83,]),'P':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,23,28,33,34,35,36,37,38,39,40,42,43,45,61,62,63,64,68,71,80,83,84,85,86,88,93,95,96,97,98,99,100,102,103,104,105,106,107,108,109,110,112,116,117,121,124,126,128,129,130,131,133,137,138,140,142,143,144,145,146,150,154,156,157,158,159,160,161,162,163,164,165,166,167,168,169,],[27,27,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-80,-53,-35,-36,-37,-38,-39,-40,-41,-65,-20,-21,-2,-90,-22,-23,-24,-91,-94,-46,-66,-68,-71,27,-48,-34,-27,-30,-96,-43,-44,-45,-33,-55,-56,-28,-31,-97,-29,-32,-95,-86,-99,-42,-54,-78,27,-47,-67,-72,27,-49,-81,-88,-89,-92,-93,27,27,27,-74,27,27,27,27,27,27,27,-98,-79,27,27,27,-70,-82,-83,]),'LPAREN':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,26,27,28,29,33,34,35,36,37,38,39,40,42,43,44,45,48,57,58,61,62,63,64,66,67,68,71,79,80,83,84,85,86,87,88,93,94,95,96,97,98,99,100,102,103,104,105,106,107,108,109,110,112,116,117,121,124,126,128,129,130,131,133,137,138,140,142,143,144,145,146,150,154,156,157,158,159,160,161,162,163,164,165,166,167,168,169,],[25,25,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,47,-16,-17,-18,-19,-22,47,-23,59,60,69,70,-53,75,-35,-36,-37,-38,-39,-40,-41,-65,-20,-21,92,-2,101,101,101,-90,-22,-23,-24,47,47,-91,-94,127,-46,-66,-68,-71,25,132,-48,-34,47,-27,-30,-96,-43,-44,-45,-33,47,47,-28,-31,-97,-29,-32,-95,-86,-99,-42,-54,-78,25,-47,-67,-72,25,-49,-81,-88,-89,-92,-93,25,25,25,-74,25,25,25,25,25,25,25,-98,-79,25,25,25,-70,-82,-83,]),'WHILE':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,23,28,33,34,35,36,37,38,39,40,42,43,45,61,62,63,64,68,71,80,83,84,85,86,88,93,95,96,97,98,99,100,102,103,104,105,106,107,108,109,110,112,116,117,121,124,126,128,129,130,131,133,137,138,140,142,143,144,145,146,150,154,156,157,158,159,160,161,162,163,164,165,166,167,168,169,],[29,29,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-80,-53,-35,-36,-37,-38,-39,-40,-41,-65,-20,-21,-2,-90,-22,-23,-24,-91,-94,-46,-66,-68,-71,29,-48,-34,-27,-30,-96,-43,-44,-45,-33,-55,-56,-28,-31,-97,-29,-32,-95,-86,-99,-42,-54,-78,29,-47,-67,-72,29,-49,-81,-88,-89,-92,-93,29,29,29,-74,29,29,29,29,29,29,29,-98,-79,29,29,29,-70,-82,-83,]),'CASE':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,23,28,33,34,35,36,37,38,39,40,42,43,45,61,62,63,64,68,71,80,83,84,85,86,88,93,95,96,97,98,99,100,102,103,104,105,106,107,108,109,110,112,116,117,121,124,126,128,129,130,131,133,137,138,140,142,143,144,145,146,150,154,156,157,158,159,160,161,162,163,164,165,166,167,168,169,],[30,30,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-80,-53,-35,-36,-37,-38,-39,-40,-41,-65,-20,-21,-2,-90,-22,-23,-24,-91,-94,-46,-66,-68,-71,30,-48,-34,-27,-30,-96,-43,-44,-45,-33,-55,-56,-28,-31,-97,-29,-32,-95,-86,-99,-42,-54,-78,30,-47,-67,-72,30,-49,-81,-88,-89,-92,-93,30,30,30,-74,30,30,30,30,30,30,30,-98,-79,30,30,30,-70,-82,-83,]),'DEF':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,23,28,33,34,35,36,37,38,39,40,42,43,45,61,62,63,64,68,71,80,83,84,85,86,88,93,95,96,97,98,99,100,102,103,104,105,106,107,108,109,110,112,116,117,121,124,126,128,129,130,131,133,137,138,140,142,143,144,145,146,150,154,156,157,158,159,160,161,162,163,164,165,166,167,168,169,],[31,31,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-80,-53,-35,-36,-37,-38,-39,-40,-41,-65,-20,-21,-2,-90,-22,-23,-24,-91,-94,-46,-66,-68,-71,31,-48,-34,-27,-30,-96,-43,-44,-45,-33,-55,-56,-28,-31,-97,-29,-32,-95,-86,-99,-42,-54,-78,31,-47,-67,-72,31,-49,-81,-88,-89,-92,-93,31,31,31,-74,31,31,31,31,31,31,31,-98,-79,31,31,31,-70,-82,-83,]),'LBRACKET':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,23,28,33,34,35,36,37,38,39,40,42,43,45,48,57,58,61,62,63,64,68,71,80,83,84,85,86,88,93,95,96,97,98,99,100,102,103,104,105,106,107,108,109,110,112,116,117,121,124,126,128,129,130,131,133,137,138,140,142,143,144,145,146,150,154,156,157,158,159,160,161,162,163,164,165,166,167,168,169,],[32,32,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-80,-53,-35,-36,-37,-38,-39,-40,-41,-65,-20,-21,-2,32,32,32,-90,-22,-23,-24,-91,-94,-46,-66,-68,-71,32,-48,-34,-27,-30,-96,-43,-44,-45,-33,-55,-56,-28,-31,-97,-29,-32,-95,-86,-99,-42,-54,-78,32,-47,-67,-72,32,-49,-81,-88,-89,-92,-93,32,32,32,-74,32,32,32,32,32,32,32,-98,-79,32,32,32,-70,-82,-83,]),'PLUS':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,28,33,34,35,36,37,38,39,40,42,43,45,61,62,63,64,66,67,68,71,80,83,84,85,86,88,93,94,95,96,97,98,99,100,102,103,104,105,106,107,108,109,110,112,116,117,121,124,126,128,129,130,131,133,137,138,140,142,143,144,145,146,150,154,156,157,158,159,160,161,162,163,164,165,166,167,168,169,],[33,33,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,33,-16,-17,-18,-19,-22,33,-23,-24,-53,-35,-36,-37,-38,-39,-40,-41,-65,-20,-21,-2,-90,-22,-23,-24,33,33,-91,-94,-46,-66,-68,-71,33,-48,-34,33,-27,-30,-96,-43,-44,-45,-33,33,33,-28,-31,-97,-29,-32,-95,-86,-99,-42,-54,-78,33,-47,-67,-72,33,-49,-81,-88,-89,-92,-93,33,33,33,-74,33,33,33,33,33,33,33,-98,-79,33,33,33,-70,-82,-83,]),'MINUS':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,28,33,34,35,36,37,38,39,40,42,43,45,61,62,63,64,66,67,68,71,80,83,84,85,86,88,93,94,95,96,97,98,99,100,102,103,104,105,106,107,108,109,110,112,116,117,121,124,126,128,129,130,131,133,137,138,140,142,143,144,145,146,150,154,156,157,158,159,160,161,162,163,164,165,166,167,168,169,],[34,34,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,34,-16,-17,-18,-19,-22,34,-23,-24,-53,-35,-36,-37,-38,-39,-40,-41,-65,-20,-21,-2,-90,-22,-23,-24,34,34,-91,-94,-46,-66,-68,-71,34,-48,-34,34,-27,-30,-96,-43,-44,-45,-33,34,34,-28,-31,-97,-29,-32,-95,-86,-99,-42,-54,-78,34,-47,-67,-72,34,-49,-81,-88,-89,-92,-93,34,34,34,-74,34,34,34,34,34,34,34,-98,-79,34,34,34,-70,-82,-83,]),'TIMES':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,28,33,34,35,36,37,38,39,40,42,43,45,61,62,63,64,66,67,68,71,80,83,84,85,86,88,93,94,95,96,97,98,99,100,102,103,104,105,106,107,108,109,110,112,116,117,121,124,126,128,129,130,131,133,137,138,140,142,143,144,145,146,150,154,156,157,158,159,160,161,162,163,164,165,166,167,168,169,],[35,35,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,35,-16,-17,-18,-19,-22,35,-23,-24,-53,-35,-36,-37,-38,-39,-40,-41,-65,-20,-21,-2,-90,-22,-23,-24,35,35,-91,-94,-46,-66,-68,-71,35,-48,-34,35,-27,-30,-96,-43,-44,-45,-33,35,35,-28,-31,-97,-29,-32,-95,-86,-99,-42,-54,-78,35,-47,-67,-72,35,-49,-81,-88,-89,-92,-93,35,35,35,-74,35,35,35,35,35,35,35,-98,-79,35,35,35,-70,-82,-83,]),'DIVIDE':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,28,33,34,35,36,37,38,39,40,42,43,45,61,62,63,64,66,67,68,71,80,83,84,85,86,88,93,94,95,96,97,98,99,100,102,103,104,105,106,107,108,109,110,112,116,117,121,124,126,128,129,130,131,133,137,138,140,142,143,144,145,146,150,154,156,157,158,159,160,161,162,163,164,165,166,167,168,169,],[36,36,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,36,-16,-17,-18,-19,-22,36,-23,-24,-53,-35,-36,-37,-38,-39,-40,-41,-65,-20,-21,-2,-90,-22,-23,-24,36,36,-91,-94,-46,-66,-68,-71,36,-48,-34,36,-27,-30,-96,-43,-44,-45,-33,36,36,-28,-31,-97,-29,-32,-95,-86,-99,-42,-54,-78,36,-47,-67,-72,36,-49,-81,-88,-89,-92,-93,36,36,36,-74,36,36,36,36,36,36,36,-98,-79,36,36,36,-70,-82,-83,]),'MOD':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,28,33,34,35,36,37,38,39,40,42,43,45,61,62,63,64,66,67,68,71,80,83,84,85,86,88,93,94,95,96,97,98,99,100,102,103,104,105,106,107,108,109,110,112,116,117,121,124,126,128,129,130,131,133,137,138,140,142,143,144,145,146,150,154,156,157,158,159,160,161,162,163,164,165,166,167,168,169,],[37,37,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,37,-16,-17,-18,-19,-22,37,-23,-24,-53,-35,-36,-37,-38,-39,-40,-41,-65,-20,-21,-2,-90,-22,-23,-24,37,37,-91,-94,-46,-66,-68,-71,37,-48,-34,37,-27,-30,-96,-43,-44,-45,-33,37,37,-28,-31,-97,-29,-32,-95,-86,-99,-42,-54,-78,37,-47,-67,-72,37,-49,-81,-88,-89,-92,-93,37,37,37,-74,37,37,37,37,37,37,37,-98,-79,37,37,37,-70,-82,-83,]),'INCREMENT':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,28,33,34,35,36,37,38,39,40,42,43,45,61,62,63,64,66,67,68,71,80,83,84,85,86,88,93,94,95,96,97,98,99,100,102,103,104,105,106,107,108,109,110,112,116,117,121,124,126,128,129,130,131,133,137,138,140,142,143,144,145,146,150,154,156,157,158,159,160,161,162,163,164,165,166,167,168,169,],[38,38,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,38,-16,-17,-18,-19,-22,38,-23,-24,-53,-35,-36,-37,-38,-39,-40,-41,-65,-20,-21,-2,-90,-22,-23,-24,38,38,-91,-94,-46,-66,-68,-71,38,-48,-34,38,-27,-30,-96,-43,-44,-45,-33,38,38,-28,-31,-97,-29,-32,-95,-86,-99,-42,-54,-78,38,-47,-67,-72,38,-49,-81,-88,-89,-92,-93,38,38,38,-74,38,38,38,38,38,38,38,-98,-79,38,38,38,-70,-82,-83,]),'DECREMENT':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,28,33,34,35,36,37,38,39,40,42,43,45,61,62,63,64,66,67,68,71,80,83,84,85,86,88,93,94,95,96,97,98,99,100,102,103,104,105,106,107,108,109,110,112,116,117,121,124,126,128,129,130,131,133,137,138,140,142,143,144,145,146,150,154,156,157,158,159,160,161,162,163,164,165,166,167,168,169,],[39,39,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,39,-16,-17,-18,-19,-22,39,-23,-24,-53,-35,-36,-37,-38,-39,-40,-41,-65,-20,-21,-2,-90,-22,-23,-24,39,39,-91,-94,-46,-66,-68,-71,39,-48,-34,39,-27,-30,-96,-43,-44,-45,-33,39,39,-28,-31,-97,-29,-32,-95,-86,-99,-42,-54,-78,39,-47,-67,-72,39,-49,-81,-88,-89,-92,-93,39,39,39,-74,39,39,39,39,39,39,39,-98,-79,39,39,39,-70,-82,-83,]),'LBRACE':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,23,28,33,34,35,36,37,38,39,40,42,43,45,48,57,58,61,62,63,64,68,71,80,83,84,85,86,88,93,95,96,97,98,99,100,102,103,104,105,106,107,108,109,110,112,116,117,121,124,126,128,129,130,131,133,137,138,140,142,143,144,145,146,150,154,156,157,158,159,160,161,162,163,164,165,166,167,168,169,],[41,41,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-80,-53,-35,-36,-37,-38,-39,-40,-41,-65,-20,-21,-2,41,41,41,-90,-22,-23,-24,-91,-94,-46,-66,-68,-71,41,-48,-34,-27,-30,-96,-43,-44,-45,-33,-55,-56,-28,-31,-97,-29,-32,-95,-86,-99,-42,-54,-78,41,-47,-67,-72,41,-49,-81,-88,-89,-92,-93,41,41,41,-74,41,41,41,41,41,41,41,-98,-79,41,41,41,-70,-82,-83,]),'NUMBER':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,23,24,25,26,27,28,32,33,34,35,36,37,38,39,40,41,42,43,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,68,69,70,71,72,73,74,75,78,80,83,84,85,86,88,92,93,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,112,116,117,118,121,124,126,127,128,129,130,131,132,133,134,135,137,138,139,140,142,143,144,145,146,150,154,156,157,158,159,160,161,162,163,164,165,166,167,168,169,],[42,42,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-80,42,42,42,42,-53,42,-35,-36,-37,-38,-39,-40,-41,-65,42,-20,-21,-2,42,42,42,42,42,-59,-60,-61,-62,-63,-64,42,42,42,42,-90,-22,-23,-24,-91,42,42,-94,42,-57,-58,42,42,-46,-66,-68,-71,42,-48,42,-34,-27,-30,-96,-43,-44,-45,42,-33,-55,-56,-28,-31,-97,-29,-32,-95,-86,-99,-42,42,-54,-78,42,42,-47,-67,-72,42,42,-49,42,42,-81,-88,42,-89,-92,-93,42,42,42,-74,42,42,42,42,42,42,42,-98,-79,42,42,42,-70,-82,-83,]),'STRING':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,23,24,25,26,27,28,32,33,34,35,36,37,38,39,40,41,42,43,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,68,69,70,71,72,73,74,75,78,80,83,84,85,86,88,92,93,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,112,116,117,118,121,124,126,127,128,129,130,131,132,133,134,135,137,138,139,140,142,143,144,145,146,150,154,156,157,158,159,160,161,162,163,164,165,166,167,168,169,],[43,43,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-80,43,43,43,43,-53,43,-35,-36,-37,-38,-39,-40,-41,-65,43,-20,-21,-2,43,43,43,43,43,-59,-60,-61,-62,-63,-64,43,43,43,43,-90,-22,-23,-24,-91,43,43,-94,43,-57,-58,43,43,-46,-66,-68,-71,43,-48,43,-34,-27,-30,-96,-43,-44,-45,43,-33,-55,-56,-28,-31,-97,-29,-32,-95,-86,-99,-42,43,-54,-78,43,43,-47,-67,-72,43,43,-49,43,43,-81,-88,43,-89,-92,-93,43,43,43,-74,43,43,43,43,43,43,43,-98,-79,43,43,43,-70,-82,-83,]),'IF':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,23,28,33,34,35,36,37,38,39,40,42,43,45,61,62,63,64,68,71,80,83,84,85,86,88,93,95,96,97,98,99,100,102,103,104,105,106,107,108,109,110,112,116,117,121,124,126,128,129,130,131,133,137,138,140,142,143,144,145,146,150,154,156,157,158,159,160,161,162,163,164,165,166,167,168,169,],[44,44,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-80,-53,-35,-36,-37,-38,-39,-40,-41,-65,-20,-21,-2,-90,-22,-23,-24,-91,-94,-46,-66,-68,-71,44,-48,-34,-27,-30,-96,-43,-44,-45,-33,-55,-56,-28,-31,-97,-29,-32,-95,-86,-99,-42,-54,-78,44,-47,-67,-72,44,-49,-81,-88,-89,-92,-93,44,44,44,-74,44,44,44,44,44,44,44,-98,-79,44,44,44,-70,-82,-83,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,23,28,33,34,35,36,37,38,39,40,42,43,45,61,62,63,64,68,71,80,83,84,85,88,93,95,96,97,98,99,100,102,103,104,105,106,107,108,109,110,112,116,117,121,124,128,129,130,133,137,138,140,142,143,150,161,162,163,166,167,168,169,],[0,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-80,-53,-35,-36,-37,-38,-39,-40,-41,-65,-20,-21,-2,-90,-22,-23,-24,-91,-94,-46,-66,-68,-71,-48,-34,-27,-30,-96,-43,-44,-45,-33,-55,-56,-28,-31,-97,-29,-32,-95,-86,-99,-42,-54,-78,-47,-67,-72,-49,-81,-88,-89,-92,-93,-74,-69,-98,-79,-73,-70,-82,-83,]),'END':([2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,23,28,33,34,35,36,37,38,39,40,42,43,45,61,62,63,64,68,71,76,77,80,83,84,85,88,93,95,96,97,98,99,100,102,103,104,105,106,107,108,109,110,112,116,117,121,124,125,128,129,130,131,133,137,138,140,142,143,145,150,156,157,161,162,163,164,165,166,167,168,169,],[-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-80,-53,-35,-36,-37,-38,-39,-40,-41,-65,-20,-21,-2,-90,-22,-23,-24,-91,-94,124,-76,-46,-66,-68,-71,-48,-34,-27,-30,-96,-43,-44,-45,-33,-55,-56,-28,-31,-97,-29,-32,-95,-86,-99,-42,-54,-78,-77,-47,-67,-72,150,-49,-81,-88,-89,-92,-93,-75,-74,162,163,167,-98,-79,168,169,-73,-70,-82,-83,]),'WHEN':([2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,23,28,30,33,34,35,36,37,38,39,40,42,43,45,61,62,63,64,68,71,76,77,80,83,84,85,88,93,95,96,97,98,99,100,102,103,104,105,106,107,108,109,110,112,116,117,121,124,125,128,129,130,133,137,138,140,142,143,145,150,161,162,163,166,167,168,169,],[-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-80,-53,78,-35,-36,-37,-38,-39,-40,-41,-65,-20,-21,-2,-90,-22,-23,-24,-91,-94,78,-76,-46,-66,-68,-71,-48,-34,-27,-30,-96,-43,-44,-45,-33,-55,-56,-28,-31,-97,-29,-32,-95,-86,-99,-42,-54,-78,-77,-47,-67,-72,-49,-81,-88,-89,-92,-93,-75,-74,-69,-98,-79,-73,-70,-82,-83,]),'ELSE':([2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,23,28,33,34,35,36,37,38,39,40,42,43,45,61,62,63,64,68,71,80,83,84,85,88,93,95,96,97,98,99,100,102,103,104,105,106,107,108,109,110,112,116,117,121,124,128,129,130,133,137,138,140,142,143,150,161,162,163,166,167,168,169,],[-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-80,-53,-35,-36,-37,-38,-39,-40,-41,86,-20,-21,-2,-90,-22,-23,-24,-91,-94,-46,86,-68,-71,-48,-34,-27,-30,-96,-43,-44,-45,-33,-55,-56,-28,-31,-97,-29,-32,-95,-86,-99,-42,-54,-78,-47,-67,-72,-49,-81,-88,-89,-92,-93,-74,-69,-98,-79,-73,-70,-82,-83,]),'ELSIF':([2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,23,28,33,34,35,36,37,38,39,40,42,43,45,61,62,63,64,68,71,80,83,84,85,88,93,95,96,97,98,99,100,102,103,104,105,106,107,108,109,110,112,116,117,121,124,128,129,130,133,137,138,140,142,143,150,161,162,163,166,167,168,169,],[-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-80,-53,-35,-36,-37,-38,-39,-40,-41,87,-20,-21,-2,-90,-22,-23,-24,-91,-94,-46,87,-68,-71,-48,-34,-27,-30,-96,-43,-44,-45,-33,-55,-56,-28,-31,-97,-29,-32,-95,-86,-99,-42,-54,-78,-47,-67,-72,-49,-81,-88,-89,-92,-93,-74,-69,-98,-79,-73,-70,-82,-83,]),'ASSIGN':([20,22,23,],[48,57,58,]),'LESSTHAN':([20,21,22,23,42,43,62,63,64,122,],[-22,51,-23,-24,-20,-21,-22,-23,-24,51,]),'GREATERTHAN':([20,21,22,23,42,43,62,63,64,122,],[-22,52,-23,-24,-20,-21,-22,-23,-24,52,]),'GREATEROREQUAL':([20,21,22,23,42,43,62,63,64,122,],[-22,53,-23,-24,-20,-21,-22,-23,-24,53,]),'LESSOREQUAL':([20,21,22,23,42,43,62,63,64,122,],[-22,54,-23,-24,-20,-21,-22,-23,-24,54,]),'EQUAL':([20,21,22,23,42,43,62,63,64,122,],[-22,55,-23,-24,-20,-21,-22,-23,-24,55,]),'NOTEQUAL':([20,21,22,23,42,43,62,63,64,122,],[-22,56,-23,-24,-20,-21,-22,-23,-24,56,]),'RPAREN':([28,42,43,59,62,63,64,65,66,67,82,93,102,103,104,111,113,114,115,119,120,121,123,127,136,141,147,148,149,151,155,],[-53,-20,-21,112,-22,-23,-24,116,117,-25,-25,-34,-33,-55,-56,137,138,-84,140,142,143,-54,144,146,154,-26,158,159,-84,160,-85,]),'AND':([28,42,43,62,63,64,93,102,103,104,],[73,-20,-21,-22,-23,-24,-34,-33,-55,-56,]),'OR':([28,42,43,62,63,64,93,102,103,104,],[74,-20,-21,-22,-23,-24,-34,-33,-55,-56,]),'RBRACKET':([32,42,43,62,63,64,81,82,141,],[80,-20,-21,-22,-23,-24,128,-25,-26,]),'RBRACE':([41,42,43,62,63,64,89,90,152,153,],[88,-20,-21,-22,-23,-24,133,-50,-51,-52,]),'COMMA':([42,43,62,63,64,67,82,89,90,114,149,152,153,],[-20,-21,-22,-23,-24,118,118,134,-50,139,139,-51,-52,]),'COLON':([42,43,62,63,64,91,],[-20,-21,-22,-23,-24,135,]),'GETS':([48,57,58,],[97,107,110,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'codigo':([0,86,126,144,146,154,158,159,160,],[1,131,145,156,157,161,164,165,166,]),'statement':([0,1,86,126,131,144,145,146,154,156,157,158,159,160,161,164,165,166,],[2,45,2,2,45,2,45,2,2,45,45,2,2,2,45,45,45,45,]),'assign':([0,1,86,126,131,144,145,146,154,156,157,158,159,160,161,164,165,166,],[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,]),'impression':([0,1,86,126,131,144,145,146,154,156,157,158,159,160,161,164,165,166,],[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,]),'tupla':([0,1,48,57,58,86,126,131,144,145,146,154,156,157,158,159,160,161,164,165,166,],[5,5,99,99,99,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,]),'conditions':([0,1,72,75,78,86,92,126,131,132,144,145,146,154,156,157,158,159,160,161,164,165,166,],[6,6,121,123,126,6,136,6,6,151,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'while_loop':([0,1,86,126,131,144,145,146,154,156,157,158,159,160,161,164,165,166,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'case':([0,1,86,126,131,144,145,146,154,156,157,158,159,160,161,164,165,166,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'Sfunction':([0,1,86,126,131,144,145,146,154,156,157,158,159,160,161,164,165,166,],[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'array':([0,1,48,57,58,86,126,131,144,145,146,154,156,157,158,159,160,161,164,165,166,],[10,10,98,98,98,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'p_SfunctionINV':([0,1,86,126,131,144,145,146,154,156,157,158,159,160,161,164,165,166,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'p_function_one_parameter':([0,1,86,126,131,144,145,146,154,156,157,158,159,160,161,164,165,166,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'p_function_two_parameter':([0,1,86,126,131,144,145,146,154,156,157,158,159,160,161,164,165,166,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'function_call':([0,1,86,126,131,144,145,146,154,156,157,158,159,160,161,164,165,166,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'aritmeticExpresion':([0,1,25,47,50,86,126,131,144,145,146,154,156,157,158,159,160,161,164,165,166,],[15,15,66,66,104,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'operator':([0,1,15,21,66,67,86,94,103,104,126,131,144,145,146,154,156,157,158,159,160,161,164,165,166,],[16,16,46,49,46,49,16,49,49,46,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'dataIn':([0,1,86,126,131,144,145,146,154,156,157,158,159,160,161,164,165,166,],[17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'control_structures':([0,1,86,126,131,144,145,146,154,156,157,158,159,160,161,164,165,166,],[18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,]),'hash':([0,1,48,57,58,86,126,131,144,145,146,154,156,157,158,159,160,161,164,165,166,],[19,19,100,100,100,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,]),'value':([0,1,24,25,26,27,32,41,46,47,48,49,50,57,58,59,60,69,70,72,75,78,86,92,101,118,126,127,131,132,134,135,139,144,145,146,154,156,157,158,159,160,161,164,165,166,],[21,21,61,67,68,71,82,91,93,94,95,102,103,105,108,114,115,119,120,122,122,122,21,122,82,82,21,149,21,122,91,153,155,21,21,21,21,21,21,21,21,21,21,21,21,21,]),'condition':([0,1,72,75,78,86,92,126,131,132,144,145,146,154,156,157,158,159,160,161,164,165,166,],[28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'if_block':([0,1,86,126,131,144,145,146,154,156,157,158,159,160,161,164,165,166,],[40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,]),'operComp':([21,122,],[50,50,]),'values':([25,32,101,118,],[65,81,65,141,]),'conector':([28,],[72,]),'whens':([30,],[76,]),'when':([30,76,],[77,125,]),'elsif_blocks':([40,],[83,]),'else_block':([40,83,],[84,129,]),'elsif_block':([40,83,],[85,130,]),'hash_contents':([41,],[89,]),'hash_pair':([41,134,],[90,152,]),'data_structure':([48,57,58,],[96,106,109,]),'params':([59,127,],[111,148,]),'param':([59,127,],[113,147,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> codigo","S'",1,None,None,None),
  ('codigo -> statement','codigo',1,'p_codigo','analizador_sintactico.py',43),
  ('codigo -> codigo statement','codigo',2,'p_codigo','analizador_sintactico.py',44),
  ('statement -> assign','statement',1,'p_statement','analizador_sintactico.py',47),
  ('statement -> impression','statement',1,'p_statement','analizador_sintactico.py',48),
  ('statement -> tupla','statement',1,'p_statement','analizador_sintactico.py',49),
  ('statement -> conditions','statement',1,'p_statement','analizador_sintactico.py',50),
  ('statement -> while_loop','statement',1,'p_statement','analizador_sintactico.py',51),
  ('statement -> case','statement',1,'p_statement','analizador_sintactico.py',52),
  ('statement -> Sfunction','statement',1,'p_statement','analizador_sintactico.py',53),
  ('statement -> array','statement',1,'p_statement','analizador_sintactico.py',54),
  ('statement -> p_SfunctionINV','statement',1,'p_statement','analizador_sintactico.py',55),
  ('statement -> p_function_one_parameter','statement',1,'p_statement','analizador_sintactico.py',56),
  ('statement -> p_function_two_parameter','statement',1,'p_statement','analizador_sintactico.py',57),
  ('statement -> function_call','statement',1,'p_statement','analizador_sintactico.py',58),
  ('statement -> aritmeticExpresion','statement',1,'p_statement','analizador_sintactico.py',59),
  ('statement -> operator','statement',1,'p_statement','analizador_sintactico.py',60),
  ('statement -> dataIn','statement',1,'p_statement','analizador_sintactico.py',61),
  ('statement -> control_structures','statement',1,'p_statement','analizador_sintactico.py',62),
  ('statement -> hash','statement',1,'p_statement','analizador_sintactico.py',63),
  ('value -> NUMBER','value',1,'p_value','analizador_sintactico.py',66),
  ('value -> STRING','value',1,'p_value','analizador_sintactico.py',67),
  ('value -> INSTANCE_VAR','value',1,'p_value','analizador_sintactico.py',68),
  ('value -> GLOBAL_VAR','value',1,'p_value','analizador_sintactico.py',69),
  ('value -> ID','value',1,'p_value','analizador_sintactico.py',70),
  ('values -> value','values',1,'p_values','analizador_sintactico.py',77),
  ('values -> value COMMA values','values',3,'p_values','analizador_sintactico.py',78),
  ('assign -> INSTANCE_VAR ASSIGN value','assign',3,'p_assign','analizador_sintactico.py',88),
  ('assign -> GLOBAL_VAR ASSIGN value','assign',3,'p_assign','analizador_sintactico.py',89),
  ('assign -> ID ASSIGN value','assign',3,'p_assign','analizador_sintactico.py',90),
  ('assign -> INSTANCE_VAR ASSIGN data_structure','assign',3,'p_assign','analizador_sintactico.py',91),
  ('assign -> GLOBAL_VAR ASSIGN data_structure','assign',3,'p_assign','analizador_sintactico.py',92),
  ('assign -> ID ASSIGN data_structure','assign',3,'p_assign','analizador_sintactico.py',93),
  ('aritmeticExpresion -> value operator value','aritmeticExpresion',3,'p_aritmeticExpresion','analizador_sintactico.py',99),
  ('aritmeticExpresion -> aritmeticExpresion operator value','aritmeticExpresion',3,'p_aritmeticExpresion','analizador_sintactico.py',100),
  ('operator -> PLUS','operator',1,'p_operator','analizador_sintactico.py',120),
  ('operator -> MINUS','operator',1,'p_operator','analizador_sintactico.py',121),
  ('operator -> TIMES','operator',1,'p_operator','analizador_sintactico.py',122),
  ('operator -> DIVIDE','operator',1,'p_operator','analizador_sintactico.py',123),
  ('operator -> MOD','operator',1,'p_operator','analizador_sintactico.py',124),
  ('operator -> INCREMENT','operator',1,'p_operator','analizador_sintactico.py',125),
  ('operator -> DECREMENT','operator',1,'p_operator','analizador_sintactico.py',126),
  ('operator -> LPAREN aritmeticExpresion RPAREN','operator',3,'p_operator','analizador_sintactico.py',127),
  ('data_structure -> array','data_structure',1,'p_data_structure','analizador_sintactico.py',131),
  ('data_structure -> tupla','data_structure',1,'p_data_structure','analizador_sintactico.py',132),
  ('data_structure -> hash','data_structure',1,'p_data_structure','analizador_sintactico.py',133),
  ('array -> LBRACKET RBRACKET','array',2,'p_emptyarray','analizador_sintactico.py',137),
  ('array -> LBRACKET values RBRACKET','array',3,'p_array','analizador_sintactico.py',140),
  ('hash -> LBRACE RBRACE','hash',2,'p_empty_hash','analizador_sintactico.py',144),
  ('hash -> LBRACE hash_contents RBRACE','hash',3,'p_hash','analizador_sintactico.py',147),
  ('hash_contents -> hash_pair','hash_contents',1,'p_hash_contents','analizador_sintactico.py',150),
  ('hash_contents -> hash_contents COMMA hash_pair','hash_contents',3,'p_hash_contents','analizador_sintactico.py',151),
  ('hash_pair -> value COLON value','hash_pair',3,'p_hash_pair','analizador_sintactico.py',154),
  ('conditions -> condition','conditions',1,'p_conditions','analizador_sintactico.py',158),
  ('conditions -> condition conector conditions','conditions',3,'p_conditions','analizador_sintactico.py',159),
  ('condition -> value operComp value','condition',3,'p_condition','analizador_sintactico.py',162),
  ('condition -> value operComp aritmeticExpresion','condition',3,'p_condition','analizador_sintactico.py',163),
  ('conector -> AND','conector',1,'p_conector','analizador_sintactico.py',166),
  ('conector -> OR','conector',1,'p_conector','analizador_sintactico.py',167),
  ('operComp -> LESSTHAN','operComp',1,'p_operComp','analizador_sintactico.py',170),
  ('operComp -> GREATERTHAN','operComp',1,'p_operComp','analizador_sintactico.py',171),
  ('operComp -> GREATEROREQUAL','operComp',1,'p_operComp','analizador_sintactico.py',172),
  ('operComp -> LESSOREQUAL','operComp',1,'p_operComp','analizador_sintactico.py',173),
  ('operComp -> EQUAL','operComp',1,'p_operComp','analizador_sintactico.py',174),
  ('operComp -> NOTEQUAL','operComp',1,'p_operComp','analizador_sintactico.py',175),
  ('control_structures -> if_block','control_structures',1,'p_control_structures','analizador_sintactico.py',179),
  ('control_structures -> if_block elsif_blocks','control_structures',2,'p_control_structures','analizador_sintactico.py',180),
  ('control_structures -> if_block elsif_blocks else_block','control_structures',3,'p_control_structures','analizador_sintactico.py',181),
  ('control_structures -> if_block else_block','control_structures',2,'p_control_structures','analizador_sintactico.py',182),
  ('if_block -> IF LPAREN conditions RPAREN codigo','if_block',5,'p_if_block','analizador_sintactico.py',185),
  ('if_block -> IF LPAREN conditions RPAREN codigo END','if_block',6,'p_if_block','analizador_sintactico.py',186),
  ('elsif_blocks -> elsif_block','elsif_blocks',1,'p_elsif_blocks','analizador_sintactico.py',190),
  ('elsif_blocks -> elsif_blocks elsif_block','elsif_blocks',2,'p_elsif_blocks','analizador_sintactico.py',191),
  ('elsif_block -> ELSIF LPAREN conditions RPAREN codigo','elsif_block',5,'p_elsif_block','analizador_sintactico.py',194),
  ('else_block -> ELSE codigo END','else_block',3,'p_else_block','analizador_sintactico.py',197),
  ('when -> WHEN conditions codigo','when',3,'p_when','analizador_sintactico.py',201),
  ('whens -> when','whens',1,'p_whens','analizador_sintactico.py',205),
  ('whens -> whens when','whens',2,'p_whens','analizador_sintactico.py',206),
  ('case -> CASE whens END','case',3,'p_case','analizador_sintactico.py',209),
  ('Sfunction -> DEF ID LPAREN RPAREN codigo END','Sfunction',6,'p_Sfunction','analizador_sintactico.py',213),
  ('p_SfunctionINV -> ID','p_SfunctionINV',1,'p_SfunctionINV','analizador_sintactico.py',217),
  ('p_SfunctionINV -> ID LPAREN params RPAREN','p_SfunctionINV',4,'p_SfunctionINV','analizador_sintactico.py',218),
  ('p_function_one_parameter -> DEF ID LPAREN param RPAREN codigo END','p_function_one_parameter',7,'p_function_one_parameter','analizador_sintactico.py',226),
  ('p_function_two_parameter -> DEF ID LPAREN params RPAREN codigo END','p_function_two_parameter',7,'p_function_two_parameter','analizador_sintactico.py',230),
  ('param -> value','param',1,'p_param','analizador_sintactico.py',234),
  ('params -> value COMMA value','params',3,'p_params','analizador_sintactico.py',238),
  ('function_call -> ID LPAREN RPAREN','function_call',3,'p_function_call','analizador_sintactico.py',245),
  ('function_call -> ID LPAREN params RPAREN','function_call',4,'p_function_call','analizador_sintactico.py',246),
  ('function_call -> ID LPAREN param RPAREN','function_call',4,'p_function_call','analizador_sintactico.py',247),
  ('impression -> PRINT LPAREN value RPAREN','impression',4,'p_impression','analizador_sintactico.py',256),
  ('impression -> PRINT value','impression',2,'p_impression','analizador_sintactico.py',257),
  ('impression -> PUTS value','impression',2,'p_impression','analizador_sintactico.py',258),
  ('impression -> PUTS LPAREN value RPAREN','impression',4,'p_impression','analizador_sintactico.py',259),
  ('impression -> P LPAREN value RPAREN','impression',4,'p_impression','analizador_sintactico.py',260),
  ('impression -> P value','impression',2,'p_impression','analizador_sintactico.py',261),
  ('dataIn -> ID ASSIGN GETS','dataIn',3,'p_dataIn','analizador_sintactico.py',269),
  ('dataIn -> INSTANCE_VAR ASSIGN GETS','dataIn',3,'p_dataIn','analizador_sintactico.py',270),
  ('dataIn -> GLOBAL_VAR ASSIGN GETS','dataIn',3,'p_dataIn','analizador_sintactico.py',271),
  ('while_loop -> WHILE LPAREN conditions RPAREN codigo END','while_loop',6,'p_while_loop','analizador_sintactico.py',277),
  ('tupla -> LPAREN values RPAREN','tupla',3,'p_tupla','analizador_sintactico.py',283),
]
