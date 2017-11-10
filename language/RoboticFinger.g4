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

fragment A          : ('A'|'a') ;
fragment C          : ('C'|'c') ;
fragment D          : ('D'|'d') ;
fragment P          : ('P'|'p') ;
fragment G          : ('G'|'g') ;
fragment R          : ('R'|'r') ;
fragment S          : ('S'|'s') ;
fragment Y          : ('Y'|'y') ;
fragment H          : ('H'|'h') ;
fragment O          : ('O'|'o') ;
fragment U          : ('U'|'u') ;
fragment T          : ('T'|'t') ;

fragment LOWERCASE  : [a-z] ;
fragment UPPERCASE  : [A-Z] ;

DIGIT   :   ('0'..'9');

TOUCH               : T O U C H ;

PUSH                : P U S H ;

DRAG		    : D R A G ;

WHITESPACE          : (' ');

NEWLINE             : ('\r'? '\n' | '\r')+ ;
