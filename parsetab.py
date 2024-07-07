
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND APOSTROPHE ASSIGN BREAK CASE CLASS COLON COMMA CONST DAPOSTROPHE DEF DIVIDE DO DOT ELSE ELSIF END EQUAL FALSE FOR GETS GLOBAL_VAR GREATEROREQUAL GREATERTHAN ID IF IN INSTANCE_VAR LBRACE LBRACKET LESSOREQUAL LESSTHAN LPAREN MINUS MOD NIL NONE NOT NOTEQUAL NUMBER OR P PLUS PRINT PUTS RBRACE RBRACKET RETURN RPAREN SEMICOLON STRING TIMES TRUE WHEN WHILEcodigo : statement\n              | codigo statementstatement : assign\n              | impression\n              | tupla\n              | conditions\n              | while_loop\n              | case\n              | Sfunction\n              | array\n              | p_SfunctionINV\n              | p_function_one_parameter\n              | p_function_two_parameter\n              | aritmeticExpresion\n              | operator\n              | dataIn\n              | control_structures\n              | hashvalue : NUMBER\n             | STRING\n             | INSTANCE_VAR\n             | GLOBAL_VAR\n             | IDvalues : value\n              | value COMMA valuesassign : INSTANCE_VAR ASSIGN value\n              | GLOBAL_VAR ASSIGN value\n              | ID ASSIGN value\n              | INSTANCE_VAR ASSIGN data_structure\n              | GLOBAL_VAR ASSIGN data_structure\n              | ID ASSIGN data_structure\n              aritmeticExpresion : value operator value\n                          | aritmeticExpresion operator valueoperator : PLUS\n                | MINUS\n                | TIMES\n                | DIVIDE\n                | MOD\n                | LPAREN aritmeticExpresion RPARENdata_structure : array\n                      | tupla\n                      | hasharray : LBRACKET RBRACKETarray : LBRACKET values RBRACKEThash : LBRACE RBRACEhash : LBRACE hash_contents RBRACEhash_contents : hash_pair\n                     | hash_contents COMMA hash_pairhash_pair : value COLON valueconditions : condition\n                  | condition conector conditionscondition : value operComp value\n                 | value operComp aritmeticExpresion conector : AND\n                | ORoperComp : LESSTHAN\n                | GREATERTHAN\n                | GREATEROREQUAL\n                | LESSOREQUAL\n                | EQUAL\n                | NOTEQUALcontrol_structures : if_block\n                          | if_block elsif_blocks\n                          | if_block elsif_blocks else_block\n                          | if_block else_blockif_block : IF LPAREN conditions RPAREN codigo\n                | IF LPAREN conditions RPAREN codigo ENDelsif_blocks : elsif_block\n                    | elsif_blocks elsif_blockelsif_block : ELSIF LPAREN conditions RPAREN codigoelse_block : ELSE codigo ENDwhen : WHEN conditions codigowhens : when\n             | whens whencase : CASE whens ENDSfunction : DEF ID LPAREN RPAREN codigo ENDp_SfunctionINV : ID\n                      | ID LPAREN params RPARENp_function_one_parameter : DEF ID LPAREN param RPAREN codigo ENDp_function_two_parameter : DEF ID LPAREN params RPAREN codigo ENDparam : valueparams : value COMMA valueimpression : PRINT LPAREN values RPAREN\n                  | PRINT values\n                  | PUTS values\n                  | PUTS LPAREN values RPAREN\n                  | P LPAREN values RPAREN\n                  | P values\n                  | PRINT\n                  | PUTSdataIn : ID ASSIGN GETS\n              | INSTANCE_VAR ASSIGN GETS\n              | GLOBAL_VAR ASSIGN GETSwhile_loop : WHILE LPAREN conditions RPAREN codigo ENDtupla : LPAREN values RPAREN'
    
_lr_action_items = {'INSTANCE_VAR':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,22,23,24,25,26,27,31,32,33,34,35,36,37,38,39,40,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,66,67,68,69,70,71,72,73,76,78,80,81,82,83,85,89,90,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,111,112,113,116,119,121,122,123,124,125,126,127,128,129,130,132,133,134,135,136,137,138,139,140,144,148,150,151,152,153,154,155,156,157,158,159,160,161,162,163,],[19,19,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-77,60,60,60,60,-50,60,-34,-35,-36,-37,-38,-62,60,-19,-20,-2,60,60,60,60,60,-56,-57,-58,-59,-60,-61,60,60,60,60,-84,-24,-21,-22,-23,-85,60,60,-88,60,-54,-55,60,60,-43,-63,-65,-68,19,-45,60,-33,-26,-29,-92,-40,-41,-42,60,-32,-52,-53,-27,-30,-93,-28,-31,-91,60,-95,-39,-51,-75,19,60,-44,-64,-69,19,60,-46,60,60,-78,60,-83,-25,-86,-87,19,19,19,-71,19,19,19,19,19,19,19,-94,-76,19,19,19,-67,-79,-80,]),'GLOBAL_VAR':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,22,23,24,25,26,27,31,32,33,34,35,36,37,38,39,40,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,66,67,68,69,70,71,72,73,76,78,80,81,82,83,85,89,90,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,111,112,113,116,119,121,122,123,124,125,126,127,128,129,130,132,133,134,135,136,137,138,139,140,144,148,150,151,152,153,154,155,156,157,158,159,160,161,162,163,],[21,21,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-77,61,61,61,61,-50,61,-34,-35,-36,-37,-38,-62,61,-19,-20,-2,61,61,61,61,61,-56,-57,-58,-59,-60,-61,61,61,61,61,-84,-24,-21,-22,-23,-85,61,61,-88,61,-54,-55,61,61,-43,-63,-65,-68,21,-45,61,-33,-26,-29,-92,-40,-41,-42,61,-32,-52,-53,-27,-30,-93,-28,-31,-91,61,-95,-39,-51,-75,21,61,-44,-64,-69,21,61,-46,61,61,-78,61,-83,-25,-86,-87,21,21,21,-71,21,21,21,21,21,21,21,-94,-76,21,21,21,-67,-79,-80,]),'ID':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,22,23,24,25,26,27,30,31,32,33,34,35,36,37,38,39,40,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,66,67,68,69,70,71,72,73,76,78,80,81,82,83,85,89,90,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,111,112,113,116,119,121,122,123,124,125,126,127,128,129,130,132,133,134,135,136,137,138,139,140,144,148,150,151,152,153,154,155,156,157,158,159,160,161,162,163,],[22,22,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-77,62,62,62,62,-50,77,62,-34,-35,-36,-37,-38,-62,62,-19,-20,-2,62,62,62,62,62,-56,-57,-58,-59,-60,-61,62,62,62,62,-84,-24,-21,-22,-23,-85,62,62,-88,62,-54,-55,62,62,-43,-63,-65,-68,22,-45,62,-33,-26,-29,-92,-40,-41,-42,62,-32,-52,-53,-27,-30,-93,-28,-31,-91,62,-95,-39,-51,-75,22,62,-44,-64,-69,22,62,-46,62,62,-78,62,-83,-25,-86,-87,22,22,22,-71,22,22,22,22,22,22,22,-94,-76,22,22,22,-67,-79,-80,]),'PRINT':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,22,23,25,27,32,33,34,35,36,37,39,40,42,58,59,60,61,62,66,69,78,80,81,82,83,85,90,92,93,94,95,96,97,99,100,101,102,103,104,105,106,107,112,113,116,119,121,123,124,125,126,128,132,134,135,136,137,138,139,140,144,148,150,151,152,153,154,155,156,157,158,159,160,161,162,163,],[23,23,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-77,-89,-90,-50,-34,-35,-36,-37,-38,-62,-19,-20,-2,-84,-24,-21,-22,-23,-85,-88,-43,-63,-65,-68,23,-45,-33,-26,-29,-92,-40,-41,-42,-32,-52,-53,-27,-30,-93,-28,-31,-91,-95,-39,-51,-75,23,-44,-64,-69,23,-46,-78,-83,-25,-86,-87,23,23,23,-71,23,23,23,23,23,23,23,-94,-76,23,23,23,-67,-79,-80,]),'PUTS':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,22,23,25,27,32,33,34,35,36,37,39,40,42,58,59,60,61,62,66,69,78,80,81,82,83,85,90,92,93,94,95,96,97,99,100,101,102,103,104,105,106,107,112,113,116,119,121,123,124,125,126,128,132,134,135,136,137,138,139,140,144,148,150,151,152,153,154,155,156,157,158,159,160,161,162,163,],[25,25,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-77,-89,-90,-50,-34,-35,-36,-37,-38,-62,-19,-20,-2,-84,-24,-21,-22,-23,-85,-88,-43,-63,-65,-68,25,-45,-33,-26,-29,-92,-40,-41,-42,-32,-52,-53,-27,-30,-93,-28,-31,-91,-95,-39,-51,-75,25,-44,-64,-69,25,-46,-78,-83,-25,-86,-87,25,25,25,-71,25,25,25,25,25,25,25,-94,-76,25,25,25,-67,-79,-80,]),'P':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,22,23,25,27,32,33,34,35,36,37,39,40,42,58,59,60,61,62,66,69,78,80,81,82,83,85,90,92,93,94,95,96,97,99,100,101,102,103,104,105,106,107,112,113,116,119,121,123,124,125,126,128,132,134,135,136,137,138,139,140,144,148,150,151,152,153,154,155,156,157,158,159,160,161,162,163,],[26,26,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-77,-89,-90,-50,-34,-35,-36,-37,-38,-62,-19,-20,-2,-84,-24,-21,-22,-23,-85,-88,-43,-63,-65,-68,26,-45,-33,-26,-29,-92,-40,-41,-42,-32,-52,-53,-27,-30,-93,-28,-31,-91,-95,-39,-51,-75,26,-44,-64,-69,26,-46,-78,-83,-25,-86,-87,26,26,26,-71,26,26,26,26,26,26,26,-94,-76,26,26,26,-67,-79,-80,]),'LPAREN':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,25,26,27,28,32,33,34,35,36,37,39,40,41,42,45,54,55,58,59,60,61,62,64,65,66,69,77,78,80,81,82,83,84,85,90,91,92,93,94,95,96,97,99,100,101,102,103,104,105,106,107,112,113,116,119,121,123,124,125,126,128,132,134,135,136,137,138,139,140,144,148,150,151,152,153,154,155,156,157,158,159,160,161,162,163,],[24,24,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,44,-15,-16,-17,-18,-21,44,-22,56,57,67,68,-50,73,-34,-35,-36,-37,-38,-62,-19,-20,89,-2,98,98,98,-84,-24,-21,-22,-23,44,44,-85,-88,122,-43,-63,-65,-68,24,127,-45,-33,44,-26,-29,-92,-40,-41,-42,-32,44,44,-27,-30,-93,-28,-31,-91,-95,-39,-51,-75,24,-44,-64,-69,24,-46,-78,-83,-25,-86,-87,24,24,24,-71,24,24,24,24,24,24,24,-94,-76,24,24,24,-67,-79,-80,]),'WHILE':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,22,23,25,27,32,33,34,35,36,37,39,40,42,58,59,60,61,62,66,69,78,80,81,82,83,85,90,92,93,94,95,96,97,99,100,101,102,103,104,105,106,107,112,113,116,119,121,123,124,125,126,128,132,134,135,136,137,138,139,140,144,148,150,151,152,153,154,155,156,157,158,159,160,161,162,163,],[28,28,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-77,-89,-90,-50,-34,-35,-36,-37,-38,-62,-19,-20,-2,-84,-24,-21,-22,-23,-85,-88,-43,-63,-65,-68,28,-45,-33,-26,-29,-92,-40,-41,-42,-32,-52,-53,-27,-30,-93,-28,-31,-91,-95,-39,-51,-75,28,-44,-64,-69,28,-46,-78,-83,-25,-86,-87,28,28,28,-71,28,28,28,28,28,28,28,-94,-76,28,28,28,-67,-79,-80,]),'CASE':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,22,23,25,27,32,33,34,35,36,37,39,40,42,58,59,60,61,62,66,69,78,80,81,82,83,85,90,92,93,94,95,96,97,99,100,101,102,103,104,105,106,107,112,113,116,119,121,123,124,125,126,128,132,134,135,136,137,138,139,140,144,148,150,151,152,153,154,155,156,157,158,159,160,161,162,163,],[29,29,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-77,-89,-90,-50,-34,-35,-36,-37,-38,-62,-19,-20,-2,-84,-24,-21,-22,-23,-85,-88,-43,-63,-65,-68,29,-45,-33,-26,-29,-92,-40,-41,-42,-32,-52,-53,-27,-30,-93,-28,-31,-91,-95,-39,-51,-75,29,-44,-64,-69,29,-46,-78,-83,-25,-86,-87,29,29,29,-71,29,29,29,29,29,29,29,-94,-76,29,29,29,-67,-79,-80,]),'DEF':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,22,23,25,27,32,33,34,35,36,37,39,40,42,58,59,60,61,62,66,69,78,80,81,82,83,85,90,92,93,94,95,96,97,99,100,101,102,103,104,105,106,107,112,113,116,119,121,123,124,125,126,128,132,134,135,136,137,138,139,140,144,148,150,151,152,153,154,155,156,157,158,159,160,161,162,163,],[30,30,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-77,-89,-90,-50,-34,-35,-36,-37,-38,-62,-19,-20,-2,-84,-24,-21,-22,-23,-85,-88,-43,-63,-65,-68,30,-45,-33,-26,-29,-92,-40,-41,-42,-32,-52,-53,-27,-30,-93,-28,-31,-91,-95,-39,-51,-75,30,-44,-64,-69,30,-46,-78,-83,-25,-86,-87,30,30,30,-71,30,30,30,30,30,30,30,-94,-76,30,30,30,-67,-79,-80,]),'LBRACKET':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,22,23,25,27,32,33,34,35,36,37,39,40,42,45,54,55,58,59,60,61,62,66,69,78,80,81,82,83,85,90,92,93,94,95,96,97,99,100,101,102,103,104,105,106,107,112,113,116,119,121,123,124,125,126,128,132,134,135,136,137,138,139,140,144,148,150,151,152,153,154,155,156,157,158,159,160,161,162,163,],[31,31,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-77,-89,-90,-50,-34,-35,-36,-37,-38,-62,-19,-20,-2,31,31,31,-84,-24,-21,-22,-23,-85,-88,-43,-63,-65,-68,31,-45,-33,-26,-29,-92,-40,-41,-42,-32,-52,-53,-27,-30,-93,-28,-31,-91,-95,-39,-51,-75,31,-44,-64,-69,31,-46,-78,-83,-25,-86,-87,31,31,31,-71,31,31,31,31,31,31,31,-94,-76,31,31,31,-67,-79,-80,]),'PLUS':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,25,27,32,33,34,35,36,37,39,40,42,58,59,60,61,62,64,65,66,69,78,80,81,82,83,85,90,91,92,93,94,95,96,97,99,100,101,102,103,104,105,106,107,112,113,116,119,121,123,124,125,126,128,132,134,135,136,137,138,139,140,144,148,150,151,152,153,154,155,156,157,158,159,160,161,162,163,],[32,32,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,32,-15,-16,-17,-18,-21,32,-22,-23,-89,-90,-50,-34,-35,-36,-37,-38,-62,-19,-20,-2,-84,-24,-21,-22,-23,32,32,-85,-88,-43,-63,-65,-68,32,-45,-33,32,-26,-29,-92,-40,-41,-42,-32,32,32,-27,-30,-93,-28,-31,-91,-95,-39,-51,-75,32,-44,-64,-69,32,-46,-78,-83,-25,-86,-87,32,32,32,-71,32,32,32,32,32,32,32,-94,-76,32,32,32,-67,-79,-80,]),'MINUS':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,25,27,32,33,34,35,36,37,39,40,42,58,59,60,61,62,64,65,66,69,78,80,81,82,83,85,90,91,92,93,94,95,96,97,99,100,101,102,103,104,105,106,107,112,113,116,119,121,123,124,125,126,128,132,134,135,136,137,138,139,140,144,148,150,151,152,153,154,155,156,157,158,159,160,161,162,163,],[33,33,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,33,-15,-16,-17,-18,-21,33,-22,-23,-89,-90,-50,-34,-35,-36,-37,-38,-62,-19,-20,-2,-84,-24,-21,-22,-23,33,33,-85,-88,-43,-63,-65,-68,33,-45,-33,33,-26,-29,-92,-40,-41,-42,-32,33,33,-27,-30,-93,-28,-31,-91,-95,-39,-51,-75,33,-44,-64,-69,33,-46,-78,-83,-25,-86,-87,33,33,33,-71,33,33,33,33,33,33,33,-94,-76,33,33,33,-67,-79,-80,]),'TIMES':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,25,27,32,33,34,35,36,37,39,40,42,58,59,60,61,62,64,65,66,69,78,80,81,82,83,85,90,91,92,93,94,95,96,97,99,100,101,102,103,104,105,106,107,112,113,116,119,121,123,124,125,126,128,132,134,135,136,137,138,139,140,144,148,150,151,152,153,154,155,156,157,158,159,160,161,162,163,],[34,34,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,34,-15,-16,-17,-18,-21,34,-22,-23,-89,-90,-50,-34,-35,-36,-37,-38,-62,-19,-20,-2,-84,-24,-21,-22,-23,34,34,-85,-88,-43,-63,-65,-68,34,-45,-33,34,-26,-29,-92,-40,-41,-42,-32,34,34,-27,-30,-93,-28,-31,-91,-95,-39,-51,-75,34,-44,-64,-69,34,-46,-78,-83,-25,-86,-87,34,34,34,-71,34,34,34,34,34,34,34,-94,-76,34,34,34,-67,-79,-80,]),'DIVIDE':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,25,27,32,33,34,35,36,37,39,40,42,58,59,60,61,62,64,65,66,69,78,80,81,82,83,85,90,91,92,93,94,95,96,97,99,100,101,102,103,104,105,106,107,112,113,116,119,121,123,124,125,126,128,132,134,135,136,137,138,139,140,144,148,150,151,152,153,154,155,156,157,158,159,160,161,162,163,],[35,35,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,35,-15,-16,-17,-18,-21,35,-22,-23,-89,-90,-50,-34,-35,-36,-37,-38,-62,-19,-20,-2,-84,-24,-21,-22,-23,35,35,-85,-88,-43,-63,-65,-68,35,-45,-33,35,-26,-29,-92,-40,-41,-42,-32,35,35,-27,-30,-93,-28,-31,-91,-95,-39,-51,-75,35,-44,-64,-69,35,-46,-78,-83,-25,-86,-87,35,35,35,-71,35,35,35,35,35,35,35,-94,-76,35,35,35,-67,-79,-80,]),'MOD':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,25,27,32,33,34,35,36,37,39,40,42,58,59,60,61,62,64,65,66,69,78,80,81,82,83,85,90,91,92,93,94,95,96,97,99,100,101,102,103,104,105,106,107,112,113,116,119,121,123,124,125,126,128,132,134,135,136,137,138,139,140,144,148,150,151,152,153,154,155,156,157,158,159,160,161,162,163,],[36,36,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,36,-15,-16,-17,-18,-21,36,-22,-23,-89,-90,-50,-34,-35,-36,-37,-38,-62,-19,-20,-2,-84,-24,-21,-22,-23,36,36,-85,-88,-43,-63,-65,-68,36,-45,-33,36,-26,-29,-92,-40,-41,-42,-32,36,36,-27,-30,-93,-28,-31,-91,-95,-39,-51,-75,36,-44,-64,-69,36,-46,-78,-83,-25,-86,-87,36,36,36,-71,36,36,36,36,36,36,36,-94,-76,36,36,36,-67,-79,-80,]),'LBRACE':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,22,23,25,27,32,33,34,35,36,37,39,40,42,45,54,55,58,59,60,61,62,66,69,78,80,81,82,83,85,90,92,93,94,95,96,97,99,100,101,102,103,104,105,106,107,112,113,116,119,121,123,124,125,126,128,132,134,135,136,137,138,139,140,144,148,150,151,152,153,154,155,156,157,158,159,160,161,162,163,],[38,38,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-77,-89,-90,-50,-34,-35,-36,-37,-38,-62,-19,-20,-2,38,38,38,-84,-24,-21,-22,-23,-85,-88,-43,-63,-65,-68,38,-45,-33,-26,-29,-92,-40,-41,-42,-32,-52,-53,-27,-30,-93,-28,-31,-91,-95,-39,-51,-75,38,-44,-64,-69,38,-46,-78,-83,-25,-86,-87,38,38,38,-71,38,38,38,38,38,38,38,-94,-76,38,38,38,-67,-79,-80,]),'NUMBER':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,22,23,24,25,26,27,31,32,33,34,35,36,37,38,39,40,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,66,67,68,69,70,71,72,73,76,78,80,81,82,83,85,89,90,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,111,112,113,116,119,121,122,123,124,125,126,127,128,129,130,132,133,134,135,136,137,138,139,140,144,148,150,151,152,153,154,155,156,157,158,159,160,161,162,163,],[39,39,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-77,39,39,39,39,-50,39,-34,-35,-36,-37,-38,-62,39,-19,-20,-2,39,39,39,39,39,-56,-57,-58,-59,-60,-61,39,39,39,39,-84,-24,-21,-22,-23,-85,39,39,-88,39,-54,-55,39,39,-43,-63,-65,-68,39,-45,39,-33,-26,-29,-92,-40,-41,-42,39,-32,-52,-53,-27,-30,-93,-28,-31,-91,39,-95,-39,-51,-75,39,39,-44,-64,-69,39,39,-46,39,39,-78,39,-83,-25,-86,-87,39,39,39,-71,39,39,39,39,39,39,39,-94,-76,39,39,39,-67,-79,-80,]),'STRING':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,22,23,24,25,26,27,31,32,33,34,35,36,37,38,39,40,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,66,67,68,69,70,71,72,73,76,78,80,81,82,83,85,89,90,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,111,112,113,116,119,121,122,123,124,125,126,127,128,129,130,132,133,134,135,136,137,138,139,140,144,148,150,151,152,153,154,155,156,157,158,159,160,161,162,163,],[40,40,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-77,40,40,40,40,-50,40,-34,-35,-36,-37,-38,-62,40,-19,-20,-2,40,40,40,40,40,-56,-57,-58,-59,-60,-61,40,40,40,40,-84,-24,-21,-22,-23,-85,40,40,-88,40,-54,-55,40,40,-43,-63,-65,-68,40,-45,40,-33,-26,-29,-92,-40,-41,-42,40,-32,-52,-53,-27,-30,-93,-28,-31,-91,40,-95,-39,-51,-75,40,40,-44,-64,-69,40,40,-46,40,40,-78,40,-83,-25,-86,-87,40,40,40,-71,40,40,40,40,40,40,40,-94,-76,40,40,40,-67,-79,-80,]),'IF':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,22,23,25,27,32,33,34,35,36,37,39,40,42,58,59,60,61,62,66,69,78,80,81,82,83,85,90,92,93,94,95,96,97,99,100,101,102,103,104,105,106,107,112,113,116,119,121,123,124,125,126,128,132,134,135,136,137,138,139,140,144,148,150,151,152,153,154,155,156,157,158,159,160,161,162,163,],[41,41,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-77,-89,-90,-50,-34,-35,-36,-37,-38,-62,-19,-20,-2,-84,-24,-21,-22,-23,-85,-88,-43,-63,-65,-68,41,-45,-33,-26,-29,-92,-40,-41,-42,-32,-52,-53,-27,-30,-93,-28,-31,-91,-95,-39,-51,-75,41,-44,-64,-69,41,-46,-78,-83,-25,-86,-87,41,41,41,-71,41,41,41,41,41,41,41,-94,-76,41,41,41,-67,-79,-80,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,22,23,25,27,32,33,34,35,36,37,39,40,42,58,59,60,61,62,66,69,78,80,81,82,85,90,92,93,94,95,96,97,99,100,101,102,103,104,105,106,107,112,113,116,119,123,124,125,128,132,134,135,136,137,144,155,156,157,160,161,162,163,],[0,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-77,-89,-90,-50,-34,-35,-36,-37,-38,-62,-19,-20,-2,-84,-24,-21,-22,-23,-85,-88,-43,-63,-65,-68,-45,-33,-26,-29,-92,-40,-41,-42,-32,-52,-53,-27,-30,-93,-28,-31,-91,-95,-39,-51,-75,-44,-64,-69,-46,-78,-83,-25,-86,-87,-71,-66,-94,-76,-70,-67,-79,-80,]),'END':([2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,22,23,25,27,32,33,34,35,36,37,39,40,42,58,59,60,61,62,66,69,74,75,78,80,81,82,85,90,92,93,94,95,96,97,99,100,101,102,103,104,105,106,107,112,113,116,119,120,123,124,125,126,128,132,134,135,136,137,139,144,150,151,155,156,157,158,159,160,161,162,163,],[-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-77,-89,-90,-50,-34,-35,-36,-37,-38,-62,-19,-20,-2,-84,-24,-21,-22,-23,-85,-88,119,-73,-43,-63,-65,-68,-45,-33,-26,-29,-92,-40,-41,-42,-32,-52,-53,-27,-30,-93,-28,-31,-91,-95,-39,-51,-75,-74,-44,-64,-69,144,-46,-78,-83,-25,-86,-87,-72,-71,156,157,161,-94,-76,162,163,-70,-67,-79,-80,]),'WHEN':([2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,22,23,25,27,29,32,33,34,35,36,37,39,40,42,58,59,60,61,62,66,69,74,75,78,80,81,82,85,90,92,93,94,95,96,97,99,100,101,102,103,104,105,106,107,112,113,116,119,120,123,124,125,128,132,134,135,136,137,139,144,155,156,157,160,161,162,163,],[-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-77,-89,-90,-50,76,-34,-35,-36,-37,-38,-62,-19,-20,-2,-84,-24,-21,-22,-23,-85,-88,76,-73,-43,-63,-65,-68,-45,-33,-26,-29,-92,-40,-41,-42,-32,-52,-53,-27,-30,-93,-28,-31,-91,-95,-39,-51,-75,-74,-44,-64,-69,-46,-78,-83,-25,-86,-87,-72,-71,-66,-94,-76,-70,-67,-79,-80,]),'ELSE':([2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,22,23,25,27,32,33,34,35,36,37,39,40,42,58,59,60,61,62,66,69,78,80,81,82,85,90,92,93,94,95,96,97,99,100,101,102,103,104,105,106,107,112,113,116,119,123,124,125,128,132,134,135,136,137,144,155,156,157,160,161,162,163,],[-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-77,-89,-90,-50,-34,-35,-36,-37,-38,83,-19,-20,-2,-84,-24,-21,-22,-23,-85,-88,-43,83,-65,-68,-45,-33,-26,-29,-92,-40,-41,-42,-32,-52,-53,-27,-30,-93,-28,-31,-91,-95,-39,-51,-75,-44,-64,-69,-46,-78,-83,-25,-86,-87,-71,-66,-94,-76,-70,-67,-79,-80,]),'ELSIF':([2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,22,23,25,27,32,33,34,35,36,37,39,40,42,58,59,60,61,62,66,69,78,80,81,82,85,90,92,93,94,95,96,97,99,100,101,102,103,104,105,106,107,112,113,116,119,123,124,125,128,132,134,135,136,137,144,155,156,157,160,161,162,163,],[-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-77,-89,-90,-50,-34,-35,-36,-37,-38,84,-19,-20,-2,-84,-24,-21,-22,-23,-85,-88,-43,84,-65,-68,-45,-33,-26,-29,-92,-40,-41,-42,-32,-52,-53,-27,-30,-93,-28,-31,-91,-95,-39,-51,-75,-44,-64,-69,-46,-78,-83,-25,-86,-87,-71,-66,-94,-76,-70,-67,-79,-80,]),'ASSIGN':([19,21,22,],[45,54,55,]),'LESSTHAN':([19,20,21,22,39,40,60,61,62,117,],[-21,48,-22,-23,-19,-20,-21,-22,-23,48,]),'GREATERTHAN':([19,20,21,22,39,40,60,61,62,117,],[-21,49,-22,-23,-19,-20,-21,-22,-23,49,]),'GREATEROREQUAL':([19,20,21,22,39,40,60,61,62,117,],[-21,50,-22,-23,-19,-20,-21,-22,-23,50,]),'LESSOREQUAL':([19,20,21,22,39,40,60,61,62,117,],[-21,51,-22,-23,-19,-20,-21,-22,-23,51,]),'EQUAL':([19,20,21,22,39,40,60,61,62,117,],[-21,52,-22,-23,-19,-20,-21,-22,-23,52,]),'NOTEQUAL':([19,20,21,22,39,40,60,61,62,117,],[-21,53,-22,-23,-19,-20,-21,-22,-23,53,]),'RPAREN':([27,39,40,59,60,61,62,63,64,65,90,99,100,101,108,110,114,115,116,118,122,131,135,141,142,143,145,149,],[-50,-19,-20,-24,-21,-22,-23,112,113,-24,-33,-32,-52,-53,132,134,136,137,-51,138,140,148,-25,152,153,-81,154,-82,]),'AND':([27,39,40,60,61,62,90,99,100,101,],[71,-19,-20,-21,-22,-23,-33,-32,-52,-53,]),'OR':([27,39,40,60,61,62,90,99,100,101,],[72,-19,-20,-21,-22,-23,-33,-32,-52,-53,]),'RBRACKET':([31,39,40,59,60,61,62,79,135,],[78,-19,-20,-24,-21,-22,-23,123,-25,]),'RBRACE':([38,39,40,60,61,62,86,87,146,147,],[85,-19,-20,-21,-22,-23,128,-47,-48,-49,]),'COMMA':([39,40,59,60,61,62,65,86,87,109,143,146,147,],[-19,-20,111,-21,-22,-23,111,129,-47,133,133,-48,-49,]),'COLON':([39,40,60,61,62,88,],[-19,-20,-21,-22,-23,130,]),'GETS':([45,54,55,],[94,104,107,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'codigo':([0,83,121,138,140,148,152,153,154,],[1,126,139,150,151,155,158,159,160,]),'statement':([0,1,83,121,126,138,139,140,148,150,151,152,153,154,155,158,159,160,],[2,42,2,2,42,2,42,2,2,42,42,2,2,2,42,42,42,42,]),'assign':([0,1,83,121,126,138,139,140,148,150,151,152,153,154,155,158,159,160,],[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,]),'impression':([0,1,83,121,126,138,139,140,148,150,151,152,153,154,155,158,159,160,],[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,]),'tupla':([0,1,45,54,55,83,121,126,138,139,140,148,150,151,152,153,154,155,158,159,160,],[5,5,96,96,96,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,]),'conditions':([0,1,70,73,76,83,89,121,126,127,138,139,140,148,150,151,152,153,154,155,158,159,160,],[6,6,116,118,121,6,131,6,6,145,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'while_loop':([0,1,83,121,126,138,139,140,148,150,151,152,153,154,155,158,159,160,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'case':([0,1,83,121,126,138,139,140,148,150,151,152,153,154,155,158,159,160,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'Sfunction':([0,1,83,121,126,138,139,140,148,150,151,152,153,154,155,158,159,160,],[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'array':([0,1,45,54,55,83,121,126,138,139,140,148,150,151,152,153,154,155,158,159,160,],[10,10,95,95,95,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'p_SfunctionINV':([0,1,83,121,126,138,139,140,148,150,151,152,153,154,155,158,159,160,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'p_function_one_parameter':([0,1,83,121,126,138,139,140,148,150,151,152,153,154,155,158,159,160,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'p_function_two_parameter':([0,1,83,121,126,138,139,140,148,150,151,152,153,154,155,158,159,160,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'aritmeticExpresion':([0,1,24,44,47,83,121,126,138,139,140,148,150,151,152,153,154,155,158,159,160,],[14,14,64,64,101,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'operator':([0,1,14,20,64,65,83,91,100,101,121,126,138,139,140,148,150,151,152,153,154,155,158,159,160,],[15,15,43,46,43,46,15,46,46,43,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'dataIn':([0,1,83,121,126,138,139,140,148,150,151,152,153,154,155,158,159,160,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'control_structures':([0,1,83,121,126,138,139,140,148,150,151,152,153,154,155,158,159,160,],[17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'hash':([0,1,45,54,55,83,121,126,138,139,140,148,150,151,152,153,154,155,158,159,160,],[18,18,97,97,97,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,]),'value':([0,1,23,24,25,26,31,38,43,44,45,46,47,54,55,56,57,67,68,70,73,76,83,89,98,111,121,122,126,127,129,130,133,138,139,140,148,150,151,152,153,154,155,158,159,160,],[20,20,59,65,59,59,59,88,90,91,92,99,100,102,105,109,59,59,59,117,117,117,20,117,59,59,20,143,20,117,88,147,149,20,20,20,20,20,20,20,20,20,20,20,20,20,]),'condition':([0,1,70,73,76,83,89,121,126,127,138,139,140,148,150,151,152,153,154,155,158,159,160,],[27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'if_block':([0,1,83,121,126,138,139,140,148,150,151,152,153,154,155,158,159,160,],[37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'operComp':([20,117,],[47,47,]),'values':([23,24,25,26,31,57,67,68,98,111,],[58,63,66,69,79,110,114,115,63,135,]),'conector':([27,],[70,]),'whens':([29,],[74,]),'when':([29,74,],[75,120,]),'elsif_blocks':([37,],[80,]),'else_block':([37,80,],[81,124,]),'elsif_block':([37,80,],[82,125,]),'hash_contents':([38,],[86,]),'hash_pair':([38,129,],[87,146,]),'data_structure':([45,54,55,],[93,103,106,]),'params':([56,122,],[108,142,]),'param':([122,],[141,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> codigo","S'",1,None,None,None),
  ('codigo -> statement','codigo',1,'p_codigo','analizador_sintactico.py',28),
  ('codigo -> codigo statement','codigo',2,'p_codigo','analizador_sintactico.py',29),
  ('statement -> assign','statement',1,'p_statement','analizador_sintactico.py',32),
  ('statement -> impression','statement',1,'p_statement','analizador_sintactico.py',33),
  ('statement -> tupla','statement',1,'p_statement','analizador_sintactico.py',34),
  ('statement -> conditions','statement',1,'p_statement','analizador_sintactico.py',35),
  ('statement -> while_loop','statement',1,'p_statement','analizador_sintactico.py',36),
  ('statement -> case','statement',1,'p_statement','analizador_sintactico.py',37),
  ('statement -> Sfunction','statement',1,'p_statement','analizador_sintactico.py',38),
  ('statement -> array','statement',1,'p_statement','analizador_sintactico.py',39),
  ('statement -> p_SfunctionINV','statement',1,'p_statement','analizador_sintactico.py',40),
  ('statement -> p_function_one_parameter','statement',1,'p_statement','analizador_sintactico.py',41),
  ('statement -> p_function_two_parameter','statement',1,'p_statement','analizador_sintactico.py',42),
  ('statement -> aritmeticExpresion','statement',1,'p_statement','analizador_sintactico.py',43),
  ('statement -> operator','statement',1,'p_statement','analizador_sintactico.py',44),
  ('statement -> dataIn','statement',1,'p_statement','analizador_sintactico.py',45),
  ('statement -> control_structures','statement',1,'p_statement','analizador_sintactico.py',46),
  ('statement -> hash','statement',1,'p_statement','analizador_sintactico.py',47),
  ('value -> NUMBER','value',1,'p_value','analizador_sintactico.py',50),
  ('value -> STRING','value',1,'p_value','analizador_sintactico.py',51),
  ('value -> INSTANCE_VAR','value',1,'p_value','analizador_sintactico.py',52),
  ('value -> GLOBAL_VAR','value',1,'p_value','analizador_sintactico.py',53),
  ('value -> ID','value',1,'p_value','analizador_sintactico.py',54),
  ('values -> value','values',1,'p_values','analizador_sintactico.py',61),
  ('values -> value COMMA values','values',3,'p_values','analizador_sintactico.py',62),
  ('assign -> INSTANCE_VAR ASSIGN value','assign',3,'p_assign','analizador_sintactico.py',79),
  ('assign -> GLOBAL_VAR ASSIGN value','assign',3,'p_assign','analizador_sintactico.py',80),
  ('assign -> ID ASSIGN value','assign',3,'p_assign','analizador_sintactico.py',81),
  ('assign -> INSTANCE_VAR ASSIGN data_structure','assign',3,'p_assign','analizador_sintactico.py',82),
  ('assign -> GLOBAL_VAR ASSIGN data_structure','assign',3,'p_assign','analizador_sintactico.py',83),
  ('assign -> ID ASSIGN data_structure','assign',3,'p_assign','analizador_sintactico.py',84),
  ('aritmeticExpresion -> value operator value','aritmeticExpresion',3,'p_aritmeticExpresion','analizador_sintactico.py',90),
  ('aritmeticExpresion -> aritmeticExpresion operator value','aritmeticExpresion',3,'p_aritmeticExpresion','analizador_sintactico.py',91),
  ('operator -> PLUS','operator',1,'p_operator','analizador_sintactico.py',110),
  ('operator -> MINUS','operator',1,'p_operator','analizador_sintactico.py',111),
  ('operator -> TIMES','operator',1,'p_operator','analizador_sintactico.py',112),
  ('operator -> DIVIDE','operator',1,'p_operator','analizador_sintactico.py',113),
  ('operator -> MOD','operator',1,'p_operator','analizador_sintactico.py',114),
  ('operator -> LPAREN aritmeticExpresion RPAREN','operator',3,'p_operator','analizador_sintactico.py',115),
  ('data_structure -> array','data_structure',1,'p_data_structure','analizador_sintactico.py',119),
  ('data_structure -> tupla','data_structure',1,'p_data_structure','analizador_sintactico.py',120),
  ('data_structure -> hash','data_structure',1,'p_data_structure','analizador_sintactico.py',121),
  ('array -> LBRACKET RBRACKET','array',2,'p_emptyarray','analizador_sintactico.py',125),
  ('array -> LBRACKET values RBRACKET','array',3,'p_array','analizador_sintactico.py',128),
  ('hash -> LBRACE RBRACE','hash',2,'p_empty_hash','analizador_sintactico.py',132),
  ('hash -> LBRACE hash_contents RBRACE','hash',3,'p_hash','analizador_sintactico.py',135),
  ('hash_contents -> hash_pair','hash_contents',1,'p_hash_contents','analizador_sintactico.py',138),
  ('hash_contents -> hash_contents COMMA hash_pair','hash_contents',3,'p_hash_contents','analizador_sintactico.py',139),
  ('hash_pair -> value COLON value','hash_pair',3,'p_hash_pair','analizador_sintactico.py',142),
  ('conditions -> condition','conditions',1,'p_conditions','analizador_sintactico.py',146),
  ('conditions -> condition conector conditions','conditions',3,'p_conditions','analizador_sintactico.py',147),
  ('condition -> value operComp value','condition',3,'p_condition','analizador_sintactico.py',150),
  ('condition -> value operComp aritmeticExpresion','condition',3,'p_condition','analizador_sintactico.py',151),
  ('conector -> AND','conector',1,'p_conector','analizador_sintactico.py',154),
  ('conector -> OR','conector',1,'p_conector','analizador_sintactico.py',155),
  ('operComp -> LESSTHAN','operComp',1,'p_operComp','analizador_sintactico.py',158),
  ('operComp -> GREATERTHAN','operComp',1,'p_operComp','analizador_sintactico.py',159),
  ('operComp -> GREATEROREQUAL','operComp',1,'p_operComp','analizador_sintactico.py',160),
  ('operComp -> LESSOREQUAL','operComp',1,'p_operComp','analizador_sintactico.py',161),
  ('operComp -> EQUAL','operComp',1,'p_operComp','analizador_sintactico.py',162),
  ('operComp -> NOTEQUAL','operComp',1,'p_operComp','analizador_sintactico.py',163),
  ('control_structures -> if_block','control_structures',1,'p_control_structures','analizador_sintactico.py',167),
  ('control_structures -> if_block elsif_blocks','control_structures',2,'p_control_structures','analizador_sintactico.py',168),
  ('control_structures -> if_block elsif_blocks else_block','control_structures',3,'p_control_structures','analizador_sintactico.py',169),
  ('control_structures -> if_block else_block','control_structures',2,'p_control_structures','analizador_sintactico.py',170),
  ('if_block -> IF LPAREN conditions RPAREN codigo','if_block',5,'p_if_block','analizador_sintactico.py',173),
  ('if_block -> IF LPAREN conditions RPAREN codigo END','if_block',6,'p_if_block','analizador_sintactico.py',174),
  ('elsif_blocks -> elsif_block','elsif_blocks',1,'p_elsif_blocks','analizador_sintactico.py',177),
  ('elsif_blocks -> elsif_blocks elsif_block','elsif_blocks',2,'p_elsif_blocks','analizador_sintactico.py',178),
  ('elsif_block -> ELSIF LPAREN conditions RPAREN codigo','elsif_block',5,'p_elsif_block','analizador_sintactico.py',181),
  ('else_block -> ELSE codigo END','else_block',3,'p_else_block','analizador_sintactico.py',184),
  ('when -> WHEN conditions codigo','when',3,'p_when','analizador_sintactico.py',188),
  ('whens -> when','whens',1,'p_whens','analizador_sintactico.py',191),
  ('whens -> whens when','whens',2,'p_whens','analizador_sintactico.py',192),
  ('case -> CASE whens END','case',3,'p_case','analizador_sintactico.py',195),
  ('Sfunction -> DEF ID LPAREN RPAREN codigo END','Sfunction',6,'p_Sfunction','analizador_sintactico.py',199),
  ('p_SfunctionINV -> ID','p_SfunctionINV',1,'p_SfunctionINV','analizador_sintactico.py',203),
  ('p_SfunctionINV -> ID LPAREN params RPAREN','p_SfunctionINV',4,'p_SfunctionINV','analizador_sintactico.py',204),
  ('p_function_one_parameter -> DEF ID LPAREN param RPAREN codigo END','p_function_one_parameter',7,'p_function_one_parameter','analizador_sintactico.py',208),
  ('p_function_two_parameter -> DEF ID LPAREN params RPAREN codigo END','p_function_two_parameter',7,'p_function_two_parameter','analizador_sintactico.py',212),
  ('param -> value','param',1,'p_param','analizador_sintactico.py',216),
  ('params -> value COMMA value','params',3,'p_params','analizador_sintactico.py',219),
  ('impression -> PRINT LPAREN values RPAREN','impression',4,'p_impression','analizador_sintactico.py',224),
  ('impression -> PRINT values','impression',2,'p_impression','analizador_sintactico.py',225),
  ('impression -> PUTS values','impression',2,'p_impression','analizador_sintactico.py',226),
  ('impression -> PUTS LPAREN values RPAREN','impression',4,'p_impression','analizador_sintactico.py',227),
  ('impression -> P LPAREN values RPAREN','impression',4,'p_impression','analizador_sintactico.py',228),
  ('impression -> P values','impression',2,'p_impression','analizador_sintactico.py',229),
  ('impression -> PRINT','impression',1,'p_impression','analizador_sintactico.py',230),
  ('impression -> PUTS','impression',1,'p_impression','analizador_sintactico.py',231),
  ('dataIn -> ID ASSIGN GETS','dataIn',3,'p_dataIn','analizador_sintactico.py',234),
  ('dataIn -> INSTANCE_VAR ASSIGN GETS','dataIn',3,'p_dataIn','analizador_sintactico.py',235),
  ('dataIn -> GLOBAL_VAR ASSIGN GETS','dataIn',3,'p_dataIn','analizador_sintactico.py',236),
  ('while_loop -> WHILE LPAREN conditions RPAREN codigo END','while_loop',6,'p_while_loop','analizador_sintactico.py',240),
  ('tupla -> LPAREN values RPAREN','tupla',3,'p_tupla','analizador_sintactico.py',244),
]
