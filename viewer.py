# A simple network chat program between to Raspberry Pi's
#Modified to GLaDOS viewer

import network
import sys
import os
import pprint

def heard(phrase):
	os.system('clear') # on linux / os x
	if(phrase == "1"):
			print """
              .,-:;//;:=,
          . :H@@@MM@M#H/.,+%;,
       ,/X+ +M@@M@MM%=,-%HMMM@X/,
     -+@MM; $M@@MH+-,;XMMMM@MMMM@+-
    ;@M@@M- XM@X;. -+XXXXXHHH@M@M#@/.
  ,%MM@@MH ,@%=            .---=-=:=,.
  =@#@@@MX .,              -%HX$$%%%+;
 =-./@M@M$                  .;@MMMM@MM:
 X@/ -$MM/                    .+MM@@@M$
,@M@H: :@:                    . =X#@@@@-
,@@@MMX, .                    /H- ;@M@M=
.H@@@@M@+,                    %MM+..%#$.
 /MMMM@MMH/.                  XM@MH; =;
  /%+%$XHH@$=              , .H@@@@MX,
   .=--------.           -%H.,@@@@@MX,
   .%MM@@@HHHXX$$$%+- .:$MMX =M@@MM%.
     =XMMM@MM@MM#H;,-+HMM@M+ /MMMX=
       =%@M@M#@$-.=$@MM@@@M; %M%=
         ,:+$+-,/H#MMMMMMM@= =,
               =++%%%%+/:-."""
	if(phrase == "2"):
			print """
            ,:/+/-
            /M/              .,-=;//;-
       .:/= ;MH/,    ,=/+%$XH@MM#@:
      -$##@+$###@H@MMM#######H:.    -/H#
 .,H@H@ X######@ -H#####@+-     -+H###@X
  .,@##H;      +XM##M/,     =%@###@X;-
X%-  :M##########$.    .:%M###@%:
M##H,   +H@@@$/-.  ,;$M###@%,          -
M####M=,,---,.-%%H####M$:          ,+@##
@##################@/.         :%H##@$-
M###############H,         ;HM##M$=
#################.    .=$M##M$=
################H..;XM##M$=          .:+
M###################@%=           =+@MH%
@################M/.          =+H#X%=
=+M##############M,       -/X#X+;.
  .;XM##########H=    ,/X#H+:,
     .=+HM######M+/+HM@+=.
         ,:/%XM####H/.
              ,.:=-."""
	if(phrase == "3"):
			print """
            .+
             /M;
              H#@:              ;,
              -###H-          -@/
               %####$.  -;  .%#X
                M#####+;#H :M#M.
..          .+/;%#########X###-
 -/%H%+;-,    +##############/
    .:$M###MH$%+############X  ,--=;-
        -/H#####################H+=.
           .+#################X.
         =%M####################H;.
            /@###############+;;/%%;,
         -%###################$.
       ;H######################M=
    ,%#####MH$%;+#####M###-/@####%
  :$H%+;=-      -####X.,H#   -+M##@-
 .              ,###;    ;      =$##+
                .#H,               :XH,
                 +                   .;-"""
	if(phrase == "3"):
			print """
                 =/;;/-
                +:    //
               /;      /;
              -X        H.
.//;;;:;;-,   X=        :+   .-;:=;:;%;.
M-       ,=;;;#:,      ,:#;;:=,       ,@
:%           :%.=/++++/=.$=           %=
 ,%;         %/:+/;,,/++:+/         ;+.
   ,+/.    ,;@+,        ,%H;,    ,/+,
      ;+;;/= @.  .H##X   -X :///+;
      ;+=;;;.@,  .XM@$.  =X.//;=%/.
   ,;:      :@%=        =$H:     .+%-
 ,%=         %;-///==///-//         =%,
;+           :%-;;;:;;;;-X-           +:
@-      .-;;;;M-        =M/;;;-.      -X
 :;;::;;-.    %-        :+    ,-;;-;:==
              ,X        H.
               ;/      %=
                //    +;
                 ,////,"""
	if(phrase == "4"):
			print """
             =+$HM####@H%;,
          /H###############M$,
          ,@################+
           .H##############+
             X############/
              $##########/
               %########/
                /X/;;+X/
 
                 -XHHX-
                ,######,
#############X  .M####M.  X#############
##############-   -//-   -##############
X##############%,      ,+##############X
-##############X        X##############-
 %############%          %############%
  %##########;            ;##########%
   ;#######M=              =M#######;
    .+M###@,                ,@###M+.
       :XH.                  .HX:"""
	if(phrase == "5"):
			print """
           .-;+$XHHHHHHX$+;-.
        ,;X@@X%/;=----=:/%X@@X/,
      =$@@%=.              .=+H@X:
    -XMX:                      =XMX=
   /@@:                          =H@+
  %@X,                            .$@$
 +@X.                               $@%
-@@,                                .@@=
%@%                                  +@$
H@:                                  :@H
H@:         :HHHHHHHHHHHHHHHHHHX,    =@H
%@%         ;@M@@@@@@@@@@@@@@@@@H-   +@$
=@@,        :@@@@@@@@@@@@@@@@@@@@@= .@@:
 +@X        :@@@@@@@@@@@@@@@M@@@@@@:%@%
  $@$,      ;@@@@@@@@@@@@@@@@@M@@@@@@$.
   +@@HHHHHHH@@@@@@@@@@@@@@@@@@@@@@@+
    =X@@@@@@@@@@@@@@@@@@@@@@@@@@@@X=
      :$@@@@@@@@@@@@@@@@@@@M@@@@$:
        ,;$@@@@@@@@@@@@@@@@@@X/-
           .-;+$XXHHHHHX$+;-."""
	if(phrase == "6"):
			print """
                          .,---.
                        ,/XM#MMMX;,
                      -%##########M%,
                     -@######%  $###@=
      .,--,         -H#######$   $###M:
   ,;$M###MMX;     .;##########$;HM###X=
 ,/@##########H=      ;################+
-+#############M/,      %##############+
%M###############=      /##############:
H################      .M#############;.
@###############M      ,@###########M:.
X################,      -$=X#######@:
/@##################%-     +######$-
.;##################X     .X#####+,
 .;H################/     -X####+.
   ,;X##############,       .MM/
      ,:+$H@M#######M#$-    .$$=
           .,-=;+$@###X:    ;/=.
                  .,/X$;   .::,
                      .,    .."""
	if(phrase == "7"):
			print """
                                     :X-
                                  :X###
                                ;@####@
                              ;M######X
                            -@########$
                          .$##########@
                         =M############-
                        +##############$
                      .H############$=.
         ,/:         ,M##########M;.
      -+@###;       =##########M;
   =%M#######;     :#########M/
-$M###########;   :#########/
 ,;X###########; =########$.
     ;H#########+#######M=
       ,+##############+
          /M#########@-
            ;M######%
              +####:
               ,$M-"""
	if(phrase == "8"):
			print """
                     -$-
                    .H##H,
                   +######+
                .+#########H.
              -$############@.
            =H###############@  -X:
          .$##################:  @#@-
     ,;  .M###################;  H###;
   ;@#:  @###################@  ,#####:
 -M###.  M#################@.  ;######H
 M####-  +###############$   =@#######X
 H####$   -M###########+   :#########M,
  /####X-   =########%   :M########@/.
    ,;%H@X;   .$###X   :##MM@%+;:-
                 ..
  -/;:-,.              ,,-==+M########H
 -##################@HX%%+%%$%%%+:,,
    .-/H%%%+%%$H@###############M@+=:/+:
/XHX%:#####MH%=    ,---:;;;;/%%XHM,:###$"""
	if(phrase == "9"):
			print """
	#+ @      # #              M#@
 .    .X  X.%##@;# #   +@#######X. @#%
   ,==.   ,######M+  -#####%M####M-    #
  :H##M%:=##+ .M##M,;#####/+#######% ,M#
 .M########=  =@#@.=#####M=M#######=  X#
 :@@MMM##M.  -##M.,#######M#######. =  M
             @##..###:.    .H####. @@ X,
   ############: ###,/####;  /##= @#. M
           ,M## ;##,@#M;/M#M  @# X#% X#
.%=   ######M## ##.M#:   ./#M ,M #M ,#$
##/         $## #+;#: #### ;#/ M M- @# :
#+ #M@MM###M-;M #:$#-##$H# .#X @ + $#. #
      ######/.: #%=# M#:MM./#.-#  @#: H#
+,.=   @###: /@ %#,@  ##@X #,-#@.##% .@#
#####+;/##/ @##  @#,+       /#M    . X,
   ;###M#@ M###H .#M-     ,##M  ;@@; ###
   .M#M##H ;####X ,@#######M/ -M###$  -H
    .M###%  X####H  .@@MM@;  ;@#M@
      H#M    /@####/      ,++.  / ==-,
               ,=/:, .+X@MMH@#H  #####$="""

	if(phrase == "10"):
			print """
      $$$$$$$O        $$$$$$$$$        
    $$Z$$$$$$$$$7   $$$$$$$$$$7$$             
    $$$$$$$$ $$$$   $$$$  $$$$$$$       
     $$$$$$$$Z 7Z   N7  $$$$$$$$        
      Z$$$$$$$$       $$$$$$$$7         
        $$$$$$  O7$7   $$$$$$N       
        $$$7N 7$$$$$$$$ $$$$D           
      $$$$7  D$$$$$$$$$  $$$$$          
     $$$$      7$$$$77     $$$$         
     $$    $$$7       $$$$   $$D        
         $$$$$$$7   $$$$$$$$            
    $   $$$$$$$$$   $$$$$$$$$  $$       
  $$$  7$$$$$$$$$   $$$$$$$$$$ 7$$      
  $$$N 7$$$$$$$$7   $$$$$$$$$7 $$$$     
 $$$$  $$$$$$$$$     7$$$$$$7  7$$$     
  $$$   8$$$$$$       D$$$$7    $$$     
  7$           7$$$$$$          $$      
     7$$      7$$$$$$$$     $$$$        
    $$$$$7   $$$$$$$$$$$  D7$$$$$       
    $$$$$$$  $$$$$$$$$$7 $$$$$$$$       
     $$$$$$$  $$$$$$$$$  $$$$$$7        
     8$$$$$$   7$$$$$7  7$$$$$$N        
       $$$$$             $$$$7          
               $$$$$$$8                 
             $$$$$$$$$$$                
               $$$$$$$           """


if (len(sys.argv) >= 2):
  network.call(sys.argv[1], whenHearCall=heard)
else:  
  network.wait(whenHearCall=heard)



while network.isConnected():
  phrase = raw_input()
  print "me:" + phrase
  network.say(phrase)
