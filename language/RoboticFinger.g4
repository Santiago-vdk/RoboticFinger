grammar RoboticFinger;



/*
 * Parser Rules
 */

chat                : line+ EOF ;

line		    : command positionX positionY NEWLINE ;

command              : (TOUCH | PUSH | DRAG) WHITESPACE ;
                                        
positionX	      : INT_NUMBER+ WHITESPACE;

positionY 	      :   INT_NUMBER+;

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

WHITESPACE          : (' ' | '\t')+ ;

NEWLINE             : ('\r'? '\n' | '\r')+ ;


