grammar RoboticFinger;



/*
 * Parser Rules
 */

roboticfinger                : line+ EOF ;

line		    : drag_command positionX positionY NEWLINE | push_cmd time NEWLINE | touch_cmd NEWLINE;

drag_command              : DRAG WHITESPACE ;

push_cmd  : PUSH WHITESPACE ;

touch_cmd : TOUCH  ;

positionX	      : INT_NUMBER+ WHITESPACE;

positionY 	      :   INT_NUMBER+;

time              : INT_NUMBER+;

INT_NUMBER		:   DIGIT+;


/*
 * Lexer Rules
 */

fragment A          : ('A') ;
fragment C          : ('C') ;
fragment D          : ('D') ;
fragment P          : ('P') ;
fragment G          : ('G') ;
fragment R          : ('R') ;
fragment S          : ('S') ;
fragment Y          : ('Y') ;
fragment H          : ('H') ;
fragment O          : ('O') ;
fragment U          : ('U') ;
fragment T          : ('T') ;


DIGIT   :   ('0'..'9');

TOUCH               : T O U C H ;

PUSH                : P U S H ;

DRAG		    : D R A G ;

WHITESPACE          : (' ');

NEWLINE             : ('\r'? '\n' | '\r')+ ;
