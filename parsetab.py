
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND APOSTROPHE ASSIGN BREAK CASE CLASS COLON COMMA CONST DAPOSTROPHE DEF DIVIDE DO DOT ELSE ELSIF END EQUAL FALSE FOR GETS GLOBAL_VAR GREATEROREQUAL GREATERTHAN ID IF IN INSTANCE_VAR LBRACE LBRACKET LESSOREQUAL LESSTHAN LPAREN MINUS MOD NIL NONE NOT NOTEQUAL NUMBER OR P PLUS PRINT PUTS RBRACE RBRACKET RETURN RPAREN SEMICOLON STRING TIMES TRUE WHEN WHILEcodigo : statement\n              | codigo statementstatement : assign\n              | impression\n              | tupla\n              | conditions\n              | while_loop\n              | case\n              | Sfunction\n              | array\n              | p_SfunctionINV\n              | p_function_one_parameter\n              | p_function_two_parameter\n              | function_call\n              | aritmeticExpresion\n              | operator\n              | dataIn\n              | control_structures\n              | hashvalue : NUMBER\n             | STRING\n             | INSTANCE_VAR\n             | GLOBAL_VAR\n             | IDvalues : value\n              | value COMMA valuesassign : INSTANCE_VAR ASSIGN value\n              | GLOBAL_VAR ASSIGN value\n              | ID ASSIGN value\n              | INSTANCE_VAR ASSIGN data_structure\n              | GLOBAL_VAR ASSIGN data_structure\n              | ID ASSIGN data_structure\n              aritmeticExpresion : value operator value\n                          | aritmeticExpresion operator valueoperator : PLUS\n                | MINUS\n                | TIMES\n                | DIVIDE\n                | MOD\n                | LPAREN aritmeticExpresion RPARENdata_structure : array\n                      | tupla\n                      | hasharray : LBRACKET RBRACKETarray : LBRACKET values RBRACKEThash : LBRACE RBRACEhash : LBRACE hash_contents RBRACEhash_contents : hash_pair\n                     | hash_contents COMMA hash_pairhash_pair : value COLON valueconditions : condition\n                  | condition conector conditionscondition : value operComp value\n                 | value operComp aritmeticExpresion conector : AND\n                | ORoperComp : LESSTHAN\n                | GREATERTHAN\n                | GREATEROREQUAL\n                | LESSOREQUAL\n                | EQUAL\n                | NOTEQUALcontrol_structures : if_block\n                          | if_block elsif_blocks\n                          | if_block elsif_blocks else_block\n                          | if_block else_blockif_block : IF LPAREN conditions RPAREN codigo\n                | IF LPAREN conditions RPAREN codigo ENDelsif_blocks : elsif_block\n                    | elsif_blocks elsif_blockelsif_block : ELSIF LPAREN conditions RPAREN codigoelse_block : ELSE codigo ENDwhen : WHEN conditions codigowhens : when\n             | whens whencase : CASE whens ENDSfunction : DEF ID LPAREN RPAREN codigo ENDp_SfunctionINV : ID\n                      | ID LPAREN params RPARENp_function_one_parameter : DEF ID LPAREN param RPAREN codigo ENDp_function_two_parameter : DEF ID LPAREN params RPAREN codigo ENDparam : valueparams : value COMMA valuefunction_call : ID LPAREN RPAREN\n                     | ID LPAREN params RPAREN\n                     | ID LPAREN param RPARENimpression : PRINT LPAREN value RPAREN\n                  | PRINT value\n                  | PUTS value\n                  | PUTS LPAREN value RPAREN\n                  | P LPAREN value RPAREN\n                  | P valuedataIn : ID ASSIGN GETS\n              | INSTANCE_VAR ASSIGN GETS\n              | GLOBAL_VAR ASSIGN GETSwhile_loop : WHILE LPAREN conditions RPAREN codigo ENDtupla : LPAREN values RPAREN'
    
_lr_action_items = {'INSTANCE_VAR':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,23,24,25,26,27,28,32,33,34,35,36,37,38,39,40,41,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,66,67,68,69,70,71,72,73,76,78,81,82,83,84,86,90,91,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,110,114,115,116,119,122,124,125,126,127,128,129,130,131,132,133,135,136,137,138,140,141,142,143,144,148,152,154,155,156,157,158,159,160,161,162,163,164,165,166,167,],[20,20,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-78,60,60,60,60,-51,60,-35,-36,-37,-38,-39,-63,60,-20,-21,-2,60,60,60,60,60,-57,-58,-59,-60,-61,-62,60,60,60,60,-88,-22,-23,-24,-89,60,60,-92,60,-55,-56,60,60,-44,-64,-66,-69,20,-46,60,-34,-27,-30,-94,-41,-42,-43,60,-33,-53,-54,-28,-31,-95,-29,-32,-93,-84,-97,-40,60,-52,-76,20,60,-45,-65,-70,20,60,-47,60,60,-79,-86,60,-87,-90,-91,20,20,20,-72,20,20,20,20,20,20,20,-96,-77,20,20,20,-68,-80,-81,]),'GLOBAL_VAR':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,23,24,25,26,27,28,32,33,34,35,36,37,38,39,40,41,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,66,67,68,69,70,71,72,73,76,78,81,82,83,84,86,90,91,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,110,114,115,116,119,122,124,125,126,127,128,129,130,131,132,133,135,136,137,138,140,141,142,143,144,148,152,154,155,156,157,158,159,160,161,162,163,164,165,166,167,],[22,22,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-78,61,61,61,61,-51,61,-35,-36,-37,-38,-39,-63,61,-20,-21,-2,61,61,61,61,61,-57,-58,-59,-60,-61,-62,61,61,61,61,-88,-22,-23,-24,-89,61,61,-92,61,-55,-56,61,61,-44,-64,-66,-69,22,-46,61,-34,-27,-30,-94,-41,-42,-43,61,-33,-53,-54,-28,-31,-95,-29,-32,-93,-84,-97,-40,61,-52,-76,22,61,-45,-65,-70,22,61,-47,61,61,-79,-86,61,-87,-90,-91,22,22,22,-72,22,22,22,22,22,22,22,-96,-77,22,22,22,-68,-80,-81,]),'ID':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,23,24,25,26,27,28,31,32,33,34,35,36,37,38,39,40,41,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,66,67,68,69,70,71,72,73,76,78,81,82,83,84,86,90,91,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,110,114,115,116,119,122,124,125,126,127,128,129,130,131,132,133,135,136,137,138,140,141,142,143,144,148,152,154,155,156,157,158,159,160,161,162,163,164,165,166,167,],[23,23,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-78,62,62,62,62,-51,77,62,-35,-36,-37,-38,-39,-63,62,-20,-21,-2,62,62,62,62,62,-57,-58,-59,-60,-61,-62,62,62,62,62,-88,-22,-23,-24,-89,62,62,-92,62,-55,-56,62,62,-44,-64,-66,-69,23,-46,62,-34,-27,-30,-94,-41,-42,-43,62,-33,-53,-54,-28,-31,-95,-29,-32,-93,-84,-97,-40,62,-52,-76,23,62,-45,-65,-70,23,62,-47,62,62,-79,-86,62,-87,-90,-91,23,23,23,-72,23,23,23,23,23,23,23,-96,-77,23,23,23,-68,-80,-81,]),'PRINT':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,23,28,33,34,35,36,37,38,40,41,43,59,60,61,62,66,69,78,81,82,83,84,86,91,93,94,95,96,97,98,100,101,102,103,104,105,106,107,108,110,114,115,119,122,124,126,127,128,129,131,135,136,138,140,141,142,143,144,148,152,154,155,156,157,158,159,160,161,162,163,164,165,166,167,],[24,24,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-78,-51,-35,-36,-37,-38,-39,-63,-20,-21,-2,-88,-22,-23,-24,-89,-92,-44,-64,-66,-69,24,-46,-34,-27,-30,-94,-41,-42,-43,-33,-53,-54,-28,-31,-95,-29,-32,-93,-84,-97,-40,-52,-76,24,-45,-65,-70,24,-47,-79,-86,-87,-90,-91,24,24,24,-72,24,24,24,24,24,24,24,-96,-77,24,24,24,-68,-80,-81,]),'PUTS':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,23,28,33,34,35,36,37,38,40,41,43,59,60,61,62,66,69,78,81,82,83,84,86,91,93,94,95,96,97,98,100,101,102,103,104,105,106,107,108,110,114,115,119,122,124,126,127,128,129,131,135,136,138,140,141,142,143,144,148,152,154,155,156,157,158,159,160,161,162,163,164,165,166,167,],[26,26,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-78,-51,-35,-36,-37,-38,-39,-63,-20,-21,-2,-88,-22,-23,-24,-89,-92,-44,-64,-66,-69,26,-46,-34,-27,-30,-94,-41,-42,-43,-33,-53,-54,-28,-31,-95,-29,-32,-93,-84,-97,-40,-52,-76,26,-45,-65,-70,26,-47,-79,-86,-87,-90,-91,26,26,26,-72,26,26,26,26,26,26,26,-96,-77,26,26,26,-68,-80,-81,]),'P':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,23,28,33,34,35,36,37,38,40,41,43,59,60,61,62,66,69,78,81,82,83,84,86,91,93,94,95,96,97,98,100,101,102,103,104,105,106,107,108,110,114,115,119,122,124,126,127,128,129,131,135,136,138,140,141,142,143,144,148,152,154,155,156,157,158,159,160,161,162,163,164,165,166,167,],[27,27,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-78,-51,-35,-36,-37,-38,-39,-63,-20,-21,-2,-88,-22,-23,-24,-89,-92,-44,-64,-66,-69,27,-46,-34,-27,-30,-94,-41,-42,-43,-33,-53,-54,-28,-31,-95,-29,-32,-93,-84,-97,-40,-52,-76,27,-45,-65,-70,27,-47,-79,-86,-87,-90,-91,27,27,27,-72,27,27,27,27,27,27,27,-96,-77,27,27,27,-68,-80,-81,]),'LPAREN':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,26,27,28,29,33,34,35,36,37,38,40,41,42,43,46,55,56,59,60,61,62,64,65,66,69,77,78,81,82,83,84,85,86,91,92,93,94,95,96,97,98,100,101,102,103,104,105,106,107,108,110,114,115,119,122,124,126,127,128,129,131,135,136,138,140,141,142,143,144,148,152,154,155,156,157,158,159,160,161,162,163,164,165,166,167,],[25,25,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,45,-16,-17,-18,-19,-22,45,-23,57,58,67,68,-51,73,-35,-36,-37,-38,-39,-63,-20,-21,90,-2,99,99,99,-88,-22,-23,-24,45,45,-89,-92,125,-44,-64,-66,-69,25,130,-46,-34,45,-27,-30,-94,-41,-42,-43,-33,45,45,-28,-31,-95,-29,-32,-93,-84,-97,-40,-52,-76,25,-45,-65,-70,25,-47,-79,-86,-87,-90,-91,25,25,25,-72,25,25,25,25,25,25,25,-96,-77,25,25,25,-68,-80,-81,]),'WHILE':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,23,28,33,34,35,36,37,38,40,41,43,59,60,61,62,66,69,78,81,82,83,84,86,91,93,94,95,96,97,98,100,101,102,103,104,105,106,107,108,110,114,115,119,122,124,126,127,128,129,131,135,136,138,140,141,142,143,144,148,152,154,155,156,157,158,159,160,161,162,163,164,165,166,167,],[29,29,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-78,-51,-35,-36,-37,-38,-39,-63,-20,-21,-2,-88,-22,-23,-24,-89,-92,-44,-64,-66,-69,29,-46,-34,-27,-30,-94,-41,-42,-43,-33,-53,-54,-28,-31,-95,-29,-32,-93,-84,-97,-40,-52,-76,29,-45,-65,-70,29,-47,-79,-86,-87,-90,-91,29,29,29,-72,29,29,29,29,29,29,29,-96,-77,29,29,29,-68,-80,-81,]),'CASE':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,23,28,33,34,35,36,37,38,40,41,43,59,60,61,62,66,69,78,81,82,83,84,86,91,93,94,95,96,97,98,100,101,102,103,104,105,106,107,108,110,114,115,119,122,124,126,127,128,129,131,135,136,138,140,141,142,143,144,148,152,154,155,156,157,158,159,160,161,162,163,164,165,166,167,],[30,30,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-78,-51,-35,-36,-37,-38,-39,-63,-20,-21,-2,-88,-22,-23,-24,-89,-92,-44,-64,-66,-69,30,-46,-34,-27,-30,-94,-41,-42,-43,-33,-53,-54,-28,-31,-95,-29,-32,-93,-84,-97,-40,-52,-76,30,-45,-65,-70,30,-47,-79,-86,-87,-90,-91,30,30,30,-72,30,30,30,30,30,30,30,-96,-77,30,30,30,-68,-80,-81,]),'DEF':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,23,28,33,34,35,36,37,38,40,41,43,59,60,61,62,66,69,78,81,82,83,84,86,91,93,94,95,96,97,98,100,101,102,103,104,105,106,107,108,110,114,115,119,122,124,126,127,128,129,131,135,136,138,140,141,142,143,144,148,152,154,155,156,157,158,159,160,161,162,163,164,165,166,167,],[31,31,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-78,-51,-35,-36,-37,-38,-39,-63,-20,-21,-2,-88,-22,-23,-24,-89,-92,-44,-64,-66,-69,31,-46,-34,-27,-30,-94,-41,-42,-43,-33,-53,-54,-28,-31,-95,-29,-32,-93,-84,-97,-40,-52,-76,31,-45,-65,-70,31,-47,-79,-86,-87,-90,-91,31,31,31,-72,31,31,31,31,31,31,31,-96,-77,31,31,31,-68,-80,-81,]),'LBRACKET':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,23,28,33,34,35,36,37,38,40,41,43,46,55,56,59,60,61,62,66,69,78,81,82,83,84,86,91,93,94,95,96,97,98,100,101,102,103,104,105,106,107,108,110,114,115,119,122,124,126,127,128,129,131,135,136,138,140,141,142,143,144,148,152,154,155,156,157,158,159,160,161,162,163,164,165,166,167,],[32,32,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-78,-51,-35,-36,-37,-38,-39,-63,-20,-21,-2,32,32,32,-88,-22,-23,-24,-89,-92,-44,-64,-66,-69,32,-46,-34,-27,-30,-94,-41,-42,-43,-33,-53,-54,-28,-31,-95,-29,-32,-93,-84,-97,-40,-52,-76,32,-45,-65,-70,32,-47,-79,-86,-87,-90,-91,32,32,32,-72,32,32,32,32,32,32,32,-96,-77,32,32,32,-68,-80,-81,]),'PLUS':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,28,33,34,35,36,37,38,40,41,43,59,60,61,62,64,65,66,69,78,81,82,83,84,86,91,92,93,94,95,96,97,98,100,101,102,103,104,105,106,107,108,110,114,115,119,122,124,126,127,128,129,131,135,136,138,140,141,142,143,144,148,152,154,155,156,157,158,159,160,161,162,163,164,165,166,167,],[33,33,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,33,-16,-17,-18,-19,-22,33,-23,-24,-51,-35,-36,-37,-38,-39,-63,-20,-21,-2,-88,-22,-23,-24,33,33,-89,-92,-44,-64,-66,-69,33,-46,-34,33,-27,-30,-94,-41,-42,-43,-33,33,33,-28,-31,-95,-29,-32,-93,-84,-97,-40,-52,-76,33,-45,-65,-70,33,-47,-79,-86,-87,-90,-91,33,33,33,-72,33,33,33,33,33,33,33,-96,-77,33,33,33,-68,-80,-81,]),'MINUS':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,28,33,34,35,36,37,38,40,41,43,59,60,61,62,64,65,66,69,78,81,82,83,84,86,91,92,93,94,95,96,97,98,100,101,102,103,104,105,106,107,108,110,114,115,119,122,124,126,127,128,129,131,135,136,138,140,141,142,143,144,148,152,154,155,156,157,158,159,160,161,162,163,164,165,166,167,],[34,34,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,34,-16,-17,-18,-19,-22,34,-23,-24,-51,-35,-36,-37,-38,-39,-63,-20,-21,-2,-88,-22,-23,-24,34,34,-89,-92,-44,-64,-66,-69,34,-46,-34,34,-27,-30,-94,-41,-42,-43,-33,34,34,-28,-31,-95,-29,-32,-93,-84,-97,-40,-52,-76,34,-45,-65,-70,34,-47,-79,-86,-87,-90,-91,34,34,34,-72,34,34,34,34,34,34,34,-96,-77,34,34,34,-68,-80,-81,]),'TIMES':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,28,33,34,35,36,37,38,40,41,43,59,60,61,62,64,65,66,69,78,81,82,83,84,86,91,92,93,94,95,96,97,98,100,101,102,103,104,105,106,107,108,110,114,115,119,122,124,126,127,128,129,131,135,136,138,140,141,142,143,144,148,152,154,155,156,157,158,159,160,161,162,163,164,165,166,167,],[35,35,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,35,-16,-17,-18,-19,-22,35,-23,-24,-51,-35,-36,-37,-38,-39,-63,-20,-21,-2,-88,-22,-23,-24,35,35,-89,-92,-44,-64,-66,-69,35,-46,-34,35,-27,-30,-94,-41,-42,-43,-33,35,35,-28,-31,-95,-29,-32,-93,-84,-97,-40,-52,-76,35,-45,-65,-70,35,-47,-79,-86,-87,-90,-91,35,35,35,-72,35,35,35,35,35,35,35,-96,-77,35,35,35,-68,-80,-81,]),'DIVIDE':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,28,33,34,35,36,37,38,40,41,43,59,60,61,62,64,65,66,69,78,81,82,83,84,86,91,92,93,94,95,96,97,98,100,101,102,103,104,105,106,107,108,110,114,115,119,122,124,126,127,128,129,131,135,136,138,140,141,142,143,144,148,152,154,155,156,157,158,159,160,161,162,163,164,165,166,167,],[36,36,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,36,-16,-17,-18,-19,-22,36,-23,-24,-51,-35,-36,-37,-38,-39,-63,-20,-21,-2,-88,-22,-23,-24,36,36,-89,-92,-44,-64,-66,-69,36,-46,-34,36,-27,-30,-94,-41,-42,-43,-33,36,36,-28,-31,-95,-29,-32,-93,-84,-97,-40,-52,-76,36,-45,-65,-70,36,-47,-79,-86,-87,-90,-91,36,36,36,-72,36,36,36,36,36,36,36,-96,-77,36,36,36,-68,-80,-81,]),'MOD':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,28,33,34,35,36,37,38,40,41,43,59,60,61,62,64,65,66,69,78,81,82,83,84,86,91,92,93,94,95,96,97,98,100,101,102,103,104,105,106,107,108,110,114,115,119,122,124,126,127,128,129,131,135,136,138,140,141,142,143,144,148,152,154,155,156,157,158,159,160,161,162,163,164,165,166,167,],[37,37,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,37,-16,-17,-18,-19,-22,37,-23,-24,-51,-35,-36,-37,-38,-39,-63,-20,-21,-2,-88,-22,-23,-24,37,37,-89,-92,-44,-64,-66,-69,37,-46,-34,37,-27,-30,-94,-41,-42,-43,-33,37,37,-28,-31,-95,-29,-32,-93,-84,-97,-40,-52,-76,37,-45,-65,-70,37,-47,-79,-86,-87,-90,-91,37,37,37,-72,37,37,37,37,37,37,37,-96,-77,37,37,37,-68,-80,-81,]),'LBRACE':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,23,28,33,34,35,36,37,38,40,41,43,46,55,56,59,60,61,62,66,69,78,81,82,83,84,86,91,93,94,95,96,97,98,100,101,102,103,104,105,106,107,108,110,114,115,119,122,124,126,127,128,129,131,135,136,138,140,141,142,143,144,148,152,154,155,156,157,158,159,160,161,162,163,164,165,166,167,],[39,39,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-78,-51,-35,-36,-37,-38,-39,-63,-20,-21,-2,39,39,39,-88,-22,-23,-24,-89,-92,-44,-64,-66,-69,39,-46,-34,-27,-30,-94,-41,-42,-43,-33,-53,-54,-28,-31,-95,-29,-32,-93,-84,-97,-40,-52,-76,39,-45,-65,-70,39,-47,-79,-86,-87,-90,-91,39,39,39,-72,39,39,39,39,39,39,39,-96,-77,39,39,39,-68,-80,-81,]),'NUMBER':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,23,24,25,26,27,28,32,33,34,35,36,37,38,39,40,41,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,66,67,68,69,70,71,72,73,76,78,81,82,83,84,86,90,91,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,110,114,115,116,119,122,124,125,126,127,128,129,130,131,132,133,135,136,137,138,140,141,142,143,144,148,152,154,155,156,157,158,159,160,161,162,163,164,165,166,167,],[40,40,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-78,40,40,40,40,-51,40,-35,-36,-37,-38,-39,-63,40,-20,-21,-2,40,40,40,40,40,-57,-58,-59,-60,-61,-62,40,40,40,40,-88,-22,-23,-24,-89,40,40,-92,40,-55,-56,40,40,-44,-64,-66,-69,40,-46,40,-34,-27,-30,-94,-41,-42,-43,40,-33,-53,-54,-28,-31,-95,-29,-32,-93,-84,-97,-40,40,-52,-76,40,40,-45,-65,-70,40,40,-47,40,40,-79,-86,40,-87,-90,-91,40,40,40,-72,40,40,40,40,40,40,40,-96,-77,40,40,40,-68,-80,-81,]),'STRING':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,23,24,25,26,27,28,32,33,34,35,36,37,38,39,40,41,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,66,67,68,69,70,71,72,73,76,78,81,82,83,84,86,90,91,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,110,114,115,116,119,122,124,125,126,127,128,129,130,131,132,133,135,136,137,138,140,141,142,143,144,148,152,154,155,156,157,158,159,160,161,162,163,164,165,166,167,],[41,41,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-78,41,41,41,41,-51,41,-35,-36,-37,-38,-39,-63,41,-20,-21,-2,41,41,41,41,41,-57,-58,-59,-60,-61,-62,41,41,41,41,-88,-22,-23,-24,-89,41,41,-92,41,-55,-56,41,41,-44,-64,-66,-69,41,-46,41,-34,-27,-30,-94,-41,-42,-43,41,-33,-53,-54,-28,-31,-95,-29,-32,-93,-84,-97,-40,41,-52,-76,41,41,-45,-65,-70,41,41,-47,41,41,-79,-86,41,-87,-90,-91,41,41,41,-72,41,41,41,41,41,41,41,-96,-77,41,41,41,-68,-80,-81,]),'IF':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,23,28,33,34,35,36,37,38,40,41,43,59,60,61,62,66,69,78,81,82,83,84,86,91,93,94,95,96,97,98,100,101,102,103,104,105,106,107,108,110,114,115,119,122,124,126,127,128,129,131,135,136,138,140,141,142,143,144,148,152,154,155,156,157,158,159,160,161,162,163,164,165,166,167,],[42,42,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-78,-51,-35,-36,-37,-38,-39,-63,-20,-21,-2,-88,-22,-23,-24,-89,-92,-44,-64,-66,-69,42,-46,-34,-27,-30,-94,-41,-42,-43,-33,-53,-54,-28,-31,-95,-29,-32,-93,-84,-97,-40,-52,-76,42,-45,-65,-70,42,-47,-79,-86,-87,-90,-91,42,42,42,-72,42,42,42,42,42,42,42,-96,-77,42,42,42,-68,-80,-81,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,23,28,33,34,35,36,37,38,40,41,43,59,60,61,62,66,69,78,81,82,83,86,91,93,94,95,96,97,98,100,101,102,103,104,105,106,107,108,110,114,115,119,122,126,127,128,131,135,136,138,140,141,148,159,160,161,164,165,166,167,],[0,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-78,-51,-35,-36,-37,-38,-39,-63,-20,-21,-2,-88,-22,-23,-24,-89,-92,-44,-64,-66,-69,-46,-34,-27,-30,-94,-41,-42,-43,-33,-53,-54,-28,-31,-95,-29,-32,-93,-84,-97,-40,-52,-76,-45,-65,-70,-47,-79,-86,-87,-90,-91,-72,-67,-96,-77,-71,-68,-80,-81,]),'END':([2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,23,28,33,34,35,36,37,38,40,41,43,59,60,61,62,66,69,74,75,78,81,82,83,86,91,93,94,95,96,97,98,100,101,102,103,104,105,106,107,108,110,114,115,119,122,123,126,127,128,129,131,135,136,138,140,141,143,148,154,155,159,160,161,162,163,164,165,166,167,],[-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-78,-51,-35,-36,-37,-38,-39,-63,-20,-21,-2,-88,-22,-23,-24,-89,-92,122,-74,-44,-64,-66,-69,-46,-34,-27,-30,-94,-41,-42,-43,-33,-53,-54,-28,-31,-95,-29,-32,-93,-84,-97,-40,-52,-76,-75,-45,-65,-70,148,-47,-79,-86,-87,-90,-91,-73,-72,160,161,165,-96,-77,166,167,-71,-68,-80,-81,]),'WHEN':([2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,23,28,30,33,34,35,36,37,38,40,41,43,59,60,61,62,66,69,74,75,78,81,82,83,86,91,93,94,95,96,97,98,100,101,102,103,104,105,106,107,108,110,114,115,119,122,123,126,127,128,131,135,136,138,140,141,143,148,159,160,161,164,165,166,167,],[-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-78,-51,76,-35,-36,-37,-38,-39,-63,-20,-21,-2,-88,-22,-23,-24,-89,-92,76,-74,-44,-64,-66,-69,-46,-34,-27,-30,-94,-41,-42,-43,-33,-53,-54,-28,-31,-95,-29,-32,-93,-84,-97,-40,-52,-76,-75,-45,-65,-70,-47,-79,-86,-87,-90,-91,-73,-72,-67,-96,-77,-71,-68,-80,-81,]),'ELSE':([2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,23,28,33,34,35,36,37,38,40,41,43,59,60,61,62,66,69,78,81,82,83,86,91,93,94,95,96,97,98,100,101,102,103,104,105,106,107,108,110,114,115,119,122,126,127,128,131,135,136,138,140,141,148,159,160,161,164,165,166,167,],[-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-78,-51,-35,-36,-37,-38,-39,84,-20,-21,-2,-88,-22,-23,-24,-89,-92,-44,84,-66,-69,-46,-34,-27,-30,-94,-41,-42,-43,-33,-53,-54,-28,-31,-95,-29,-32,-93,-84,-97,-40,-52,-76,-45,-65,-70,-47,-79,-86,-87,-90,-91,-72,-67,-96,-77,-71,-68,-80,-81,]),'ELSIF':([2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,23,28,33,34,35,36,37,38,40,41,43,59,60,61,62,66,69,78,81,82,83,86,91,93,94,95,96,97,98,100,101,102,103,104,105,106,107,108,110,114,115,119,122,126,127,128,131,135,136,138,140,141,148,159,160,161,164,165,166,167,],[-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-78,-51,-35,-36,-37,-38,-39,85,-20,-21,-2,-88,-22,-23,-24,-89,-92,-44,85,-66,-69,-46,-34,-27,-30,-94,-41,-42,-43,-33,-53,-54,-28,-31,-95,-29,-32,-93,-84,-97,-40,-52,-76,-45,-65,-70,-47,-79,-86,-87,-90,-91,-72,-67,-96,-77,-71,-68,-80,-81,]),'ASSIGN':([20,22,23,],[46,55,56,]),'LESSTHAN':([20,21,22,23,40,41,60,61,62,120,],[-22,49,-23,-24,-20,-21,-22,-23,-24,49,]),'GREATERTHAN':([20,21,22,23,40,41,60,61,62,120,],[-22,50,-23,-24,-20,-21,-22,-23,-24,50,]),'GREATEROREQUAL':([20,21,22,23,40,41,60,61,62,120,],[-22,51,-23,-24,-20,-21,-22,-23,-24,51,]),'LESSOREQUAL':([20,21,22,23,40,41,60,61,62,120,],[-22,52,-23,-24,-20,-21,-22,-23,-24,52,]),'EQUAL':([20,21,22,23,40,41,60,61,62,120,],[-22,53,-23,-24,-20,-21,-22,-23,-24,53,]),'NOTEQUAL':([20,21,22,23,40,41,60,61,62,120,],[-22,54,-23,-24,-20,-21,-22,-23,-24,54,]),'RPAREN':([28,40,41,57,60,61,62,63,64,65,80,91,100,101,102,109,111,112,113,117,118,119,121,125,134,139,145,146,147,149,153,],[-51,-20,-21,110,-22,-23,-24,114,115,-25,-25,-34,-33,-53,-54,135,136,-82,138,140,141,-52,142,144,152,-26,156,157,-82,158,-83,]),'AND':([28,40,41,60,61,62,91,100,101,102,],[71,-20,-21,-22,-23,-24,-34,-33,-53,-54,]),'OR':([28,40,41,60,61,62,91,100,101,102,],[72,-20,-21,-22,-23,-24,-34,-33,-53,-54,]),'RBRACKET':([32,40,41,60,61,62,79,80,139,],[78,-20,-21,-22,-23,-24,126,-25,-26,]),'RBRACE':([39,40,41,60,61,62,87,88,150,151,],[86,-20,-21,-22,-23,-24,131,-48,-49,-50,]),'COMMA':([40,41,60,61,62,65,80,87,88,112,147,150,151,],[-20,-21,-22,-23,-24,116,116,132,-48,137,137,-49,-50,]),'COLON':([40,41,60,61,62,89,],[-20,-21,-22,-23,-24,133,]),'GETS':([46,55,56,],[95,105,108,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'codigo':([0,84,124,142,144,152,156,157,158,],[1,129,143,154,155,159,162,163,164,]),'statement':([0,1,84,124,129,142,143,144,152,154,155,156,157,158,159,162,163,164,],[2,43,2,2,43,2,43,2,2,43,43,2,2,2,43,43,43,43,]),'assign':([0,1,84,124,129,142,143,144,152,154,155,156,157,158,159,162,163,164,],[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,]),'impression':([0,1,84,124,129,142,143,144,152,154,155,156,157,158,159,162,163,164,],[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,]),'tupla':([0,1,46,55,56,84,124,129,142,143,144,152,154,155,156,157,158,159,162,163,164,],[5,5,97,97,97,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,]),'conditions':([0,1,70,73,76,84,90,124,129,130,142,143,144,152,154,155,156,157,158,159,162,163,164,],[6,6,119,121,124,6,134,6,6,149,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'while_loop':([0,1,84,124,129,142,143,144,152,154,155,156,157,158,159,162,163,164,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'case':([0,1,84,124,129,142,143,144,152,154,155,156,157,158,159,162,163,164,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'Sfunction':([0,1,84,124,129,142,143,144,152,154,155,156,157,158,159,162,163,164,],[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'array':([0,1,46,55,56,84,124,129,142,143,144,152,154,155,156,157,158,159,162,163,164,],[10,10,96,96,96,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'p_SfunctionINV':([0,1,84,124,129,142,143,144,152,154,155,156,157,158,159,162,163,164,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'p_function_one_parameter':([0,1,84,124,129,142,143,144,152,154,155,156,157,158,159,162,163,164,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'p_function_two_parameter':([0,1,84,124,129,142,143,144,152,154,155,156,157,158,159,162,163,164,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'function_call':([0,1,84,124,129,142,143,144,152,154,155,156,157,158,159,162,163,164,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'aritmeticExpresion':([0,1,25,45,48,84,124,129,142,143,144,152,154,155,156,157,158,159,162,163,164,],[15,15,64,64,102,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'operator':([0,1,15,21,64,65,84,92,101,102,124,129,142,143,144,152,154,155,156,157,158,159,162,163,164,],[16,16,44,47,44,47,16,47,47,44,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'dataIn':([0,1,84,124,129,142,143,144,152,154,155,156,157,158,159,162,163,164,],[17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'control_structures':([0,1,84,124,129,142,143,144,152,154,155,156,157,158,159,162,163,164,],[18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,]),'hash':([0,1,46,55,56,84,124,129,142,143,144,152,154,155,156,157,158,159,162,163,164,],[19,19,98,98,98,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,]),'value':([0,1,24,25,26,27,32,39,44,45,46,47,48,55,56,57,58,67,68,70,73,76,84,90,99,116,124,125,129,130,132,133,137,142,143,144,152,154,155,156,157,158,159,162,163,164,],[21,21,59,65,66,69,80,89,91,92,93,100,101,103,106,112,113,117,118,120,120,120,21,120,80,80,21,147,21,120,89,151,153,21,21,21,21,21,21,21,21,21,21,21,21,21,]),'condition':([0,1,70,73,76,84,90,124,129,130,142,143,144,152,154,155,156,157,158,159,162,163,164,],[28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'if_block':([0,1,84,124,129,142,143,144,152,154,155,156,157,158,159,162,163,164,],[38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'operComp':([21,120,],[48,48,]),'values':([25,32,99,116,],[63,79,63,139,]),'conector':([28,],[70,]),'whens':([30,],[74,]),'when':([30,74,],[75,123,]),'elsif_blocks':([38,],[81,]),'else_block':([38,81,],[82,127,]),'elsif_block':([38,81,],[83,128,]),'hash_contents':([39,],[87,]),'hash_pair':([39,132,],[88,150,]),'data_structure':([46,55,56,],[94,104,107,]),'params':([57,125,],[109,146,]),'param':([57,125,],[111,145,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> codigo","S'",1,None,None,None),
  ('codigo -> statement','codigo',1,'p_codigo','analizador_sintactico.py',30),
  ('codigo -> codigo statement','codigo',2,'p_codigo','analizador_sintactico.py',31),
  ('statement -> assign','statement',1,'p_statement','analizador_sintactico.py',34),
  ('statement -> impression','statement',1,'p_statement','analizador_sintactico.py',35),
  ('statement -> tupla','statement',1,'p_statement','analizador_sintactico.py',36),
  ('statement -> conditions','statement',1,'p_statement','analizador_sintactico.py',37),
  ('statement -> while_loop','statement',1,'p_statement','analizador_sintactico.py',38),
  ('statement -> case','statement',1,'p_statement','analizador_sintactico.py',39),
  ('statement -> Sfunction','statement',1,'p_statement','analizador_sintactico.py',40),
  ('statement -> array','statement',1,'p_statement','analizador_sintactico.py',41),
  ('statement -> p_SfunctionINV','statement',1,'p_statement','analizador_sintactico.py',42),
  ('statement -> p_function_one_parameter','statement',1,'p_statement','analizador_sintactico.py',43),
  ('statement -> p_function_two_parameter','statement',1,'p_statement','analizador_sintactico.py',44),
  ('statement -> function_call','statement',1,'p_statement','analizador_sintactico.py',45),
  ('statement -> aritmeticExpresion','statement',1,'p_statement','analizador_sintactico.py',46),
  ('statement -> operator','statement',1,'p_statement','analizador_sintactico.py',47),
  ('statement -> dataIn','statement',1,'p_statement','analizador_sintactico.py',48),
  ('statement -> control_structures','statement',1,'p_statement','analizador_sintactico.py',49),
  ('statement -> hash','statement',1,'p_statement','analizador_sintactico.py',50),
  ('value -> NUMBER','value',1,'p_value','analizador_sintactico.py',53),
  ('value -> STRING','value',1,'p_value','analizador_sintactico.py',54),
  ('value -> INSTANCE_VAR','value',1,'p_value','analizador_sintactico.py',55),
  ('value -> GLOBAL_VAR','value',1,'p_value','analizador_sintactico.py',56),
  ('value -> ID','value',1,'p_value','analizador_sintactico.py',57),
  ('values -> value','values',1,'p_values','analizador_sintactico.py',64),
  ('values -> value COMMA values','values',3,'p_values','analizador_sintactico.py',65),
  ('assign -> INSTANCE_VAR ASSIGN value','assign',3,'p_assign','analizador_sintactico.py',82),
  ('assign -> GLOBAL_VAR ASSIGN value','assign',3,'p_assign','analizador_sintactico.py',83),
  ('assign -> ID ASSIGN value','assign',3,'p_assign','analizador_sintactico.py',84),
  ('assign -> INSTANCE_VAR ASSIGN data_structure','assign',3,'p_assign','analizador_sintactico.py',85),
  ('assign -> GLOBAL_VAR ASSIGN data_structure','assign',3,'p_assign','analizador_sintactico.py',86),
  ('assign -> ID ASSIGN data_structure','assign',3,'p_assign','analizador_sintactico.py',87),
  ('aritmeticExpresion -> value operator value','aritmeticExpresion',3,'p_aritmeticExpresion','analizador_sintactico.py',93),
  ('aritmeticExpresion -> aritmeticExpresion operator value','aritmeticExpresion',3,'p_aritmeticExpresion','analizador_sintactico.py',94),
  ('operator -> PLUS','operator',1,'p_operator','analizador_sintactico.py',113),
  ('operator -> MINUS','operator',1,'p_operator','analizador_sintactico.py',114),
  ('operator -> TIMES','operator',1,'p_operator','analizador_sintactico.py',115),
  ('operator -> DIVIDE','operator',1,'p_operator','analizador_sintactico.py',116),
  ('operator -> MOD','operator',1,'p_operator','analizador_sintactico.py',117),
  ('operator -> LPAREN aritmeticExpresion RPAREN','operator',3,'p_operator','analizador_sintactico.py',118),
  ('data_structure -> array','data_structure',1,'p_data_structure','analizador_sintactico.py',122),
  ('data_structure -> tupla','data_structure',1,'p_data_structure','analizador_sintactico.py',123),
  ('data_structure -> hash','data_structure',1,'p_data_structure','analizador_sintactico.py',124),
  ('array -> LBRACKET RBRACKET','array',2,'p_emptyarray','analizador_sintactico.py',128),
  ('array -> LBRACKET values RBRACKET','array',3,'p_array','analizador_sintactico.py',131),
  ('hash -> LBRACE RBRACE','hash',2,'p_empty_hash','analizador_sintactico.py',135),
  ('hash -> LBRACE hash_contents RBRACE','hash',3,'p_hash','analizador_sintactico.py',138),
  ('hash_contents -> hash_pair','hash_contents',1,'p_hash_contents','analizador_sintactico.py',141),
  ('hash_contents -> hash_contents COMMA hash_pair','hash_contents',3,'p_hash_contents','analizador_sintactico.py',142),
  ('hash_pair -> value COLON value','hash_pair',3,'p_hash_pair','analizador_sintactico.py',145),
  ('conditions -> condition','conditions',1,'p_conditions','analizador_sintactico.py',149),
  ('conditions -> condition conector conditions','conditions',3,'p_conditions','analizador_sintactico.py',150),
  ('condition -> value operComp value','condition',3,'p_condition','analizador_sintactico.py',153),
  ('condition -> value operComp aritmeticExpresion','condition',3,'p_condition','analizador_sintactico.py',154),
  ('conector -> AND','conector',1,'p_conector','analizador_sintactico.py',157),
  ('conector -> OR','conector',1,'p_conector','analizador_sintactico.py',158),
  ('operComp -> LESSTHAN','operComp',1,'p_operComp','analizador_sintactico.py',161),
  ('operComp -> GREATERTHAN','operComp',1,'p_operComp','analizador_sintactico.py',162),
  ('operComp -> GREATEROREQUAL','operComp',1,'p_operComp','analizador_sintactico.py',163),
  ('operComp -> LESSOREQUAL','operComp',1,'p_operComp','analizador_sintactico.py',164),
  ('operComp -> EQUAL','operComp',1,'p_operComp','analizador_sintactico.py',165),
  ('operComp -> NOTEQUAL','operComp',1,'p_operComp','analizador_sintactico.py',166),
  ('control_structures -> if_block','control_structures',1,'p_control_structures','analizador_sintactico.py',170),
  ('control_structures -> if_block elsif_blocks','control_structures',2,'p_control_structures','analizador_sintactico.py',171),
  ('control_structures -> if_block elsif_blocks else_block','control_structures',3,'p_control_structures','analizador_sintactico.py',172),
  ('control_structures -> if_block else_block','control_structures',2,'p_control_structures','analizador_sintactico.py',173),
  ('if_block -> IF LPAREN conditions RPAREN codigo','if_block',5,'p_if_block','analizador_sintactico.py',176),
  ('if_block -> IF LPAREN conditions RPAREN codigo END','if_block',6,'p_if_block','analizador_sintactico.py',177),
  ('elsif_blocks -> elsif_block','elsif_blocks',1,'p_elsif_blocks','analizador_sintactico.py',182),
  ('elsif_blocks -> elsif_blocks elsif_block','elsif_blocks',2,'p_elsif_blocks','analizador_sintactico.py',183),
  ('elsif_block -> ELSIF LPAREN conditions RPAREN codigo','elsif_block',5,'p_elsif_block','analizador_sintactico.py',186),
  ('else_block -> ELSE codigo END','else_block',3,'p_else_block','analizador_sintactico.py',191),
  ('when -> WHEN conditions codigo','when',3,'p_when','analizador_sintactico.py',195),
  ('whens -> when','whens',1,'p_whens','analizador_sintactico.py',200),
  ('whens -> whens when','whens',2,'p_whens','analizador_sintactico.py',201),
  ('case -> CASE whens END','case',3,'p_case','analizador_sintactico.py',204),
  ('Sfunction -> DEF ID LPAREN RPAREN codigo END','Sfunction',6,'p_Sfunction','analizador_sintactico.py',208),
  ('p_SfunctionINV -> ID','p_SfunctionINV',1,'p_SfunctionINV','analizador_sintactico.py',212),
  ('p_SfunctionINV -> ID LPAREN params RPAREN','p_SfunctionINV',4,'p_SfunctionINV','analizador_sintactico.py',213),
  ('p_function_one_parameter -> DEF ID LPAREN param RPAREN codigo END','p_function_one_parameter',7,'p_function_one_parameter','analizador_sintactico.py',221),
  ('p_function_two_parameter -> DEF ID LPAREN params RPAREN codigo END','p_function_two_parameter',7,'p_function_two_parameter','analizador_sintactico.py',225),
  ('param -> value','param',1,'p_param','analizador_sintactico.py',229),
  ('params -> value COMMA value','params',3,'p_params','analizador_sintactico.py',233),
  ('function_call -> ID LPAREN RPAREN','function_call',3,'p_function_call','analizador_sintactico.py',240),
  ('function_call -> ID LPAREN params RPAREN','function_call',4,'p_function_call','analizador_sintactico.py',241),
  ('function_call -> ID LPAREN param RPAREN','function_call',4,'p_function_call','analizador_sintactico.py',242),
  ('impression -> PRINT LPAREN value RPAREN','impression',4,'p_impression','analizador_sintactico.py',251),
  ('impression -> PRINT value','impression',2,'p_impression','analizador_sintactico.py',252),
  ('impression -> PUTS value','impression',2,'p_impression','analizador_sintactico.py',253),
  ('impression -> PUTS LPAREN value RPAREN','impression',4,'p_impression','analizador_sintactico.py',254),
  ('impression -> P LPAREN value RPAREN','impression',4,'p_impression','analizador_sintactico.py',255),
  ('impression -> P value','impression',2,'p_impression','analizador_sintactico.py',256),
  ('dataIn -> ID ASSIGN GETS','dataIn',3,'p_dataIn','analizador_sintactico.py',264),
  ('dataIn -> INSTANCE_VAR ASSIGN GETS','dataIn',3,'p_dataIn','analizador_sintactico.py',265),
  ('dataIn -> GLOBAL_VAR ASSIGN GETS','dataIn',3,'p_dataIn','analizador_sintactico.py',266),
  ('while_loop -> WHILE LPAREN conditions RPAREN codigo END','while_loop',6,'p_while_loop','analizador_sintactico.py',272),
  ('tupla -> LPAREN values RPAREN','tupla',3,'p_tupla','analizador_sintactico.py',278),
]
